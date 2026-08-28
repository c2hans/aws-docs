---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/metric-pub-impl-emf.html
---

# Publish SDK metrics for AWS Lambda functions using the AWS SDK for Java 2.x
<a name="metric-pub-impl-emf"></a>

Because Lambda functions typically execute for milliseconds to minutes, any delay in sending the metrics, which happens with the `CloudWatchMetricPublisher`, risks the loss of data.

`[EmfMetricLoggingPublisher](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/metrics/publishers/emf/EmfMetricLoggingPublisher.html)` provides a more suitable approach by immediately writing metrics as structured log entries in [CloudWatch Embedded Metric Format (EMF)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html). `EmfMetricLoggingPublisher` works in execution environments that have built-in integration with Amazon CloudWatch Logs such as AWS Lambda and Amazon Elastic Container Service.

## Set-up
<a name="metric-pub-impl-emf-set-up"></a>

Before you can enable and use metrics by using `EmfMetricLoggingPublisher`, complete the following steps.

### Step 1: Add required dependency
<a name="metric-pub-impl-emf-set-up-deps"></a>

Configure your project dependencies (for example, in your `pom.xml` or `build.gradle` file) to use version `2.30.3` or later of the AWS SDK for Java.

Include the artifactId `emf-metric-logging-publisher` with the version number `2.30.3` or later in your project's dependencies.

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
      <artifactId>emf-metric-logging-publisher</artifactId>
   </dependency>
  </dependencies>
</project>
```

### Step 2: Configure required permissions
<a name="metric-pub-impl-emf-set-up-perm"></a>

Enable `logs:PutLogEvents` permissions for the IAM identity used by the metrics publisher to allow the SDK for Java to write EMF-formatted logs.

### Step 3: Setup logging
<a name="metric-pub-impl-emf-set-up-logger"></a>

To ensure proper metric collection, configure your logging to output to the console at the `INFO` level or lower (such as `DEBUG`). In your `log4j2.xml` file:

```
<Loggers>
  <Root level="WARN">
   <AppenderRef ref="ConsoleAppender"/>
  </Root>
  <Logger name="software.amazon.awssdk.metrics.publishers.emf.EmfMetricLoggingPublisher" level="INFO" />
</Loggers>
```

See the [logging topic](logging-slf4j.md) in this guide for more information on how to set up a `log4j2.xml` file.

## Configure and use `EmfMetricLoggingPublisher`
<a name="metric-pub-impl-emf-use"></a>

The following Lambda function class first creates and configures an `EmfMetricLoggingPublisher` instance and then uses it with a Amazon DynamoDB service client:

```
public class GameIdHandler implements RequestHandler<Map<String, String>, String> {
    private final EmfMetricLoggingPublisher emfPublisher;
    private final DynamoDbClient dynamoDb;

    public GameIdHandler() {
        // Build the publisher.
        this.emfPublisher = EmfMetricLoggingPublisher.builder()
                .namespace("namespace")
                .dimensions(CoreMetric.SERVICE_ID,
                        CoreMetric.OPERATION_NAME)
                .build();
        // Add the publisher to the client.
        this.dynamoDb = DynamoDbClient.builder()
                .overrideConfiguration(c -> c.addMetricPublisher(emfPublisher))
                .region(Region.of(System.getenv("AWS_REGION")))
                .build();
    }

    @Override
    public String handleRequest(Map<String, String> event, Context context) {
        Map<String, AttributeValue> gameItem = new HashMap<>();

        gameItem.put("gameId", AttributeValue.builder().s(event.get("id")).build());

        PutItemRequest putItemRequest = PutItemRequest.builder()
                .tableName("games")
                .item(gameItem)
                .build();

        dynamoDb.putItem(putItemRequest);

        return "Request handled";
    }
}
```

When the DynamoDB client executes the `putItem` method, it automatically publishes metrics to a CloudWatch log stream in EMF format.

### Example of an EMF log event
<a name="emf-logged-output"></a>

For example, if you send the following event to the GameHandler Lambda function with logging configured as shown previously:

```
{
  "id": "23456"
}
```

After the function processes the event, you find two log events that look similar to the following example. The JSON object in the second event contains the Java SDK metric data for the `PutItem` operation to DynamoDB.

When CloudWatch receives a log event in EMF format, it automatically parses the structured JSON to extract metric data. CloudWatch then creates corresponding metrics while storing the original log entry in CloudWatch Logs.

```
2025-07-11 15:58:30 [main] INFO  org.example.GameIdHandler:39 - Received map: {id=23456}

2025-07-11 15:58:34 [main] INFO  software.amazon.awssdk.metrics.publishers.emf.EmfMetricLoggingPublisher:43 -
{
    "_aws": {
        "Timestamp": 1752249513975,
        "LogGroupName": "/aws/lambda/GameId",
        "CloudWatchMetrics": [
            {
                "Namespace": "namespace",
                "Dimensions": [
                    [
                        "OperationName",
                        "ServiceId"
                    ]
                ],
                "Metrics": [
                    {
                        "Name": "AvailableConcurrency"
                    },
                    {
                        "Name": "PendingConcurrencyAcquires"
                    },
                    {
                        "Name": "ServiceCallDuration",
                        "Unit": "Milliseconds"
                    },
                    {
                        "Name": "EndpointResolveDuration",
                        "Unit": "Milliseconds"
                    },
                    {
                        "Name": "MaxConcurrency"
                    },
                    {
                        "Name": "BackoffDelayDuration",
                        "Unit": "Milliseconds"
                    },
                    {
                        "Name": "MarshallingDuration",
                        "Unit": "Milliseconds"
                    },
                    {
                        "Name": "LeasedConcurrency"
                    },
                    {
                        "Name": "SigningDuration",
                        "Unit": "Milliseconds"
                    },
                    {
                        "Name": "ConcurrencyAcquireDuration",
                        "Unit": "Milliseconds"
                    },
                    {
                        "Name": "ApiCallSuccessful"
                    },
                    {
                        "Name": "RetryCount"
                    },
                    {
                        "Name": "UnmarshallingDuration",
                        "Unit": "Milliseconds"
                    },
                    {
                        "Name": "ApiCallDuration",
                        "Unit": "Milliseconds"
                    },
                    {
                        "Name": "CredentialsFetchDuration",
                        "Unit": "Milliseconds"
                    }
                ]
            }
        ]
    },
    "AvailableConcurrency": 0,
    "PendingConcurrencyAcquires": 0,
    "OperationName": "PutItem",
    "ServiceCallDuration": 1339,
    "EndpointResolveDuration": 81,
    "MaxConcurrency": 50,
    "BackoffDelayDuration": 0,
    "ServiceId": "DynamoDB",
    "MarshallingDuration": 181,
    "LeasedConcurrency": 1,
    "SigningDuration": 184,
    "ConcurrencyAcquireDuration": 83,
    "ApiCallSuccessful": 1,
    "RetryCount": 0,
    "UnmarshallingDuration": 85,
    "ApiCallDuration": 1880,
    "CredentialsFetchDuration": 138
}
```

The [API documentation](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/metrics/publishers/emf/EmfMetricLoggingPublisher.Builder.html) for `EmfMetricLoggingPublisher.Builder` shows the configuration options that you can use.

You can also enable EMF metric logging for a single request as [shown for the CloudWatchMetricPublisher](metric-pub-impl-cwmp.md#enable-metrics-for-a-specific-request).

**Next steps:** For long-running applications, see [Publish SDK metrics from long-running applications](metric-pub-impl-cwmp.md) for CloudWatch-based metrics publishing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
