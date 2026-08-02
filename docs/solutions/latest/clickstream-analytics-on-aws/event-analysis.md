---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/event-analysis.html
---

# Event Analysis
<a name="event-analysis"></a>

 Event analysis is used to study the frequency of certain behavioral events. You can conduct multi-dimensional analysis of user behavior through custom metrics, groupings, filters, and various visual charts.

## Use cases
<a name="use-cases"></a>

 Event analysis are commonly used when analyzing user behaviors, for example:
+  Query on user usage of certain product functions, such as adding favorite, video playback, and view live stream;
+  Compare different groups of user behaviors, such as the number of logins per country;
+  Compare different channel's effectiveness, such as sign-up rate per traffic source.

## Key concept
<a name="key-concept"></a>
+  **Metric**: perform aggregation on a selected event, such as the number of events, or the number of distinct users generating the event.

## How to use event analysis
<a name="how-to-use-event-analysis"></a>

1.  Select an event, and select the aggregation method for the metric.

1.  Add filter to the event by clicking the  icon next to the metric.

1.  Select an event parameter or user attribute as filter. You can add multiple filters by clicking on the filter icon. You can also configure the filter relationship by choosing AND or OR.

1.  Repeat above step to add more metric if needed.

1.  If needed, configure global filter by selecting event parameter or user attributes. Similar to event filter, you can add multiple global filters and configure the filter relationship.

1.  If needed, configure grouping by selecting an event parameter or user attribute.

1.  Choose **Query** to start the analysis.

1.  Adjust the data granularity, such as Daily, Weekly, Monthly, if needed.

1.  Adjust query time range if needed.

1.  Choose **Save to Dashboard** to save the analysis to a Dashboard, enter a name, description, and select a dashboard and sheet.

## Example
<a name="example"></a>

 Calculate the daily page views (PV) and active user count (UV) on the web from different countries over the past month, requiring active users to have a session duration of at least 30,000 milliseconds.

## Steps
<a name="steps-1"></a>

1.  Select the **Event Analysis** model.

1.  In the left **Define Metrics** area, choose \_page\_view as the metric for calculating events and select Event number as the metric type.

1.  Click the **\+ Add Event** button to add another metric. Choose \_app\_end as the metric for calculating events and select User number as the metric type.

1.  Click the filter icon to the right of \_app\_end to add a event filter condition:
   +  Filter property: Session / Session duration(msec)
   +  Operation: >=
   +  Value: 30000 (the unit of Session duration(msec)  is millisecond)

1.  Configure a global filter in the right **Filters** area:
   +  Choose Event preset / Platform  as the filter property.
   +  Operation: =
   +  Value: Web

1.  In the right **Attribute Grouping** area, configure grouping by selecting Geography/Country.

1.  In the time selector at the bottom, choose Past Month and click **OK**.

1.  Click the **Save to Dashboard** button in the top right corner. In the pop-up dialog, enter:
   +  Chart Name: PV and UV
   +  Chart Description: PV and UV on the web over the past month (at least 30 seconds)
   +  Choose a Dashboard: Select a dashboard. (You need to create a dashboard first. For more information, see [Create dashboard](dashboards-1.md#custom-report).)
   +  Choose a Worksheet: Select a worksheet.
   +  Click **OK**.

 All configurations are shown below:

![Event analysis interface showing metrics configuration, filters, and parameter grouping settings.](http://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/explore-event-en.png)
