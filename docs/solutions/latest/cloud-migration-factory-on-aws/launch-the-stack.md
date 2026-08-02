---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/launch-the-stack.html
---

# Step 2: Launch the stack
<a name="launch-the-stack"></a>

**Important**
This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Policy](https://aws.amazon.com/privacy/).
To opt out of this feature, download the template, modify the AWS CloudFormation mapping section, and then use the AWS CloudFormation console to upload your template and deploy the solution. For more information, refer to the [Anonymized data collection](anonymized-data-collection.md) section of this guide.

This automated AWS CloudFormation template deploys the Cloud Migration Factory on AWS solution in the AWS Cloud.

**Note**
You are responsible for the cost of the AWS services used while running this solution. Refer to the [Cost](cost.md) section for more details. For full details, refer to the pricing webpage for each AWS service you will be using in this solution.

1. Sign into [AWS Management Console](https://aws.amazon.com/console) and select the button to launch `cloud-migration-factory-solution` CloudFormation template. [https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fsolutions-reference.s3.amazonaws.com%2Fcloud-migration-factory-on-aws%2Flatest%2Faws-cloud-migration-factory-solution.template](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fsolutions-reference.s3.amazonaws.com%2Fcloud-migration-factory-on-aws%2Flatest%2Faws-cloud-migration-factory-solution.template)

   You can also [download the template](https://solutions-reference.s3.amazonaws.com/cloud-migration-factory-on-aws/latest/aws-cloud-migration-factory-solution.template&redirectId=ImplementationGuide) as a starting point for your own implementation.

1. The template launches in the US East (N. Virginia) Region by default. To launch this solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
This solution uses Amazon Cognito and Amazon QuickSight, which are currently available in specific AWS Regions only. Therefore, you must launch this solution in an AWS Region where these services are available. For the most current availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).
When deployed in Public and Public with WAF deployment types, the solution also uses Amazon CloudFront logging to Amazon S3. Today, log delivery from Amazon CloudFront to Amazon S3 is only available in specific Regions. Refer to [Choosing an Amazon S3 bucket for your standard logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html#access-logs-choosing-s3-bucket) to verify your Region is supported.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/launch-the-stack.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Check the boxes acknowledging that the template will create [AWS Identity and Access Management](https://aws.amazon.com/iam) (IAM) resources and that it might require the capability **CAPABILITY\_AUTO\_EXPAND**.

1. Choose **Submit** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 20 minutes.

**Important**
If you are using AWS MGN, you must complete the prerequisite for AWS MGN before continuing to Step 3.
