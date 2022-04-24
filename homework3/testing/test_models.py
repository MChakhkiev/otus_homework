from main import (
    User,
    Post,
    Comment,
    create_user,
    create_comment,
    create_post,
    query_user_by_id,
    query_posts_by_user,
    query_posts_by_id,
    query_all_posts,
    query_all_users,
    query_user_by_name,
    query_comments_by_post
)

from mock_alchemy.mocking import UnifiedAlchemyMagicMock

session = UnifiedAlchemyMagicMock()
session.add(User(id=1, username='john'))
session.add(Post(id=1, user=1, text='text', title='title'))
session.add(Comment(id=1, user=1, text='text', post=1))


def test_create_user():
    user = create_user(session, 'sam')
    assert isinstance(user, User)
    assert user.username == 'sam'


def test_create_comment():
    comment = create_comment(session, user=1, post=1, text='text')
    assert isinstance(comment, Comment)
    assert comment.text == 'text'


def test_create_post():
    post = create_post(session, user=1, text='text', title='title')
    assert isinstance(post, Post)
    assert post.text == 'text'


def test_get_user():
    user = query_user_by_id(session, 1)
    assert isinstance(user, User)
    assert user.username == 'john'


def test_query_post_by_user():
    posts = query_posts_by_user(session, 1)
    assert isinstance(posts, list)
    assert isinstance(posts[0], Post)


def test_query_post_by_id():
    post = query_posts_by_id(session, 1)
    assert isinstance(post, Post)
    assert post.text == 'text'


def test_query_all_posts():
    posts = query_all_posts(session)
    assert isinstance(posts, list)
    assert isinstance(posts[0], Post)


def test_query_all_users():
    users = query_all_users(session)
    assert isinstance(users, list)
    assert isinstance(users[0], User)


def test_query_user_by_name():
    user = query_user_by_name(session, 'john')
    assert isinstance(user, User)


def test_query_comments_by_post():
    comments = query_comments_by_post(session, 1)
    assert isinstance(comments, list)
    assert isinstance(comments[0], Comment)
