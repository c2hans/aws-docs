---
source_url: https://docs.aws.amazon.com/dtconsole/latest/userguide/limits-connections.html
---

# Quotas for connections
<a name="limits-connections"></a>

The following tables list the quotas (also referred to as *limits*) for connections in the Developer Tools console.

Quotas in this table apply per AWS Region and can be increased. For AWS Region information and quotas that can be changed, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

**Note**
You must enable the Europe (Milan) AWS Region before you can use it. For more information, see [ Enabling a Region](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable).

| Resource | Default limit |
| --- | --- |
| Maximum number of connections per AWS account | 250 |

Quotas in this table are fixed and cannot be changed.

| Resource | Default limit |
| --- | --- |
| Maximum characters in connection names | 32 characters |
| Maximum number of hosts per AWS account | 50 |
| Maximum number of repository links | 100 |
| Maximum number of CloudFormation stack sync configurations | 100 |
| Maximum number of sync configurations per repository link | 100 |
| Maximum number of sync configurations per branch | 50 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Developer Tools Console. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dtconsole` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
