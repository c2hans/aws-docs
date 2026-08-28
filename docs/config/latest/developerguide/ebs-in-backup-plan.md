---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ebs-in-backup-plan.html
---

# ebs-in-backup-plan
<a name="ebs-in-backup-plan"></a>

Check if Amazon Elastic Block Store (Amazon EBS) volumes are added in backup plans of AWS Backup. The rule is NON\_COMPLIANT if Amazon EBS volumes are not included in backup plans.

**Identifier:** EBS\_IN\_BACKUP\_PLAN

**Resource Types:** AWS::EC2::Volume

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d517c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
