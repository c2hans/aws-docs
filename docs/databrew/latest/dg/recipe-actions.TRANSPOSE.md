---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.TRANSPOSE.html
---

# TRANSPOSE
<a name="recipe-actions.TRANSPOSE"></a>

Converts all selected rows to columns and columns to rows.

![Table transformation from rows to columns, showing data reorganization for improved analysis.](http://docs.aws.amazon.com/databrew/latest/dg/images/transpose.png)

**Parameters**
+ `pivotColumns` — A JSON-encoded string representing a list of columns whose rows will be converted to column names.
+ `valueColumns` — A JSON-encoded string representing a list of one or more columns to be converted to rows.
+ `aggregateFunction` — The name of an aggregation function. If you don't want aggregation, use the keyword `COLLECT_LIST`.
+ `newColumn` — The column to hold transposed columns as values.

**Example**

```
{
    "Action": {
        "Operation": "TRANSPOSE",
        "Parameters": {
            "pivotColumns": "[\"Teacher\"]",
            "valueColumns": "[\"Tom\",\"John\",\"Harry\"]",
            "aggregateFunction": "COLLECT_LIST",
            "newColumn": "Student"
        }
    }

}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
