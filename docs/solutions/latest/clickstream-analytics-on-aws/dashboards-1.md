---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/dashboards-1.html
---

# Dashboard
<a name="dashboards-1"></a>

## Overview
<a name="overview-6"></a>

 Clickstream Analytics on AWS collects data from your websites and apps to create dashboards that derive insights. You can use dashboards to monitor traffic, investigate data, and understand your users and their activities.

Depends on your pipeline configuration, the time for data to be available in your dashboard varies. By default, the metrics in the out-of-the-box dashboards are calculated on a daily basis, you should see the data and metrics from previous day (according to your app's time zone).

### View dashboards
<a name="view-dashboards"></a>

 Use this procedure to view dashboards:

1.  Go to **Clickstream Analytics on AWS Console**, in the **Navigation Bar**, choose **Analytics Studio**.

1.  In the Analytics Studio page that opens, select the project and app you just created in the drop-down list at the top of the web page.

1.  Choose the **User lifecycle - default** dashboard.

### Reports
<a name="reports"></a>

 The dashboard contains a set of reports throughout the user lifecycle, which aim to help you understand how people use your website or app, from acquisition to retention.

|  **Report name**  |  **What it is**  |
| --- | --- |
|  [Acquisition](acquisition-report.md)  |  Summarizes key metrics about new users, and provides detail view user profile  |
|  [Engagement](engagement-report.md)  |  Summarizes key metrics about user engagements and sessions  |
|  [Retention](retention-report.md)  |  Summarizes key metrics about active users and user retentions  |
|  [Device](device-report.md)  |  Summarizes key metrics about the devices users are using to access your apps and websites, and provides detail view of each device  |
|  [Details](details-report.md)  | This report allows you to query and view user' attributes and the events the user performed.  |

### Custom report
<a name="custom-report"></a>

 If you want to investigate certain pieces of data further, you can write SQL to create views in Redshift or Athena, then add dataset into QuickSight to create visualization. Refer to [this example](custom-report-1.md) to learn how to create a customize report with Redshift.

**Create Dashboard**

You can create a custom dashboard to save the result of exploration query. Below are the steps:

1.  Select **Create Dashboard** button on the top-left.

1. Fill in a name as **Dashboard name** .

1. Fill in a description for the dashboard.

1. Enter a sheet name, then click on the \+ button on the right. You can add multiple sheets in one dashboard.

1. You can remove a sheet by click on the X button on the sheet name.

1. Select **Create** button.

1. After the dashboard was created, you can select the dashboard to save query results.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
