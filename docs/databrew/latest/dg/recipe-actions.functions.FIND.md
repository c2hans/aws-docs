---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.FIND.html
---

# FIND
<a name="recipe-actions.functions.FIND"></a>

Searching left to right, finds strings that match a specified string from the source column or from a custom value, and returns the result in a new column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `pattern` – A regular expression to search for.
+ `position` – The character position to begin with, from the left end of the string.
+ `ignoreCase` – If `true`, ignore differences of case (between uppercase and lowercase) among letters. To enforce strict matching, use `false` instead.
+ `targetColumn` – The name of the new column to be created.

**Example**

```
{
    "RecipeAction": {
        "Operation": "FIND",
        "Parameters": {
            "sourceColumn": "city",
            "pattern": "[AEIOU]",
            "position": "1",
            "ignoreCase": "false",
            "targetColumn": "begins_with_a_vowel"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
