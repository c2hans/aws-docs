---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.UNNEST_ARRAY.html
---

# UNNEST\_ARRAY
<a name="recipe-actions.UNNEST_ARRAY"></a>

Unnests a column of type `array` into a new column. If the array contains more than one value, then a row corresponding to each element is generated. This function only unnests one level of an array column.

**Parameters**
+ `sourceColumn` — The name of an existing column. This column must be of `struct` type.
+ `targetColumn` — Name of the target column that is generated.

**Example**

```
{
    "RecipeAction": {
        "Operation": "UNNEST_ARRAY",
        "Parameters": {
            "sourceColumn": "address",
            "targetColumn": "address"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
