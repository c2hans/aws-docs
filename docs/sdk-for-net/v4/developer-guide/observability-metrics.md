---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/observability-metrics.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Metrics
<a name="observability-metrics"></a>

The following table lists the telemetry metrics that the SDK emits. [Configure a telemetry provider](observability.md#observability-conf-telemetry-provider) to make the metrics observable.

**What metrics are emitted?**

| Metric name | Units | Type | Attributes | Description |
| --- | --- | --- | --- | --- |
| client.call.duration | s | Histogram | rpc.service, rpc.method | Overall call duration (including retries and time to send or receive request and response body) |
| client.uptime | s | Histogram | rpc.service | The amount of time since a client was created |
| client.call.attempts | {attempt} | MonotonicCounter | rpc.service, rpc.method | The number of attempts for an individual operation |
| client.call.errors | {error} | MonotonicCounter | rpc.service, rpc.method, exception.type | The number of errors for an operation |
| client.call.attempt\_duration | s | Histogram | rpc.service, rpc.method | The time it takes to connect to the service, send the request, and get back HTTP status code and headers (including time queued waiting to be sent) |
| client.call.resolve\_endpoint\_duration | s | Histogram | rpc.service, rpc.method | The time it takes to resolve an endpoint (endpoint resolver, not DNS) for the request |
| client.call.serialization\_duration | s | Histogram | rpc.service, rpc.method | The time it takes to serialize a message body |
| client.call.deserialization\_duration | s | Histogram | rpc.service, rpc.method | The time it takes to deserialize a message body |
| client.call.auth.signing\_duration | s | Histogram | rpc.service, rpc.method | The time it takes to sign a request |
| client.call.auth.resolve\_identity\_duration | s | Histogram | rpc.service, rpc.method | The time it takes to acquire an identity (such as AWS credentials or a bearer token) from an Identity Provider |
| client.http.bytes\_sent | By | MonotonicCounter | server.address | The total number of bytes sent by the HTTP client |
| client.http.bytes\_received | By | MonotonicCounter | server.address | The total number of bytes received by the HTTP client |

Following are the column descriptions:
+ **Metric name**–The name of the emitted metric.
+ **Units**–The unit of measure for the metric. Units are given in the [UCUM](https://unitsofmeasure.org/ucum) case sensitive ("c/s") notation.
+ **Type**–The type of instrument used to capture the metric.
+ **Attributes**–The set of attributes (dimensions) emitted with the metric.
+ **Description**–A description of what the metric is measuring.
