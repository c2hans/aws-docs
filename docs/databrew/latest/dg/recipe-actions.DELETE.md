---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.DELETE.html
---

# DELETE
<a name="recipe-actions.DELETE"></a>

Removes a column from the dataset.

**Parameters**
+ `sourceColumn` – The name of an existing column.

**Example**

```
{
    "RecipeAction": {
        "Operation": "DELETE",
        "Parameters": {
            "sourceColumn": "extra_data"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
