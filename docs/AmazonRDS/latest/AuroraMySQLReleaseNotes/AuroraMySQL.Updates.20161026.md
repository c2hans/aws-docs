---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.20161026.html
---

# Aurora MySQL database engine updates: 2016-10-26 (version 1.8.1) (Deprecated)
<a name="AuroraMySQL.Updates.20161026"></a>

**Version:** 1.8.1

## Improvements
<a name="AuroraMySQL.Updates.20161026.Improvements"></a>
+ Fixed an issue where bulk inserts that use triggers that invoke AWS Lambda procedures fail.
+ Fixed an issue where catalog migration fails when autocommit is off globally.
+ Resolved a connection failure to Aurora when using SSL and improved Diffie-Hellman group to deal with LogJam attacks.

## Integration of MySQL bug fixes
<a name="AuroraMySQL.Updates.20161026.BugFixes"></a>
+ OpenSSL changed the Diffie-Hellman key length parameters due to the LogJam issue. (Bug \#18367167)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
