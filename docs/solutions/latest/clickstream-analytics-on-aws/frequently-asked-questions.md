---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/frequently-asked-questions.html
---

# Frequently Asked Questions
<a name="frequently-asked-questions"></a>

## General
<a name="general"></a>

 **Q: **What is Clickstream Analytics on AWS?****

A Guidance that enables customers to build clickstream analytic system on AWS easily. This guidance automates the data pipeline creation per customers’ configurations with a visual pipeline builder, and provides SDKs for web and mobiles apps (including iOS, and Android) to help customers to collect and ingest client-side data into the data pipeline on AWS. After data ingestion, the guidance allows customers to further enrich and model the event data for business users to query, and provides built-in visualizations (for example, acquisition, engagement, retention) to help them generate insights faster.

## Data pipeline
<a name="data-pipeline-faq"></a>

**Q: When do I choose Amazon Redshift Serverless for data modeling?**

If the data pipeline meets the below criteria, Amazon Redshift Serverless is preferred.
+ The data processing interval is equal to or larger than one hour.
+ The report querying and other usage, such as ETL, is intensive for a few hours at most.
+ Redshift is not used for streaming ingestion.
+ The estimated cost is lower than the provisioned cluster.

**Q: I already enable data modeling on Redshift, so why can't I see the schema and tables created by this guidance in the Redshift query editor? **

This guidance creates a separate database and schema within your Amazon Redshift cluster for storing and processing clickstream events. By default, the schema, tables, and views are only owned by the user who created them and are not visible to other users who log into the Redshift query editor.

You could use the superusers or the admin of Redshift to view them.
+ For provisioned Redshift, you could use admin or the Database user specified when configuring the data pipeline.
+ For Redshift serverless, the schema and tables are created by an IAM role managed by the guidance; there is no default password for this user. You could edit admin credentials for the Redshift serverless namespace.

Once you view the schema and tables in the query editor, you can grant permissions to other Redshift users.

**Q: How do I monitor the health of the data pipeline for my project?**

You can open the built-in [observability dashboard](pipeline-maintenance.md) to view the key metrics of your data pipeline.

The dashboard displays metrics for different components of your data pipeline, including data ingestion, processing, and modeling.
+ **Data Ingestion - Server**
  + **Server Request Counts**: The total requests received by the ingestion servers in the given period. You can use it to calculate the request per second (RPS) of the ingestion servers.
  + **Server Response Time**: The average response time in seconds of the ingestion servers in the given period.
  + **Server (ECS) Tasks**: The number of tasks/instances running for the ingestion servers.
+ **Data Ingestion - Sink - Kinesis Data Stream** (available when enabling KDS as ingestion sink)
  + **Kinesis Throttled and Failed Records**: The total putting records of KDS were throttled or failed in the given period.
  + **Kinesis to S3 Lambda Error count**: The total error count in a given period when sinking records in KDS to S3.
  + **Kinesis to S3 Lambda success rate (%)**: The success rate of sinking KDS records to S3.
+ **Data Processing** (available when enabling data processing)
  + **Data Processing Job success rate (%)**: The success rate of a data processing job in a given period.
  + **Data Processing Row counts**: The chart contains four metrics.
    + **source count**: The raw request count of the ingestion server received in the batch data processing.
    + **flatted source count**: The SDK sends multiple clickstream events in a request in batch. It's the total clickstream events in the processed `source requests`.
    + **sink count**: The total number of valid clickstream events that are transformed and enriched in data processing, and sink to S3 again.
    + **corrupted count**: The total invalid or unprocessable events in the data processing batch. You can check the corrupted file log in the bucket with path `clickstream/<project id>/data/pipeline-temp/<project id>/job-data/etl_corrupted_json_data/jobName=<emr serverless run job id>/` configured for your data pipeline.
+ **Data Modeling** (available when enabling data modeling on Redshift)
  + **'Load data to Redshift tables' workflow**: The success or failure count of the workflow loading processed data into Redshift in the given period.
  + **File max-age**: The maximum age of processed files located in S3 is not loaded to Redshift. There is a built-in alarm that will be triggered when the max-age exceeds the data processing interval.
  + **Redshift-Serverless ComputeCapacity** (available when using Redshift serverless): The RPU usage of the Redshift serverless workgroup. If the used RPU count always reaches the maximum RPU number of the Redshift serverless, it means there are insufficient compute resources for the workload in Redshift.

