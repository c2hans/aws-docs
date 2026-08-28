---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/agent-installations-in-aws.html
---

# Using an instance profile for agent installation in AWS
<a name="agent-installations-in-aws"></a>

When installing the AWS Replication Agent on an Amazon EC2 instance (when the source and recovery servers are both in AWS Regions), you don't need to generate credentials. Instead, you can use an instance profile with the required IAM policy. For the actual agent installation steps, see [Installing on Linux](linux-agent.md) or [Installing on Windows](windows-agent.md).
+ Go to the EC2 console and select your EC2 instance.
+ From the top right-hand menu, select **Actions > Security > Modify IAM role**.
+ Use a role that contains the [AWSElasticDisasterRecoveryEc2InstancePolicy](security-iam-awsmanpol-AWSElasticDisasterRecoveryEc2InstancePolicy.md) policy.

  If none exists, click **Create new IAM role**, attach the policy and return to the EC2 console window.
+ Select your new role from the drop-down list and click **Update**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
