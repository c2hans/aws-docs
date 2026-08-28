---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.CEILING.html
---

# CEILING
<a name="recipe-actions.functions.CEILING"></a>

Returns the smallest integer number greater than or equal to the input decimal numbers in a new column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `value1` – A numeric value.
+ `targetColumn` – The name of the new column to be created.

**Example**

```
{
    "RecipeAction": {
        "Operation": "CEILING",
        "Parameters": {
            "sourceColumn": "weight_kg",
            "targetColumn": "weight_kg_CEILING"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
