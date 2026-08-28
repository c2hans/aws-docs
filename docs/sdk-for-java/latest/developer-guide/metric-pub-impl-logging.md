---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/metric-pub-impl-logging.html
---

# Output SDK metrics to the console using the AWS SDK for Java 2.x
<a name="metric-pub-impl-logging"></a>

The `[LoggingMetricPublisher](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/metrics/LoggingMetricPublisher.html)` implementation outputs metrics directly to your application's console or log files. This approach is ideal for development, debugging, and understanding what metrics the SDK collects without requiring external services like Amazon CloudWatch.

Unlike `CloudWatchMetricPublisher` and `EmfMetricLoggingPublisher`, `LoggingMetricPublisher` provides immediate output with no delays or external dependencies. This makes it perfect for local development and troubleshooting scenarios.

## When to use LoggingMetricPublisher
<a name="logging-metric-publisher-when-to-use"></a>

Use `LoggingMetricPublisher` when you need to:
+ Debug metric collection during development
+ Understand what metrics the SDK collects for your operations
+ Troubleshoot performance issues locally
+ Test metric collection without external service dependencies
+ View metrics immediately in your console or log files

**Note**
`LoggingMetricPublisher` is not recommended for production environments where you need persistent metric storage and analysis capabilities.

## Set up console logging for metrics
<a name="logging-metric-publisher-setup"></a>

To see `LoggingMetricPublisher` output, configure your logging framework to display `INFO` level messages. The following `log4j2.xml` configuration ensures metrics appear in your console:

```
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">
    <Appenders>
        <Console name="ConsoleAppender" target="SYSTEM_OUT">
            <PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} - %msg%n"/>
        </Console>
    </Appenders>
    <Loggers>
        <Root level="INFO">
            <AppenderRef ref="ConsoleAppender"/>
        </Root>
        <!-- Ensure LoggingMetricPublisher output appears. -->
        <Logger name="software.amazon.awssdk.metrics.LoggingMetricPublisher" level="INFO" />
    </Loggers>
</Configuration>
```

This configuration directs the SDK to output metrics to your console at the `INFO` level. The `LoggingMetricPublisher` logger configuration ensures that metric output appears even if your root logger uses a higher level like `WARN` or `ERROR`.

## Enable console metrics for a service client
<a name="logging-metric-publisher-basic-usage"></a>

The following example shows how to create a `LoggingMetricPublisher` and use it with an Amazon Simple Storage Service client:

```
import software.amazon.awssdk.metrics.LoggingMetricPublisher;
import software.amazon.awssdk.metrics.MetricPublisher;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;

// Create a LoggingMetricPublisher with default settings.
MetricPublisher metricPublisher = LoggingMetricPublisher.create();

// Add the publisher to your service client.
S3Client s3Client = S3Client.builder()
    .region(Region.US_EAST_1)
    .overrideConfiguration(config -> config.addMetricPublisher(metricPublisher))
    .build();

// Make requests - metrics will appear in your console.
s3Client.listBuckets();

// Clean up resources.
metricPublisher.close();
s3Client.close();
```

## Choose metric output format
<a name="logging-metric-publisher-formatting-options"></a>

`LoggingMetricPublisher` supports two output formats:
+ **PLAIN format (default):** Outputs metrics as compact, single-line entries
+ **PRETTY format:** Outputs metrics in a multi-line, human-readable format

The following example shows how to use the PRETTY format for easier reading during development:

```
import org.slf4j.event.Level;
import software.amazon.awssdk.metrics.LoggingMetricPublisher;

// Create a LoggingMetricPublisher with PRETTY format.
MetricPublisher prettyMetricPublisher = LoggingMetricPublisher.create(
    Level.INFO,
    LoggingMetricPublisher.Format.PRETTY
);

// Use with your service client.
S3Client s3Client = S3Client.builder()
    .region(Region.US_EAST_1)
    .overrideConfiguration(config -> config.addMetricPublisher(prettyMetricPublisher))
    .build();
```

