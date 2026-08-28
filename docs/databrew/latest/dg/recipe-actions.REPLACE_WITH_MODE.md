---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.REPLACE_WITH_MODE.html
---

# REPLACE\_WITH\_MODE
<a name="recipe-actions.REPLACE_WITH_MODE"></a>

Replaces each invalid value in a column with the mode of all other values.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – The data type of the column. This type must be `number`.
+ `modeType` – How to resolve tie values in the data. This value must be `MINIMUM`, `NONE`, `AVERAGE`, or `MAXIMUM`.

**Example**

```
{
    "RecipeAction": {
        "Operation": "REPLACE_WITH_MODE",
        "Parameters": {
            "columnDataType": "number",
            "modeType": "MAXIMUM",
            "sourceColumn": "height_cm"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
