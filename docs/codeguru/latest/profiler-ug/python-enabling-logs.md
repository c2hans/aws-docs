---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-enabling-logs.html
---

# Enabling logs
<a name="python-enabling-logs"></a>

The Amazon CodeGuru Profiler agent uses the `logging` library. It only uses logs at or below the `INFO` level. To see the logs, include `logging.basicConfig(level=logging.INFO)` or `logging.getLogger('codeguru_profiler_agent').setLevel(logging.INFO)` in your handler code.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
