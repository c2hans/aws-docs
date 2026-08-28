---
source_url: https://docs.aws.amazon.com/entityresolution/latest/userguide/delete-records.html
---

# Deleting records from a rule-based or ML-based matching workflow
<a name="delete-records"></a>

If you need to comply with data management regulations, you can delete the records from either a rule-based or ML-based matching workflow.

**To delete records from a rule-based or ML-based matching workflow**

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/).

1. In the left navigation pane, under **Workflows**, choose **Matching**.

1. Choose the rule-based or ML-based matching workflow.

1. On the matching workflow details page, choose **Delete unique IDs** from the **Actions** dropdown list.

1. Enter the unique ID you want to delete in the **Unique IDs** section.

   You can enter up to 10 unique IDs.

1. Specify the **Input source** from which to delete the unique IDs.

   If there is only one **Input source** for the workflow, the **Input source** is listed by default.

   If you only specify one **Input source**, the unique IDs in other input sources won't be affected.

1. Choose **Delete unique IDs**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
