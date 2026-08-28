---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.ADD_PREFIX.html
---

# ADD\_PREFIX
<a name="recipe-actions.ADD_PREFIX"></a>

Adds one or more characters, concatenating them as a prefix to the beginning of a column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `pattern` – The character or characters to place at the beginning of the column values.

**Example**

```
{
    "RecipeAction": {
        "Operation": "ADD_PREFIX",
        "Parameters": {
            "pattern": "aaa",
            "sourceColumn": "info_url"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
