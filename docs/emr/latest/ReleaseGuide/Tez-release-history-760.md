---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-760.html
---

# Amazon EMR 7.6.0 - Tez release notes
<a name="Tez-release-history-760"></a>

## Amazon EMR 7.6.0 - Tez changes
<a name="Tez-release-history-changes-760"></a>

| Type | Description |
| --- | --- |
| Improvement | Rack and node locality constraints won't be considered while requesting container for a task by changing default of tez.task.relaxed.locality to false |
| Improvement | Tune configs to disable delay due to locality and allow non-local fallback |
| Improvement | [TEZ-4547](https://issues.apache.org/jira/browse/TEZ-4547): Add Tez AM JobID to the JobConf |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
