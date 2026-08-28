---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.UNNEST_STRUCT_N.html
---

# UNNEST\_STRUCT\_N
<a name="recipe-actions.UNNEST_STRUCT_N"></a>

Creates a new column for each field of a selected column of type `struct`.

For example, given the following struct:

```
            user {
               name: “Ammy”
               address: {
                  state: "CA",
                  zipcode: 12345
               }
            }
```

This function creates 3 columns:

| user.name | user.address.state | user.address.zipcode |
| --- | --- | --- |
| Ammy | CA | 12345 |

**Parameters**
+ `sourceColumns` — List of the source columns.
+ `regexColumnSelector` — A regular expression to select the columns to unnest.
+ `removeSourceColumn` — A Boolean value. If true, then remove the source column; otherwise keep it.
+ `unnestLevel` — The number of levels to unnest.
+ `delimiter` — The delimiter is used in the newly created column name to separate the different levels of the struct. For example: if the delimiter is “/”, the column name will be in this form: “user/address/state”.
+ `conditionExpressions` — Condition expressions.

**Example**

```
{
    "RecipeAction": {
        "Operation": "UNNEST_STRUCT_N",
        "Parameters": {
            "sourceColumns": "[\"address\"]",
            "removeSourceColumn": "true",
            "unnestLevel": "2",
            "delimiter": "/"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
