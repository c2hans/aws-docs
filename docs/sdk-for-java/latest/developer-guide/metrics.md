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

## Metrics limitation of the AWS CRT-based S3 client
<a name="metrics-using-s3-crt-based-client"></a>

The [AWS CRT-based S3 client](crt-based-s3-client.md) does not currently support SDK metrics collection. The builder for an AWS CRT-based S3 client instance, [`S3CrtAsyncClientBuilder`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3CrtAsyncClientBuilder.html), does not provide methods to configure metrics publishers.

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
