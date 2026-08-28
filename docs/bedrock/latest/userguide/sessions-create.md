---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/sessions-create.html
---

# Create a session to prepare to store conversation history and context
<a name="sessions-create"></a>

To create a session, you use the [CreateSession](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_CreateSession.html) API operation. In the response, Amazon Bedrock returns a unique session ID and Amazon Resource Name (ARN) for the session. You use either the session ID or the ARN when you use the [CreateInvocation](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_CreateInvocation.html) and [PutInvocationStep](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_PutInvocationStep.html) API operations to record the session events.

When you create a session, you can specify a AWS KMS key to encrypt conversations. For information about encryption, see [Session encryption](sessions-encryption.md).

```
def create_session():
try:
    session_id = client.create_session(
        encryptionKeyArn="arn:aws:kms:us-west-2:<123456789012>:key/keyId",
        tags={
            'Environment': 'Test',
            'Project': 'Demo'
        },
        sessionMetadata={
            "deviceType": "mobile"
        }
    )["sessionId"]
    print("Session created. Session ID: " + session_id)
    return session_id
except ClientError as e:
    print(f"Error: {e}")
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
