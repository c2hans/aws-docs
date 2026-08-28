---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/redshift-require-tls-ssl.html
---

# redshift-require-tls-ssl
<a name="redshift-require-tls-ssl"></a>

Checks if Amazon Redshift clusters require TLS/SSL encryption to connect to SQL clients. The rule is NON\_COMPLIANT if any Amazon Redshift cluster has parameter require\_SSL not set to true.

**Identifier:** REDSHIFT\_REQUIRE\_TLS\_SSL

**Resource Types:** AWS::Redshift::Cluster, AWS::Redshift::ClusterParameterGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Mexico (Central) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1315c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
