import pytest

from pgbackup import cli

url = "postgres://bob:password@example.com:5432/db_one"

@pytest.fixture()
def parser():
    return cli.create_parser()

def test_parser_without_driver(parser):
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url])

def test_parser_with_driver(parser):
    """
    The parser will exit if it recieves a driver without a destination
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'local'])

def test_parser_with_driver_and_destination(parser):
    """
    The parser will not exit if it receives a driver and a destination
    """
    args = parser.parse_args([url, '--driver', 'local', '/usr/local/backup.sql'])

    assert args.driver == 'local'
    assert args.destination == '/usr/local/backup.sql'

def test_parser_with_unknown_driver(parser):
    """
    The parser will exit if the driver name is unknown
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'foo', '/my/path'])

def test_parser_with_known_drivers(parser):
    """
    The parser will not exit if the driver name is known
    """
    for driver in ['local', 's3']:
        assert parser.parse_args([url, '--driver', driver, 'destination'])
