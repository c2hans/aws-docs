---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements-using-models.html
---

# Using third-party Bedrock models with granted licenses
<a name="managed-entitlements-using-models"></a>

After you activate a grant in your account, you can invoke the third-party Amazon Bedrock model using the Amazon Bedrock console, AWS CLI, or AWS SDKs. The experience is the same as invoking a model with a direct subscription.

## To verify you have an active license
<a name="managed-entitlements-verify-active"></a>

Before attempting to use a third-party Bedrock model, verify that your grant is in an Active state.

1. Open the AWS License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. Make sure you are in the us-east-1 Region.

1. In the navigation pane, choose **Granted Licenses**.

1. Find the grant for the third-party Bedrock model you want to use.

1. Verify the Grant status shows as **Active**.

If the status shows Disabled, you must activate the grant before using the model. If the status shows Pending Acceptance, you must first accept the grant.

## To invoke a third-party Bedrock model with a granted license
<a name="managed-entitlements-invoke-model"></a>

1. Open the Amazon Bedrock console in any supported Region where the model is available.

1. In the navigation pane, choose **Text** or **Chat** under **Playgrounds**, depending on the model type.

1. Select the model you have a license for from the model dropdown.

1. Enter your prompt and choose **Run**.

The model invocation works the same way as if you had subscribed directly. All usage is billed to the account that holds the original subscription (typically the management account).

You can also invoke models programmatically using the AWS CLI or AWS SDKs with the [InvokeModel API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html). The only requirement is that you have an active license grant in your account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
