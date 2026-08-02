---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/launch-the-stack.html
---

# Launch the stack (default, CloudFront \+ S3 hosted web console)
<a name="launch-the-stack"></a>

Follow these steps to deploy the Distributed Load Testing on AWS solution into your account. This automated AWS CloudFormation template deploys Distributed Load Testing on AWS.

1. Sign in to the AWS Management Console and select the button to launch the CloudFormation template.

    [https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws.template&redirectId=ImplementationGuide](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws.template&redirectId=ImplementationGuide)

   Alternatively, you can [download the template](https://solutions-reference.s3.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws.template) as a starting point for your own implementation.

1. The template is launched in the US East (N. Virginia) Region by default. To launch this solution in a different AWS Region, use the region selector in the console navigation bar.
**Note**
This solution uses Amazon Cognito, which is currently available in specific AWS Regions only. Therefore, you must launch this solution in an AWS Region where Amazon Cognito is available. For the most current service availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/launch-the-stack.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Check the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1. Choose **Create stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 15 minutes.

**Note**
In addition to the primary AWS Lambda function, this solution includes the custom-resource Lambda function, which runs only during initial configuration or when resources are updated or deleted.

When running this solution, the custom-resource Lambda function is inactive. However, do not delete this function as it is necessary to manage associated resources.
