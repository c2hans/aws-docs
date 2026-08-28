---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/redshift-cluster-multi-az-enabled.html
---

# redshift-cluster-multi-az-enabled
<a name="redshift-cluster-multi-az-enabled"></a>

Checks if an Amazon Redshift cluster has multiple Availability Zones deployments enabled. This rule is NON\_COMPLIANT if Amazon Redshift cluster does not have multiple Availability Zones deployments enabled.

**Identifier:** REDSHIFT\_CLUSTER\_MULTI\_AZ\_ENABLED

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Mexico (Central), US West (N. California), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1301c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
