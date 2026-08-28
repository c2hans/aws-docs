---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.REPLACE_WITH_ROLLING_AVERAGE.html
---

# REPLACE\_WITH\_ROLLING\_AVERAGE
<a name="recipe-actions.REPLACE_WITH_ROLLING_AVERAGE"></a>

Replaces each value in a column with the rolling average from a previous "window" of rows.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – The data type of the column. This type must be `number`.
+ `period` - – The size of the window. For example, if `period` is 10, the rolling average is computed using the previous 10 rows.

**Example**

```
{
    "RecipeStep": {
        "Action": {
            "Operation": "REPLACE_WITH_ROLLING_AVERAGE",
            "Parameters": {
                "sourceColumn": "created_at",
                "columnDataType": "number",
                "period": "2"
            }
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
