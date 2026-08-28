---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/wkld-06.html
---

# WKLD.06 Use Systems Manager instead of SSH or RDP
<a name="wkld-06"></a>

*Public subnets*, which have a default route pointing to an internet gateway, present a greater security risk than *private subnets*, which have no route to the internet. You can run Amazon EC2 instances in private subnets and use the Session Manager capability of AWS Systems Manager to remotely access the instances through either the AWS Command Line Interface (AWS CLI) or AWS Management Console. You can then use the AWS CLI or console to start a session that connects into the instance through a secure tunnel, which removes the need to manage credentials for Secure Shell (SSH) or Windows remote desktop protocol (RDP).

Use Session Manager instead of running Amazon EC2 instances in public subnets or running bastion hosts.

**To set up Session Manager**

1. Verify that the Amazon EC2 instance uses a supported operating system Amazon Machine Image (AMI), such as Amazon Linux or Ubuntu, with the AWS Systems Manager Agent (SSM Agent) pre-installed.

1. Confirm that the instance has connectivity, either through an internet gateway or through VPC endpoints, to the following endpoints (replacing `<Region>` with the appropriate AWS Region):
   + `ec2messages.<Region>.amazonaws.com`
   + `ssm.<Region>.amazonaws.com`
   + `ssmmessages.<Region>.amazonaws.com`

1. Attach the `AmazonSSMManagedInstanceCore` AWS managed policy to the IAM role associated with your instances.

For more information, see [Setting up Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started.html) in the *AWS Systems Manager User Guide*.

**To start a session**

1. See [Starting a session](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-start.html#start-sys-console) in the Systems Manager documentation.

**Note**
Session Manager is available at no additional charge for Amazon EC2 instances. If you use VPC endpoints for Session Manager connectivity, interface endpoints incur an hourly charge and a per-GB data-processing charge. For more information, see [Systems Manager pricing](https://aws.amazon.com/systems-manager/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
