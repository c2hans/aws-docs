---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/observability-telemetry-metrics.html
---

# Metrics
<a name="observability-telemetry-metrics"></a>

The following table lists the telemetry metrics that the SDK emits. [Configure a telemetry provider](observability.md#observability-conf-telemetry-provider) to make the metrics observable.

**What metrics are emitted?**

| Metric name | Units | Type | Attributes | Description |
| --- | --- | --- | --- | --- |
| smithy.client.call.duration | s | Histogram | rpc.service, rpc.method | Overall call duration (including retries) |
| smithy.client.call.attempts | {attempt} | MonotonicCounter | rpc.service, rpc.method | The number of attempts for an individual operation |
| smithy.client.call.errors | {error} | MonotonicCounter | rpc.service, rpc.method, exception.type | The number of errors for an operation |
| smithy.client.call.attempt\_duration | s | Histogram | rpc.service, rpc.method | The time it takes to connect to the service, send the request, and get back HTTP status code and headers (including time queued waiting to be sent) |
| smithy.client.call.resolve\_endpoint\_duration | s | Histogram | rpc.service, rpc.method | The time it takes to resolve an endpoint (endpoint resolver, not DNS) for the request |
| smithy.client.call.serialization\_duration | s | Histogram | rpc.service, rpc.method | The time it takes to serialize a message body |
| smithy.client.call.deserialization\_duration | s | Histogram | rpc.service, rpc.method | The time it takes to deserialize a message body |
| smithy.client.call.auth.signing\_duration | s | Histogram | rpc.service, rpc.method, auth.scheme\_id | The time it takes to sign a request |
| smithy.client.call.auth.resolve\_identity\_duration | s | Histogram | rpc.service, rpc.method, auth.scheme\_id | The time it takes to acquire an identity (such as AWS credentials or a bearer token) from an Identity Provider |
| smithy.client.http.connections.acquire\_duration | s | Histogram |  | The time it takes a request to acquire a connection |
| smithy.client.http.connections.limit | {connection} | [Async]UpDownCounter |  | The maximum open connections allowed/configured for the HTTP client |
| smithy.client.http.connections.usage | {connection} | [Async]UpDownCounter | state: idle \| acquired | Current state of connections pool |
| smithy.client.http.connections.uptime | s | Histogram |  | The amount of time a connection has been open |
| smithy.client.http.requests.usage | {request} | [Async]UpDownCounter | state: queued \| in-flight | The current state of HTTP client request concurrency |
| smithy.client.http.requests.queued\_duration | s | Histogram |  | The amount of time a request spent queued and waiting to be executed by the HTTP client |
| smithy.client.http.bytes\_sent | By | MonotonicCounter | server.address | The total number of bytes sent by the HTTP client |
| smithy.client.http.bytes\_received | By | MonotonicCounter | server.address | The total number of bytes received by the HTTP client |

Following are the column descriptions:
+ Metric name –The name of the emitted metric.
+ Units –The unit of measure for the metric. Units are given in the [UCUM](https://unitsofmeasure.org/ucum) case sensitive ("c/s") notation.
+ Type –The type of instrument used to capture the metric.
+ Description –A description of what the metric is measuring.
+ Attributes –The set of attributes (dimensions) emitted with the metric.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
