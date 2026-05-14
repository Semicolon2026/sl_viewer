from app.utils import load_targets

def test_load_targets():
    targets = load_targets("data/sample_targets.txt")

    assert len(targets) > 0
