---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/appsync-api-gateway.html
---

# AWS AppSync Events and API Gateway
<a name="appsync-api-gateway"></a>

AWS AppSync Events and Amazon API Gateway both provide a managed WebSocket experience for your microservices.

[AWS AppSync Events](https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-welcome.html) offers a simplified experience for real-time messaging by using a WebSocket. AWS AppSync Events supports unicast and multicast messaging and a flexible grouping of channels into namespaces, with support for wildcards. Microservices can communicate with one another in a variety of ways by using AWS AppSync Events. For example, a service that receives real-time data can transform and publish the data to the appropriate channel, where subscribers will receive it in real time.

[API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) also supports WebSocket APIs. You can define integrations with AWS services, such as AWS Lambda and Amazon DynamoDB, and configure route selection expressions that are mapped to those integrations. API Gateway has special routes that you can use to authorize and manage your WebSocket connections. Depending on your needs, you can store WebSocket connection information in a data store such as DynamoDB. Using this information, messages can be published to specific WebSocket connections through a REST API, given a specific connection ID.

## Guidance
<a name="appsync-api-gateway-guidance"></a>

Use AWS AppSync Events when:
+ You have multiple messaging channels that are grouped into namespaces and want to publish and subscribe to groups of channels by using wildcards.
+ Your communications are primarily between different systems instead of being between AWS services.

Use API Gateway WebSocket APIs when:
+ You want to enable clients to have real-time persistent connections to AWS service integrations.
+ You want to manage WebSocket connections yourself. For example, you might want to allow other systems to send messages to a particular client after looking up their connection ID.
+ You want to use API Gateway features such as stage deployments or proxy integrations, or you want to configure your own subprotocols.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
