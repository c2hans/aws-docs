---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/sessions-delete-session.html
---

# Delete a session and all of its data
<a name="sessions-delete-session"></a>

After you end a session, you can delete it with the [DeleteSession](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_DeleteSession.html) API operation. Deleting a session deletes all Invocations, and InvocationSteps and associated data. You can’t undo deleting a session.

The following example code shows how to delete a session with the AWS SDK for Python (Boto3).

```
def delete_session(session_identifier):
try:
    client.delete_session(
        sessionIdentifier=session_identifier
    )
    print("session deleted")
except ClientError as e:
    print(f"Error: {e}")
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
