---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.GET_ADVANCED_DATATYPE.html
---

# GET\_ADVANCED\_DATATYPE
<a name="recipe-actions.GET_ADVANCED_DATATYPE"></a>

Given a string column, identifies the advanced data type of the column, if any.

**Parameters**
+ `columnName` – The name of the string column.

**Example**

```
{
    "RecipeAction": {
        "Operation": "GET_ADVANCED_DATATYPE",
        "Parameters": {
            "sourceColumn": "columnName"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
