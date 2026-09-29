---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-metrics.html
---

# Changes in SDK metric publishing from version 1 to version 2
<a name="migration-metrics"></a>

This topic details the changes in client-side SDK metric publishing from version 1.x (v1) to version 2.x (v2) of the AWS SDK for Java.

## High-level changes
<a name="migration-metrics-high-level"></a>

### Architecture changes
<a name="migration-metrics-architecture"></a>

In v1, metrics collection is a global, JVM-wide setting that you enable with a system property. The SDK automatically publishes all collected metrics to CloudWatch. There is only one metrics destination.

In v2, metrics collection uses a pluggable [MetricPublisher](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/metrics/MetricPublisher.html) interface that you attach to individual service clients or requests. The SDK provides three implementations:
+ **[CloudWatchMetricPublisher](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/metrics/publishers/cloudwatch/CloudWatchMetricPublisher.html)**: Aggregates and periodically uploads metrics to CloudWatch. Best suited for long-running applications.
+ **[EmfMetricLoggingPublisher](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/metrics/publishers/emf/EmfMetricLoggingPublisher.html)**: Writes metrics as structured log entries in CloudWatch Embedded Metric Format (EMF). Best suited for Lambda functions and other short-lived environments.
+ **[LoggingMetricPublisher](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/metrics/LoggingMetricPublisher.html)**: Outputs metrics to the console through SLF4J logging. Best suited for local development and debugging.

### Scope changes
<a name="migration-metrics-scope"></a>

In v1, enabling metrics publishes data for all AWS service clients in the JVM. In v2, you control metrics at the service client level or at the individual request level.

### Metric type changes
<a name="migration-metrics-types"></a>

v1 collects three categories of metrics: AWS Request Metrics, AWS Service Metrics, and Machine Metrics (heap memory, thread count, open file descriptors).

v2 focuses on SDK request and response metrics, such as API call duration, marshalling duration, signing duration, and retry count. v2 does not collect machine metrics such as heap memory, thread count, and open file descriptors. To continue collecting JVM metrics in CloudWatch, you can use the [CloudWatch Agent with JMX metric collection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-JMX-metrics.html).

## Changes in dependencies
<a name="migration-metrics-deps"></a>

The following table shows the Maven dependency and package name changes between v1 and v2.

