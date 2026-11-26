---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/sandbox-spaces-architecture.html
---

# Sandbox Spaces

A Sandbox Space is an AI agent workspace attached to a lease. Managers enable Sandbox Spaces in a lease template, and every lease created from that template gets its own Space. In the Innovation Sandbox web UI, users on the lease describe what they want to do in the account in plain language. The agent then runs AWS CLI commands in the lease’s sandbox account to create, change, and inspect resources. The agent works within the bounds of the user’s permission set, and its activity, including model usage, counts against the lease budget. For instructions on managing and using Sandbox Spaces, see [Managing Sandbox Spaces](administrator-guide.md#manage-sandbox-spaces) and [Using Sandbox Spaces](user-section.md#using-sandbox-spaces).

The Compute stack deploys the Sandbox Spaces components in every deployment, but the feature stays off until you turn it on. An administrator turns on Sandbox Spaces for the deployment and enables at least one model on the **Settings** page. The Hub Region must also be in the AccountPool stack’s **ISB Managed Regions** parameter. Otherwise, the agent rejects every chat message. The agent runs Amazon Bedrock inference in the Hub Region, and the solution cleans up only managed Regions when it recycles an account.

In the Hub account, an Amazon API Gateway WebSocket API receives each chat message and puts it in an Amazon SQS queue. An Amazon DynamoDB table records each open connection and the user’s identity. An AWS Lambda function, the agent worker, reads the message and invokes the agent in Amazon Bedrock AgentCore Runtime. The agent assumes a role in the sandbox account of the lease to call the Amazon Bedrock model and run AWS CLI commands. The agent worker then relays the response to the web UI through the WebSocket API. The following diagram shows this message flow from the web UI through the Hub account to the sandbox account.

![Sandbox Spaces components in the Hub account and the sandbox account.](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/diagrams/sandbox-spaces.drawio.png)

**Sandbox Spaces architecture**
The following steps describe how the solution processes a chat message, from the web UI to the sandbox account and back:

1. A user sends a chat message from the web UI to an [Amazon API Gateway](https://aws.amazon.com/api-gateway/) WebSocket API, which is separate from the solution’s REST API. API Gateway authorizes the connection with IAM. When the connection opens, an [AWS Lambda](https://aws.amazon.com/lambda/) function verifies the user’s Amazon Cognito ID token. It records the connection and the user’s identity in an [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) connections table. For more information, see [Authentication mechanism](authentication-mechanism.md).

1. API Gateway puts the message in an [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/) FIFO queue, so the messages from one connection are processed in order, one at a time.

1. The agent worker Lambda function reads the identity and role of the user from the connections table. It checks that Sandbox Spaces is turned on and that the lease is Active. It also checks that the user can use a Sandbox Space on the lease and that the requested model is enabled for the lease. It then reads the permission set that is assigned to the user on the lease and invokes the agent.

1. The agent runs in [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) Runtime. It loads the conversation from AgentCore Memory, and [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) screens each user message and the output of each command.

1. The agent assumes the sandbox agent role in the sandbox account of the lease, with a separate session for each kind of call. It calls the Amazon Bedrock model with an inference-only session. For each AWS CLI command, it uses a new session that the user’s permission set and the solution’s deny statements limit.

1. The agent worker function sends a processing indicator to the web UI through the WebSocket API. When the agent finishes its response, the function forwards the reply to the web UI in parts.
