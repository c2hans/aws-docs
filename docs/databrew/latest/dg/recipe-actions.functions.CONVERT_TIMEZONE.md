---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.CONVERT_TIMEZONE.html
---

# CONVERT\_TIMEZONE
<a name="recipe-actions.functions.CONVERT_TIMEZONE"></a>

Converts a time value from the source column into a new column based on a specified timezone.

**Parameters**
+ `sourceColumn` – The name of an existing column. The source column can be of type `string`, `date`, or `timestamp`.
+ `fromTimeZone` – Source value timezone. If nothing is specified, the default timezone is UTC.
+ `toTimeZone` – Timezone to be converted to. If nothing is specified, the default timezone is UTC.
+ `targetColumn` – A name for the newly-created column.
+ `dateTimeFormat` – Optional. A format string for the date. If the format isn't specified, the default format is used: `yyyy-mm-dd HH:MM:SS`.

**Example**

```
{
    "RecipeAction": {
        "Operation": "CONVERT_TIMEZONE",
        "Parameters": {
            "sourceColumn": "DATETIME Column 1",
            "fromTimeZone": "UTC+08:00",
            "toTimeZone": "UTC+08:00",
            "targetColumn": "DATETIME Column CONVERT_TIMEZONE",
            "dateTimeFormat": "yyyy-mm-dd HH:MM:SS"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
