---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/retention-report.html
---

# Retention report
<a name="retention-report"></a>

You can use the Retention report to get insights into how frequently and for how long users engage with your website or mobile app after their first visit. This helps you understand how effective your product is at attracting users to return after their initial visit.

**Note**
This article describes the default report. You can customize the report by applying filters or comparisons or by changing the dimensions, metrics, or charts in QuickSight. For more information, refer to [Visualizing data in Quick](https://docs.aws.amazon.com/quicksight/latest/user/working-with-visuals.html).

## View the report
<a name="view-the-report-3"></a>

1.  Access the dashboard for your application. Refer to [Access dashboard](dashboards-1.md#view-dashboards).

1.  In the dashboard, choose the sheet with name of `Retention`.

## Data sources
<a name="where-the-data-comes-from-3"></a>

 Retention report are created based on the following QuickSight dataset:

|  **QuickSight dataset**  |  **Redshift view / table**  |  **Description**  |
| --- | --- | --- |
| User\_New\_Return-<app>-<project>  | clickstream\_retention\_user\_new\_return  | This dataset stores data on the number of new users and number of returning users for each day  |
| Retention\_View-<app>-<project>  | clickstream\_retention\_view\_v3  | This dataset stores data on the cohort of user return by their first visit date and days since their first visit.  |
| Event\_Overtime-<app>-<project>  | clickstream\_retention\_event\_overtime  | This dataset stores data on daily event counts.  |
| DAU\_MAU-<app>-<project>  | clickstream\_retention\_dau\_wau  | This dataset stores the user\_ids of active users for each day.  |
| Lifecycle\_Weekly\_View-<app>-<project>  | clickstream\_retention\_dau\_wau  | This dataset stores data on the number of new users, number of retained users, number of return users, and number of lost users for each week.  |

## Metrics
<a name="dimensions-and-metrics-3"></a>

 The report includes the following metrics:

|  **Metric**  |  **Definition**  |  **How it's calculated**  |
| --- | --- | --- |
| New users  | The number of users who visited your website or app for the first time.  | Count distinct user\_id or user\_pseudo\_id (if user\_id is not available) when event\_name equals '\_first\_open'.  |
| Returning users  | The number of users who have visited your website or app before.  | Count distinct user\_id or user\_pseudo\_id (if user\_id is not available) when user\_first\_visit\_date does not equal event\_date.  |
| Returning rate  | The percentage of users returned over total users in that cohort.  | Returning users / total users.  |
| Lifecycle - New  | Number of new users in the week.  | Number of users that triggered no events in previous weeks.  |
| Lifecycle - Retained  | Number of users are active in this week and were active in last week.  | Number of users that triggered events in previous week and this week.  |
| Lifecycle - Return  | Number of users visited before and were not active in previous week, but are active in this week (excludes new users). | Number of users that triggered events in at least two weeks before and are active in this week.  |
| Lifecycle - Churn  |  Number of users were active in previous week, but are not active in this week.  | Number of users that triggered events in previous week but triggered no event this week.  |

## Sample dashboard
<a name="sample-dashboard-4"></a>

Below image is a sample dashboard for your reference.

![Dashboard showing user retention metrics including new versus returning users and activity trends.](http://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/retention.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
