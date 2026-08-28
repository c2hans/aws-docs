---
source_url: https://docs.aws.amazon.com/glue/latest/dg/transforms-uuid.html
---

# Add a UUID column
<a name="transforms-uuid"></a>

When you add a *UUID* (Universally Unique Identified) column, each row will be assigned a unique 36-character string.

**To add a *UUID* transform node in your job diagram**

1. Open the Resource panel and then choose **UUID** to add a new transform to your job diagram. The node selected at the time of adding the node will be its parent.

1. (Optional) On the **Node properties** tab, you can enter a name for the node in the job diagram. If a node parent is not already selected, then choose a node from the **Node parents** list to use as the input source for the transform.

1. (Optional) On the **Transform** tab, you can customize the name of the new column. By default it will be named "uuid".

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