## Complete example
<a name="logging-metric-publisher-complete-example"></a>

The following example demonstrates using `LoggingMetricPublisher` in two ways:
+ At the service client level
+ For a single request

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.event.Level;
import software.amazon.awssdk.metrics.LoggingMetricPublisher;
import software.amazon.awssdk.metrics.MetricPublisher;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.ListBucketsRequest;
import software.amazon.awssdk.services.s3.model.ListBucketsResponse;

/**
 * Demonstrates how to use LoggingMetricPublisher with AWS S3 SDK for Java 2.x.
 * <p>
 * This demo focuses on the S3 listBuckets operation to show how metrics are collected
 * and logged to the console for development and debugging purposes.
 * <p>
 * LoggingMetricPublisher is ideal for:
 * - Development and debugging
 * - Console output for troubleshooting
 * - Understanding what metrics are being collected
 * - Testing metric collection without external dependencies
 */
public class S3LoggingMetricPublisherDemo {

    private static final Logger logger = LoggerFactory.getLogger(S3LoggingMetricPublisherDemo.class);

    public static void main(String[] args) {
        S3LoggingMetricPublisherDemo demo = new S3LoggingMetricPublisherDemo();
        demo.demonstrateUsage();
    }

    /**
     * Demonstrates basic usage with S3Client and metrics enabled at the client level.
     */
    private void demonstrateUsage() {

        // Create a LoggingMetricPublisher with default settings. The SDK logs metrics as text in a single line.
        // The default settings are equivalent to using `LoggingMetricPublisher.Format.PLAIN`.

        MetricPublisher metricPublisher = LoggingMetricPublisher.create();

        // Create an S3 client with metrics enabled.
        try (S3Client s3Client = S3Client.builder()
                .region(Region.US_EAST_1)
                .overrideConfiguration(config -> config.addMetricPublisher(metricPublisher))
                .build()) {

            // Make the listBuckets request - metrics will be logged to console.
            ListBucketsResponse response = s3Client.listBuckets(ListBucketsRequest.builder().build());

            // The next block shows the using a different LoggingMetricPublisher with a `PRETTY` format.
            // Since the metric publisher is added to the request using the `overrideConfiguration`, this formatting
            // applies only to the one request.
            try {
                s3Client.listBuckets(ListBucketsRequest.builder()
                        .overrideConfiguration(config -> config
                                .addMetricPublisher(LoggingMetricPublisher.create(
                                        Level.INFO, LoggingMetricPublisher.Format.PRETTY)))
                        .build());
            } catch (Exception e) {
                logger.info("Request failed with metrics logged: {}", e.getMessage());
            }
            logger.info("Found {} buckets in your AWS account.", response.buckets().size());

        } catch (Exception e) {
            logger.error("Error during S3 operation: {}", e.getMessage());
            logger.info("Note: This is expected if AWS credentials are not configured.");
        }

        // Close the metric publisher to flush any remaining metrics.
        metricPublisher.close();
    }
}
```

The code logs the following to the console:

```
INFO  LoggingMetricPublisher - Metrics published: MetricCollection(name=ApiCall, metrics=[MetricRecord(metric=MarshallingDuration, value=PT0.005409792S), MetricRecord(metric=RetryCount, value=0), MetricRecord(metric=ApiCallSuccessful, value=true), MetricRecord(metric=OperationName, value=ListBuckets), MetricRecord(metric=EndpointResolveDuration, value=PT0.000068S), MetricRecord(metric=ApiCallDuration, value=PT0.163802958S), MetricRecord(metric=CredentialsFetchDuration, value=PT0.145686542S), MetricRecord(metric=ServiceEndpoint, value=https://s3.amazonaws.com), MetricRecord(metric=ServiceId, value=S3)], children=[MetricCollection(name=ApiCallAttempt, metrics=[MetricRecord(metric=TimeToFirstByte, value=PT0.138816S), MetricRecord(metric=SigningDuration, value=PT0.007803459S), MetricRecord(metric=ReadThroughput, value=165153.96002660287), MetricRecord(metric=ServiceCallDuration, value=PT0.138816S), MetricRecord(metric=AwsExtendedRequestId, value=e13Swj3uwn0qP1Oz+m7II5OGq7jf8xxT8H18iDfRBCQmDg+gU4ek91Xrsl8XxRLROlIzCAPQtsQF0DAAWOb8ntuKCzX2AJdj), MetricRecord(metric=HttpStatusCode, value=200), MetricRecord(metric=BackoffDelayDuration, value=PT0S), MetricRecord(metric=TimeToLastByte, value=PT0.148915667S), MetricRecord(metric=AwsRequestId, value=78AW9BM7SWR6YMGB)], children=[MetricCollection(name=HttpClient, metrics=[MetricRecord(metric=MaxConcurrency, value=50), MetricRecord(metric=AvailableConcurrency, value=0), MetricRecord(metric=LeasedConcurrency, value=1), MetricRecord(metric=ConcurrencyAcquireDuration, value=PT0.002623S), MetricRecord(metric=PendingConcurrencyAcquires, value=0), MetricRecord(metric=HttpClientName, value=Apache)], children=[])])])
INFO  LoggingMetricPublisher - [4e6f2bb5] ApiCall
INFO  LoggingMetricPublisher - [4e6f2bb5] ┌──────────────────────────────────────────┐
INFO  LoggingMetricPublisher - [4e6f2bb5] │ MarshallingDuration=PT0.000063S          │
INFO  LoggingMetricPublisher - [4e6f2bb5] │ RetryCount=0                             │
INFO  LoggingMetricPublisher - [4e6f2bb5] │ ApiCallSuccessful=true                   │
INFO  LoggingMetricPublisher - [4e6f2bb5] │ OperationName=ListBuckets                │
INFO  LoggingMetricPublisher - [4e6f2bb5] │ EndpointResolveDuration=PT0.000024375S   │
INFO  LoggingMetricPublisher - [4e6f2bb5] │ ApiCallDuration=PT0.018463083S           │
INFO  LoggingMetricPublisher - [4e6f2bb5] │ CredentialsFetchDuration=PT0.000022334S  │
INFO  LoggingMetricPublisher - [4e6f2bb5] │ ServiceEndpoint=https://s3.amazonaws.com │
INFO  LoggingMetricPublisher - [4e6f2bb5] │ ServiceId=S3                             │
INFO  LoggingMetricPublisher - [4e6f2bb5] └──────────────────────────────────────────┘
INFO  LoggingMetricPublisher - [4e6f2bb5]     ApiCallAttempt
INFO  LoggingMetricPublisher - [4e6f2bb5]     ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
INFO  LoggingMetricPublisher - [4e6f2bb5]     │ TimeToFirstByte=PT0.0165575S                                                                                          │
INFO  LoggingMetricPublisher - [4e6f2bb5]     │ SigningDuration=PT0.000301125S                                                                                        │
INFO  LoggingMetricPublisher - [4e6f2bb5]     │ ReadThroughput=1195591.792850103                                                                                      │
INFO  LoggingMetricPublisher - [4e6f2bb5]     │ ServiceCallDuration=PT0.0165575S                                                                                      │
INFO  LoggingMetricPublisher - [4e6f2bb5]     │ AwsExtendedRequestId=3QI1eenRuokdszWqZBmBMDUmko6FlSmHkM+CUMNMeLor7gJml4D4lv6QXUZ1zWoTgG+tHbr6yo2vHdz4h1P8PDovvtMFRCeB │
INFO  LoggingMetricPublisher - [4e6f2bb5]     │ HttpStatusCode=200                                                                                                    │
INFO  LoggingMetricPublisher - [4e6f2bb5]     │ BackoffDelayDuration=PT0S                                                                                             │
INFO  LoggingMetricPublisher - [4e6f2bb5]     │ TimeToLastByte=PT0.017952625S                                                                                         │
INFO  LoggingMetricPublisher - [4e6f2bb5]     │ AwsRequestId=78AVFAF795AAWAXH                                                                                         │
INFO  LoggingMetricPublisher - [4e6f2bb5]     └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
INFO  LoggingMetricPublisher - [4e6f2bb5]         HttpClient
INFO  LoggingMetricPublisher - [4e6f2bb5]         ┌───────────────────────────────────────┐
INFO  LoggingMetricPublisher - [4e6f2bb5]         │ MaxConcurrency=50                     │
INFO  LoggingMetricPublisher - [4e6f2bb5]         │ AvailableConcurrency=0                │
INFO  LoggingMetricPublisher - [4e6f2bb5]         │ LeasedConcurrency=1                   │
INFO  LoggingMetricPublisher - [4e6f2bb5]         │ ConcurrencyAcquireDuration=PT0.00004S │
INFO  LoggingMetricPublisher - [4e6f2bb5]         │ PendingConcurrencyAcquires=0          │
INFO  LoggingMetricPublisher - [4e6f2bb5]         │ HttpClientName=Apache                 │
INFO  LoggingMetricPublisher - [4e6f2bb5]         └───────────────────────────────────────┘
INFO  S3LoggingMetricPublisherDemo - Found 6 buckets in your AWS account.
```

### Additional artifacts for the example
<a name="logging-metric-publisher-complete-example-artifacts"></a>

Maven `pom.xml` file

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>s3-logging-metric-publisher-demo</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <name>AWS S3 LoggingMetricPublisher Demo</name>
    <description>Demonstrates how to use LoggingMetricPublisher with AWS S3 SDK for Java 2.x</description>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <aws.java.sdk.version>2.31.66</aws.java.sdk.version>
        <log4j.version>2.24.3</log4j.version>
    </properties>

    <dependencyManagement>
        <dependencies>
            <!-- AWS SDK BOM for dependency management -->
            <dependency>
                <groupId>software.amazon.awssdk</groupId>
                <artifactId>bom</artifactId>
                <version>${aws.java.sdk.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>

            <!-- Log4j BOM for logging dependency management -->
            <dependency>
                <groupId>org.apache.logging.log4j</groupId>
                <artifactId>log4j-bom</artifactId>
                <version>${log4j.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <dependencies>
        <!-- AWS S3 SDK for demonstration -->
        <dependency>
            <groupId>software.amazon.awssdk</groupId>
            <artifactId>s3</artifactId>
        </dependency>

        <!-- Log4j2 SLF4J implementation -->
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-slf4j2-impl</artifactId>
        </dependency>

        <!-- Log4j2 Core -->
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-core</artifactId>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.13.0</version>
                <configuration>
                    <source>17</source>
                    <target>17</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

`Log4j2.xml` configuration file

```
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">
    <Appenders>
        <Console name="ConsoleAppender" target="SYSTEM_OUT">
            <PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} - %msg%n"/>
        </Console>
    </Appenders>
    <Loggers>
        <Root level="INFO">
            <AppenderRef ref="ConsoleAppender"/>
        </Root>
        <!-- Ensure LoggingMetricPublisher output appears. -->
        <Logger name="software.amazon.awssdk.metrics.LoggingMetricPublisher" level="INFO"/>
    </Loggers>
</Configuration>
```

The metrics include timing information, service details, operation names, and HTTP status codes that help you understand your application's AWS API usage patterns.

## Next steps
<a name="logging-metric-publisher-next-steps"></a>

After using `LoggingMetricPublisher` for development and debugging, consider these options for production environments:
+ For long-running applications, use [CloudWatchMetricPublisher](metric-pub-impl-cwmp.md) to send metrics to Amazon CloudWatch for analysis and alerting
+ For AWS Lambda functions, use [EmfMetricLoggingPublisher](metric-pub-impl-emf.md) to publish metrics in CloudWatch Embedded Metric Format

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
