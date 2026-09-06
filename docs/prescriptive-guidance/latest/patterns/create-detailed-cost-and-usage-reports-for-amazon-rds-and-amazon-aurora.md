---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-detailed-cost-and-usage-reports-for-amazon-rds-and-amazon-aurora.html
---

# Create detailed cost and usage reports for Amazon RDS and Amazon Aurora
<a name="create-detailed-cost-and-usage-reports-for-amazon-rds-and-amazon-aurora"></a>

*Lakshmanan Lakshmanan and Sudarshan Narasimhan, Amazon Web Services*

## Summary
<a name="create-detailed-cost-and-usage-reports-for-amazon-rds-and-amazon-aurora-summary"></a>

This pattern shows how to track usage costs for Amazon Relational Database Service (Amazon RDS) or Amazon Aurora clusters by configuring [user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/custom-tags.html). You can use these tags to create detailed cost and usage reports in AWS Cost Explorer for clusters across multiple dimensions. For example, you can track usage costs at the team, project, or cost center level, and then analyze the data in Amazon Athena.

## Prerequisites and limitations
<a name="create-detailed-cost-and-usage-reports-for-amazon-rds-and-amazon-aurora-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ One or more [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html) or [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html) instances

**Limitations**

For tagging restrictions, see the [AWS Billing User Guide](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html).

## Architecture
<a name="create-detailed-cost-and-usage-reports-for-amazon-rds-and-amazon-aurora-architecture"></a>

**Target technology stack**
+ Amazon RDS or Amazon Aurora
+ AWS Cost and Usage Report
+ AWS Cost Explorer
+ Amazon Athena

**Workflow and architecture**

The tagging and analysis workflow consists of these steps:

1. A data engineer, database administrator, or AWS administrator creates user-defined cost allocation tags for the Amazon RDS or Aurora clusters.

1. An AWS administrator activates the tags.

1. The tags report metadata to AWS Cost Explorer.

