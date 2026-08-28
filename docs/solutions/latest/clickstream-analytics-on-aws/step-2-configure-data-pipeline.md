---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/step-2-configure-data-pipeline.html
---

# Step 2: Configure data pipeline
<a name="step-2-configure-data-pipeline"></a>

 After you create a project, you need to configure the data pipeline for it. A data pipeline is a set of connected modules that collect and process the clickstream data sent from your applications. A data pipeline contains four modules of ingestion, processing, modeling and reporting. For more information, see [pipeline management](pipeline-management.md).

 Here we provide an example with steps to create a data pipeline with end-to-end serverless infrastructure.

## Steps
<a name="steps-1"></a>

1.  Sign in to **Clickstream Analytics on AWS Management Console**.

1.  In the left navigation pane, choose **Projects**, then select the project you just created in **Step 1**, choose **View Details** in the top right corner to navigate to the project homepage.

1.  Choose **Configure pipeline**, and it will bring you to the wizard of creating data pipeline for your project.

1.  On the **Basic information** page, fill in the form as follows:
   +  AWS Region: **us-east-1**
   +  VPC: select a VPC that meets the following requirements
     +  At least two public subnets across two different AZs (Availability Zone)
     +  At least two private subnets across two different AZs
     +  One NAT Gateway or Instance
   +  Data collection SDK: **Clickstream SDK**
   +  Data location: select an S3 bucket. (You can create one bucket, and select it after choosing **Refresh**.)
**Note**
Please comply with [Security best practices for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) to create and configure Amazon S3 buckets. For example, Enable Amazon S3 server access logging, Enable S3 Versioning and so on.
If you don't have a VPC meet the criteria, you can create a VPC with VPC wizard quickly. For more information, see [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html).

1.  Choose **Next**.

1.  On the **Configure ingestion** page, fill in the information as follows:
   +  Fill in the **Ingestion endpoint settings** form.
     +  Public Subnets: Select two public subnets in two different AZs
     +  Private Subnets: Select two private subnets in the same AZs as public subnets
     +  Ingestion capacity: Keep the default values
     +  Enable HTTPS: Uncheck and then **Acknowledge** the security warning
     +  Additional settings: Keep the default values
   +  Fill in the **Data sink settings** form.
     +  Sink type: **Amazon Kinesis Data Stream(KDS)**
     +  Provision mode: **On-demand**
     +  In **Additional Settings**, change **Sink Maximum Interval** to 60 and **Batch Size** to 1000
   +  Choose **Next** to move to step 3.
**Important**
 Using HTTP is not a recommended configuration for production workload. This example configuration is to help you get started quickly.

1.  On the **Configure data processing** information, fill in the information as follows:
   +  In the **Enable data processing** form, turn on **Enable data processing**
   +  In the **Execution parameters** form,
     +  Data processing interval:
       +  Select **Fixed Rate**
       +  Enter **10**
       +  Select **Minutes**
     +  Event freshness: **35** **Days**
**Important**
This example sets Data processing interval to be 10 minutes so that you can view the data faster. You can change the interval to be less frequent later to save cost. Refer to [Pipeline Management](pipeline-management.md) to make changes to data pipeline.
   +  In the **Enrichment plugins** form, make sure the two plugins of **IP lookup** and **UA parser** are selected.
   +  In the form of **Analytics engine**, fill in the form as follow:
     +  Select the box for **Redshift**
     +  Select the **Redshift Serverless**
     +  Keep **Base RPU** as **8**
     +  VPC: select the default VPC or the same one you selected previously in the last step
     +  Security group: select the default security group
     +  Subnet: select **three** subnets across three different AZs
     +  Keep **Athena** selection as default
   +  Choose **Next**.

1.  On the **Reporting** page, fill in the form as follows:
   +  If your AWS account has not subscribed to QuickSight, please follow this [guide](https://docs.aws.amazon.com/quicksight/latest/user/signing-up.html) to subscribe.
   +  Toggle on the option** Enable Analytics Studio**.
   +  Choose **Next**.

1.  On the **Review and launch** page, review your pipeline configuration details. If everything is configured properly, choose **Create**.

 We have completed all the steps of configuring a pipeline for your project. This pipeline will take about 15 minutes to create, and please wait for the pipeine status change to be **Active** in pipeline detail page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
