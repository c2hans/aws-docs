---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.TO_BOOLEAN_COLUMN.html
---

# TO\_BOOLEAN\_COLUMN
<a name="recipe-actions.TO_BOOLEAN_COLUMN"></a>

Changes the data type of an existing column to BOOLEAN.

**Note**
We recommend using CHANGE\_DATA\_TYPE recipe action rather than TO\_BOOLEAN\_COLUMN.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – A value that must be `boolean`.

**Example**

```
{
    "RecipeAction": {
        "Operation": "TO_BOOLEAN_COLUMN",
        "Parameters": {
            "columnDataType": "boolean",
            "sourceColumn": "is_present"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
