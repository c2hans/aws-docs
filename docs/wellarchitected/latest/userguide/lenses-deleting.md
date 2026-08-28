---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-deleting.html
---

# Deleting a custom lens in AWS WA Tool
<a name="lenses-deleting"></a>

**To delete a custom lens**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Custom lenses**.

1. Select the custom lens to be deleted and choose **Delete**.

1. Choose **Delete**.

   Existing workloads with the lens applied are notified that the custom lens has been deleted, but can continue to use it. The custom lens can no longer be applied to new workloads.

**Disclaimer**
By sharing your custom lenses with other AWS accounts, you acknowledge that AWS will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own AWS account or terminate your AWS account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
