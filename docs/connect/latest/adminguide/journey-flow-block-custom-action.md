---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/journey-flow-block-custom-action.html
---

# Custom action
<a name="journey-flow-block-custom-action"></a>

## Description
<a name="journey-flow-block-custom-action-description"></a>

Use this block to call Lambda functions that fetch, validate, or transform data for use in the journey.

## How to configure this block
<a name="journey-flow-block-custom-action-configure"></a>

You can configure the **Custom action** block in the admin website or using the InvokeLambda action.

### Common properties
<a name="journey-flow-block-custom-action-common-properties"></a>

| Property | Description |
| --- | --- |
| Action | Select Invoke Lambda action |
| Function ARN | Select a registered Lambda function. |

**Example**

Invoke a Lambda to check offer eligibility, store the result in eligibilityStatus, and branch accordingly.

## Configuration
<a name="journey-flow-block-custom-action-configuration"></a>

Before you can invoke a Lambda using this block, you need to set up your Lambda functions at your Amazon Connect instance at AWS admin console. For more information, see [Invoke Lambda functions](lambda-invoke-functions.md).

When you do this for a journey flow block, you use the **Outbound campaigns** under the **Channels and communications** section, and to choose your Lambda function, you use the **Set up custom actions** section and then the **Lambda Functions** drop down.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
