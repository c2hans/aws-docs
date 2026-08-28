---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/flows-version-delete.html
---

# Delete a version of a flow in Amazon Bedrock
<a name="flows-version-delete"></a>

To learn how to delete a version of a flow, choose the tab for your preferred method, and then follow the steps:

------
#### [ Console ]

**To delete a version of a flow**

1. Open the [AWS Management Console](https://console.aws.amazon.com) and sign in to your account. Navigate to Amazon Bedrock.

1. Select **Flows** from the left navigation pane. Then, in the **Flows** section, select a flow.

1. Choose **Delete**.

1. A dialog box appears warning you about the consequences of deletion. To confirm that you want to delete the version, enter **delete** in the input field and choose **Delete**.

1. A banner appears to inform you that the version is being deleted. When deletion is complete, a success banner appears.

------
#### [ API ]

To delete a version of a flow, send a [DeleteFlowVersion](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DeleteFlowVersion.html) request with an [Agents for Amazon Bedrock build-time endpoint](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#bra-bt). Specify the ARN or ID of the flow in the `flowIdentifier` field and the version to delete in the `flowVersion` field.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
