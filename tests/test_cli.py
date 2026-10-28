from shopkit.cli import main


def test_list(capsys):
    assert main(["list", "--category", "pantry"]) == 0
    out = capsys.readouterr().out
    assert "Green Tea" in out and "Blue Mug" not in out


def test_quote(capsys):
    assert main(["quote", "MUG-BLU:2"]) == 0
    out = capsys.readouterr().out
    assert "Subtotal: $25.00" in out
    assert "Total:    $27.00" in out


def test_quote_unknown_sku(capsys):
    assert main(["quote", "NOPE:1"]) == 2