1. A data engineer, database administrator, or AWS administrator creates a [monthly cost allocation report](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/configurecostallocreport.html#allocation-viewing).

1. A data engineer, database administrator, or AWS administrator analyzes the monthly cost allocation report by using Amazon Athena.

The following diagram shows how to apply tags to track usage costs for Amazon RDS or Aurora instances.

![Applying tags to track usage costs for database instances and clusters](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/eab5001d-5115-4aa6-bdd2-23063b08b262/images/63292b18-01d6-4523-b8ac-2c3b12b11b84.png)

The following architecture diagram shows how the cost allocation report is integrated with Amazon Athena for analysis.

![Querying cost allocation reports in Athena](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/eab5001d-5115-4aa6-bdd2-23063b08b262/images/9c028405-1e93-4f6a-a0e5-36154e2b8eab.png)

The monthly cost allocation report is stored in an Amazon S3 bucket that you specify. When you set up Athena with the AWS CloudFormation template, as described in the *Epics* section, the template provisions several additional resources, including an AWS Glue crawler, an AWS Glue database, an Amazon Simple Notification System (Amazon SNS) event, AWS Lambda functions, and AWS Identity and Access Management (IAM) roles for the Lambda functions. As new cost data files arrive in the S3 bucket, event notifications are used to forward these files to a Lambda function for processing. The Lambda function initiates an AWS Glue crawler job to create or update the table in the AWS Glue Data Catalog. This table is then used to query data in Athena.

## Tools
<a name="create-detailed-cost-and-usage-reports-for-amazon-rds-and-amazon-aurora-tools"></a>
+ [Amazon Athena](https://aws.amazon.com/athena/) is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL.
+ [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) is a fully managed relational database engine that's built for the cloud and compatible with MySQL and PostgreSQL.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/) is an infrastructure as code (IaC) service that allows you to easily model, provision, and manage AWS and third-party resources.
+ [AWS Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-what-is.html) helps you view and analyze your AWS costs and usage.

## Epics
<a name="create-detailed-cost-and-usage-reports-for-amazon-rds-and-amazon-aurora-epics"></a>

### Create and activate tags for your Amazon RDS or Aurora cluster
<a name="create-and-activate-tags-for-your-amazon-rds-or-aurora-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create user-defined cost allocation tags for your Amazon RDS or Aurora cluster. | To add tags to a new or existing Amazon RDS or Aurora cluster, follow the instructions in [Adding, listing, and removing tags](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html#Tagging.HowTo) in the *Amazon Aurora User Guide*.For information about how to set up an Amazon Aurora cluster, see the instructions for [MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.Aurora.html) and [PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.AuroraPostgreSQL.html) in the *Amazon Aurora User Guide*. | AWS administrator, Data engineer, DBA |
| Activate the user-defined cost allocation tags. | Follow the instructions in [Activating user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html) in the *AWS Billing User Guide*. | AWS administrator |

### Create cost and usage reports
<a name="create-cost-and-usage-reports"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create and configure cost and usage reports for your clusters. | 1. Sign in to the AWS Management Console and open the [AWS Billing console](https://console.aws.amazon.com/billing/home#/).<br />2. In the left navigation pane, choose **Cost & Usage Reports**.<br />3. Choose **Create report**.<br />4. Provide a report name, keep the default settings for other options, and then choose **Next**.<br />5. Choose **Configure** and provide the details of an existing S3 bucket. You can also choose to create a new S3 bucket from this screen. Choose **Next**.<br />6. Verify the default policy that will be applied to your bucket, select the confirmation check box, and then choose **Save**.<br />7. For **Report path prefix**, specify the prefix you want to prepend to the report name.<br />8. For **Time granularity**, choose **Hourly**, **Daily** or **Monthly**, depending on how often you want data to be collected for the report.<br />9. For **Report versioning**, choose whether you want new versions of the report to be created separately or overwrite the existing report with each version.<br />10. For **Enable report data integration for**,** **choose **Amazon Athena**. Verify that the compression type is set to Parquet.<br />11. Choose **Next**.<br />12. Review the report settings, and then choose **Review and Complete**.The data will be available in 24 hours. | App owner, AWS administrator, DBA, General AWS, Data engineer |

### Analyze cost and usage report data
<a name="analyze-cost-and-usage-report-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Analyze the cost and usage report data. | 1. Set up and use Athena to analyze the report data. For instructions, see [Querying Cost and Usage Reports using Amazon Athena](https://docs.aws.amazon.com/cur/latest/userguide/cur-query-athena.html) in the *AWS Cost and Usage Reports User Guide*. We recommend that you use the [AWS CloudFormation template provided by Athena](https://docs.aws.amazon.com/cur/latest/userguide/use-athena-cf.html).<br />2. Run Athena queries. For example, you can use the following SQL query to check the status of the data refresh.<pre>select status from cost_and_usage_data_status</pre>For more information, see [Running Amazon Athena queries](https://docs.aws.amazon.com/cur/latest/userguide/cur-ate-run.html) in the *AWS Cost and Usage Reports User Guide*.When you run your SQL query, make sure that the correct database is selected from the dropdown list. | App owner, AWS administrator, DBA, General AWS, Data engineer |

## Related resources
<a name="create-detailed-cost-and-usage-reports-for-amazon-rds-and-amazon-aurora-resources"></a>

**References**
+ [Setting up Athena using AWS CloudFormation templates](https://docs.aws.amazon.com/cur/latest/userguide/use-athena-cf.html) (recommended)
+ [Setting up Athena manually](https://docs.aws.amazon.com/cur/latest/userguide/cur-ate-manual.html)
+ [Running Amazon Athena queries](https://docs.aws.amazon.com/cur/latest/userguide/cur-ate-run.html)
+ [Loading report data to other resources](https://docs.aws.amazon.com/cur/latest/userguide/cur-query-other.html)

**Tutorials and videos**
+ [Analyze Cost and Usage Reports using Amazon Athena ](https://youtu.be/KEeJEZTYE8E)(YouTube video)
