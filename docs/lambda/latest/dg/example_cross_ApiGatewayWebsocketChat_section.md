---
source_url: https://docs.aws.amazon.com/lambda/latest/dg/example_cross_ApiGatewayWebsocketChat_section.html
---

# Create a websocket chat application with API Gateway
<a name="example_cross_ApiGatewayWebsocketChat_section"></a>

The following code example shows how to create a chat application that is served by a websocket API built on Amazon API Gateway.

------
#### [ Python ]

**SDK for Python (Boto3)**
 Shows how to use the AWS SDK for Python (Boto3) with Amazon API Gateway V2 to create a websocket API that integrates with AWS Lambda and Amazon DynamoDB.
+ Create a websocket API served by API Gateway.
+ Define a Lambda handler that stores connections in DynamoDB and posts messages to other chat participants.
+ Connect to the websocket chat application and send messages with the Websockets package.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/cross_service/apigateway_websocket_chat).

**Services used in this example**
+ API Gateway
+ DynamoDB
+ Lambda

------

For a complete list of AWS SDK developer guides and code examples, see [Using Lambda with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
