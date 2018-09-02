from gecko.validators import USER_TITLE_PATTERN as pattern


def test_user_title_pattern():
    assert pattern.match('nickname')
    assert pattern.match('nickname123')
    assert pattern.match('nickname_123')
    assert pattern.match('nickname_NICKNAME')
    assert pattern.match('NICKNAME')
    assert pattern.match('NICK123NAME')
    assert pattern.match('NICK123name')
    assert pattern.match('nick123NAME')
    assert pattern.match('nick123name')

    assert not pattern.match('0nickname')
    assert not pattern.match('nickname@')
    assert not pattern.match('nick name')
    assert not pattern.match('nick-name')
    assert not pattern.match('123456')
    assert not pattern.match('nick')
    assert not pattern.match('nick+name')
    assert not pattern.match('nick@name')
    assert not pattern.match('nick^name')
    assert not pattern.match('nick&name')
    assert not pattern.match('nick*name')
    assert not pattern.match('nick(name')
    assert not pattern.match('nick)name')
    assert not pattern.match('nick~name')
    assert not pattern.match('nick`name')
    assert not pattern.match('nick!name')
    assert not pattern.match('nick%name')
    assert not pattern.match('nick<name')
    assert not pattern.match('nick>name')
    assert not pattern.match('nick/name')
    assert not pattern.match('nick\name')
    assert not pattern.match('nickname_nickname_')
    assert not pattern.match('nick,ame')
    assert not pattern.match('nick:ame')
    assert not pattern.match('nick;ame')
    assert not pattern.match('nick\'ame')
    assert not pattern.match('nick"name')

