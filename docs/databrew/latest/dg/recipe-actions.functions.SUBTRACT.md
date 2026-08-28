---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.SUBTRACT.html
---

# SUBTRACT
<a name="recipe-actions.functions.SUBTRACT"></a>

Subtracts one number from another and returns the result in a new column.

**Parameters**
+ `sourceColumn1` – The name of an existing column.
+ `value1` – A numeric value.
+ `sourceColumn2` – The name of an existing column.
+ `value2` – A numeric value.
+ `targetColumn` – The name of the new column to be created.

**Example**

```
{
    "RecipeAction": {
        "Operation": "SUBTRACT",
        "Parameters": {
            "sourceColumn1": "weight_kg",
            "targetColumn": "weight_minus_10_kg",
            "value2": "10"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
