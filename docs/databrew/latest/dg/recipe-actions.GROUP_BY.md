---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.GROUP_BY.html
---

# GROUP\_BY
<a name="recipe-actions.GROUP_BY"></a>

Summarizes the data by grouping rows by one or more columns, and then applying an aggregation function to each group.

**Parameters**
+ `sourceColumns` — A JSON-encoded string representing a list of columns that form the basis of each group.
+ `groupByAggFunctions` — A JSON-encoded string representing a list of aggregation function to apply. (If you don't want aggregation, specify `UNAGGREGATED`.)
+ `useNewDataFrame` — If true, the results from GROUP\_BY are made available in the project session, replacing its current contents.

**Example**

```
[
  {
    "Action": {
      "Operation": "GROUP_BY",
      "Parameters": {
        "groupByAggFunctionOptions": "[{\"sourceColumnName\":\"all_votes\",\"targetColumnName\":\"all_votes_count\",\"targetColumnDataType\":\"number\",\"functionName\":\"COUNT\"}]",
        "sourceColumns": "[\"year\",\"state_name\"]",
        "useNewDataFrame": "true"
      }
    }
  }
]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
