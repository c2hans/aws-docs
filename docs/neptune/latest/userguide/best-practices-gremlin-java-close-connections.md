---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin-java-close-connections.html
---

# Close the client to avoid the connections limit
<a name="best-practices-gremlin-java-close-connections"></a>

It is important to close the client when you are finished with it to ensure that the WebSocket connections are closed by the server and all resources associated with the connections are released. This happens automatically if you close the cluster using `Cluster.close( )`, because `client.close( )` is then called internally.

If the client is not closed properly, Neptune terminates all idle WebSocket connections after 20 to 25 minutes. However, if you don't explicitly close WebSocket connections when you're done with them and the number of live connections reaches the [WebSocket concurrent connection limit](limits.md#limits-websockets), additional connections are then refused with an HTTP `429` error code. At that point, you must restart the Neptune instance to close the connections.

The advice to call `cluster.close()` does not apply to Java AWS Lambda functions. See [Managing Gremlin WebSocket connections in AWS Lambda functions](lambda-functions-websocket-connections.md) for details.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
