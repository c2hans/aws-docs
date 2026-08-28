---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/metric-pub-impl-cwmp.html
---

# Publish SDK metrics from long-running applications using the AWS SDK for Java 2.x
<a name="metric-pub-impl-cwmp"></a>

Because the `[CloudWatchMetricPublisher](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/metrics/publishers/cloudwatch/CloudWatchMetricPublisher.html)` implementation aggregates and periodically uploads metrics to Amazon CloudWatch with a delay, its use is best suited for long-running applications.

The default settings of the metrics publisher are meant to minimize memory usage and CloudWatch cost, while still providing a useful amount of insight into the metric data.

## Set-up
<a name="prerequisitesmetrics"></a>

Before you can enable and use metrics by using `CloudWatchMetricPublisher`, complete the following steps.

### Step 1: Add required dependency
<a name="cwmp-set-up-deps"></a>

Configure your project dependencies (for example, in your `pom.xml` or `build.gradle` file) to use version `2.14.0` or later of the AWS SDK for Java.

Include the artifactId `cloudwatch-metric-publisher` with the version number `2.14.0` or later in your project's dependencies.

For example:

```
<project>
  <dependencyManagement>
   <dependencies>
      <dependency>
        <groupId>software.amazon.awssdk</groupId>
        <artifactId>bom</artifactId>
        <version>{{[2.30.11](https://central.sonatype.com/artifact/software.amazon.awssdk/bom)}}</version>  <!-- Navigate the link to see the latest version. -->
        <type>pom</type>
        <scope>import</scope>
      </dependency>
   </dependencies>
  </dependencyManagement>
  <dependencies>
   <dependency>
      <groupId>software.amazon.awssdk</groupId>
      <artifactId>cloudwatch-metric-publisher</artifactId>
   </dependency>
  </dependencies>
</project>
```

### Step 2: Configure required permissions
<a name="cwmp-set-up-perms"></a>

Enable `cloudwatch:PutMetricData` permissions for the IAM identity used by the metrics publisher to allow the SDK for Java to write metrics.

## Enable metrics for a specific request
<a name="enable-metrics-for-a-specific-request"></a>

The following class shows how to enable the CloudWatch metrics publisher for a request to Amazon DynamoDB. It uses the default metrics publisher configuration.

```
import software.amazon.awssdk.metrics.MetricPublisher;
import software.amazon.awssdk.metrics.publishers.cloudwatch.CloudWatchMetricPublisher;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.ListTablesRequest;

public class DefaultConfigForRequest {
    // Use one MetricPublisher for your application. It can be used with requests or service clients.
    static MetricPublisher metricsPub = CloudWatchMetricPublisher.create();

    public static void main(String[] args) {
        DynamoDbClient ddb = DynamoDbClient.create();
        // Publish metrics the for ListTables operation.
        ddb.listTables(ListTablesRequest.builder()
            .overrideConfiguration(c -> c.addMetricPublisher(metricsPub))
            .build());

        // Perform more work in your application.

        // A MetricsPublisher has its own lifecycle independent of any service client or request that uses it.
        // If you no longer need the publisher, close it to free up resources.
        metricsPub.close();  // All metrics stored in memory are flushed to CloudWatch.

        // Perform more work with the DynamoDbClient instance without publishing metrics.
        // Close the service client when you no longer need it.
        ddb.close();
    }
}
```

**Important**
Make sure your application calls `close` on the `[MetricPublisher](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/metrics/MetricPublisher.html)` instance when the service client is no longer in use. Failure to do so results in possible thread or file descriptor leaks.

## Enable summary metrics for a specific service client
<a name="enable-metrics-for-a-specific-service-client"></a>

The following code snippet shows how to enable a CloudWatch metrics publisher with default settings for a service client.

```
MetricPublisher metricsPub = CloudWatchMetricPublisher.create();

DynamoDbClient ddb = DynamoDbClient.builder()
          .overrideConfiguration(c -> c.addMetricPublisher(metricsPub))
          .build();
```

## Customize a CloudWatch metrics publisher
<a name="customize-metrics-publisher"></a>

The following class demonstrates how to set up a custom configuration for the metrics publisher for a specific service client. The customizations include loading a specific profile, specifying a AWS Region where the metrics publisher sends requests, and customizing how often the publisher sends metrics to CloudWatch.

```
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.core.metrics.CoreMetric;
import software.amazon.awssdk.metrics.MetricPublisher;
import software.amazon.awssdk.metrics.publishers.cloudwatch.CloudWatchMetricPublisher;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.cloudwatch.CloudWatchAsyncClient;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;

import java.time.Duration;

public class CustomConfigForDDBClient {
    // Use one MetricPublisher for your application. It can be used with requests or service clients.
    static MetricPublisher metricsPub = CloudWatchMetricPublisher.builder()
        .cloudWatchClient(CloudWatchAsyncClient.builder()
            .region(Region.US_WEST_2)
            .credentialsProvider(ProfileCredentialsProvider.create("cloudwatch"))
            .build())
        .uploadFrequency(Duration.ofMinutes(5))
        .maximumCallsPerUpload(100)
        .namespace("ExampleSDKV2Metrics")
        .detailedMetrics(CoreMetric.API_CALL_DURATION)
        .build();

    public static void main(String[] args) {
        DynamoDbClient ddb = DynamoDbClient.builder()
            .overrideConfiguration(c -> c.addMetricPublisher(metricsPub))
            .build();
        // Publish metrics for DynamoDB operations.
        ddb.listTables();
        ddb.describeEndpoints();
        ddb.describeLimits();
        // Perform more work in your application.

        // A MetricsPublisher has its own lifecycle independent of any service client or request that uses it.
        // If you no longer need the publisher, close it to free up resources.
        metricsPub.close();  // All metrics stored in memory are flushed to CloudWatch.

        // Perform more work with the DynamoDbClient instance without publishing metrics.
        // Close the service client when you no longer need it.
        ddb.close();
    }
}
```

The customizations shown in the previous snippet have the following effects.
+ The `cloudWatchClient` method lets you customize the CloudWatch client used to send metrics. In this example, we use a different region from the default of *us-east-1* where the client sends metrics. We also use a different named profile, *cloudwatch*, whose credentials will be used to authenticate requests to CloudWatch. Those credentials must have permissions to `cloudwatch:PutMetricData`.
+ The `uploadFrequency` method allows you to specify how frequently the metrics publisher uploads metrics to CloudWatch. The default is once a minute.
+ The `maximumCallsPerUpload` method limits the number of calls made per upload. The default is unlimited.
+ By default, the SDK for Java 2.x publishes metrics under the namespace `AwsSdk/JavaSdk2`. You can use the `namespace` method to specify a different value.
+ By default, the SDK publishes summary metrics. Summary metrics consist of average, minimum, maximum, sum, and sample count. By specifying one or more SDK metrics in the `detailedMetrics` method, the SDK publishes additional data for each metric. This additional data enables percentile statistics like p90 and p99 that you can query in CloudWatch. The detailed metrics are especially useful for latency metrics like `APICallDuration`, which measures the end-to-end latency for SDK client requests. You can use fields of the `[CoreMetric](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/metrics/CoreMetric.html)` class to specify other common SDK metrics.

**Next steps:** If you're also working with Lambda functions, see [Publish SDK metrics for AWS Lambda functions](metric-pub-impl-emf.md) for EMF-based metrics publishing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
