---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/troubleshooting-dataset-changed-tables.html
---

# My visual can’t find the query table
<a name="troubleshooting-dataset-changed-tables"></a>

In this case, the visuals in your analysis aren't working as expected. The error message says `"Amazon Quick Sight can’t find the query table."`

The most common cause of this error is that your data source schema changed. For example, it's possible a table name changed from `x_table` to `y_table`.

Depending on how the dataset accesses the data source, choose one of the following.
+ If the dataset is based on custom SQL, do one or more of the following:
  + Edit the dataset.
  + Edit the SQL statement.

    For example, if the table name changed from `x_table` to `y_table`, you can update the FROM clause in the SQL statement to refer to the new table instead.

  When you're done, choose **Save & visualize**, then choose each visual and readd the fields as needed.
+ If the dataset isn't based on custom SQL, do the following:

  1. Create a new dataset using the new table, `y_table` for example.

  1. Open your analysis.

  1. Replace the original dataset with the newly created dataset. If there are no column changes, all the visuals should work after you replace the dataset. For more information, see [Replacing datasets](replacing-data-sets.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
