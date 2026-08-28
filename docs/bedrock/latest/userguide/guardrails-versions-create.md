---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-versions-create.html
---

# Create a version of a guardrail
<a name="guardrails-versions-create"></a>

To create a version of a guardrail, choose the tab for your preferred method, and then follow the steps:

------
#### [ Console ]

**To create a version of an existing guardrail follow these steps:**

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock).

1. Select **Guardrails** from the left navigation pane in the Amazon Bedrock console and choose the name of the guardrail that you want to edit in the **Guardrails** section.

1. Carry out one of the following steps.
   + In the **Versions**, section, select **Create**.
   + Choose the **Working draft** and select **Create version** at the top of the page

1. Provide an optional description for the version and then select **Create version**.

1. If successful, you will be redirected to the screen with a list of versions with your new version added there.

------
#### [ API ]

To create a version of your guardrail, send a [CreateGuardrailVersion](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateGuardrailVersion.html) request. Include the guardrail ID and an optional description.

The request format is as follows:

```
POST /guardrails/{{guardrailIdentifier}} HTTP/1.1
Content-type: application/json

{
  "clientRequestToken": "string",
  "description": "string"
}
```

The response format is as follows:

```
HTTP/1.1 202
Content-type: application/json

{
   "guardrailId": "string",
   "version": "string"
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
