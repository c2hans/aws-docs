---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.REPLACE_BETWEEN_POSITIONS.html
---

# REPLACE\_BETWEEN\_POSITIONS
<a name="recipe-actions.REPLACE_BETWEEN_POSITIONS"></a>

Replaces the characters between two positions with user-specified text.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `startPosition` – A number indicting at what character position in the string the substitution is to begin.
+ `endPosition` – A number indicting at what character position in the string the substitution is to end.
+ `value` – The replacement character or characters to be substituted.

**Example**

```
{
    "RecipeAction": {
        "Operation": "REPLACE_BETWEEN_POSITIONS",
        "Parameters": {
            "endPosition": "20",
            "sourceColumn": "nationality",
            "startPosition": "10",
            "value": "E"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
