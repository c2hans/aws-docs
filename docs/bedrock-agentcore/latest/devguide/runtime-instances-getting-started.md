---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-instances-getting-started.html
---

# Get started with Instances
<a name="runtime-instances-getting-started"></a>

These tutorials walk through hosting an agent on the **Instances** compute type. You first create a [capacity provider](runtime-instances-how-it-works.md#runtime-instances-capacity-provider) that defines the EC2 infrastructure, then create an agent runtime that uses it, and finally invoke the agent. Choose the path that matches how you work: the AWS Management Console, or the AWS CLI and SDKs.

## Prerequisites
<a name="runtime-instances-prerequisites"></a>
+ An AWS account with access to Amazon Bedrock AgentCore.
+ Permissions to create AgentCore capacity providers and agent runtimes, and to create or pass the required IAM roles. For more information, see [IAM roles](runtime-instances-how-it-works.md#runtime-instances-permissions).
+ An agent or tool artifact — either a container image in Amazon ECR, or an agent package in an Amazon S3 bucket.

**Topics**
