---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-applications-required.html
---

# ec2-managedinstance-applications-required
<a name="ec2-managedinstance-applications-required"></a>

Checks if all of the specified applications are installed on the instance. Optionally, specify the minimum acceptable version. You can also specify the platform to apply the rule only to instances running that platform.

**Note**
Ensure that SSM agent is running on the EC2 instance and an association to gather application software inventory is created. The rule returns `NOT_APPLICABLE` if SSM agent is not installed or an association is not yet created or running.

**Identifier:** EC2\_MANAGEDINSTANCE\_APPLICATIONS\_REQUIRED

**Resource Types:** AWS::SSM::ManagedInstanceInventory

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

applicationNamesType: CSV
Comma-separated list of application names. Optionally, specify versions appended with ':' (for example, 'Chrome:0.5.3, Firefox').
The application names must be an exact match. For example, use **firefox** on Linux or **firefox-compat** on Amazon Linux. In addition, AWS Config does not currently support wildcards for the *applicationNames* parameter (for example, **firefox\***).

platformType (Optional)Type: String
Platform type (for example, 'Linux' or 'Windows').

## AWS CloudFormation template
<a name="w2aac20c16c17b7d581c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
