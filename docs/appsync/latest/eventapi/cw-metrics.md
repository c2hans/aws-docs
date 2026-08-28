---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/cw-metrics.html
---

# CloudWatch metrics
<a name="cw-metrics"></a>

You can use CloudWatch metrics to monitor and provide alerts about specific events that can result in HTTP status codes or from latency.

## HTTP endpoint metrics
<a name="cw-metrics-HTTP-endpoints"></a>

 `4XXError`
Errors resulting from requests that are not valid due to an incorrect client configuration. For example, these errors can occur when the request includes an incorrect JSON payload, when the service is throttled, or when the authorization settings are misconfigured.
 **Unit**: *Count*. Use the Sum statistic to get the total occurrences of these errors.

 `5XXError`
Errors encountered during the execution of a request. This could also happen if AWS AppSyncc encounters an issue during processing of a request.
 **Unit**: *Count*. Use the Sum statistic to get the total occurrences of these errors.

 `Latency`
The time between when AWS AppSync receives a request from a client and when it returns a response to the client. This doesn’t include the network latency encountered for a response to reach the end devices.
 **Unit**: *Millisecond*. Use the Average statistic to evaluate expected latencies.

`Requests`
The number of requests that all APIs in your account have processed, by Region.
 **Unit**: *Count*. The number of all requests processed in a particular Region.

`TokensConsumed`
Tokens are allocated to `Requests` based on the amount of resources (processing time and memory used) that a `Request` consumes. Usually, each `Request` consumes one token. However, a `Request` that consumes large amounts of resources is allocated additional tokens as needed.
 **Unit**: *Count*. The number of tokens allocated to requests processed in a particular Region.

## Handler metrics
<a name="cw-metrics-handler"></a>

`DroppedEvents`
The count of input events filtered by a OnPublish handler.
 **Unit**: *Count*.

`FailedEvents`
The count of input events that encountered error during processing.
 **Unit**: *Count*.

`SuccessfulEvents`
The count of input events that were processed successfully and submitted for broadcast in the OnPublish handler.
 **Unit**: *Count*.

`PublishedHandlerInvocations`
The number of OnPublish handler invocations.
 **Unit**: *Count*.

## Real-time endpoint metrics
<a name="cw-metrics-real-time-endpoints"></a>

`ConnectRequests`
The number of WebSocket connection requests made to AWS AppSync, including both successful and unsuccessful attempts.
**Unit**: *Count*. Use the Sum statistic to get the total number of connection requests.

`ConnectSuccess`
The number of successful WebSocket connections to AWS AppSync. It is possible to have connections without subscriptions.
**Unit**: *Count*. Use the Sum statistic to get the total occurrences of the successful connections.

`ConnectClientError`
The number of WebSocket connections that were rejected by AWS AppSync because of client-side errors. This could imply that the service is throttled or that the authorization settings are misconfigured.
**Unit**: *Count*. Use the Sum statistic to get the total occurrences of the client-side connection errors.

`ConnectServerError`
The number of errors that originated from AWS AppSync while processing connections. This usually happens when an unexpected server-side issue occurs.
**Unit**: *Count*. Use the Sum statistic to get the total occurrences of the server-side connection errors.

`DisconnectSuccess`
The number of successful WebSocket disconnections from AWS AppSync.
**Unit**: *Count*. Use the Sum statistic to get the total occurrences of the successful disconnections.

`DisconnectClientError`
The number of client errors that originated from AWS AppSync while disconnecting WebSocket connections.
**Unit**: *Count*. Use the Sum statistic to get the total occurrences of the disconnection errors.

`DisconnectServerError`
The number of server errors that originated from AWS AppSync while disconnecting WebSocket connections.
**Unit**: *Count*. Use the Sum statistic to get the total occurrences of the disconnection errors.

`SubscribeSuccess`
The number of subscriptions that were successfully registered to AWS AppSync through WebSocket. It's possible to have connections without subscriptions, but it's not possible to have subscriptions without connections.
**Unit**: *Count*. Use the Sum statistic to get the total occurrences of the successful subscriptions.

