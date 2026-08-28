---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.MEDIAN.html
---

# MEDIAN
<a name="recipe-actions.functions.MEDIAN"></a>

 Returns the median, the middle number of a sorted group of numbers, from the selected source columns in a new column. Any non-number is ignored.

**Parameters**
+ `sourceColumns` – A JSON-encoded string representing a list of existing columns.
+ `targetColumn` – A name for the newly created column.

**Example**

```
{
    "RecipeAction": {
        "Operation": "MEDIAN",
        "Parameters": {
            "sourceColumns": "[\"age\",\"years_in_service\"]",
            "targetColumn": "MEDIAN Column 1"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
