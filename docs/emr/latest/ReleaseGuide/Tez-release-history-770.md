---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Tez-release-history-770.html
---

# Amazon EMR 7.7.0 - Tez release notes
<a name="Tez-release-history-770"></a>

## Amazon EMR 7.7.0 - Tez changes
<a name="Tez-release-history-changes-770"></a>

| Type | Description |
| --- | --- |
| Improvement | The tez.task.relaxed.locality property in Apache Tez controls whether task scheduling strictly follows data locality constraints (rack and node locality). When set to true (default in EMR-7.6\+), Tez does not enforce locality, allowing tasks to be assigned to any available container, which improves resource utilization and reduces wait times in busy clusters. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