**Q: How do I re-run a failed data processing job?**

Occasionally, the data processing job fails. You can re-run the failed job to reprocess the data in that given period. The steps are:

1. Locate the failed job in **EMR Studio - Applications - Clickstream-<project id>**.

1. Choose **Clone**.

1. Keep all parameters unchanged, and choose **Submit job run**.

**Q: How do I resume a failed data-loading workflow?**

This guidance uses a workflow named `ClickstreamLoadDataWorkflow`, orchestrated by AWS Step Functions to load the processed data into Amazon Redshift. The workflow uses a DynamoDB table to record the files to be loaded that are processed by the data processing job. Any failure won't lose any data for loading into Redshift. It's safe to execute the workflow again to resume the loading workflow after it fails.

Q: How do I recalculate historical events for out-of-the-box dashboards?

The metrics in the out-of-the-box dashboards are calculated on a daily basis. If you need to recalculate the metrics in case of there are changes to your historical data, you could manually reschedule the workflow to re-calculate the metrics. Follow these steps:

1. Open the Step Functions service in the AWS console for the region where your data pipeline is located.

1. Find the state machine named RefreshMaterializedViewsWorkflowRefreshMVStateMachine. If you have multiple projects in the same region, check the tags of the state machine to ensure it belongs to the project for which you want to recalculate the metrics.

1. Start a new execution with the following input JSON. You need to change the refreshStartTime and refreshEndTime values to the date range for the data you want to recalculate.

   ```
   {
   “refreshEndTime”: 171540689200,
   “refreshStartTime”: 1711929600000
   }
   ```

## SDK
<a name="sdk"></a>

**Q: Could I use other SDK to send data to the pipeline created by this guidance?**

Yes. The guidance supports using third-party SDK to send data to the pipeline. Note that, if you want to enable data processing and modeling module when using a third-party SDK to send data, you need to provide an transformation plugin to map third-party SDK's data structure to guidance data schema. Please refer to [Custom plugin](processing-plugin.md#custom-plugins) for more details.

## Analytics Studio
<a name="analytics-studio-3"></a>

**Q: Why is the Analytics Studio is not available?**

Possible reasons are:
+ The version of the pipeline is not v1.1 or higher. You can try upgrading the pipeline and wait for the upgrade to complete before trying again.
+ The reporting module is not enabled on the pipeline.

**Q: How can I modify the default dashboard?**

You are not allowed to modify the default dashboard directly. However, you can create a new analysis from the default dashboard and then create a new dashboard from the analysis that you copied. Below are the steps to create analysis from the default dashboard:

1. In Analytics Studio, choose the Analyzes module, and choose **Dashboards**.

1. Open the default dashboard with the name of `Clickstream Dashboard - - `.

1. Choose the **Share** icon and choose **Share Dashboard** in the upper right corner.

