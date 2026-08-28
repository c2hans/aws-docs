---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.FORMAT_DATE.html
---

# FORMAT\_DATE
<a name="recipe-actions.FORMAT_DATE"></a>

Returns a column in which a date string is converted into a formatted value.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetDateFormat` – One of the following date formats:
  + `mm/dd/yyyy`
  + `mm-dd-yyyy`
  + `dd month yyyy`
  + `month yyyy`
  + `dd month`

**Example**

```
{
    "RecipeAction": {
        "Operation": "FORMAT_DATE",
        "Parameters": {
            "sourceColumn": "birth_date",
            "targetDateFormat": "mm-dd-yyyy"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
