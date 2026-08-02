---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

How to deploy the Live Streaming on AWS solution

This solution uses [AWS CloudFormation templates and stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) to automate its deployment. The CloudFormation template specifies the AWS resources included in this solution and their properties. The CloudFormation stack provisions the resources that are described in the template.

<a name="deployment-consideration"></a>== Deployment consideration

The Live Streaming on AWS solution configures AWS Elemental MediaLive with one of three progressive, 30 frames-per-second encoding profiles. You can choose one of the following encoding profiles.
+  **HD-1080p profile** - 1920x1080, 1280x720, 960x540, 768x432, 640x360, 512x288
+  **HD-720p profile** - 1280x720, 960x540, 768x432, 640x360, 512x288
+  **SD-540p profile** - 960x540, 768x432, 640x360, 512x288

**Important**
This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Policy](https://aws.amazon.com/privacy/). To opt out of this feature, download the template, modify the AWS CloudFormation mapping section, and then use the AWS CloudFormation console to upload your template and deploy the solution. For more information, refer to the [Anonymized data collection ](reference.md#anonymized-data-collection)section of this guide.

<a name="aws-cloudformation-template"></a>== AWS CloudFormation template

 [https://s3.amazonaws.com/solutions-reference/live-streaming-on-aws/latest/live-streaming-on-aws.template](https://s3.amazonaws.com/solutions-reference/live-streaming-on-aws/latest/live-streaming-on-aws.template) **live-streaming-on-aws.template** - Use this template to launch the solution and all associated components. The default configuration deploys an AWS Lambda function, an AWS Elemental MediaLive input and channel, an AWS Elemental MediaPackage channel, two Amazon CloudFront distributions, and an Amazon Simple Storage Service (Amazon S3) bucket for the demo HTML preview player, but you can also customize the template based on your specific needs.

<a name="step-1-launch-the-stack"></a>== Launch the stack

Before you launch the solution, review the cost, architecture, security, and other considerations discussed in this guide. Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately 20 minutes

This automated AWS CloudFormation template deploys the Live Streaming on AWS solution in the AWS Cloud.

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/) and select the button to launch the `live-streaming-on-aws` AWS CloudFormation template.

    [https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=LiveStreaming&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Flive-streaming-on-aws%2Flatest%2Flive-streaming-on-aws.template&redirectId=ImplementationGuide](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=LiveStreaming&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Flive-streaming-on-aws%2Flatest%2Flive-streaming-on-aws.template&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch this solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
This solution uses the AWS Elemental MediaLive, MediaPackage, and MediaConnect services, which are currently available in specific AWS Regions only. Therefore, you must launch this solution in an AWS Region where these services are available. For the most current service availability by Region, see the [AWS Regional Service List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your Live Streaming on AWS solution stack.

1. Under **Parameters**, review the parameters for the template, and modify them as necessary. This solution uses the following default values. Refer to the table below for detailed instruction for setting up each input type.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws/deploy-the-solution.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1. Choose **Submit** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 20 minutes.

   To test the live stream playback, navigate to the AWS CloudFormation stack **Outputs** tab, select the **Demo Console URL** from the **Value** column.

**Note**
In addition to the primary AWS Lambda function, this solution includes the `solution-helper` Lambda function, which runs only during initial configuration or when resources are updated or deleted.
When running this solution, both Lambda functions are displayed in the AWS Lambda console, do not delete the `solution-helper` function because it is necessary to manage associated resources.

Once the live streaming event is complete, stop the resources created by this solution to help ensure that you don’t incur unnecessary AWS charges.
