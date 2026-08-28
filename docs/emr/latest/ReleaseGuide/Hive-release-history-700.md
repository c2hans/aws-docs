---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-700.html
---

# Amazon EMR 7.0.0 - Hive release notes
<a name="Hive-release-history-700"></a>

## Amazon EMR 7.0.0 - Hive changes
<a name="Hive-release-history-changes-700"></a>

| Type | Description |
| --- | --- |
| Upgrade | Hive Runtime now uses Java 17 by default. Please refer [EMR 7.0.0 Release Guide](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-700-release.html) for more details. |
| Backport | [HIVE-17709](https://issues.apache.org/jira/browse/HIVE-17709): remove sun.misc.Cleaner references |
| Bug Fix | Disable Tez Async Init RR when LLAP or ACID is enabled  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
