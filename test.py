import unittest
from io import StringIO

from flake8.api import legacy as flake8
from pylint import lint
from pylint.reporters import text


class MyTestCase(unittest.TestCase):
    def test_flake8(self):
        style_guide = flake8.get_style_guide()
        report = style_guide.check_files(["chatwatch"])
        assert report.get_statistics("E") == [], "Flake8 found violations"

    def test_pylint(self):
        stdout = StringIO()
        reporter = text.TextReporter(stdout)
        opts = ["chatwatch"]
        lint.Run(opts, reporter=reporter, do_exit=False)
        out = reporter.out.getvalue()

        assert bool(out), "Pylint found violations"

    def test_import(self):
        import chatwatch



if __name__ == '__main__':
    unittest.main()
