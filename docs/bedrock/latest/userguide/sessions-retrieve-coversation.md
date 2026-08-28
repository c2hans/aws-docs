---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/sessions-retrieve-coversation.html
---

# Retrieve conversation history and context from a session
<a name="sessions-retrieve-coversation"></a>

Use the [GetSession](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetSession.html), [ListInvocations](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListInvocations.html), and [GetInvocationStep](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetInvocationStep.html) API operations to retrieve session details, details for the interaction state at different checkpoints, and summary information for all invocations.

The following example code shows how to get text and image data for a checkpoint with the AWS SDK for Python (Boto3) and the [GetInvocationStep](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetInvocationStep.html) API operation.

```
def get_invocation_step(invocation_identifier, session_identifier, invocation_step_identifier):
try:
    response = client.get_invocation_step(
        sessionIdentifier=session_identifier,
        invocationIdentifier=invocation_identifier,
        invocationStepId=invocation_step_identifier
    )  ["invocationStep"]["payload"]["contentBlocks"]
    print(response)
except ClientError as e:
    print(f"Error: {e}")
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
