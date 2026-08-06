---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/metrics-list.html
---

# AWS SDK for Java 2.x: Comprehensive Metrics Reference
<a name="metrics-list"></a>

With the AWS SDK for Java 2.x, you can collect metrics from the service clients in your application and then publish (output) those metrics to [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

These tables list the metrics that you can collect and any HTTP client usage requirement.

For more information about enabling and configuring metrics for the SDK, see [Enabling SDK metrics](metrics.md).

## Metrics collected with each request
<a name="metrics-perrequest"></a>

| Metric name | Description | Type |
| --- | --- | --- |
| ApiCallDuration | The duration of the API call. This includes all call attempts made. | Duration\* |
| ApiCallSuccessful | True if the API call succeeded, false otherwise. | Boolean |
| CredentialsFetchDuration | The duration of time to fetch signing credentials for the API call. | Duration\* |
| EndpointResolveDuration | The duration of time to resolve the endpoint used for the API call. | Duration\* |
| MarshallingDuration | The duration of time to marshall the SDK request to an HTTP request. | Duration\* |
| OperationName | The name of the service operation being invoked. | String |
| RetryCount | The number of retries that the SDK performed in the execution of the request. 0 implies that the request worked the first time and that no retries were attempted.<br />For more information about configuring retry behavior, see [Retry strategies](retry-strategy.md#retry-strategies). | Integer |
| ServiceId | The unique ID for the service. | String |
| ServiceEndpoint | The endpoint for the service. | URI |
| TokenFetchDuration | The duration of time to fetch signing credentials for the API call. | Duration\* |

\*[java.time.Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html).

## Metrics collected for each request attempt
<a name="metrics-perattempt"></a>

Each API call might require multiple attempts before a response is received. These metrics are collected for each attempt.

### Core metrics
<a name="metrics-perattempt-core"></a>

| Metric name | Description | Type |
| --- | --- | --- |
| AwsExtendedRequestId | The extended request ID of the service request. | String |
| AwsRequestId | The request ID of the service request. | String |
| BackoffDelayDuration | The duration of time that the SDK has waited before this API call attempt. The value is based on the `[https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/retries/api/BackoffStrategy.html](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/retries/api/BackoffStrategy.html)` set on the client. See the [Retry strategies](retry-strategy.md#retry-strategies) section in this guide for more information. | Duration\* |
| ErrorType | The type of error that occurred for a call attempt.<br />The following are possible values:+ `Throttling`: The service responded with a throttling error.<br />+ `ServerError`: The service responded with an error other than throttling.<br />+ `ConfiguredTimeout`: A client timeout occurred, either at the API call level, or API call attempt level.<br />+ `IO`: An I/O error occurred.<br />+ `Other`: Catch-all for other errors that don't fall into one of categories list above. | String |
| ReadThroughput | The read throughput of the client, defined as `NumberOfResponseBytesRead / (TTLB - TTFB)`. This value is in bytes per second.<br />Note that this metric only measures the bytes read from within the `ResponseTransformer` or `AsyncResponseTransformer`. Data that is read outside the transformer—for example when the response stream is returned as the result of the transformer—is not included in the calculation. | Double |
| WriteThroughput | The write throughput of the client, defined as `RequestBytesWritten / (LastByteWrittenTime - FirstByteWrittenTime)`. This value is in bytes per second.<br />This metric measures the rate at which the SDK provides the request body to the HTTP client. It excludes connection setup, TLS handshake time, and server processing time. This metric is only reported for requests that have a streaming body such as S3 PutObject.<br />Note that this metric does not account for buffering in the HTTP client layer. The actual network transmission rate may be lower if the HTTP client buffers data before sending. This metric represents an upper bound of the network throughput. | Double |
| ServiceCallDuration | The duration of time to connect to the service (or acquire a connection from the connection pool), send the serialized request and receive the initial response (for example HTTP status code and headers). This DOES NOT include the time to read the entire response from the service. | Duration\* |
| SigningDuration | The duration of time to sign the HTTP request. | Duration\* |
| TimeToFirstByte | The duration of time from sending the HTTP request (including acquiring a connection) to the service, and receiving the first byte of the headers in the response. | Duration\* |
| TimeToLastByte | The duration of time from sending the HTTP request (including acquiring a connection) to the service, and receiving the last byte of the response.<br />Note that for APIs that return streaming responses, this metric spans the time until the `ResponseTransformer` or `AsyncResponseTransformer` completes. | Duration\* |
| UnmarshallingDuration | The duration of time to unmarshall the HTTP response to an SDK response.<br />Note: For streaming operations, this does not include the time to read the response payload. | Duration\* |

\*[java.time.Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html).

### HTTP Metrics
<a name="metrics-perattempt-http"></a>

| Metric name | Description | Type | HTTP client required\* |
| --- | --- | --- | --- |
| AvailableConcurrency | The number of additional concurrent requests that the HTTP client supports without establishing new connections to the target server.<br />For HTTP/1 operations, this equals the number of idle TCP connections established with the service. For HTTP/2 operations, this equals the number of idle streams.<br />Note: This value varies by HTTP client implementation:+  Apache client: Value applies to the entire HTTP client <br />+  Netty client: Value applies per endpoint <br />+  AWS CRT-based client: Value applies per endpoint <br />The value is scoped to an individual HTTP client instance and excludes concurrency from other HTTP clients in the same JVM. | Integer | Apache, Netty, CRT |
| ConcurrencyAcquireDuration | The duration of time to acquire a channel from the connection pool.<br />For HTTP/1 operations, a channel equals a TCP connection. For HTTP/2 operations, a channel equals an HTTP/2 stream channel.<br />Acquiring a new channel may include time for:1.  Awaiting a concurrency permit, as restricted by the client's max concurrency configuration. <br />2.  Establishing a new connection, if no existing connection is available in the pool. <br />3.  Performing the TLS handshake and negotiation, if TLS is enabled.  | Duration\* | Apache, Netty, CRT |
| HttpClientName | The name of the HTTP used for the request. | String | Apache, Netty, CRT |
| HttpStatusCode | The status code of the HTTP response. | Integer | Any |
| LeasedConcurrency | The number of requests that the HTTP client currently executes. <br />For HTTP/1 operations, this equals the number of active TCP connections with the service (excluding idle connections). For HTTP/2 operations, this equals the number of active HTTP streams with the service (excluding idle stream capacity). <br />Note: This value varies by HTTP client implementation:+  Apache client: Value applies to the entire HTTP client <br />+  Netty client: Value applies per endpoint <br />+  AWS CRT-based client: Value applies per endpoint <br />The value is scoped to an individual HTTP client instance and excludes concurrency from other HTTP clients in the same JVM. | Integer | Apache, Netty, CRT |
| LocalStreamWindowSize | The local HTTP/2 window size in bytes for the stream that executes this request. | Integer | Netty |
| MaxConcurrency | The maximum number of concurrent requests that the HTTP client supports.<br />For HTTP/1 operations, this equals the maximum number of TCP connections that the HTTP client can pool. For HTTP/2 operations, this equals the maximum number of streams that the HTTP client can pool.<br />Note: This value varies by HTTP client implementation:+  Apache client: Value applies to the entire HTTP client <br />+  Netty client: Value applies per endpoint <br />+  AWS CRT-based client: Value applies per endpoint <br />The value is scoped to an individual HTTP client instance and excludes concurrency from other HTTP clients in the same JVM. | Integer | Apache, Netty, CRT |
| PendingConcurrencyAcquires | The number of requests that wait for concurrency from the HTTP client.<br />For HTTP/1 operations, this equals the number of requests waiting for a TCP connection to establish or return from the connection pool. For HTTP/2 operations, this equals the number of requests waiting for a new stream (and possibly a new HTTP/2 connection) from the connection pool.<br />Note: This value varies by HTTP client implementation:+  Apache client: Value applies to the entire HTTP client <br />+  Netty client: Value applies per endpoint <br />+  AWS CRT-based client: Value applies per endpoint <br />The value is scoped to an individual HTTP client instance and excludes concurrency from other HTTP clients in the same JVM. | Integer | Apache, Netty, CRT |
| RemoteStreamWindowSize | The remote HTTP/2 window size in bytes for the stream that executes this request. | Integer | Netty |

\*[java.time.Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html).

The terms used in the column mean:
+ Apache: the Apache-based HTTP client (`[ApacheHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/apache/ApacheHttpClient.html)`)
+ Netty: the Netty-based HTTP client (`[NettyNioAsyncHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/nio/netty/NettyNioAsyncHttpClient.html)`)
+ CRT: the AWS CRT-based HTTP client (`[AwsCrtAsyncHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/crt/AwsCrtAsyncHttpClient.html)`)
+ Any: the collection of metric data does not depend on the HTTP client; this includes the URLConnection-based HTTP client (`[UrlConnectionHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/urlconnection/UrlConnectionHttpClient.html)`)
