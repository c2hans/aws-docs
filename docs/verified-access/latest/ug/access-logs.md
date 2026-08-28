---
source_url: https://docs.aws.amazon.com/verified-access/latest/ug/access-logs.html
---

# Verified Access logs
<a name="access-logs"></a>

After AWS Verified Access evaluates each access request, it logs all access attempts. This provides you with centralized visibility into application access, and helps you quickly respond to security incidents and audit requests. Verified Access supports the Open Cybersecurity Schema Framework (OCSF) logging format.

When you enable logging, you need to configure a destination for the logs to be sent. The IAM principal being used to configure the logging destination needs to have certain permissions for logging to work properly. The required IAM permissions for each logging destination can be seen in the [Verified Access logging permissions](access-logs-permissions.md) section. Verified Access supports the following destinations for publishing access logs:
+ Amazon CloudWatch Logs log groups
+ Amazon S3 buckets
+ Amazon Data Firehose delivery streams

**Topics**
+ [Verified Access logging versions](logging-versions.md)
+ [Verified Access logging permissions](access-logs-permissions.md)
+ [Enable or disable Verified Access logs](access-logs-enable.md)
+ [Enable or disable Verified Access trust context](include-trust-context.md)
+ [OCSF version 0.1 log examples for Verified Access](ocsfv01-examples.md)
+ [OCSF version 1.0.0-rc.2 log examples for Verified Access](ocsfv1-examples.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Verified Access. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verified-access` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
