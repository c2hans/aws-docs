---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/metrics.html
---

# Publish SDK metrics from the AWS SDK for Java 2.x
<a name="metrics"></a>

With the AWS SDK for Java 2.x you can collect metrics about the service clients and requests in your application, analyze the output in Amazon CloudWatch Logs, and then act on it.

By default, metrics collection is disabled in the SDK. This topic helps you to enable and configure it.

## Getting started with SDK metrics
<a name="getting-started-with-metrics"></a>

To enable metrics collection in your application, choose the appropriate implementation of the `[MetricPublisher](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/metrics/MetricPublisher.html)` interface based on your use case and follow the detailed setup instructions:

**For long-running applications:**
+ Use `[CloudWatchMetricPublisher](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/metrics/publishers/cloudwatch/CloudWatchMetricPublisher.html)`
+ See [Publish SDK metrics from long-running applications](metric-pub-impl-cwmp.md) for complete setup instructions, code examples, and configuration options.

**For AWS Lambda functions:**
+ Use `[EmfMetricLoggingPublisher](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/metrics/publishers/emf/EmfMetricLoggingPublisher.html)`
+ See [Publish SDK metrics for AWS Lambda functions](metric-pub-impl-emf.md) for complete setup instructions, dependencies, and Lambda-specific configuration.

**For troubleshooting and console output:**
+ Use `[LoggingMetricPublisher](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/metrics/LoggingMetricPublisher.html)`
+ See [Output SDK metrics to console for development and debugging](metric-pub-impl-logging.md) for setup instructions, formatting options, and examples for local development and troubleshooting.

## Quick implementation preview
<a name="quick-implementation-preview"></a>

Here's what enabling metrics looks like for each use case:

**Long-running applications:**

```
MetricPublisher metricsPub = CloudWatchMetricPublisher.create();
DynamoDbClient ddb = DynamoDbClient.builder()
    .overrideConfiguration(c -> c.addMetricPublisher(metricsPub))
    .build();
```

**Lambda functions:**

```
EmfMetricLoggingPublisher emfPublisher = EmfMetricLoggingPublisher.builder()
    .namespace("MyApp")
    .build();
DynamoDbClient dynamoDb = DynamoDbClient.builder()
    .overrideConfiguration(c -> c.addMetricPublisher(emfPublisher))
    .build();
```

**Development and debugging:**

```
MetricPublisher loggingPublisher = LoggingMetricPublisher.create();
S3Client s3 = S3Client.builder()
    .overrideConfiguration(c -> c.addMetricPublisher(loggingPublisher))
    .build();
```

## Publish SDK metrics with the CRT-based S3 client
<a name="metrics-using-s3-crt-based-client"></a>

The AWS CRT-based S3 client supports the standard `MetricPublisher` interface. For interface details, see the [AWS SDK for Java API Reference](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/metrics/MetricPublisher.html) on the AWS SDK for Java website. Existing SDK-provided and custom publishers can consume the generated metric collections without CRT-specific handling.

**Note**
Metric publishing requires version `0.48.5` or later of the `aws-crt` dependency. If your application explicitly uses an earlier version, update it before you configure a metric publisher.

To publish metrics for every request made by a client, add a publisher when you create the client:

```
import software.amazon.awssdk.metrics.LoggingMetricPublisher;
import software.amazon.awssdk.metrics.MetricPublisher;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3AsyncClient;

MetricPublisher metricPublisher = LoggingMetricPublisher.create();

S3AsyncClient s3AsyncClient =
    S3AsyncClient.crtBuilder()
                 .region(Region.US_WEST_2)
                 .addMetricPublisher(metricPublisher)
                 .build();
```

To publish metrics for an individual request, add a publisher to the request's `overrideConfiguration`. Request-level publishers replace the client-level publishers for that request:

```
import software.amazon.awssdk.services.s3.model.GetObjectRequest;

GetObjectRequest request =
    GetObjectRequest.builder()
                    .bucket("amzn-s3-demo-bucket")
                    .key("object-key")
                    .overrideConfiguration(c -> c.addMetricPublisher(metricPublisher))
                    .build();
```

The AWS CRT-based S3 client publishes one `ApiCall` metric collection for each underlying HTTP request attempt that CRT performs for an operation. A single logical SDK operation can produce multiple collections when CRT performs multipart transfers or retries. Metric publishing reports these attempts; it does not create additional S3 requests.

The AWS CRT-based S3 client does not currently publish `CredentialsFetchDuration`, `ReadThroughput`, or `WriteThroughput`. It also does not publish `MarshallingDuration`, `EndpointResolveDuration`, `UnmarshallingDuration`, or `ErrorType`.

For definitions of these fields and other available metrics, see the [SDK metrics reference](metrics-list.md).

**Note**
The SDK publishes metrics asynchronously and on a best-effort basis. If a publisher cannot process collections quickly enough, the SDK can discard collections and write details to DEBUG-level logs. This does not affect the result of the S3 operation. The SDK does not close your metric publishers. Keep a publisher open while any client uses it. If you close it while final metric delivery is in progress, the SDK might not publish those collections.

## When are metrics available?
<a name="when-are-metrics-available"></a>

Metrics are generally available within 5-10 minutes after the SDK for Java emits them. For accurate and up-to-date metrics, check Cloudwatch at least 10 minutes after emitting the metrics from your Java applications.

## What information is collected?
<a name="what-information-is-collected"></a>

Metrics collection includes the following:
+ Number of API requests, including whether they succeed or fail
+ Information about the AWS services you call in your API requests, including exceptions returned
+ The duration for various operations such as Marshalling, Signing, and HTTP requests
+ HTTP client metrics, such as the number of open connections, the number of pending requests, and the name of the HTTP client used

**Note**
The metrics available vary by HTTP client.

For a complete list, see [Service client metrics](metrics-list.md).

## How can I use this information?
<a name="how-can-i-use-this-information"></a>

You can use the metrics the SDK collects to monitor the service clients in your application. You can look at overall usage trends, identify anomalies, review service client exceptions returned, or to dig in to understand a particular issue. Using Amazon CloudWatch Logs, you can also create alarms to notify you as soon as your application reaches a condition that you define.

For more information, see [Using Amazon CloudWatch Logs Metrics](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) and [Using Amazon CloudWatch Logs Alarms](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the [ Amazon CloudWatch Logs User Guide](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).
