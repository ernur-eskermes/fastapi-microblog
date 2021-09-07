from sqlalchemy import select

from core.db import database
from microblog.models import posts
from microblog.schemas import PostCreate
from user.models import User
from user.models import users


async def get_post_list():
    post_list = await database.fetch_all(
        query=posts.select().where(posts.c.parent_id.is_(None))
    )
    post_list = list(map(dict, post_list))
    for post in post_list:
        user_id = post.pop('user')
        post['user'] = {"id": user_id}
    return post_list


async def get_post_list_children(pk: int):
    post_list = await database.fetch_all(
        query=posts.select().where(posts.c.parent_id == pk))
    if post_list is not None:
        post_list = list(map(dict, post_list))
        for post in post_list:
            user_id = post.pop('user')
            post['user'] = {"id": user_id}
        return post_list
    return None


async def get_post(pk: int):
    u = users.alias('user')
    p = posts.alias('post')
    q = select([u.c.id.label("userId"), u.c.name.label("userName"), p]) \
        .select_from(p.join(u)) \
        .where((p.c.id == pk) & (u.c.id == p.c.user))
    post = await database.fetch_one(q)
    if post is not None:
        post = dict(post)
        return {**post, "user": {"id": post.pop("userId"),
                                 "name": post.pop("userName")}}
    return None


async def get_post_list_user(user: User):
    post_list = await database.fetch_all(
        query=posts.select().where(posts.c.user == user.id))
    post_list = list(map(dict, post_list))
    for post in post_list:
        user_id = post.pop('user')
        post['user'] = {"id": user_id}
    return post_list


async def create_post(item: PostCreate, user: User):
    post = posts.insert().values(**item.dict(), user=user.id)
    pk = await database.execute(post)
    return {**item.dict(), "id": pk, "user": {"id": user.id}}


async def update_post(pk: int, item: PostCreate, user: User):
    post = posts.update().where(
        (posts.c.id == pk) & (posts.c.user == user.id)
    ).values(**item.dict())
    return await database.execute(post)


async def delete_post(pk: int, user: User):
    post = posts.delete().where(
        (posts.c.id == pk) & (posts.c.user == user.id)
    )
    return await database.execute(post)
