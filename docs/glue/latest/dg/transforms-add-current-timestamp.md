---
source_url: https://docs.aws.amazon.com/glue/latest/dg/transforms-add-current-timestamp.html
---

# Using the Add Current Timestamp transform
<a name="transforms-add-current-timestamp"></a>

 The **Add Current Timestamp** transform allows you to mark the rows with the time on which the data was processed. This is useful for auditing purposes or to track latency in the data pipeline. You can add this new column as a timestamp data type or a formatted string.

**To add a Add Current Timestamp transform:**

1. Open the Resource panel and then choose **Add Current Timestamp** to add a new transform to your job diagram. The node selected at the time of adding the node will be its parent.

1. (Optional) On the **Node properties** tab, you can enter a name for the node in the job diagram. If a node parent is not already selected, then choose a node from the Node parents list to use as the input source for the transform.
![The screenshot shows the Transform tab for the Add Current Timestamp transform.](http://docs.aws.amazon.com/glue/latest/dg/images/transforms-add-current-timestamp-transform-tab.png)

1. (Optional) On the **Transform** tab, enter a custom name for the new column and a format if you rather the column to be a formatted date string.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
