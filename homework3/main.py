from datetime import datetime

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import (
    declarative_base,
    scoped_session,
    sessionmaker,
    Session,
    relationship
)


DB_URL = "sqlite:///blog.db"
DB_ECHO = False
engine = create_engine(url=DB_URL, echo=DB_ECHO)
session_factory = sessionmaker(bind=engine)
scop_session = scoped_session(session_factory)
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    posts = relationship("Post")
    comments = relationship("Comment")

    def __str__(self):
        return self.username

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('user.id'))
    text = Column(String(2000))
    title = Column(String(60))
    created_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return self.title


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('user.id'))
    post = Column(Integer, ForeignKey('post.id'))
    text = Column(String(255))

    def __str__(self):
        return self.text


def create_user(session: Session, username: str) -> User:
    user = User(username=username)
    session.add(user)
    session.commit()
    return user


def query_all_users(session: Session) -> list[User]:
    users = session.query(User).all()
    return users


def query_user_by_name(session: Session, username: str) -> User:
    user = session.query(User).filter_by(username=username).first()
    return user


def query_user_by_id(session: Session, ident: int) -> User:
    user = session.query(User).filter_by(id=ident).first()
    return user


def create_post(session: Session, user: User, title: str, text: str) -> Post:
    post = Post(user=user, text=text, title=title)
    session.add(post)
    session.commit()
    return post


def query_all_posts(session: Session) -> list[Post]:
    posts = session.query(Post).all()
    return posts


def query_posts_by_user(session: Session, user: User) -> list[Post]:
    posts = session.query(Post).filter_by(user=user).all()
    return posts


def query_posts_by_id(session: Session, ident: int) -> Post:
    posts = session.query(Post).filter_by(id=ident).first()
    return posts


def create_comment(session: Session, user: User, post: Post, text: str) -> Comment:
    comment = Comment(user=user, post=post, text=text)
    session.add(comment)
    session.commit()
    return comment


def query_comments_by_post(session: Session, post: Post) -> list[Comment]:
    comments = session.query(Comment).filter_by(post=post).all()
    return comments


def main():

    Base.metadata.create_all()

    session: Session = scop_session()

    user = create_user(session, "first___")
    user2 = create_user(session, "second___")
    create_post(session, user.id, 'title', 'text')
    post = query_posts_by_id(session, 1)
    create_comment(session, user2.id, post.id, 'text')
    comments = query_comments_by_post(session, post.id)
    print(comments[0])
    print(post.title, query_user_by_id(session, post.user))

    session.close()


if __name__ == '__main__':
    main()
