---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/funnel-analysis.html
---

# Funnel Analysis
<a name="funnel-analysis"></a>

 Funnel analysis, or conversion analysis, is mainly used to analyze the conversion status of users in a specified process. The model first breaks down the entire process into steps and then counts the conversion rate from each step to the next. It can be used to measure the performance of each step.

## Use cases
<a name="use-cases-1"></a>

 Funnel analysis is commonly used when analyzing the following user behaviors:
+  Analysis of the conversion rate of the key process in a product such as order to purchase rate, and registration completion rate;
+  Analysis of the conversion rate of promotion such as conversion rate of different in-app promotion spot;
+  Analysis of marketing channels's effectiveness such as purchase rate of new users brought by different ad campaigns.

## Key concepts
<a name="key-concepts"></a>
+  **Metric**: The entity used for funnel analysis, such as event number or user number.
+  **Funnel**: A funnel is a sequence of events that represents a process. It contains at least two events, and each event represents a step in the funnel.
+  **Funnel window**: A funnel window refers to the time for the user to complete the entire process. It is considered a successful conversion only when the user completes all the selected steps within the set window period.

## How to use funnel analysis
<a name="how-to-use-funnel-analysis"></a>

1.  Select a metric type.

   1.  User number: calculate the number of distinct users passing through the entire funnel.

   1.  Event number: calculate the number of completions of the entire funnel.

1.  Configure the funnel window.

   1.  Custom: you can define any duration as the funnel window.

   1.  The day: complete the funnel within the same date of the first step.

1.  Select event for as the step. If needed, choose **\+Add Step** to add more steps. You can add up to 10 steps.

1.  Choose the filter button to filter the event. Only the events meeting the filter criterial will be considered as passing through the funnel. You can add multiple filters to one event.

1.  If needed, configure global filter by selecting event parameter or user attributes. Similar to event filter, you can add multiple global filters and configure the filter relationship.

1.  If needed, configure grouping by selecting an event parameter or an user attribute.

**Note**
The Funnel visualization does not support grouping. If you need to group funnel result, please select bar chart.

1.  If you want to only apply the grouping on the first event, toggle on Apply grouping to first step only. If this option is not selected, the grouping will apply to all the steps in the funnel, which means all the events should have parameter or attributes that used to group.

1.  Choose **Query** to start the analysis.

1.  Adjust the data granularity, such as Daily, Weekly, Monthly, if needed.

1.  Adjust query time range if needed.

1.  Choose **Save to Dashboard** to save the analysis to a Dashboard. Enter a name, description, and select a dashboard and sheet.

## Example
<a name="example-1"></a>

 Calculate the conversion rate of users on the web from opening the website -> viewing the product details page -> adding to the shopping cart -> making a payment over the past week.

1.  Select the **Funnel Analysis** model.

1.  Choose User number as the metric.

1.  In the left **Define Funnel** area, choose The Day as the funnel window.

1.  Choose \_session\_start, view\_item, add\_to\_cart, purchase as funnel events.

1.  Configure a global filter in the right **Filters** area:
   +  Choose Event preset / Platform as the filter property.
   +  Operation: =
   +  Value: Web

1.  Click **Query**.

 All configurations are as shown in the image below:

![Funnel analysis configuration showing User number metric, The Day window, four funnel steps, and Web filter applied.](http://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/explore-funnel-en.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
