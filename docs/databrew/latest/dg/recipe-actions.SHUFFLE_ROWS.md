---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.SHUFFLE_ROWS.html
---

# SHUFFLE\_ROWS
<a name="recipe-actions.SHUFFLE_ROWS"></a>

Shuffles values in a given column. The shuffling can occur with values grouped by a secondary column.

**Parameters**
+ `sourceColumns` – An array of existing columns.
+ `groupByColumns` – An array of columns to group the source columns by while shuffling.

**Example**

```
{
   "sourceColumns": ["age"],
   "*groupByColumns*": ["country"]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
