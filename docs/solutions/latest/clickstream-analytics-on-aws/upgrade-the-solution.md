---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/upgrade-the-solution.html
---

# Upgrade the guidance
<a name="upgrade-the-solution"></a>

**Note**
Be advised that upgrading directly from version 1.0.x to 1.1.6(\+) version is not supported. It is necessary to upgrade to version 1.1.5 first.

**Note**
By upgrading the web console from earlier 1.1 versions before 1.1.6, you could continue to view the dashboards of the project. However, you could not explore the existing Clickstream data due the changes of data schemas. If you wish to continue to use the Explorations, you will need to upgrade the data pipeline as well and migrate the existing data to new data schemas (if you want to explore historical data).

## Planning and Preparation
<a name="planning-and-preparation"></a>

1.  **Backup of Modified QuickSight Analysis and Dashboard**: The guidance upgrade may involve modifying the out-of-the-box analysis and dashboard. In this case, you can back them up following [this documentation](https://docs.aws.amazon.com/quicksight/latest/developerguide/assetbundle-export.html).

1.  **Data Processing Interval** (only applicable to upgrade from v1.0.x): The pipeline upgrade will take about 20 minutes. Make sure no data processing job is running while upgrading the existing pipeline. You can update the existing pipeline to increase the interval and view whether there are running jobs of the EMR Serverless application in the console.

## Upgrade Process
<a name="upgrade-process"></a>

### Upgrade the web console stack
<a name="upgrade-web-console-stack"></a>

1.  Log in to [AWS CloudFormation console](https://console.aws.amazon.com/cloudfromation/), select your existing web console stack, and choose **Update**.

1.  Select **Replace current template**.

1.  Under **Specify template**:
   +  Select Amazon S3 URL.
   +  Refer to the table below to find the link for your deployment type.
   +  Paste the link in the Amazon S3 URL box.
   +  Choose **Next**.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/upgrade-the-solution.html)

1.  Under **Parameters**, review the parameters for the template and modify them as necessary. Refer to [Deployment](deployment.md) for details about the parameters.

1.  Choose **Next**.

1.  On the **Configure stack options** page, choose **Next**.

1.  On the **Review** page, review and confirm the settings. Be sure to check the box acknowledging that the template might create (IAM) resources.

1.  Choose **View change set** and verify the changes.

1.  Choose **Execute change set** to deploy the stack.

 You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive an UPDATE\_COMPLETE status after a few minutes.

### Upgrade the pipeline of project
<a name="upgrade-the-pipeline-of-project"></a>

**Important**
If you encounter any issues during the upgrade process, refer to [Troubleshooting](troubleshooting.md) for more information.

1.  Log in to the web console of the guidance.

1.  Go to **Projects**, and choose the project to be upgraded.

1.  Choose project id or **View Details** button.

1.  In the project details page, choose the **Upgrade** button. You will be prompted to confirm the upgrade action.

1.  Choose **Confirm**.

 You can view the status of the pipeline in the guidance console in the **Status** column. After a few minutes, you can receive an Active status.

## Post-Upgrade Actions
<a name="post-upgrade-actions"></a>

This section provides instructions for post-upgrade actions.

### Ingestion
<a name="post-upgrade-ingestion"></a>

As of version 1.1.7, this guidance uses [launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html). After upgrading the data ingestion module, complete the following steps to replace the Amazon EC2 instances used by Amazon ECS with the new launch template configuration.

1. Increase the desired task number by [updating the Amazon ECS service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html).

1. After the newly added Amazon ECS tasks have started successfully, [manually stop the old tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/standalone-task-stop.html).

1. Manually [terminate the old Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html).

### Data Modeling
<a name="post-upgrade-data-modeling"></a>

#### Upgrade the Data Schema and Out-of-the-box Dashboards
<a name="upgrade-the-data-schema"></a>

The guidance automatically and asynchronously upgrades the views and materialized views used by the dashboard after upgrading the pipeline of the project. The duration of the update depends on the workload of the Redshift cluster and the existing data volume, and can take minutes to hours. You can track the progress in the** Redshift Schemas** section in the **Processing** tab of the Pipeline Detail page. If the post-configuration job fails, you can access the execution of the workflow through its link and rerun the job via **Actions - Redrive or New** execution with the input unchanged.

#### Migrate the existing data (only applicable when upgrading from version earlier than v1.1.6)
<a name="migrate-the-existing-data-after-upgrading-from-1.0.x"></a>

1.  Open [Redshift query editor v2](https://aws.amazon.com/redshift/query-editor-v2/). For more information, refer to [Working with query editor v2](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-using.html) to log in and query data using Redshift query editor v2.
**Note**

The data migration process is CPU-intensive and **will incur additional cost**. Before starting the migration, ensure that the load on your Redshift is low. It's also advisable to consider temporarily increasing the RPUs of Redshift Serverless or the cluster size when migrating large volumes of data.
In our benchmark, we migrated 100 million events in 25 minutes using 32 RPUs of Redshift Serverless.
Average number of events per day: \*\*10 million\*\*
Total events for 30 days: \*\*300 million\*\*
RedShift RPU: \*\*32 RPUs\*\*
Total duration: \*\*4 hours 45 minutes\*\*
Total cost: \*\*$47.77\*\*

1.  Select the Serverless workgroup or provisioned cluster, `<project-id>`->`<app-id>`->Tables, and make sure tables for the appId are listed there.

1.  Create a new SQL Editor, select your project's schema.

1.  Execute below SQL in editor. Customize the date range as desired, and execute the following SQL in the editor to migrate events from the past 30 days, or any number of days up to the present, to the new tables.

   ```
   -- please replace `<app-id>` with your actual app id
   -- update the day range based on your need
   CALL "<app-id>".sp_migrate_data_v2(30);
   ```

1.  Wait for the SQL to complete. The execution time depends on the volume of data in `events` table.

1.  Execute the following SQL to check the stored procedure execution log; ensure there are no errors. If there are any interruptions, timeouts, or other errors, you can re-execute step 4 to continue the data migration.

   ```
   -- please replace `<app-id>` with your actual app id

   SELECT * FROM "<app-id>"."clickstream_log" WHERE log_name = 'sp_migrate_event_to_v2' ORDER BY log_date DESC;

   SELECT * FROM "<app-id>"."clickstream_log" WHERE log_name = 'sp_migrate_user_to_v2' ORDER BY log_date DESC;

   SELECT * FROM "<app-id>"."clickstream_log" WHERE log_name = 'sp_migrate_item_to_v2' ORDER BY log_date DESC;

   SELECT * FROM "<app-id>"."clickstream_log" WHERE log_name = 'sp_migrate_session_to_v2' ORDER BY log_date DESC;

   SELECT * FROM "<app-id>"."clickstream_log" WHERE log_name = 'sp_migrate_data_to_v2' ORDER BY log_date DESC;
   ```

1.  Populate the event data to clickstream\_event\_base\_view table.

   ```
   -- please replace `<app-id>` with your actual app id
   -- update the day range (30 days in below example based on your need
   CALL "<app-id>".clickstream_event_base_view_sp(NULL, NULL,24*30);
   ```
**Note**
It is recommended to refresh the clickstream\_event\_base\_view in batches, especially in the following scenarios:
• When there are new event load jobs coming in before the migration job completes.
• When there are new event load jobs coming in before the migration job completes.
Refreshing the data in batches needs to be done based on the event timestamp. Call the following stored procedure multiple times, in order from old to new event timestamps using below SQL command.
`call "schema".clickstream_event_base_view(start_event_timestamp, end_event_timestamp, 1); `
For example, to refresh data between 2024-05-10 00:00:00 and 2024-05-12 00:00:00, execute the following SQL:
`call "schema".clickstream_event_base_view_sp(TIMESTAMP 'epoch' + 1715270400 * INTERVAL '1 second', TIMESTAMP 'epoch' + 1715443200 * INTERVAL '1 second', 1); `

1. Follow this guide to calculate metrics for the new preset dashboard based on the migrated data.

1. If your applications no longer use the legacy tables and views, run the SQLs below to clean them to save the storage of Redshift.

   ```
   -- please replace `<app-id>` with your actual app id

   DROP TABLE "<app-id>".event CASCADE;

   DROP TABLE "<app-id>".item CASCADE;

   DROP TABLE "<app-id>".user CASCADE;

   DROP TABLE "<app-id>".event_parameter CASCADE;

   DROP PROCEDURE "<app-id>".sp_migrate_event_to_v2(nday integer);

   DROP PROCEDURE "<app-id>".sp_migrate_item_to_v2(nday integer);

   DROP PROCEDURE "<app-id>".sp_clear_expired_events(retention_range_days integer);

   DROP PROCEDURE "<app-id>".sp_migrate_data_to_v2(nday integer);

   DROP PROCEDURE "<app-id>".sp_migrate_user_to_v2();

   DROP PROCEDURE "<app-id>".sp_migrate_session_to_v2();

   DROP PROCEDURE "<app-id>".sp_clear_item_and_user();
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
