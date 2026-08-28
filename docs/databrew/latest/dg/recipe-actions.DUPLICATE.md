---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.DUPLICATE.html
---

# DUPLICATE
<a name="recipe-actions.DUPLICATE"></a>

Creates a new column with the different name, but with all of the same data. Both the old and new columns are retained in the dataset.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – A name for the duplicate column.

**Example**

```
{
    "RecipeAction": {
        "Operation": "DUPLICATE",
        "Parameters": {
            "sourceColumn": "last_name",
            "targetColumn": "copy_of_last_name"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
