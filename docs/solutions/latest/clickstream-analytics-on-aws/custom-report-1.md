---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/custom-report-1.html
---

# Custom report
<a name="custom-report-1"></a>

 One of the key benefits of this guidance is that you have complete control over the clickstream data collected from your apps and websites. You have complete flexbility to analyze the data for your specific business needs. This article illustrates the steps of creating a custom report with an example of creating funnel analysis by using Redshift Serverless as analytics engine and QuickSight as reporting tools.

There are two options to create custom analyses. The following examples will guide you through the detailed steps.

## Option 1- create custom analysis with preset QuickSight dataset
<a name="option-1"></a>

The guidance had created a `Event_View-<app>-<project> `dataset which stores all the raw event data, includes both common and custom dimension, joined with user attributes and session attributes in QuickSight, you can use these datasets to create custom analysis based on your specific requirements.

For example, let's say you have a custom event view\_item that records when a user views an item's detail page. This custom event has a custom attribute event\_category to track the promotion spot from which the user came to the item detail page. Now, you want to create a custom analysis that uses a pie chart to show the percentage of each event\_category that led user to item detail pages.

1. Go to **Analyze module** in Clickstream Analytics on AWS web console.

1. Click on **New analysis** in the top-right corner.

1. Select `Event_View-<app>-<project>` dataset.

1. Select the **USE IN ANALYSIS** button.

1. Since the `event_category` is a custom parameter for the view\_item event, we need to extract it from the `custom_parameters_json_st`r field, which is a JSON string, we can use parseJSON function to extract values from it. Select **\+ CALCULATED FIELD** button to add a calculated field.

1. Input **Event Category **as the name for the calculated field, and input parseJson({custom\_parameters\_json\_str}, "$.event\_category") as the formula, then select **Save**.

1. In the analysis author console, you can see a new field called Event Category appear in the Data panel.

1.  In the Visuals panel, click on **\+ ADD **button, and select Pie chart.

1. Drag the Event Category field to **GROUP/COLOR**, drag event\_id to **VALUE**.

1.  In the Filter panel, add a filter to only include event\_name equals view\_item.

1. Now you should be able to see a bar chart shows the percentage of each event\_category that led to view\_item events.

1. You can format the analysis according to your need then publish it as dashboard.

1. To enable your custom analysis to appear in the Dashboards module of the Clickstream Analytics Studio, you need to add the dashboard into the Shared folder with name of the <project-id>\_<app\_id>, which was pre-created by the guidance. After you added the custom dashboard into the Shared folder, it will automatically display in the Clickstream Analytics Studio.

## Option 2 - create custom view in Redshift and import to QuickSight
<a name="option-2"></a>

### Part 1 - Dataset preparation
<a name="part1-dataset-preparation"></a>

1.  Open **Redshift Serverless dashboard**.

1.  Choose the workgroup starting with `clickstream-<project-id>` created by the guidance.

1.  Choose **Query data**. You will be directed to the Redshift Query Editor.

1.  In the **Editor** view on the Redshift Query Editor, right click on the workgroup with name of `clickstream-<project-id>`. In the prompted drop-down, select **Edit connection**, and you will be asked to provide connection parameters. Follow this [guide](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-using.html) to use an appropriate method to connect.
**Important**
Read and write permissions are required for the database (with name as <project-id>) to create custom view or table. For example, you can use Admin user to connect to the cluster or workgroup. If you don't know the password for the Admin user, you can reset the admin password in the Redshift Console. For more information, refer to [Security and connections in Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-security.html).

1.  If it is the first time you access the query editor, you will be prompted to configure the account. Choose **Config account** to open query editor.

1.  Add a new SQL editor, and make sure you selected the correct workgroup and schema.

1.  Create a new view for funnel analysis. In this example, we used below SQL.

   ```
   CREATE OR REPLACE VIEW {{schema}}.clickstream_funnel_view as
   SELECT
   platform,
   COUNT(DISTINCT step1_id) AS session_start_users,
   COUNT(DISTINCT step2_id) AS page_view_users,
   COUNT(DISTINCT step3_id) AS scroll_users
   FROM (
   SELECT
       platform,
       user_pseudo_id AS step1_id,
       event_timestamp AS step1_timestamp,
       step2_id,
       step2_timestamp,
       step3_id,
       step3_timestamp
   FROM
      {{schema}}.clickstream_event_base_view
   LEFT JOIN (
   SELECT
       user_pseudo_id AS step2_id,
       event_timestamp AS step2_timestamp
   FROM
       {{schema}}.clickstream_event_base_view
   WHERE
       event_name = '_page_view')
   ON
       user_pseudo_id = step2_id
       AND event_timestamp < step2_timestamp
   LEFT JOIN (
   SELECT
       user_pseudo_id AS step3_id,
       event_timestamp AS step3_timestamp
   FROM
       {{schema}}.clickstream_event_base_view
   WHERE
       event_name= '_scroll' )
   ON
       step3_id  = step2_id
       AND step2_timestamp < step3_timestamp
   WHERE
   event_name = '_session_start' )
   group by
   platform
   ```

1. Go to QuickSight console, choose **Dataset**, and then choose **New dataset**.

1.  In the New Dataset page, choose **Redshift Manual connect** to add dataset, and fill in the prompted form with the following parameters.
   +  **Data source name**: clickstream-funnel-view-<project-id>
   +  **Connection type**: select VPC connections / VPC Connection for Clickstream pipeline <project-id>
   +  **Database server**: input the endpoint url of the serverless workgroup, which you can find on the workgroup console.
   +  **Port**: 5439
   +  **Database name**: <project-id>
   +  **User name**: name of the user you used to created the custom view in previous steps
   +  **Password**: password of the user you used to created the custom view in previous steps

1.  Validate the connection, and then choose **Create data source**.

1.  Choose the view from Redshift as data source - "**clickstream\_funnel\_view**", then
   +  Schema: select notepad
   +  Tables: clickstream\_funnel\_view
**Note**
 When prompted to select Import to SPICE or Directly query your data, select `Directly query your data` for this example.
   +  Choose **Edit/Preview data** to preview the data. Once you're familiar with the data, choose **PUBLISH & VISUALIZE** at the top-right.

### Part 2 - Create visulizations in QuickSight
<a name="part2-create-visualizations-in-quicksight"></a>

1.  When prompted, select a layout for your visualization.

1.  Choose "**\+Add**" at the top-left of the screen then choose "**Add visual**".

1.  Select a Visual type at the bottom-left of the screen, in this example, select **Vertical bar chart**.

1.  In the Field wells, select platform as X axis, login\_user, add\_button\_click\_users, and note\_create\_users as Value.

   Now you can publish this analysis as dashboard or continue to format it. For more information, see [Visualizing data in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/working-with-visuals.html).

### Part 3 - Add the custom dashboard to Analytics Studio
<a name="part3-add-the-custom-dashboard-to-analytic-studio"></a>

To enable your custom dashboard to appear in the Dashboards module of the Analytics Studio, you need to add the dashboard into the Shared folder with the name of `<project-id>_<app_id>`, which was pre-created by the guidance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
