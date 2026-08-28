---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/topics-in-analysis.html
---

# Using Topics in Quick Sight analysis
<a name="topics-in-analysis"></a>

|  |
| --- |
|  Applies to:  Enterprise Edition  |

|  |
| --- |
|    Intended audience:  Amazon Quick administrators and authors  |

You can use a Topic as the data model for your Quick Sight analysis. When you create an analysis from a Topic, you can select fields from any of the datasets in the Topic. Quick Sight automatically performs runtime inner joins based on the relationships you defined, assembling precisely the join it needs for each visual.

This means you no longer need to pre-join all your tables into a single flat dataset before building an analysis. Each dataset maintains its own level of detail, and Quick Sight joins only the relevant tables at analysis time.

## Creating an analysis from a Topic
<a name="topics-in-analysis-create"></a>

**To create an analysis from a Topic**

1. Navigate to the Topic and choose **Create analysis**.

1. Select **Interactive sheet** and choose **Create**.

1. In the analysis, select fields from multiple datasets and add them to a visual. Quick Sight performs runtime joins automatically based on the defined relationships.

1. (Optional) Create calculated fields that reference columns from different datasets.

## How runtime joins work in analysis
<a name="topics-in-analysis-how-joins-work"></a>

When a visual references fields from multiple datasets:

1. Quick Sight identifies which datasets contain the fields used in the visual.

1. It uses the defined relationships to determine the join path between datasets.

1. It performs inner joins at runtime using the specified join keys.

1. The result is displayed in the visual with the correct aggregation and grouping.

**Note**
Runtime joins in analysis use inner join semantics. Only rows with matching keys in both datasets appear in results. If you need outer join behavior for analytical scenarios, use the Topic in Amazon Quick chat instead, where the chat agent can generate SQL with outer joins based on your custom instructions.

## Benefits of using Topics in analysis
<a name="topics-in-analysis-benefits"></a>
+ **Less upfront data preparation.** Define relationships once. Quick Sight joins only the relevant tables at analysis time.
+ **Preserved native granularity.** Each dataset maintains its own level of detail, avoiding measure duplication across grains.
+ **Reuse across analyses.** A single Topic with defined relationships serves multiple analytical use cases without rebuilding datasets.
+ **Independent refresh schedules.** Each dataset can be refreshed at different cadences (hourly, daily, monthly) based on data volatility.
+ **Row-level security at runtime.** RLS rules are enforced during runtime joins, so data-access policies apply consistently across datasets.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
