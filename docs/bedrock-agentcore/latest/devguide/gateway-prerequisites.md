---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-prerequisites.html
---

# Prerequisites for using the Amazon Bedrock AgentCore gateway service
<a name="gateway-prerequisites"></a>

To interact with the AgentCore Gateway service, you’ll need to complete the following prerequisites:

 **Prerequisites for using the AgentCore Gateway service**

1. Install and set up the tools that you wish to use and ensure that you have the necessary permissions to use AgentCore Gateway methods and access AgentCore Gateway resources.

1. Set up and retrieve your AWS credentials. To access your AWS credentials and configure them, follow the steps at [Using IAM Identity Center to authenticate AWS SDK and Tools](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) . You need AWS credentials for the following tools:

1. Ensure you have the necessary permissions to perform AgentCore Gateway-related API operations and access AgentCore Gateway resources.

1. Set up inbound authorization to authenticate requests made to your gateway.

1. Set up at least one target for your gateway.

1. Set up outbound authorization to authenticate access to your gateway targets.

The following topics describe where you can find information about setting up the tools that you can use to interact with the AgentCore Gateway service.

**Topics**
+ [Set up dependencies and credentials to create, maintain, and use gateway resources](gateway-setup-tools-credentials.md)
+ [Set up permissions for AgentCore Gateway](gateway-prerequisites-permissions.md)
+ [Set up inbound authorization for your gateway](gateway-inbound-auth.md)
+ [Set up outbound authorization for your gateway](gateway-outbound-auth.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
