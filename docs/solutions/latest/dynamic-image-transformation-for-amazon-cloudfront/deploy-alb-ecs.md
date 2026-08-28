---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/deploy-alb-ecs.html
---

# Deploy ECS architecture
<a name="deploy-alb-ecs"></a>

Follow the step-by-step instructions in this section to configure and deploy the high-performance ECS architecture into your account.

 **Time to deploy:** Approximately 20 minutes

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and select the button to launch the `dynamic-image-transformation-for-amazon-cloudfront-ecs` AWS CloudFormation template.

1. Sign into [AWS Management Console](https://aws.amazon.com/console) and select the button to launch `dynamic-image-transformation-for-amazon-cloudfront-ecs` CloudFormation template. [![Launch solution](http://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=DynamicImageTransformationForAmazonCloudFront&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fdynamic-image-transformation-for-amazon-cloudfront%2Flatest%2Fdynamic-image-transformation-for-amazon-cloudfront-ecs.template&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar. For a list of which AWS Regions support this solution, see [Supported AWS Regions](supported-aws-regions.md).

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
