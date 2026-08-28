---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.ADD_SUFFIX.html
---

# ADD\_SUFFIX
<a name="recipe-actions.ADD_SUFFIX"></a>

Adds one more characters concatenating them as a suffix to the end of a column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `pattern` – The character or characters to place at the end of the column.

**Example**

```
{
    "RecipeAction": {
        "Operation": "ADD_SUFFIX",
        "Parameters": {
            "pattern": "bbb",
            "sourceColumn": "info_url"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
