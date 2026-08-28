---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ec2-spot-fleet-request-ct-encryption-at-rest.html
---

# ec2-spot-fleet-request-ct-encryption-at-rest
<a name="ec2-spot-fleet-request-ct-encryption-at-rest"></a>

Checks if Amazon EC2 Spot Fleet request launch parameters set encrypted to True for attached EBS volumes. The rule is NON\_COMPLIANT if any EBS volumes has encrypted set to False. The rule does not evaluate spot fleet requests using launch templates.

**Identifier:** EC2\_SPOT\_FLEET\_REQUEST\_CT\_ENCRYPTION\_AT\_REST

**Resource Types:** AWS::EC2::SpotFleet

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d615c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
