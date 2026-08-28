---
source_url: https://docs.aws.amazon.com/entityresolution/latest/userguide/delete-schema-mapping.html
---

# Deleting a schema mapping
<a name="delete-schema-mapping"></a>

You can't delete a schema mapping when it's associated to a matching workflow. You must first remove the schema mapping from all associated matching workflows before you can delete it.

**To delete a schema mapping:**

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/).

1. In the left navigation pane, under **Data preparation**, choose **Schema mappings**.

1. Choose the schema mapping.

1. Choose **Delete**.

1. Confirm the deletion and then choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
