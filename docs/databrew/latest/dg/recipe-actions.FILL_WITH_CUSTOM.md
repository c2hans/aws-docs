---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.FILL_WITH_CUSTOM.html
---

# FILL\_WITH\_CUSTOM
<a name="recipe-actions.FILL_WITH_CUSTOM"></a>

Returns a column with missing data replaced by a specific value.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `columnDataType` – The data type for the column. This type must be `date`, `number`, `boolean`, `unsupported`, `string`, or `timestamp`.
+ `value` – The custom value to fill in. The data type must match the value that you choose for `columnDataType`.

**Example**

```
{
    "RecipeAction": {
        "Operation": "FILL_WITH_CUSTOM",
        "Parameters": {
            "columnDataType": "string",
            "sourceColumn": "last_name",
            "value": "No last name provided"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
