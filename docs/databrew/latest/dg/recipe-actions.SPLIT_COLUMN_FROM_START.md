---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.SPLIT_COLUMN_FROM_START.html
---

# SPLIT\_COLUMN\_FROM\_START
<a name="recipe-actions.SPLIT_COLUMN_FROM_START"></a>

Splits a column into two new columns, at an offset from the beginning of the string.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `position` – The character position, from the left end of the string, where the split is to occur.

**Example**

```
{
    "RecipeAction": {
        "Operation": "SPLIT_COLUMN_FROM_START",
        "Parameters": {
            "position": "1",
            "sourceColumn": "first_name"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
