---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/retention-analysis.html
---

# Retention Analysis
<a name="retention-analysis"></a>

 Retention rate is a common metric used to assess the user stickiness for an app or website. Retention means that the user returns to your app or website again some time after they used your app. In addition to the standard retention metrics in the default dashboard, Retention Analysis module allows you to select a start event and returning event to customize a retention or attrition rate of a target user group.

## Use cases
<a name="use-cases-3"></a>

 Retention analysis is commonly used to understand how well your app or website is doing in terms of retaining users.
+  Calculate new user retention rate to measure the effectiveness of traffic channel;
+  Calculate the active user retention rate to measure the effectiveness for a promotion campaign;
+  Compare the repurchase rate for different groups of users to identify the most valuable customers.

## Key concept
<a name="key-concept-1"></a>
+  **Start**: the event indicates that users start using the app or website.
+  **Revisit**: the event indicates that users returning to the app or website.
+  **Associated parameter**: Associated parameter are used to keep the value of a parameter consistent between the starting event and the return event. For example, promotion campaign name, page title, or product titles must be the same values for both starting event and return event.

**Note**
 The two associated parameter must both have values, and the value types must be consistent.
+  **Retention Rate**: retention rate refers to the relationship between the number of users who perform the specified starting event on the start date (or week, or month depending on the granularity selection) and the number of the same users who perform the specified returning event on the the return date (or week, or month).

## How to use retention analysis
<a name="how-to-use-retention-analysis"></a>

1.  Select a **Start** event, you can add filter to the event by clicking the filter icon.

1.  Select a **Revisit** event, you can add filter to the event by clicking the filter icon.

1.  If needed, you can toggle on **Associate parameter**, then select parameters for both starting event and return event.

1.  Repeat above step to add more metric if needed.

1.  If needed, configure global filter by selecting event parameter or user attributes. Similar to event filter, you can add multiple global filters and configure the filter relationship.

1.  If needed, configure grouping by selecting an event parameter or user attribute.

1.  Choose **Query** to start the analysis.

1.  Adjust the data granularity, such as Daily, Weekly, Monthly, if needed.

1.  Specify query time range.
**Note**
 The start time will be the starting point (i.e., day 0) for the retention analysis, and the retention rate % will be calculated against the number of users who performed the specified starting event on the start date (or week, or month depends on the granularity selection).

1.  Choose **Save to Dashboard** to save the analysis to a Dashboard. Enter a name, description, and select a dashboard and sheet.

## Example
<a name="example-3"></a>

 Calculate the retention rate of new customers who downloaded from different app markets on Android one week ago.

1.  Select the **Retention Analysis** model.

1.  Choose \_first\_open as the start event.

1.  Choose \_app\_start as the return event.

1.  Configure a global filter in the right **Filters** area:
   +  Choose Event preset / Platform as the filter property.
   +  Operation: =
   +  Value: Android

1.  In the right **Attribute Grouping** area, configure grouping by selecting Application / App install source.

1.  Click **Query**.

 All configurations are as shown in the image below:

![Retention analysis configuration with Start and Revisit metrics, filters for Android platform, and parameter grouping by app_info.install_source.](http://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/explore-retention-en.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
