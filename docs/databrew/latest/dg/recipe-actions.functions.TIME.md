---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.TIME.html
---

# TIME
<a name="recipe-actions.functions.TIME"></a>

Creates a new column containing the time value, from the source columns or values provided.

**Parameters**
+ `dateTimeFormat` – Optional. A format string for the date, as it is to appear in the new column. If this string isn't specified, the default format is `yyyy-mm-dd HH:MM:SS`.
+ `dateTimeParameters` – A JSON-encoded string representing the components of the date and time:
  + `year`
  + `value`
  + `month`
  + `day`
  + `hour`
  + `second`

  Each component must specify one of the following:
  + `sourceColumn` – The name of an existing column.
  + `value` – A character string to evaluate.
+ `targetColumn` – A name for the newly created column.

**Example**

```
{
    "RecipeAction": {
        "Operation": "TIME",
        "Parameters": {
            "dateTimeFormat": "HH:MM:SS",
            "dateTimeParameters": "{\"year\":{},\"month\":{},\"day\":{},\"hour\":{\"sourceColumn\":\"rand_hour\"},\"minute\":{\"sourceColumn\":\"rand_minute\"},\"second\":{\"sourceColumn\":\"rand_second\"}}",
            "targetColumn": "TIME Column 1"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
