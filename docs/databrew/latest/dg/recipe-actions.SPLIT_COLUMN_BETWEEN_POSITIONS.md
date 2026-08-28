---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.SPLIT_COLUMN_BETWEEN_POSITIONS.html
---

# SPLIT\_COLUMN\_BETWEEN\_POSITIONS
<a name="recipe-actions.SPLIT_COLUMN_BETWEEN_POSITIONS"></a>

Splits a column into three new columns, according to offsets that you specify.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `startPosition` – The character position where the split is to begin.
+ `endPosition` – The character position where the split is to end.

**Example**

```
{
    "RecipeAction": {
        "Operation": "SPLIT_COLUMN_BETWEEN_POSITIONS",
        "Parameters": {
            "endPosition": "12",
            "sourceColumn": "last_name",
            "startPosition": "2"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
