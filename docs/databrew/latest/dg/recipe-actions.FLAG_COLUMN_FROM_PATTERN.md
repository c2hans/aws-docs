---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.FLAG_COLUMN_FROM_PATTERN.html
---

# FLAG\_COLUMN\_FROM\_PATTERN
<a name="recipe-actions.FLAG_COLUMN_FROM_PATTERN"></a>

Creates a new column, based on the presence of a user-specified pattern in an existing column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – The name of a new column to be created.
+ `flagType` – A value that must be set to `Pattern`.
+ `pattern` – A regular expression, indicating the pattern to be evaluated.
+ `trueString` – A value for the new column, if a null value is found in the source. If no value is specified, the default is `True`.
+ `falseString` – A value for the new column, if a non-null value is found in the source. If no value is specified, the default is `False`.

**Example**

```
{
    "RecipeAction": {
        "Operation": "FLAG_COLUMN_FROM_PATTERN",
        "Parameters": {
            "falseString": "No",
            "flagType": "Pattern",
            "pattern": "N.*",
            "sourceColumn": "wind_direction",
            "targetColumn": "northerly",
            "trueString": "yes"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