`SubscribeClientError`
The number of subscriptions that were rejected by AWS AppSync because of client-side errors. This can occur when a JSON payload is incorrect, the service is throttled, or the authorization settings are misconfigured.
**Unit**: *Count*. Use the Sum statistic to get the total occurrences of the client-side subscription errors.

`SubscribeServerError`
The number of errors that originated from AWS AppSync while processing subscriptions. This usually happens when an unexpected server-side issue occurs.
**Unit**: *Count*. Use the Sum statistic to get the total occurrences of the server-side subscription errors.

`UnsubscribeSuccess`
The number of unsubscribe requests that were successfully processed.
**Unit**: *Count*. Use the Sum statistic to get the total occurrences of the successful unsubscribe requests.

`UnsubscribeClientError`
The number of unsubscribe requests that were rejected by AWS AppSync because of client-side errors.
**Unit**: *Count*. Use the Sum statistic to get the total occurrences of the client-side unsubscribe request errors.

`UnsubscribeServerError`
The number of errors that originated from AWS AppSync while processing unsubscribe requests. This usually happens when an unexpected server-side issue occurs.
**Unit**: *Count*. Use the Sum statistic to get the total occurrences of the server-side unsubscribe request errors.

`BroadcastEventSuccess`
The number of events that were successfully broadcast to subscribers.
**Unit**: *Count*. Use the Sum statistic to get the total of events that were successfully broadcast.

`BroadcastEventClientError`
The number of events that failed to broadcast because of client-side errors.
`Unit`: *Count*. Use the Sum statistic to get the total occurrences of the client-side broadcast events errors

`BroadcastEventServerError`
The number of errors that originated from AWS AppSync while broadcasting events . This usually happens when an unexpected server-side issue occurs.
**Unit**: *Count*. Use the Sum statistic to get the total occurrences of the server-side broadcast errors.

`BroadcastEventSize`
The size of events broadcast.
**Unit**: *Bytes*.

`ActiveConnections`
The number of concurrent WebSocket connections from clients to AWS AppSync in 1 minute.
**Unit**: *Count*. Use the Sum statistic to get the total opened connections.

`ActiveSubscriptions`
The number of concurrent subscriptions from clients in 1 minute.
**Unit**: *Count*. Use the Sum statistic to get the total active subscriptions.

`ConnectionDuration`
The amount of time that the connection stays open.
**Unit**: *Milliseconds*. Use the Average statistic to evaluate connection duration.

`InboundMessages`
The number of inbound metered events. One metered event equals 5 kB of received event.
**Unit**: *Count*.

`OutboundMessages`
The number of metered messages successfully published. One metered message equals 5 kB of delivered data.
**Unit**: *Count*. Use the Sum statistic to get the total number of successfully published metered messages.

`InboundMessageDelayed`
The number of delayed inbound messages. Inbound messages can be delayed when either the inbound message rate quota or outbound message rate quota is breached.
**Unit**: *Count*. Use the Sum statistic to get the total number of inbound messages that were delayed.

`InboundMessageDropped`
The number of delayed inbound messages. Inbound messages can be delayed when either the inbound message rate quota or outbound message rate quota is breached.
**Unit**: *Count*. Use the Sum statistic to get the total number of inbound messages that were dropped.

`SubscribeHandlerInvocations `
The number of Subscribe handlers invoked.
**Unit**: *Count*.

`PublishSuccess `
The number of publish requests that were successfully sent on a WebSocket connection to AWS AppSync.
**Unit**: *Count*. Use the Sum statistic to get the total number of publish requests that were successfully sent.

`PublishClientError `
The number of publish requests that were rejected by AWS AppSync because of client-side errors when sending publish requests on a WebSocket connection. This can occur when a JSON payload is incorrect, the service is throttled, or the authorization settings are misconfigured.
**Unit**: *Count*. Use the Sum statistic to get the total occurrences of these errors.

`PublishServerError `
The number of publish requests that originated from AWS AppSync while processing publish requests on a WebSocket connection. This is usually caused by an unexpected server-side issue.
**Unit**: *Count*. Use the Sum statistic to get the total occurrences of these errors.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
