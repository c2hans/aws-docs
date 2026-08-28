---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.POWER.html
---

# POWER
<a name="recipe-actions.functions.POWER"></a>

Returns the value of a number to the power of the exponent in a new column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `value` – A number whose value is to be raised.
+ `targetColumn` – The name of the new column to be created.
+ `exponent` – The power to which the value will be raised.

**Note**
You can specify either `sourceColumn` or `value`, but not both.

**Example**

```
{
    "RecipeAction": {
        "Operation": "POWER",
        "Parameters": {
            "exponent": "3",
            "sourceColumn": "age",
            "targetColumn": "age_cubed"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
