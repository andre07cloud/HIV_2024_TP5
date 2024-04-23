def test_strong_password_checker(strong_password_checker):
    assert strong_password_checker("a") == 5
    assert strong_password_checker("aA1") == 2
    assert strong_password_checker("1337C0d3") == 0
    assert strong_password_checker("312312312") == 2
    assert strong_password_checker("abc") == 2
    assert strong_password_checker("Abc123") == 0
    assert strong_password_checker("aaaccxxxyyyzzz") == 3
    assert strong_password_checker("aaabbcccxxxxx") == 3
    assert strong_password_checker("aaabbccccxxxxx") == 2
    assert strong_password_checker("aaaabbbbccccxxxxx") == 1
    assert strong_password_checker("aaaaaaaaaaaaaaaaaaaaa") == 5
    assert strong_password_checker("aaaaaaaaaaaaaaaaaaaaaa") == 4
    assert strong_password_checker("aaaaaaaaaaaaaaaaaaaaaaa") == 3
    assert strong_password_checker("aaaaaaaaaaaaaaaaaaaaaaaa") == 2
    assert strong_password_checker("aaaaaaaaaaaaaaaaaaaaaaaaa") == 1
