---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.UNNEST_MAP.html
---

# UNNEST\_MAP
<a name="recipe-actions.UNNEST_MAP"></a>

Unnests a column of type `map` and generates a column for the key and value. If there is more than one key-value pair, a row corresponding to each key value would be generated. This function only unnests one level of a map column.

**Parameters**
+ `sourceColumn` — The name of an existing column. This column must be of `struct` type.
+ `removeSourceColumn` — If `true`, the source column is deleted after the function is complete.
+ `targetColumn` — If provided, each of the generated column will start with this as the prefix.

**Example**

```
{
    "RecipeAction": {
        "Operation": "UNNEST_MAP",
        "Parameters": {
            "sourceColumn": "address",
            "removeSourceColumn": "false",
            "targetColumn": "address"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
