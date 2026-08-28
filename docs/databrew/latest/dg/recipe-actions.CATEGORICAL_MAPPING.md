---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.CATEGORICAL_MAPPING.html
---

# CATEGORICAL\_MAPPING
<a name="recipe-actions.CATEGORICAL_MAPPING"></a>

Maps one or more categorical values to numeric or other values

**Parameters**
+ `sourceColumn` – The name of an existing column.

  `categoryMap` – A JSON-encoded string representing a map of values to categories.

  `deleteOtherRows` – If `true`, all non-mapped rows will be removed from the dataset.

  `other` – When provided, all non-mapped values will be replaced by this value.

  `keepOthers` – If true, all non-mapped values will remain the same.

  `mapType` – The data type of the mapped column.

  `targetColumn` – The name of a column to contain the results.

**Example**

```
{
    "Action": {
        "Operation": "CATEGORICAL_MAPPING",
        "Parameters": {
            "categoryMap": "{\"United States of America\":\"1\",\"Canada\":\"2\",\"Cuba\":\"3\",\"Haiti\":\"4\",\"Dominican Republic\":\"5\"}",
            "deleteOtherRows": "false",
            "keepOthers": "true",
            "mapType": "NUMERIC",
            "sourceColumn": "state_name",
            "targetColumn": "state_name_mapped"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
