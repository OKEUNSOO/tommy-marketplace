# Supported Job Sites

The skill-local fetch router currently dispatches URLs by substring:

| URL pattern | Parser |
| --- | --- |
| `jumpit` | `scripts/parsers/dynamic.py::build_jumpit` |
| `rallit` | `scripts/parsers/dynamic.py::build_rallit` |
| `zighang` | `scripts/parsers/dynamic.py::build_zighang` |
| `wanted` | `scripts/parsers/dynamic.py::build_wanted` |
| `groupby`, `grpby` | `scripts/parsers/dynamic.py::build_groupby` |
| `jasoseol` | `scripts/parsers/dynamic.py::build_jasoseol` |
| `jobkorea` | `scripts/parsers/jobkorea.py` |
| `saramin` | `scripts/parsers/saramin.py` |
| `samsungcareers.com/hr/?no=` | `scripts/parsers/samsungcareers.py` |
| anything else | `scripts/parsers/general.py` |

The dynamic parsers avoid app-level Gemini refinement. They produce direct Markdown from DOM text, then Codex should apply `references/formatting-rules.md` when cleaned output is needed. If a site blocks browser automation or renders content behind login, return the precise error and ask the user for pasted JD text or a screenshot.
