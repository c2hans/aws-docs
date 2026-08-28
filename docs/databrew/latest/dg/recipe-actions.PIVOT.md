---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.PIVOT.html
---

# PIVOT
<a name="recipe-actions.PIVOT"></a>

Converts all the row values in a selected column into individual columns with values.

![Diagram showing pivot column transformation: original table to new table with columns as values.](http://docs.aws.amazon.com/databrew/latest/dg/images/pivot.png)

**Parameters**
+ `sourceColumn` — The name of an existing column. The column can have a maximum of 10 distinct values.
+ `valueColumn` — The name of an existing column. The column can have a maximum of 10 distinct values.
+ `aggregateFunction` — The name of an aggregation function. If you don't want aggregation, use the keyword `COLLECT_LIST`.

**Example**

```
{
    "Action": {
        "Operation": "PIVOT",
        "Parameters": {
            "aggregateFunction": "SUM",
            "sourceColumn": "state_name",
            "valueColumn": "all_votes"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
