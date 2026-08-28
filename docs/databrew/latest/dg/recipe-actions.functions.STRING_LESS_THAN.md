---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.STRING_LESS_THAN.html
---

# STRING\_LESS\_THAN
<a name="recipe-actions.functions.STRING_LESS_THAN"></a>

Creates a new column populated with one of the following:
+ `True` if one string in a column (or value) is less than another string in a different column (or value).
+ `False` if there is no match.

**Parameters**
+ `sourceColumn1` – The name of an existing column.
+ `sourceColumn2` – The name of an existing column.
+ `value1` – A character string to evaluate.
+ `value2` – A character string to evaluate.
+ `targetColumn` – The name of the new column to be created.

**Note**
You can specify only one of the following combinations:
Both of `sourceColumn{{N}}`.
One of `sourceColumn{{N}}` and one of `value{{N}}`.
Both of `value{{N}}`.

**Example**

```
{
    "RecipeAction": {
        "Operation": "STRING_LESS_THAN",
        "Parameters": {
            "sourceColumn1": "first_name",
            "sourceColumn2": "last_name",
            "targetColumn": "string_less_than"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
