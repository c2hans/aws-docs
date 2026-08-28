---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-association-compliance-status-check.html
---

# ec2-managedinstance-association-compliance-status-check
<a name="ec2-managedinstance-association-compliance-status-check"></a>

Checks if the status of the AWS Systems Manager association compliance is COMPLIANT or NON\_COMPLIANT after the association execution on the instance. The rule is compliant if the field status is COMPLIANT. For more information about associations, see [What is an association?](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html#state-manager-association-what-is).

**Identifier:** EC2\_MANAGEDINSTANCE\_ASSOCIATION\_COMPLIANCE\_STATUS\_CHECK

**Resource Types:** AWS::SSM::AssociationCompliance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Osaka), Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d583c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
