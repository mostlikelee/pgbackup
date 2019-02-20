import pytest
import subprocess

from pgbackup import pgdump 

url = "postgres://bob:password@example.com:5432/db_one"

def test_dump_call_pgdump(mocker):
    """
    utilize pgdump to interact with database
    """
    proc = mocker.Mock()
    mocker.patch('subprocess.Popen', return_value=proc)
    assert pgdump.dump(url) == proc
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)

def test_dump_handles_oserror(mocker):
    """
    pg_dump.dump returns a resonable error if pg_dump isn't installed
    """
    mocker.patch('subprocess.Popen', side_effect=OSError("no such file"))
    with pytest.raises(SystemExit):
        pgdump.dump(url)
