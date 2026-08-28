---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/troubleshooting-dataset-changed-columns.html
---

# My visual can’t find missing columns
<a name="troubleshooting-dataset-changed-columns"></a>

The visuals in my analysis aren't working as expected. The error message says `"The column(s) used in this visual do not exist."`

The most common cause of this error is that your data source schema changed. For example, it's possible a column name changed from `a_column` to `b_column`.

Depending on how your dataset accesses the data source, choose one of the following.
+ If the dataset is based on custom SQL, do one or more of the following:
  + Edit the dataset.
  + Edit the SQL statement.

    For example, if the table name changed from `a_column` to `b_column`, you can update the SQL statement to create an alias: `SELECT b_column as a_column`. By using the alias to maintain the same field name in the dataset, you avoid having to add the column to your visuals as a new entity.

  When you're done, choose **Save & visualize**.
+ If the dataset isn't based on custom SQL, do one or more of the following:
  + Edit the dataset.
  + For fields that now have different names, rename them in the dataset. You can use the field names from your original dataset. Then open your analysis and add the renamed fields to the affected visuals.

  When you're done, choose **Save & visualize**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
