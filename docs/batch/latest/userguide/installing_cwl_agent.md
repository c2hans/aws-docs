---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/installing_cwl_agent.html
---

# Install and configure the CloudWatch agent
<a name="installing_cwl_agent"></a>

You can create an Amazon EC2 launch template that includes CloudWatch monitoring. For more information, see [ Launch an instance from a launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#lt-initiate-launch-template) and [ Advanced details](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#lt-advanced-details) in the *Amazon EC2 User Guide*.

You can also install the CloudWatch agent on an existing Amazon EC2 AMI and then specify the image in the AWS Batch first-run wizard. For more information, see [ Installing the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html) and [Getting started with AWS Batch tutorials](Batch_GetStarted.md).

**Note**
Launch templates are not supported on AWS Fargate resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
