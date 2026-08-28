---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/engagement-report.html
---

# Engagement report
<a name="engagement-report"></a>

You can use the Engagement report to get insights into how users interact with your websites and apps. It shows metrics around user engagement levels, activities performed, and which pages/screens are most visited.

**Note**
This article describes the default report. You can customize the report by applying filters or comparisons or by changing the dimensions, metrics, or charts in QuickSight. For more information, refer to [Visualizing data in Quick](https://docs.aws.amazon.com/quicksight/latest/user/working-with-visuals.html).

## View the report
<a name="view-the-report-1"></a>

1.  Access the dashboard for your application. Refer to [Access dashboard](dashboards-1.md#view-dashboards).

1.  In the dashboard, choose the sheet with name of `Engagement`.

## Data sources
<a name="where-the-data-comes-from-1"></a>

Engagement report are created based on the following QuickSight datasets:

|  **QuickSight dataset**  |  **Redshift view / table**  |  **Description**  |
| --- | --- | --- |
| Engagement\_KPI-<app>-<project>  | clickstream\_engagement\_kpi | This dataset stores data on Engagement KPIs per day. |
| Day\_Event\_View\_Engagement-<app>-<project>  | clickstream\_engagement\_day\_event\_view | This dataset stores data on the number of events and number of view events for each day |
| Event\_Name-<app>-<project>  | clickstream\_engagement\_event\_name | This dataset stores data on the number of events per event name for each user for each day. |
| Page\_Screen\_View-<app>-<project>  | clickstream\_engagement\_page\_screen\_view | This dataset stores data on the number of views per each page or screen for each day. |
| Page\_Screen\_View\_Detail-<app>-<project>  | clickstream\_engagement\_page\_screen\_detail\_view | This dataset stores data on the view event per page title/ page url or screen name/screen id for each user for each day. |

## Dimensions
<a name="engagement-dimensions"></a>

 The report includes the following dimensions:

|  **Dimension**  |  **Description**  |  **How it's calculated**  |
| --- | --- | --- |
| Event name  | Name of the event triggered by users  | Derived from the event name you set for an event with Clickstream SDK or HTTP API.  |
| Page title  | Title of the web page | Page title derives from the title tag in your HTML.  |
| Page URL path  | The path in the web page URL  | Page path derives from the value after the domain. For example, if someone visits www.example.com/books, then example.com is the domain and /books is the page path.  |
| Screen name  | Title of the screen | Screen name derives from the name you set for a screen using clickstream SDK or HTTP API .  |
| Screen class  | The class name of the screen | Screen class derives from the class name of the UIViewController or Activity that is currently in focus. |

## Metrics
<a name="engagement-metrics"></a>

 The report includes the following metrics:

|  **Metric**  |  **Description**  |  **How it's calculated**  |
| --- | --- | --- |
| Avg\_session\_per\_user  | The average number of sessions per active user.  | Total number of sessions / total number of active users  |
| Avg\_engagement\_time\_per\_user\_minute  | The average time per user that your website was in focus in a user's browser or an app was in the foreground of a user's device.  | Total user engagement durations / Number of active users  |
| Avg\_engagement\_time\_per\_session\_minute  | The average time per session that your website was in focus in a user's browser or an app was in the foreground of a user's device  | Total user engagement durations / Number of sessions  |
| Active users | Number of active users that had page\_view or screen\_view events. .  | Count distinct user\_id or user\_pseudo\_id (if user\_id is not available) when event\_name is '\_page\_view' or '\_screen\_view'.  |
|  Event count  | The number of times users triggered a '\_page\_view' or '\_screen\_view' event. | Count event\_id when event\_name is '\_page\_view' or '\_screen\_view'.  |
| Event count per user  |  Average event count per user |  Event count / Active users |

## Sample dashboard
<a name="sample-dashboard-2"></a>

Below image is a sample dashboard for your reference.

![Engagement dashboard showing event metrics, page views, and session data with charts and tables.](http://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/engagement.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
