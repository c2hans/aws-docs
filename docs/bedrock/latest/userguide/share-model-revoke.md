---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/share-model-revoke.html
---

# Revoke access to a shared model
<a name="share-model-revoke"></a>

To learn how to revoke access to a model that you've shared, choose the tab for your preferred method, and then follow the steps:

------
#### [ Console ]

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock).

1. From the left navigation pane, choose **Custom models** under **Tune**.

1. In the **Models** table, select the model that you want to revoke access to.

1. In the **Model sharing details** section, do the following to delete a model share and revoke access from the accounts specified in that model share:

   1. Select a model share and choose **Revoke shared model**.

   1. Review the message, type **revoke** in the text box, and choose **Revoke shared model** to confirm revoking of access.

------
#### [ API ]

To revoke access to a model from an account, send a [DisassociateResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_DisassociateResourceShare.html) request with an [AWS Resource Access Manager endpoint](https://docs.aws.amazon.com/general/latest/gr/ram.html). Specify the ARN of the share in the `resourceShareArn` field and the account whose access you want to revoke in the list of `principals`.

To completely delete a resource share by sending a [DeleteResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_DeleteResourceShare.html) request with an [AWS Resource Access Manager endpoint](https://docs.aws.amazon.com/general/latest/gr/ram.html). Specify the ARN of the share in the `resourceShareArn`.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
