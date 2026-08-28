---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-stop-session.html
---

# Stopping a AgentCore Code Interpreter session
<a name="code-interpreter-stop-session"></a>

When you are finished using a Code Interpreter session, you should stop it to release resources and avoid unnecessary charges.

**Example**

1. To stop a code interpreter session using the AWS CLI, use the `stop-code-interpreter-session` command:

   ```
   aws bedrock-agentcore stop-code-interpreter-session \
     --region <Region> \
     --code-interpreter-id "<your-code-interpreter-id>" \
     --session-id "<your-session-id>"
   ```

1. To stop a Code Interpreter session using the AWS SDK for Python, use the `stop_code_interpreter_session` method:

   ```
   import boto3

   # Initialize the boto3 client
   dp_client = boto3.client(
       'bedrock-agentcore',
       region_name="<Region>",
       endpoint_url="https://bedrock-agentcore.<Region>.amazonaws.com"
   )

   # Stop the Code Interpreter session
   response = dp_client.stop_code_interpreter_session(
       codeInterpreterIdentifier="aws.codeinterpreter.v1",
       sessionId="<your-session-id>"
   )

   print("Session stopped successfully")
   ```

1. To stop a code interpreter session using the API, use the following call:

   ```
   # Using awscurl
   awscurl -X PUT \
     "https://bedrock-agentcore.<Region>.amazonaws.com/code-interpreters/aws.codeinterpreter.v1/sessions/stop?sessionId=<your-session-id>" \
     -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     --service bedrock-agentcore \
     --region <Region>
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
