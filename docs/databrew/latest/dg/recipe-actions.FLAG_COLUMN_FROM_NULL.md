---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.FLAG_COLUMN_FROM_NULL.html
---

# FLAG\_COLUMN\_FROM\_NULL
<a name="recipe-actions.FLAG_COLUMN_FROM_NULL"></a>

Creates a new column, based on the presence of null values in an existing column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – The name of a new column to be created.
+ `flagType` – A value that must be set to `Null values`.
+ `trueString` – A value for the new column, if a null value is found in the source. If no value is specified, the default is `True`.
+ `falseString` – A value for the new column, if a non-null value is found in the source. If no value is specified, the default is `False`.

**Example**

```
{
    "RecipeAction": {
        "Operation": "FLAG_COLUMN_FROM_NULL",
        "Parameters": {
            "flagType": "Null values",
            "sourceColumn": "weight_kg",
            "targetColumn": "is_weight_kg_missing"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
