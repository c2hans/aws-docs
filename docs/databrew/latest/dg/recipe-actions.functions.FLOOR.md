---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.FLOOR.html
---

# FLOOR
<a name="recipe-actions.functions.FLOOR"></a>

Returns the largest integral number greater than or equal to the input number in a new column.

**Parameters**
+ `sourceColumn1` – The name of an existing column.
+ `value` – A numeric value.
+ `targetColumn` – The name of the new column to be created.

**Example**

```
{
    "RecipeAction": {
        "Operation": "FLOOR",
        "Parameters": {
            "targetColumn": "FLOOR Column 1",
            "value": "42"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
