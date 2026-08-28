---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/msk-cluster-public-access-disabled.html
---

# msk-cluster-public-access-disabled
<a name="msk-cluster-public-access-disabled"></a>

Checks if public access is disabled on Amazon MSK clusters. The rule is NON\_COMPLIANT if public access on an Amazon MSK cluster is not disabled.

**Identifier:** MSK\_CLUSTER\_PUBLIC\_ACCESS\_DISABLED

**Resource Types:** AWS::MSK::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1123c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
