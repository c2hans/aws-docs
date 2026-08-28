---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ebs-snapshot-block-public-access.html
---

# ebs-snapshot-block-public-access
<a name="ebs-snapshot-block-public-access"></a>

Checks if block public access is enabled for Amazon EBS snapshots in an AWS Region. The rule is NON\_COMPLIANT if block public access is not enabled for all public sharing of EBS snapshots in an AWS Region.

**Identifier:** EBS\_SNAPSHOT\_BLOCK\_PUBLIC\_ACCESS

**Resource Types:** AWS::EC2::SnapshotBlockPublicAccess

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d529c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
