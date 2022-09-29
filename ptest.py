
import pytest


@pytest.mark.parametrize("username,password",
                                [
                                    ('user', 'Pass@123'),
                                    ("abc", "welcome@123"),
                                    ("Kavita", "12345"),
                                    ("sumit", "9876")
                                ]
                        )
def test_login(username, password):
    print(f"{username} : {password}")

    if(username != "CT11User" and password != 'Pass@123'):
        assert False