---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.MOVE_TO_INDEX.html
---

# MOVE\_TO\_INDEX
<a name="recipe-actions.MOVE_TO_INDEX"></a>

Moves a column to a position specified by a number.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetIndex` – The new position for the column. Positions start with 0—so, for example, `1` refers to the second column, `2` refers to the third column, and so on.

**Example**

```
{
    "RecipeAction": {
        "Operation": "MOVE_TO_INDEX",
        "Parameters": {
            "sourceColumn": "nationality",
            "targetIndex": "5"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
