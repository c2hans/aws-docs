---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/managing-gdu-agent-ec2-manually.html
---

# Managing security agent manually for Amazon EC2 resource
<a name="managing-gdu-agent-ec2-manually"></a>

This section provides the steps to manually install and update the security agent for your Amazon EC2 resources.

After you enable Runtime Monitoring, you will need to install the GuardDuty security agent manually. To manage the GuardDuty security agent manually, you must first create an Amazon VPC endpoint manually. After this, you can install the security agent so that GuardDuty will start receiving the runtime events from the Amazon EC2 instances. When GuardDuty releases a new agent version for this resource, you can update the agent version in your account.

The following topics include the steps to continuously manage the security agent for your Amazon EC2 resources.

**Topics**
+ [Prerequisite – Creating Amazon VPC endpoint manually](creating-vpc-endpoint-ec2-agent-manually.md)
+ [Installing the security agent manually](installing-gdu-security-agent-ec2-manually.md)
+ [Updating the GuardDuty security agent for Amazon EC2 instance manually](gdu-update-security-agent-ec2.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
