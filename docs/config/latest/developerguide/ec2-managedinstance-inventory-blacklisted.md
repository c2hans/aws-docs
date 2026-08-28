---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-inventory-blacklisted.html
---

# ec2-managedinstance-inventory-blacklisted
<a name="ec2-managedinstance-inventory-blacklisted"></a>

Checks whether instances managed by Amazon EC2 Systems Manager are configured to collect blacklisted inventory types.

**Identifier:** EC2\_MANAGEDINSTANCE\_INVENTORY\_BLACKLISTED

**Resource Types:** AWS::SSM::ManagedInstanceInventory

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

inventoryNamesType: CSV
Comma separated list of Systems Manager inventory types (for example, 'AWS:Network, AWS:WindowsUpdate').

platformType (Optional)Type: String
Platform type (for example, 'Linux').

## AWS CloudFormation template
<a name="w2aac20c16c17b7d585c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
