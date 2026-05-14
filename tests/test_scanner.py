from app.scanner import get_rsync_version

def test_rsync_version():
    version = get_rsync_version()

    assert "rsync" in version.lower()
