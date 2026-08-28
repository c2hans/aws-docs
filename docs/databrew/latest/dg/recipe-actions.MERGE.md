---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.MERGE.html
---

# MERGE
<a name="recipe-actions.MERGE"></a>

Merges two or more columns into a new column.

**Parameters**
+ `sourceColumns` – A JSON-encoded string representing a list of one or more columns to be merged.
+ `delimiter` – An optional separator between the values, to appear in the target column.
+ `targetColumn` – The name of the merged column to be created.

**Example**

```
{
    "RecipeAction": {
        "Operation": "MERGE",
        "Parameters": {
            "delimiter": " ",
            "sourceColumns": "[\"first_name\",\"last_name\"]",
            "targetColumn": "Merged Column 1"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
