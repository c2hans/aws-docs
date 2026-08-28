---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/exploration.html
---

# Exploration
<a name="exploration"></a>

 The Exploration module provides a collection of advanced analytics models with flexible and easy-to-use query method, allowing you to derive deeper insights from your clickstream data.

 When you want to explore the clickstream data in more details, you can use explorations to:
+  perform ad hoc queries
+  focus on the most relevant data by using filters on event parameters and user attributes
+  group metrics by dimension to make it easy to compare
+  easily switch visualization type and drill down or up into data
+  view and export summary data into the excel or csv
+  save the explorative analytics results into a dashboard for share or regular use

## Access Exploration
<a name="access-exploration"></a>

 You can create an ingestion module with the following settings:

 To access Explorations, follow below steps:

1.  Go to Clickstream Analytics on AWS Console, in the **Navigation Bar**, choose **Analytics Studio**.

1.  In the Analytics Studio page that opens, choose **Explorations** in the left navigation panel.

## How Exploration works
<a name="how-exploration-works"></a>

 Currently, exploration provides 4 analytics models:

|  **Report name**  |  **Description**  |
| --- | --- |
|  [Event Analysis](event-analysis.md)  |  Event analysis is used to study the frequency of certain behavioral events. You can conduct multi-dimensional analysis of user behavior through custom metrics, groupings, filters, and various visual charts.  |
|  [Funnel Analysis](funnel-analysis.md)  |  Funnel analysis, or conversion analysis, is mainly used to analyze the conversion status of users in a specified process. The model first breaks down the entire process into steps and then counts the conversion rate from each step to the next. It can be used to measure the performance of each step. Common usage scenarios include analyzing registration conversion rates, purchase conversion rates, etc.  |
|  [Path Analysis](path-analysis.md)  |  Path analysis refers to the distribution of the behavior of a group of users after sorting them in sequential order. It is mainly used to analyze and record the distribution ratio of users between pages or events. For example, check how many customers clicked on the product list after opening the app, how many customers viewed the product detail page after visiting landing page, how many customers searched for the product, etc.  |
|  [Retention Analysis](retention-analysis.md)  |  Retention analysis supports configuring initial event and returning event to calculate the retention or attrition rate of target user groups. It also supports setting associated attributes for initial event and return event.  |
| [Attribution Analysis](attribution-analysis.md) | Attribution analysis allows you to understand the importance of different touchpoints for a specific goal in your website and apps. |

## How to use Exploration
<a name="how-to-use-exploration"></a>

 Explorations interface consists of the following components:

![Explore module interface showing analytics model selector, filters, parameter grouping, date range, and query options.](http://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/explore.png)

+  **Analytics Model**. A drop-down list to select or switch analytics model.
+  **Model Configuration**. Specifies the configurations for the analytics model, such as select event, adding filters. Each model might have different configuration.
+  **Global Filters**. Filters that apply to all the metrics that defined in the Model Configuration. You can add multiple filters and adjust the filter relationship (i.e., 'And' or 'Or').
+  **Grouping**. Group the analytics result by specified parameter's value, make it easy for you can compare the metrics at a dimension.
+  **Analysis Time Range**. Specifies the time range for the analysis.
+  **Aggregation Granularity**. Specifies the level of granularity to display metrics, such by day, week, or month.
+  **Visual Type**. Specifies the chart type of the visualization.
+  **Save to Dashboard**. Save the exploration analysis
+  **Result Display Area**. Show visualization and detail data.
+  **Help Panel**. Display additional helpful info when click "Info" icon.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
