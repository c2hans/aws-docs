---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.MERGE.html
---

# MERGE\_COLUMNS\_AND\_VALUES
<a name="recipe-actions.functions.MERGE"></a>

Concatenates the strings in the source columns and returns the result in a new column. You can insert a delimiter between the merged values.

**Parameters**
+ `sourceColumns` – The names of two or more existing columns, in JSON-encoded format.
+ `delimiter` – Optional. One or more characters to place between each two source column values.
+ `targetColumn` – The name of the new column to be created.

**Example**

```
{
    "RecipeAction": {
        "Operation": "MERGE_COLUMNS_AND_VALUES",
        "Parameters": {
            "sourceColumns": "[\"last_name\",\"birth_date\"]",
            "delimiter": " was born on: ",
            "targetColumn": "merged_column"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
