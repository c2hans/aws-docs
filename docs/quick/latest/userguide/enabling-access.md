---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/enabling-access.html
---

# Authorizing connections from Amazon Quick Sight to AWS data stores
<a name="enabling-access"></a>

|  |
| --- |
|    Applies to: Enterprise Edition and Standard Edition  |

|  |
| --- |
|    Intended audience:  System administrators  |

For Amazon Quick Sight to access your AWS resources, you must create security groups for them that authorize connections from the IP address ranges used by Amazon Quick Sight servers. You must have AWS credentials that permit you to access these AWS resources to modify their security groups.

Use the procedures in the following sections to enable Amazon Quick Sight connections.

**Topics**
+ [Authorizing connections from Amazon Quick Sight to Amazon RDS DB instances](enabling-access-rds.md)
+ [Authorizing connections from Amazon Quick Sight to Amazon Redshift clusters](enabling-access-redshift.md)
+ [Authorizing connections from Amazon Quick to Amazon EC2 instances](enabling-access-ec2.md)
+ [Authorizing connections through AWS Lake Formation](lake-formation.md)
+ [Authorizing connections to Amazon OpenSearch Service](opensearch.md)
+ [Authorizing connections to Amazon Athena](athena.md)
+ [Data access integrations](data-access-integrations.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
