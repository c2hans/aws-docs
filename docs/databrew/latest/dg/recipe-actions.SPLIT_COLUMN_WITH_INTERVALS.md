---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.SPLIT_COLUMN_WITH_INTERVALS.html
---

# SPLIT\_COLUMN\_WITH\_INTERVALS
<a name="recipe-actions.SPLIT_COLUMN_WITH_INTERVALS"></a>

Splits a column at intervals of *n* characters, where you specify *n*.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `startPosition` – The character position where the split is to begin.
+ `interval` – The number of characters to skip before the next split.

**Example**

```
{
    "RecipeAction": {
        "Operation": "SPLIT_COLUMN_WITH_INTERVALS",
        "Parameters": {
            "interval": "4",
            "sourceColumn": "nationality",
            "startPosition": "1"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
