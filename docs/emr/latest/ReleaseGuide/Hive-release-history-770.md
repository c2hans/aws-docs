---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Hive-release-history-770.html
---

# Amazon EMR 7.7.0 - Hive release notes
<a name="Hive-release-history-770"></a>

## Amazon EMR 7.7.0 - Hive changes
<a name="Hive-release-history-changes-770"></a>

| Type | Description |
| --- | --- |
| Bug Fix | Fixes CVE-2024-29869: Apache Hive: Credentials file created with non restrictive permissions. |
| Bug Fix | Fixes SemanticException when a row-level filtering policy is enabled in Apache Ran. |
| Bug Fix | Disable Tez Async Init RR when LLAP or ACID is enabled. |

**Known issues**
+ For Hive Insert Over-write queries with Amazon S3 Express One Zone as the output location, set the core-site config: `fs.s3a.directory.operations.purge.uploads` to `false`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
