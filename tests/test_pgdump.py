import pytest
import subprocess

from pgbackup import pgdump
from mock import mocker

url = "postgres://bob:password@example.com:5432/db_one"

def test_dump_call_pgdump(mocker):
    """
    utilize pgdump to interact with database
    """
    mocker.patch('subprocess.Popen')
    assert pgdump.dump(url)
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)