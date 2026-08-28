---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/launch-the-stack.html
---

# Launch the stack
<a name="launch-the-stack"></a>

This automated AWS CloudFormation template deploys DeepRacer on AWS.

1. Sign in to the AWS Management Console and select the button to launch the CloudFormation template.

    [![Launch solution.](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/deepracer-on-aws/latest/deepracer-on-aws.template&redirectId=ImplementationGuide)

   Alternatively, you can [download the template](https://solutions-reference.s3.amazonaws.com/deepracer-on-aws/latest/deepracer-on-aws.template) as a starting point for your own implementation.

1. The template is launched in the US East (N. Virginia) region by default. To launch this solution in a different AWS region, use the region selector in the console navigation bar.
**Note**
This solution uses Amazon Cognito, which is currently available in specific AWS Regions only. Therefore, you must launch this solution in an AWS Region where Amazon Cognito is available. For the most current service availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.
**Important**
This solution provisions log groups that are set to be retained following stack deletion. If you have previously deployed DeepRacer on AWS, be sure to provide a unique stack name to prevent the deployment from failing due to log groups with the same name already existing.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/launch-the-stack.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Be sure to check the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1. Choose **Create stack** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately five minutes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
