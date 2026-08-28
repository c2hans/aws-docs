---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.MOVE_AFTER.html
---

# MOVE\_AFTER
<a name="recipe-actions.MOVE_AFTER"></a>

Moves a column to the position immediately after another column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – The name of another column. The column specified by `sourceColumn` will be moved immediately after the column specified by `targetColumn`.

**Example**

```
{
    "RecipeAction": {
        "Operation": "MOVE_AFTER",
        "Parameters": {
            "sourceColumn": "rating",
            "targetColumn": "height_cm"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
