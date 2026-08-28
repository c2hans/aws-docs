---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-platform-check.html
---

# ec2-managedinstance-platform-check
<a name="ec2-managedinstance-platform-check"></a>

Checks whether EC2 managed instances have the desired configurations.

**Identifier:** EC2\_MANAGEDINSTANCE\_PLATFORM\_CHECK

**Resource Types:** AWS::SSM::ManagedInstanceInventory

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

platformTypeType: String
Platform type (for example, 'Linux').

platformVersion (Optional)Type: String
Platform version (for example, '2016.09').

agentVersion (Optional)Type: String
Agent version (for example, '2.0.433.0').

platformName (Optional)Type: String
The name of the platform (for example, 'Amazon Linux')

## AWS CloudFormation template
<a name="w2aac20c16c17b7d589c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
