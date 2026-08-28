---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.REPLACE_BETWEEN_DELIMITERS.html
---

# REPLACE\_BETWEEN\_DELIMITERS
<a name="recipe-actions.REPLACE_BETWEEN_DELIMITERS"></a>

Replaces the characters between two delimiters with user-specified text.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `startPattern` – Character or characters or a regular expression, indicating where the substitution is to begin.
+ `endPattern` – Character or characters or a regular expression, indicating where the substitution is to end.
+ `value` – The replacement character or characters to be substituted.

**Example**

```
{
    "RecipeAction": {
        "Operation": "REPLACE_BETWEEN_DELIMITERS",
        "Parameters": {
            "endPattern": ">",
            "sourceColumn": "last_name",
            "startPattern": "&lt;",
            "value": "?"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
