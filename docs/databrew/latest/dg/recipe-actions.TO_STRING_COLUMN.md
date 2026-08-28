---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.TO_STRING_COLUMN.html
---

# TO\_STRING\_COLUMN
<a name="recipe-actions.TO_STRING_COLUMN"></a>

Changes the data type of an existing column to STRING.

**Note**
We recommend using CHANGE\_DATA\_TYPE recipe action rather than TO\_STRING\_COLUMN.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – A value that must be `string`.

**Example**

```
{
    "RecipeAction": {
        "Operation": "TO_STRING_COLUMN",
        "Parameters": {
            "columnDataType": "string",
            "sourceColumn": "age"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
