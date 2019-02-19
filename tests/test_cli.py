import pytest

from pgbackup import cli

url = "postgres://bob:password@example.com:5432/db_one"

def test_parser_without_driver():
    """
    Without a specified driver the parser will exit
    """
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([url])

def test_parser_with_driver():
    """
    The parser will exit if it recieves a driver without a destination
    """
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'local'])

def test_parser_with_driver_and_destination():
    """
    The parser will not exit if it receives a driver and a destination
    """
    parser = cli.create_parser()
    args = parser.parse_args([url, '--driver', 'local', '/usr/local/backup.sql'])

    assert args.driver == 'local'
    assert args.destination == '/usr/local/backup.sql'