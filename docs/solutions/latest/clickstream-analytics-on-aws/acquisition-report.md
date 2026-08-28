---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/acquisition-report.html
---

# Acquisition report
<a name="acquisition-report"></a>

 You can use the acquisition report to get insights into how new users arrive at your website or app for the first time, as well as the sources of everyday traffic.

**Note**
This article describes the default report. You can customize the report by applying filters or comparisons or by changing the dimensions, metrics, or charts in QuickSight. For more information, refer to [Visualizing data in Quick](https://docs.aws.amazon.com/quicksight/latest/user/working-with-visuals.html).

## View the report
<a name="view-the-report"></a>

1.  Access the dashboard for your application. Refer to [Access dashboard](dashboards-1.md#view-dashboards).

1.  In the dashboard, choose the sheet with name of `Acquisition`.

## Data sources
<a name="where-the-data-comes-from"></a>

 Acquisition report is created based on the following QuickSight datasets:

|  **QuickSight dataset**  |  **Redshift view / table**  |  **Description**  |
| --- | --- | --- |
| User\_User\_View-<app>-<project> | clickstream\_acquisition\_day\_user\_view\_cnt | This dataset stores data on the number of new users and number of active users on your websites or apps for each day. |
|  Day\_Traffic\_Source\_User-<app>-<project>  | clickstream\_acquisition\_day\_traffic\_source\_user  | This dataset stores data on the number of new users per each traffic source type for each day.  |
|  Day\_User\_Acquisition-<app>-<project>  | clickstream\_acquisition\_day\_user\_acquisition  | This dataset stores data on the number of new users, number of active users, number of sessions, number of engaged sessions, and number of events per each traffic source type for each day. |
| Country\_New\_User\_Acquisition-<app>-<project> | clickstream\_acquisition\_country\_new\_user  | This dataset stores data on the number of new users per each country and city for each day. |

## Dimensions
<a name="dimensions-and-metrics"></a>

 TheAcquisition report includes the following dimensions.

|  **Dimension**  |  **Description**  |  **How it's calculated**  |
| --- | --- | --- |
| First user traffic source  | The source of the traffic that acquires new users to your websites or apps (for example, google, baidu, and bing).  | Traffic source is populated from utm parameters in page\_url (i.e., utm\_source) or traffic-source preserved attribute (i.e., \_traffic\_source\_source), or derived from referrer url (only for web).  |
| First user traffic medium  | The medium of the traffic that acquires new users to your websites or apps (for example, organic, paid search)  | Traffic medium is populated from utm parameters in page\_url (i.e., utm\_medium) or traffic-source preserved attribute (i.e., \_traffic\_source\_medium), or derived from referrer url (only for web).  |
| First user traffic campaign  | The name of a promotion or marketing campaign that acquires new users to your websites or apps.  | Traffic campaign is populated from utm parameters in page\_url (i.e., utm\_campaign) and traffic-source preserved attribute (i.e., \_traffic\_source\_campaign), or derived from referrer url (only for web).  |
| First user traffic source / Medium First  | The combination of traffic source and medium that acquires new users to your websites or apps.  | Same as above for traffic source and traffic medium.  |
| user traffic channel group  | Channel groups are rule-based definitions of the traffic sources. The name of the traffic channel group that acquires new users to your websites or apps.  | Traffic channel group is derived based on the traffic source and medium.  |
| First user traffic clid platform  | The name of platform for click id (auto-tagging from advertisement platform) that acquires new users to your websites or apps.  | Traffic source clid platform is populated from clid parameter in page\_url and traffic-source preserved attribute (i.e., \_traffic\_source\_clid\_platform).  |
| First user app install source  | The name of app store that acquires new users to your apps, for example, App Store, Google Store.  | App install source is from traffic-source preserved attribute (i.e., \_app\_install\_channel).  |
| Session traffic source  | The traffic source that acquires users into a new session on your websites or apps (for example, google, baidu, and bing)  | Traffic source is populated from utm parameters in page\_url (i.e., utm\_source) or traffic-source preserved attribute (i.e., \_traffic\_source\_source), or derived from referrer url (only for web). |
| Session traffic medium  | The traffic medium that acquires users into a new session on your websites or apps (for example, organic, paid search)  |  Traffic medium is populated from utm parameters in page\_url (i.e., utm\_medium) or traffic-source preserved attribute (i.e., \_traffic\_source\_medium), or derived from referrer url (only for web).  |
| Session traffic campaign  | The name of a promotion or marketing campaign that acquires users into a new session on your websites or apps.  | Traffic campaign is populated from utm parameters in page\_url (i.e., utm\_campaign) and traffic-source preserved attribute (i.e., \_traffic\_source\_campaign), or derived from referrer url (only for web).  |
| Session traffic Source / Medium  | The combination of traffic source and medium that acquires users into a new session on your websites or apps.  | Same as above for traffic source and traffic medium.  |
| Session traffic channel group  | Channel groups are rule-based definitions of the traffic sources. The name of the traffic channel group that acquires users into a new session on your websites or apps.  | Traffic channel group is derived based on the traffic-source and medium.  |
| Session traffic clid platform  | The name of platform for click id (auto-tagging from advertisement platform) that acquires users into new session on your websites or apps.  | Traffic clid platform is populated from clid parameter in page\_url and traffic-source preserved attribute (i.e., \_traffic\_source\_clid\_platform).  |
| Geo country  | The country where users are when they are using your websites or apps. | Geo location information is inferred based on user IP address. |
| Geo city | The city where the users are when they are using your websites or apps. | Geo location information is inferred based on user IP address.  |

## Metrics
<a name="metrics-1"></a>

The Acquisition report includes the following metrics:

|  **Metric**  |  **Description**  |  **How it's calculated**  |
| --- | --- | --- |
| New users  | The number of users who interacted with your site or launched your app for the first time (event triggered: \_first\_open).  | Count distinct user\_id or user\_pseudo\_id (if user\_id is not available) when event\_name equals '\_first\_open'.  |
| Active users  | The number of distinct users who triggered any event in the selected time range.  | Count distinct user\_id or user\_pseudo\_id (if user\_id is not available) at any event  |
| Sessions  | The number of sessions users created.  | Count distinct session\_id.  |
| Engaged Session  | The number of sessions that lasted 10 seconds or longer, or had 1 or more page or screen views. | Count distinct session\_id if the session is engaged.  |
| Engaged Rate  |  The percentage of sessions that were engaged sessions.  | Engaged sessions / total sessions.  |
| Events  | The number of times users triggered an event.  | Count event\_id |
| Avg\_engagement\_time\_per\_user  | The average time per user that your website was in focus in a user's browser or an app was in the foreground of a user's device.  | Total user engagement durations / Number of active users Count distinct user\_id or user\_pseudo\_id (if user\_id is not available) when event\_name equals '\_first\_open'.  |

## Sample dashboard
<a name="sample-dashboard-1"></a>

Below image is a sample dashboard for your reference.

![Dashboard showing user metrics, traffic sources, and geographic data with graphs and charts.](http://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/sample-dash.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
