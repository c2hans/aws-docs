---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/deploying-a-standalone-agent-use-case.html
---

# Deploying a standalone Bedrock Agent use case
<a name="deploying-a-standalone-agent-use-case"></a>

Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately 10-30 minutes

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and select the button to launch the CloudFront template.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/deploying-a-standalone-agent-use-case.html)

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
This solution uses Amazon Bedrock, which is not currently available in all AWS Regions. If you’re using these features, you must launch this solution in an AWS Region where these services are available. For the most current availability by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, see {https---docs-aws-amazon-com-https---docs-aws-amazon-com-IAM-latest-UserGuide-reference-iam-limits-html}[IAM and AWS STS quotas] in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/deploying-a-standalone-agent-use-case.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1. Choose **Create stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 10-30 minutes.
