---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/pivot-table-limitations.html
---

# Pivot table limitations
<a name="pivot-table-limitations"></a>

The following limitations apply to pivot tables:
+ You can create pivot tables with up to 500,000 records.
+ You can add any combination of row and column field values that add up to 40. For example, if you have 10 row field values, then you can add up to 30 column field values.
+ You can create pivot table calculations only on nonaggregated values. For example, if you create a calculated field that is a sum of a measure, you can't also add a pivot table calculation to it.
+ If you are sorting by a custom metric, you can't add a table calculation until you remove the custom metric sort.
+ If you are using a table calculation and then add a custom metric, you can't sort by the custom metric.
+ Totals and subtotals are blank for table calculations on metrics aggregated by distinct count.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
