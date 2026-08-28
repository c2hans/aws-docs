---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.MILLISECOND.html
---

# MILLISECOND
<a name="recipe-actions.functions.MILLISECOND"></a>

Creates a new column containing the millisecond value from a source column or input value.

**Parameters**
+ `sourceColumn` – The name of an existing column. The source column can be of type `string`, `date`, or `timestamp`.
+ `value` – A character string to evaluate.
+ `targetColumn` – A name for the newly-created column.

**Note**
You can specify either `sourceColumn` or `value`, but not both.

**Example**

```
{
    "RecipeAction": {
        "Operation": "MILLISECOND",
        "Parameters": {
            "sourceColumn": "DATETIME Column 1",
            "targetColumn": "DATETIME Column 1_MILLISECOND"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
