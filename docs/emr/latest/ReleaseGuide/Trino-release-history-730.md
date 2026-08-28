---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Trino-release-history-730.html
---

# Amazon EMR 7.3.0 - Trino release notes
<a name="Trino-release-history-730"></a>

## Amazon EMR 7.3.0 - Trino changes
<a name="Trino-release-history-changes-730"></a>
+ This release upgrades Trino from version 436 to 442.
+ This release redirects Hudi queries to the new Hudi corrector. The old Hive connector can no longer read Hudi tables. Note
+ This release removes the Rubix module from Amazon EMR because it is now deprecated from open-source.
+ This release [ removes legacy mode](https://github.com/trinodb/trino/pull/21013) in the `hive.security` property. The default is now `allow-all`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