| Change | v1 | v2 |
| --- | --- | --- |
| Maven dependencies |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>com.amazonaws</groupId><br />            <artifactId>aws-java-sdk-bom</artifactId><br />            <version>{{1.12.x1}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>com.amazonaws</groupId><br />        <artifactId>aws-java-sdk-cloudwatchmetrics</artifactId><br />    </dependency><br /></dependencies></pre>  |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>software.amazon.awssdk</groupId><br />            <artifactId>bom</artifactId><br />            <version>{{2.x.x2}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>software.amazon.awssdk</groupId><br />        <artifactId>cloudwatch-metric-publisher</artifactId><br />    </dependency><br /></dependencies></pre>  |
| Package name | com.amazonaws.metrics | software.amazon.awssdk.metrics |

1 [Latest version](https://central.sonatype.com/artifact/com.amazonaws/aws-java-sdk-bom). 2 [Latest version](https://central.sonatype.com/artifact/software.amazon.awssdk/bom).

The v2 artifact depends on the use case, as shown in the following table.

| Use case | v2 artifactId | Minimum SDK version |
| --- | --- | --- |
| Long-running applications | cloudwatch-metric-publisher | 2.14.0 |
| Lambda functions | emf-metric-logging-publisher | 2.30.3 |
| Development and debugging | No additional dependency needed (LoggingMetricPublisher is in the SDK core) | 2.14.0 |

## API changes
<a name="migration-metrics-api"></a>

### Enabling metrics
<a name="migration-metrics-enabling"></a>

The following table compares how to enable metrics in v1 and v2 for different use cases.

| Use case | v1 | v2 |
| --- | --- | --- |
| Enable metrics globally | Add a JVM system property:<pre>-Dcom.amazonaws.sdk.enableDefaultMetrics=credentialFile=/path/aws.properties</pre> | Not supported. Attach a MetricPublisher to each service client. |
| Enable metrics on Amazon EC2 without credentials file |  <pre>-Dcom.amazonaws.sdk.enableDefaultMetrics</pre>  | Not applicable. v2 uses its standard credential resolution. |
| Enable metrics for a service client | Not supported. Metrics are global or off. |  <pre>MetricPublisher metricsPub =<br />    CloudWatchMetricPublisher.create();<br /><br />DynamoDbClient ddb = DynamoDbClient.builder()<br />    .overrideConfiguration(c -> c<br />        .addMetricPublisher(metricsPub))<br />    .build();<br /><br />// ... use the client ...<br /><br />metricsPub.close();<br />ddb.close();</pre>  |
| Enable metrics for a single request | Not supported. |  <pre>ddb.listTables(ListTablesRequest.builder()<br />    .overrideConfiguration(c -> c<br />        .addMetricPublisher(metricsPub))<br />    .build());</pre>  |

### Configuring the CloudWatch destination
<a name="migration-metrics-cw-config"></a>

The following table shows how to configure the CloudWatch destination in v1 compared to v2.

| Use case | v1 | v2 |
| --- | --- | --- |
| Set CloudWatch region | System property attribute:<pre>-Dcom.amazonaws.sdk.enableDefaultMetrics=cloudwatchRegion={{us-west-2}}</pre> |  <pre>CloudWatchMetricPublisher.builder()<br />    .cloudWatchClient(<br />        CloudWatchAsyncClient.builder()<br />            .region(Region.US_WEST_2)<br />            .build())<br />    .build();</pre>  |
| Set upload frequency | Not configurable. Uploads approximately once per minute. |  <pre>CloudWatchMetricPublisher.builder()<br />    .uploadFrequency(Duration.ofMinutes(5))<br />    .build();</pre>  |
| Set CloudWatch namespace | Fixed to AWSSDK/Java. | Defaults to `AwsSdk/JavaSdk2`. Configurable via:<pre>CloudWatchMetricPublisher.builder()<br />    .namespace("MyApp/SDK")<br />    .build();</pre> If you have existing CloudWatch dashboards or alarms referencing the v1 namespace `AWSSDK/Java`, set `.namespace("AWSSDK/Java")` to preserve continuity.  |
| Exclude machine metrics | System property attribute:<pre>-Dcom.amazonaws.sdk.enableDefaultMetrics=excludeMachineMetrics</pre> | Not applicable. v2 does not collect machine metrics. |

### Metrics for Lambda functions
<a name="migration-metrics-lambda"></a>

v1 does not have a Lambda-specific metrics solution. In v2, use `EmfMetricLoggingPublisher` which writes metrics as structured log entries in CloudWatch Embedded Metric Format (EMF):

```
// v2 - Lambda-optimized metrics publishing
EmfMetricLoggingPublisher emfPublisher = EmfMetricLoggingPublisher.builder()
        .namespace("MyApp")
        .dimensions(CoreMetric.SERVICE_ID, CoreMetric.OPERATION_NAME)
        .build();

DynamoDbClient dynamoDb = DynamoDbClient.builder()
        .overrideConfiguration(c -> c.addMetricPublisher(emfPublisher))
        .build();
```

**Note**
In Lambda environments, the `logGroupName` is auto-detected from the `AWS_LAMBDA_LOG_GROUP_NAME` environment variable. In non-Lambda environments such as Amazon ECS or Amazon EC2, you must set `logGroupName` explicitly on the builder.

### Metrics for development and debugging
<a name="migration-metrics-debugging"></a>

v1 does not have a console-based metrics output. In v2, use `LoggingMetricPublisher`:

```
// v2 - Console output for debugging
MetricPublisher loggingPublisher = LoggingMetricPublisher.create();

S3Client s3 = S3Client.builder()
        .overrideConfiguration(c -> c.addMetricPublisher(loggingPublisher))
        .build();
```

### Lifecycle management
<a name="migration-metrics-lifecycle"></a>

In v1, metrics collection runs for the lifetime of the JVM once the system property is set. In v2, you must manage the lifecycle of the `MetricPublisher`:

```
// v2 - Close the publisher when no longer needed
MetricPublisher metricsPub = CloudWatchMetricPublisher.create();
DynamoDbClient ddb = DynamoDbClient.builder()
        .overrideConfiguration(c -> c.addMetricPublisher(metricsPub))
        .build();

// ... use the client ...

metricsPub.close(); // Flushes remaining metrics to CloudWatch
ddb.close();
```

**Important**
Call `close` on the `MetricPublisher` instance when it is no longer needed. Failure to do so can result in thread or file descriptor leaks.

### Required permissions
<a name="migration-metrics-permissions"></a>

The following table lists the IAM permissions required for each metrics publisher.

| Permission type | v1 | v2 (CloudWatchMetricPublisher) | v2 (EmfMetricLoggingPublisher) |
| --- | --- | --- | --- |
| IAM permission | cloudwatch:PutMetricData | cloudwatch:PutMetricData | logs:PutLogEvents |

## Limitations
<a name="migration-metrics-limitations"></a>

The [AWS CRT-based S3 client](crt-based-s3-client.md) does not currently support SDK metrics collection in v2.

## Additional resources
<a name="migration-metrics-resources"></a>
+ [v1 metrics documentation](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/generating-sdk-metrics.html)
+ [Publish SDK metrics from the AWS SDK for Java 2.x](metrics.md)
+ [Publish SDK metrics from long-running applications](metric-pub-impl-cwmp.md)
+ [Publish SDK metrics for AWS Lambda functions](metric-pub-impl-emf.md)
+ [Output SDK metrics to the console](metric-pub-impl-logging.md)
+ [Comprehensive Metrics Reference](metrics-list.md)
