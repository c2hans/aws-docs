---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api.html
---

# Invoke WebSocket APIs
<a name="apigateway-how-to-call-websocket-api"></a>

After you've deployed your WebSocket API, client applications can connect to it and send messages to it—and your backend service can send messages to connected client applications:
+ You can use `wscat` to connect to your WebSocket API and send messages to it to simulate client behavior. See [Use `wscat` to connect to a WebSocket API and send messages to it](apigateway-how-to-call-websocket-api-wscat.md).
+ You can use the @connections API from your backend service to send a callback message to a connected client, get connection information, or disconnect the client. See [Use `@connections` commands in your backend service](apigateway-how-to-call-websocket-api-connections.md).
+ A client application can use its own WebSocket library to invoke your WebSocket API.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
