from pytest import fixture

from models import (
    Desk,
    Member,
    Bot,
    User,
    Bag
)


@fixture
def desk_d() -> Desk:
    return Desk()


class TestDesk():
    def test_init(self, desk_d):
        assert desk_d.numbers == 15
        assert len(desk_d.rows) == 3
        assert len(desk_d.rows[1]) == 9
        assert len(list(filter(('-').__ne__, desk_d.rows[1]))) == 5

    def test_cross_out(self, desk_d):
        desk_d.cross_out(list(filter(('-').__ne__, desk_d.rows[1]))[0])
        assert len(list(filter(('-').__ne__, desk_d.rows[1]))) == 4
        assert desk_d.numbers == 14


@fixture
def member_d() -> Member:
    return Member('somename')

@fixture
def bot_d() -> Bot:
    return Bot()

@fixture
def user_d() -> User:
    return User('username')


class TestMember:
    def test_init(self, member_d):
        assert member_d.name == 'somename'
        assert isinstance(member_d.desk, Desk)


class TestUser:
    def test_init(self, user_d):
        assert user_d.name == 'username'
        assert isinstance(user_d.desk, Desk)


class TestBot:
    def test_init(self, bot_d):
        assert bot_d.name == 'username'
        assert isinstance(bot_d.desk, Desk)


@fixture
def bag_d() -> Member:
    return Bag()


class TestBag:
    def test_init(self, bag_d):
        assert len(bag_d.numbers) == 90

    def test_get_num(self, bag_d):
        isinstance(bag_d.get_num(), int)
        assert len(bag_d.numbers) == 89




