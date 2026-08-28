---
source_url: https://docs.aws.amazon.com/glue/latest/dg/transforms-filter.html
---

# Filtering keys within a dataset
<a name="transforms-filter"></a>

Use the *Filter* transform to create a new dataset by filtering records from the input dataset based on a regular expression. Rows that don't satisfy the filter condition are removed from the output.
+ For string data types, you can filter rows where the key value matches a specified string.
+ For numeric data types, you can filter rows by comparing the key value to a specified value using the comparison operators `<`, `>`, `=`, `!=`, `<=`, and `>=`.

If you specify multiple filter conditions, the results are combined using an `AND` operator by default, but you can choose `OR` instead.

The *Filter* transform is case sensitive. Add an *ApplyMapping* transform as a parent node if you need case-insensitive property key names.

**To add a Filter transform node to your job diagram**

1. (Optional) Open the Resource panel and then choose **Filter** to add a new transform to your job diagram, if needed.

1. On the **Node properties** tab, enter a name for the node in the job diagram. If a node parent isn't already selected, then choose a node from the **Node parents** list to use as the input source for the transform.

1. Choose the **Transform** tab.

1. Choose either **Global AND** or **Global OR**. This determines how multiple filter conditions are combined. All conditions are combined using either `AND` or `OR` operations. If you have only a single filter conditions, then you can choose either one.

1. Choose the **Add condition** button in the **Filter condition** section to add a filter condition.

   In the **Key** field, choose a property key name from the dataset. In the **Operation** field, choose the comparison operator. In the **Value** field, enter the comparison value. Here are some examples of filter conditions:
   + `year >= 2018`
   + `State matches 'CA*'`

   When you filter on string values, make sure that the comparison value uses a regular expression format that matches the script language selected in the job properties (Python or Scala).

1. Add additional filter conditions, as needed.

1. (Optional) After configuring the transform node properties, you can view the modified schema for your data by choosing the **Output schema** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. If you have not specified an IAM role on the **Job details** tab, you are prompted to enter an IAM role here.

1. (Optional) After configuring the node properties and transform properties, you can preview the modified dataset by choosing the **Data preview** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. There is a cost associated with using this feature, and billing starts as soon as you provide an IAM role.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
