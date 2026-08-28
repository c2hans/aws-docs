---
source_url: https://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/automated-deployment.html
---

# Automated deployment
<a name="automated-deployment"></a>

 Before you launch the automated deployment, review the architecture, configuration, network security, and other considerations discussed in this guide. Follow the step-by-step instructions in this section to configure and deploy the guidance into your account.

 **Time to deploy:** Approximately 60 minutes.

## Prerequisites
<a name="prerequisites"></a>

 Before deploying this guidance, verify that you have an administrator role in [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) in your AWS account. Refer to [Roles and permissions](roles-and-permissions.md) for details on permissions used by this guidance. For information about setting up an administrator user, refer to [Create an administrative user](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin) in the *AWS Identity and Access Management User Guide*.

Also, verify that the Data Catalog settings allow for access control using IAM by navigating to the AWS Lakeformation Console. In the navigation pane on the left, go to **Data catalog – Settings** and make sure that the options **Use only IAM access for new databases** and **Use only IAM access for new tables in new databases** options are selected under **Default permissions for newly created databases and tables**.

 Before you explore the data in this guidance using [Quick](https://aws.amazon.com/quicksight/), you must first sign up for an Quick subscription. For more information about signing up for Quick, refer to [Signing up for an Quick subscription](https://docs.aws.amazon.com/quicksight/latest/user/signing-up.html) in the *Quick User Guide*.

## Launch the stack
<a name="launch-the-stack"></a>

**Important**
 This guidance includes an option to send anonymous operational metrics to AWS. We use this data to better understand how customers use this guidance and related services and products. AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Policy](https://aws.amazon.com/privacy/).
 To opt out of this feature, download the template, modify the AWS CloudFormation mapping section, and then use the AWS CloudFormation console to upload your template and deploy the guidance. For more information, refer to the [Collection of operational metrics](collection-of-operational-metrics.md) section of this guide.

 This automated AWS CloudFormation template deploys the guidance in the AWS Cloud. You must have the appropriate IAM permissions before launching the stack.

**Note**
You are responsible for the cost of the AWS services used while running this guidance. Refer to the [Cost](cost.md) section for more details. For full details, see the pricing webpage for each AWS service used in this guidance.

1. Sign in to the AWS Management Console and select the button to launch the `guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws.template` AWS CloudFormation template.

   [![Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS launch button](http://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=GenomicsAnalysis-Base&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fgenomics-tertiary-analysis-and-data-lakes-using-aws-glue-and-amazon-athena%2Flatest%2Fguidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws.template)

   You can also [download the template](https://solutions-reference.s3.amazonaws.com/genomics-tertiary-analysis-and-data-lakes-using-aws-glue-and-amazon-athena/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws.template) as a starting point for your own implementation.

1.  The template launches in the US East (N. Virginia) Region by default. To launch this guidance in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
This guidance uses the AWS CodePipeline and Amazon Omics services, which are currently available in specific AWS Regions only. Therefore, you must launch this guidance in an AWS Region where these services are available. For the most current service availability by AWS Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1.  On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1.  On the **Specify stack details** page, assign a name to your stack and provide a project name for the guidance installation. For information about naming character limitations, refer to [IAM and STS Limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1.  Choose **Next.**

1.  On the **Configure stack options** page, choose **Next**.

1.  On the **Review** page, review and confirm the settings. Check the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1.  Choose **Create stack** to deploy the stack.

1. You can view the status of the stack in the AWS CloudFormation Console in the **Status** column. You should see a status of CREATE\_COMPLETE in approximately 60 minutes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
