import unittest
from io import StringIO

import pylint.lint as pylint
from flake8.api import legacy as flake8
from pylint.reporters import text


class Tests(unittest.TestCase):
    def test_flake8(self):
        style_guide = flake8.get_style_guide()
        report = style_guide.check_files(["chatwatch", "examples"])
        assert report.get_statistics("E") == [], "Flake8 found violations"

    def test_pylint(self):
        stdout = StringIO()
        reporter = text.TextReporter(stdout)
        opts = ["--score=no", "chatwatch"]
        pylint.Run(opts, reporter=reporter, do_exit=False)
        out = reporter.out.getvalue()
        failed = bool(out)
        assert not failed, "Pylint found violations"

    def test_import(self):
        import chatwatch


if __name__ == '__main__':
    unittest.main()
