---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ebs-snapshot-public-restorable-check.html
---

# ebs-snapshot-public-restorable-check
<a name="ebs-snapshot-public-restorable-check"></a>

Checks if Amazon Elastic Block Store (Amazon EBS) snapshots are not publicly restorable. The rule is NON\_COMPLIANT if one or more individual snapshots with RestorableByUserIds field are set to all.

**Identifier:** EBS\_SNAPSHOT\_PUBLIC\_RESTORABLE\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Europe (Spain) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d531c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