1. In the new window, turn on Allow "save as" in the **Save as Analysis** column for "ClickstreamPublishUser" (scroll the window to the right if you don't see the column).

1. Go back to the Dashboard, refresh the webpage, and you should be able to see the **Save as** button in the upper right corner.

1. Choose **Save as**, enter a name for the analysis, and choose **SAVE**. Now you should be able to see a new analysis in the Analyzes, with which now you can edit and publish a new dashboard.

**Q: How to speed up the loading of the default dashboard? **

You can accelerate report loading by converting QuickSight datasets to SPICE mode. Here are the steps to do this:

1. Purchase SPICE capacity through the QuickSight console. The required capacity depends on your data volume; it is recommended to enable the auto-purchase option.

1. Open the guidance console, select the target project, click the pipeline **Active** status on the pipeline details page, and then open the stack detail link of **Reporting** in the CloudFormation console.

1. Click the Update button and select the **Use existing template** option.

1. Find the **Enable QuickSight SPICE Import Mode** parameter and change its value to yes. Keep other parameters unchanged.

1. Click next to complete the stack update. Once the update is complete, you can start using it.

**Note**
1. Enabling SPICE will incur additional cost, refer to QuickSight pricing page for more details.
2. By default, the guidance refreshes data in SPICE at 6 AM in your dashboard’s time zone every day. You can manually update the schedule in QuickSight

**Q: How to implement a dedicated Redshift for Analytics Studio? **

Redshift supports sharing data across different Redshift clusters, allowing you to use a dedicated Redshift cluster for Analytics Studio to achieve better query performance and cost optimization.

Before implementing Amazon Redshift data sharing, please note the following:
+ You can share data between the same cluster types, as well as between provisioned clusters and serverless clusters.
+ Only Ra3 type clusters and Redshift serverless support data sharing.

  Taking Redshift serverless as an example of data sharing, follow these operational steps:

  1. Create a Redshift serverless as the data consumer.

  2. Run SQL in the producer Redshift database (The project database configured in the Clickstream guidance) to create a data share and grant consumer permissions:

```
-- Create Data sharing
CREATE DATASHARE <data share name> SET PUBLICACCESSIBLE FALSE;
ALTER DATASHARE <data share name> ADD SCHEMA <schema>;
ALTER DATASHARE <data share name> ADD ALL TABLES IN SCHEMA <schema>;

-- Grant the Data sharing to the consumer Redshift.

GRANT USAGE ON DATASHARE <data share name> TO NAMESPACE '<consumer namespace id>';
```

Replace **<data share name> **with the name you want to share, **<schema>** with the schema you want to share, and **<consumer namespace id>** with the consumer Redshift serverless namespace ID.

3. Run following SQLs in the consumer Redshift database:

```
-- Create database
CREATE DATABASE <new database name> WITH PERMISSIONS FROM DATASHARE <data share name> OF NAMESPACE '<source namespace id>';

-- Create bi user
CREATE USER bi_user PASSWORD '<strong password>';

GRANT USAGE ON DATABASE "<new database name>" TO bi_user;

GRANT USAGE ON SCHEMA "<new database name>"."<schema>" TO bi_user;

GRANT SELECT ON ALL TABLES IN SCHEMA "<new database name>"."<schema>" TO bi_user;
-- Grant permission to data api role

CREATE USER "IAMR:<data api role name>" PASSWORD DISABLE;
GRANT USAGE ON DATABASE "<new database name>" TO "IAMR:<data api role name>";
GRANT USAGE ON SCHEMA "<new database name>"."<schema>" TO "IAMR:<data api role name>";
GRANT SELECT ON ALL TABLES IN SCHEMA "<new database name>"."<schema>" TO "IAMR:<data api role name>";

-- Test bi_user permission (optional)

SET SESSION AUTHORIZATION bi_user;
SELECT CURRENT_USER;
SELECT * FROM "<new database name>"."<schema>"."event_v2" limit 1;
```

Replace **<new database name> **with the database name in the consumer Redshift (it can be different from the original database name), replace **<source namespace id>** with the producer Redshift serverless namespace ID, and replace **<data api role name>** with the name of Data Api Role, which can be obtained from the output RedshiftDataApiRoleArn of the Reporting stack.

4. Create a new secret for the BI user in Secrets Manager, specifying the value as plaintext like below:

```
{"username":"bi_user","password":"<strong password>"}
```

The key name should be like: **/clickstream/reporting/user/bi\_user**.

5. Go to Cloudformation in AWS console, update the reporting stack to use the consumer Redshift:
+ Redshift Endpoint Url (Required): Consumer Redshift access endpoint
+ Redshift Default database name (Required): dev
+ Redshift Database Name (Required): <new database name>
+ Parameter Key Name (Required): <key name>
+ Comma Delimited Security Group Ids (Optional): The security group for VPC connection to access Redshift
+ Comma Delimited Subnet Ids (Optional): The subnet IDs for the consumer Redshift

## Pricing
<a name="pricing"></a>

**Q: How will I be charged and billed for the use of this guidance?**

The guidance is free to use, and you are responsible for the cost of AWS services used while running this guidance. You pay only for what you use, and there are no minimum or setup fees. Refer to the Cost section for detailed cost estimation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
