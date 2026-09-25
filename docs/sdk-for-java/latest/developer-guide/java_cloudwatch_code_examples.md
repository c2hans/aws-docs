---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_cloudwatch_code_examples.html
---

# CloudWatch examples using SDK for Java 2.x
<a name="java_cloudwatch_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Java 2.x with CloudWatch.

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Get started](#get_started)
+ [Basics](#basics)
+ [Actions](#actions)
+ [Scenarios](#scenarios)

## Get started
<a name="get_started"></a>

### Hello CloudWatch
<a name="cloudwatch_Hello_java_topic"></a>

The following code example shows how to get started using CloudWatch.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.cloudwatch.CloudWatchClient;
import software.amazon.awssdk.services.cloudwatch.model.CloudWatchException;
import software.amazon.awssdk.services.cloudwatch.model.ListMetricsRequest;
import software.amazon.awssdk.services.cloudwatch.paginators.ListMetricsIterable;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class HelloService {
    public static void main(String[] args) {
        final String usage = """

                Usage:
                  <namespace>\s

                Where:
                  namespace - The namespace to filter against (for example, AWS/EC2).\s
                """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String namespace = args[0];
        Region region = Region.US_EAST_1;
        CloudWatchClient cw = CloudWatchClient.builder()
                .region(region)
                .build();

        listMets(cw, namespace);
        cw.close();
    }

    public static void listMets(CloudWatchClient cw, String namespace) {
        try {
            ListMetricsRequest request = ListMetricsRequest.builder()
                    .namespace(namespace)
                    .build();

            ListMetricsIterable listRes = cw.listMetricsPaginator(request);
            listRes.stream()
                    .flatMap(r -> r.metrics().stream())
                    .forEach(metrics -> System.out.println(" Retrieved metric is: " + metrics.metricName()));

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}
```
+  For API details, see [ListMetrics](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListMetrics) in *AWS SDK for Java 2.x API Reference*.

## Basics
<a name="basics"></a>

### Learn the basics
<a name="cloudwatch_GetStartedMetricsDashboardsAlarms_java_topic"></a>

The following code example shows how to:
+ List CloudWatch namespaces and metrics.
+ Start OpenTelemetry enrichment so CloudWatch correlates incoming OTLP metrics with the resources that produced them.
+ See how OTLP metrics reach the CloudWatch metrics endpoint. Metric ingestion over OTLP is not an AWS SDK operation.
+ Create an alarm that evaluates a PromQL query.
+ Inspect the alarm's contributors, the individual series that the query matched.
+ Get statistics for a metric and chart it on a dashboard.
+ Mute the alarm for a maintenance window, then clean up.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).
Run an interactive scenario demonstrating the CloudWatch OpenTelemetry experience.

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.services.cloudwatch.model.AlarmContributor;
import software.amazon.awssdk.services.cloudwatch.model.AlarmMuteRuleSummary;
import software.amazon.awssdk.services.cloudwatch.model.Dimension;
import software.amazon.awssdk.services.cloudwatch.model.GetAlarmMuteRuleResponse;

import java.time.Instant;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;

/**
 * Before running this Java V2 code example, set up your development environment,
 * including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 *
 * This scenario demonstrates the Amazon CloudWatch OpenTelemetry (OTel) experience.
 * CloudWatch ingests OpenTelemetry metrics natively, and this example walks through what
 * you do with them: turning on enrichment so CloudWatch can correlate incoming OTLP
 * metrics with the resources that produced them, alarming on those metrics with a PromQL
 * query, and finding out which individual series drove the alarm.
 *
 * A PromQL alarm works differently from a classic metric alarm. Rather than watching one
 * metric and counting breaching periods, it evaluates a query that can match many series
 * at once, and tracks each matching series separately as a contributor.
 *
 * Note that sending OTLP metrics to CloudWatch is not an AWS SDK operation. Metrics
 * arrive over the OTLP protocol through the CloudWatch agent, an OpenTelemetry
 * Collector, or an ADOT SDK. Everything this scenario does is configuration and querying
 * around that ingestion path.
 *
 * This Java code example performs the following tasks:
 *
 * 1. List metrics and namespaces from Amazon CloudWatch.
 * 2. Start OpenTelemetry enrichment for the account.
 * 3. Explain how OTLP metrics reach CloudWatch.
 * 4. Create an alarm that evaluates a PromQL query.
 * 5. Inspect the contributors to the PromQL alarm.
 * 6. Get metric statistics and chart the metric on a dashboard.
 * 7. Mute the alarm for a maintenance window.
 * 8. Clean up the Amazon CloudWatch resources.
 */
public class CloudWatchScenario {
    public static final String DASHES = new String(new char[80]).replace("\0", "-");

    private static final String DEFAULT_QUERY = "avg by (host) (system_cpu_utilization) > 80";

    // Valid evaluation intervals are 10, 20, 30, or any multiple of 60 up to 3600 seconds.
    private static final int EVALUATION_INTERVAL = 60;
    private static final int PENDING_PERIOD = 300;
    private static final int RECOVERY_PERIOD = 120;

    static CloudWatchActions cwActions = new CloudWatchActions();

    private static final Logger logger = LoggerFactory.getLogger(CloudWatchScenario.class);
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws Throwable {

        // Suffix the resource names so repeated runs do not collide.
        String suffix = String.valueOf(new Random().nextInt(9000) + 1000);
        String alarmName = "doc-example-promql-alarm-" + suffix;
        String dashboardName = "doc-example-dashboard-" + suffix;
        String muteRuleName = "doc-example-mute-rule-" + suffix;

        logger.info(DASHES);
        logger.info("Welcome to the Amazon CloudWatch Basics scenario.");
        logger.info("""
            CloudWatch now ingests OpenTelemetry metrics natively. This scenario walks through
            that experience: it turns on OTel enrichment so CloudWatch can correlate incoming
            OTLP metrics with the resources that produced them, alarms on those metrics with a
            PromQL query, and shows you which individual series drove the alarm.

            A PromQL alarm works differently from a classic metric alarm. Rather than watching
            one metric and counting breaching periods, it evaluates a query that can match many
            series at once, and tracks each one separately as a contributor.

            Let's get started...
            """);
        waitForInputToContinue(scanner);

        try {
            runScenario(alarmName, dashboardName, muteRuleName);
        } catch (RuntimeException e) {
            e.printStackTrace();
        }
        logger.info(DASHES);
    }

    private static void runScenario(String alarmName, String dashboardName, String muteRuleName)
            throws Throwable {

        // Tracks whether this run turned enrichment on, so that cleanup only turns off
        // enrichment that this run started.
        boolean startedEnrichment = false;

        logger.info(DASHES);
        logger.info("""
            1. List metrics and namespaces

            Before configuring anything, let's see what CloudWatch is already collecting in
            this account by calling ListMetrics.
            """);
        waitForInputToContinue(scanner);

        ArrayList<String> namespaces = cwActions.listNameSpacesAsync().join();
        logger.info("Found {} namespaces in this account:", namespaces.size());
        namespaces.stream().limit(10).forEach(namespace -> logger.info("  {}", namespace));
        if (namespaces.isEmpty()) {
            logger.info("""
                No metrics found in this account. The statistics and dashboard steps later on
                need an existing metric, so they will be skipped.
                """);
        }
        waitForInputToContinue(scanner);

        logger.info(DASHES);
        logger.info("""
            2. Start OpenTelemetry enrichment

            Enrichment is what lets CloudWatch attach AWS resource context to the OTLP metrics
            you send it. Without it, your metrics arrive as opaque series with no connection to
            the resources that emitted them.

            We check the current state first, and only start enrichment if it isn't already on.
            """);
        waitForInputToContinue(scanner);

        String status = cwActions.getOTelEnrichmentStatusAsync().join();
        logger.info("Enrichment status: {}", status);

        if (!"Running".equalsIgnoreCase(status)) {
            cwActions.startOTelEnrichmentAsync().join();
            startedEnrichment = true;
            status = cwActions.getOTelEnrichmentStatusAsync().join();
            logger.info("Enrichment status: {}", status);
            logger.info("""
                Note: this run started enrichment, so the cleanup step will stop it again.
                """);
        } else {
            logger.info("""
                Enrichment was already running, so we will leave it alone. The cleanup step
                will not stop it, because other workloads in this account may depend on it.
                """);
        }
        waitForInputToContinue(scanner);

        logger.info(DASHES);
        logger.info("""
            3. Send OTLP metrics to CloudWatch

            This step is not an AWS SDK operation, and that's worth being explicit about.
            Metrics reach CloudWatch over the OTLP protocol, through the CloudWatch agent, an
            OpenTelemetry Collector, or an ADOT SDK. There is no PutOTelMetrics API to call.

            Point your collector at the CloudWatch metrics endpoint, which follows the pattern
            https://monitoring.<region>.amazonaws.com/v1/metrics

            The endpoint is HTTP/1.1 only and does not support gRPC, so use an otlphttp
            exporter rather than otlp. The metrics endpoint signs as "monitoring".
            """);
        waitForInputToContinue(scanner);

        logger.info(DASHES);
        logger.info("""
            4. Create a PromQL alarm

            Now we alarm on those metrics. The comparison goes inside the query itself: a
            PromQL alarm has no separate threshold, comparison operator, statistic, or period.
            """);
        logger.info("Enter a PromQL query, or press <ENTER> for the default");
        logger.info("[{}]:", DEFAULT_QUERY);
        String queryInput = scanner.nextLine();
        String query = queryInput == null || queryInput.isBlank() ? DEFAULT_QUERY : queryInput.trim();

        cwActions.putPromQLMetricAlarmAsync(alarmName, query, EVALUATION_INTERVAL,
                PENDING_PERIOD, RECOVERY_PERIOD).join();
        logger.info("Created alarm {}:", alarmName);
        logger.info("  query:              {}", query);
        logger.info("  evaluationInterval: {} seconds", EVALUATION_INTERVAL);
        logger.info("  pendingPeriod:      {} seconds", PENDING_PERIOD);
        logger.info("  recoveryPeriod:     {} seconds", RECOVERY_PERIOD);
        logger.info("""

            A PromQL alarm starts in the OK state rather than INSUFFICIENT_DATA, which is
            another way it differs from a classic alarm.
            """);
        waitForInputToContinue(scanner);

        logger.info(DASHES);
        logger.info("""
            5. Inspect the alarm's contributors

            Each contributor is one series the query matched, identified by its label set. This
            is how you find out which host is unhealthy rather than only that something is.
            Classic alarms have no equivalent.
            """);
        waitForInputToContinue(scanner);

        List<AlarmContributor> contributors = cwActions.describeAlarmContributorsAsync(alarmName).join();
        if (contributors.isEmpty()) {
            logger.info("""
                No contributors yet. The query matched no series, which usually means no OTel
                metrics with these labels have arrived. Once your collector is sending data,
                each matching series appears here with its labels and the reason it breached.
                """);
        } else {
            logger.info("Found {} contributors:", contributors.size());
            for (AlarmContributor contributor : contributors) {
                StringBuilder labels = new StringBuilder();
                for (Map.Entry<String, String> attribute : contributor.contributorAttributes().entrySet()) {
                    if (labels.length() > 0) {
                        labels.append(", ");
                    }
                    labels.append(attribute.getKey()).append("=").append(attribute.getValue());
                }
                logger.info("  {}: {}", contributor.contributorId(), labels);
                logger.info("    reason: {}", contributor.stateReason());
            }
        }
        waitForInputToContinue(scanner);

        logger.info(DASHES);
        logger.info("""
            6. Get statistics and chart the metric on a dashboard

            Statistics and dashboards are how you see what the alarm is evaluating.
            """);
        waitForInputToContinue(scanner);

        boolean dashboardCreated = false;
        if (!namespaces.isEmpty()) {
            String namespace = namespaces.get(0);
            ArrayList<String> metrics = cwActions.listMetsAsync(namespace).join();
            if (metrics != null && !metrics.isEmpty()) {
                String metricName = metrics.get(0);
                String startDate = Instant.now().minus(24, ChronoUnit.HOURS).toString();
                Dimension dimension = null;
                try {
                    dimension = cwActions.getSpecificMetAsync(namespace).join();
                    cwActions.getAndDisplayMetricStatisticsAsync(namespace, metricName,
                            "Average", startDate, dimension).join();
                } catch (RuntimeException e) {
                    logger.info("Could not get statistics for {}/{}: {}", namespace, metricName,
                            e.getMessage());
                }

                // Chart the metric this run just discovered. Reading the widgets from a
                // file would chart metrics that may not exist in this account.
                try {
                    String dashboardBody = buildDashboardBody(namespace, metricName, dimension,
                            cwActions.getRegion());
                    cwActions.createDashboardAsync(dashboardName, dashboardBody).join();
                    dashboardCreated = true;
                    cwActions.listDashboardsAsync().join();
                } catch (RuntimeException e) {
                    logger.info("Could not create the dashboard: {}", e.getMessage());
                }
            } else {
                logger.info("No metrics found in namespace {}, skipping statistics and the "
                        + "dashboard.", namespace);
            }
        } else {
            logger.info("Skipping statistics and dashboard because no metrics exist yet.");
        }
        waitForInputToContinue(scanner);

        logger.info(DASHES);
        logger.info("""
            7. Mute the alarm for a maintenance window

            While a mute rule is active the targeted alarms keep evaluating and keep changing
            state, but their actions do not fire. This is the supported way to suppress
            notifications during planned maintenance, instead of disabling alarm actions and
            hoping someone remembers to turn them back on.
            """);
        waitForInputToContinue(scanner);

        // The expression is a five-field cron expression,
        // cron(Minutes Hours Day-of-month Month Day-of-week). Note that this is five fields,
        // not the six that Amazon EventBridge uses. For a one-time window, use
        // at(yyyy-MM-ddThh:mm), with no seconds. The duration is an ISO 8601 duration from
        // PT1M to P15D, so PT2H rather than 2h.
        String expression = "cron(0 2 * * SUN)";
        String duration = "PT2H";
        String timezone = "America/Los_Angeles";

        cwActions.putAlarmMuteRuleAsync(muteRuleName, expression, duration, timezone,
                List.of(alarmName)).join();
        logger.info("Created mute rule {}:", muteRuleName);
        logger.info("  schedule: {} for {}", expression, duration);
        logger.info("  timezone: {}", timezone);
        logger.info("  targets:  {}", alarmName);
        logger.info("""

            Note the two formats here. The expression is a five-field cron expression, five
            rather than the six Amazon EventBridge uses. The duration is an ISO 8601 duration,
            so 'PT2H' and not '2h'.

            Also note that muteTargets is set explicitly. If you leave it out, the rule applies
            to every alarm in the account.
            """);

        GetAlarmMuteRuleResponse muteRule = cwActions.getAlarmMuteRuleAsync(muteRuleName).join();
        logger.info("Read the rule back: status {}, mute type {}.", muteRule.statusAsString(),
                muteRule.muteType());

        List<AlarmMuteRuleSummary> summaries = cwActions.listAlarmMuteRulesAsync(alarmName).join();
        logger.info("Found {} mute rules targeting this alarm.", summaries.size());
        // Mute rule summaries carry no name field, only an ARN, so match on the ARN suffix.
        summaries.stream()
                .filter(summary -> summary.alarmMuteRuleArn().endsWith("/" + muteRuleName)
                        || summary.alarmMuteRuleArn().endsWith(":" + muteRuleName))
                .findFirst()
                .ifPresent(summary -> logger.info("  matched by ARN: {} ({})",
                        summary.alarmMuteRuleArn(), summary.statusAsString()));
        waitForInputToContinue(scanner);

        logger.info(DASHES);
        logger.info("8. Clean up");
        logger.info("Delete the resources this scenario created? (y/n)");
        String cleanUp = scanner.nextLine();
        if (cleanUp == null || !cleanUp.trim().equalsIgnoreCase("y")) {
            logger.info("""
                Skipping cleanup. Note that the alarm, dashboard, and mute rule are still in
                your account, and enrichment may still be running.
                """);
            logger.info(DASHES);
            logger.info("This concludes the Amazon CloudWatch Basics scenario.");
            return;
        }

        // Each deletion is attempted independently so that one failure does not leave the
        // remaining resources behind.
        try {
            cwActions.deleteAlarmMuteRuleAsync(muteRuleName).join();
        } catch (RuntimeException e) {
            logger.info("Could not delete the mute rule: {}", e.getMessage());
        }

        try {
            cwActions.deleteCWAlarmAsync(alarmName).join();
            logger.info("Deleted alarm {}.", alarmName);
        } catch (RuntimeException e) {
            logger.info("Could not delete the alarm: {}", e.getMessage());
        }

        if (dashboardCreated) {
            try {
                cwActions.deleteDashboardAsync(dashboardName).join();
                logger.info("Deleted dashboard {}.", dashboardName);
            } catch (RuntimeException e) {
                logger.info("Could not delete the dashboard: {}", e.getMessage());
            }
        }

        if (startedEnrichment) {
            try {
                cwActions.stopOTelEnrichmentAsync().join();
                logger.info("Stopped OTel enrichment, because this run started it.");
            } catch (RuntimeException e) {
                logger.info("Could not stop OTel enrichment: {}", e.getMessage());
            }
        } else {
            logger.info("""
                Left OTel enrichment running, because it was already on before this run.
                """);
        }

        logger.info(DASHES);
        logger.info("This concludes the Amazon CloudWatch Basics scenario.");
        logger.info(DASHES);
    }

    /**
     * Builds a single-widget dashboard body that charts the given metric.
     *
     * @param metricNamespace the namespace of the metric to chart
     * @param metricName      the name of the metric to chart
     * @param dimension       a dimension to narrow the metric to, or null for none
     * @param region          the Region the metric is in. A metric widget must name its
     *                        Region, because a dashboard can chart metrics from several.
     * @return the dashboard body, as JSON
     */
    static String buildDashboardBody(String metricNamespace, String metricName,
            Dimension dimension, String region) {
        String dimensionParts = dimension == null ? ""
                : String.format(", \"%s\", \"%s\"", dimension.name(), dimension.value());

        return String.format("""
            {
                "widgets": [
                    {
                        "type": "text",
                        "x": 0, "y": 0, "width": 24, "height": 2,
                        "properties": {
                            "markdown": "This dashboard was created programmatically by an AWS SDK code example."
                        }
                    },
                    {
                        "type": "metric",
                        "x": 0, "y": 2, "width": 12, "height": 6,
                        "properties": {
                            "metrics": [[ "%s", "%s"%s ]],
                            "view": "timeSeries",
                            "stat": "Average",
                            "period": 300,
                            "region": "%s",
                            "title": "%s"
                        }
                    }
                ]
            }
            """, metricNamespace, metricName, dimensionParts, region, metricName);
    }

    private static void waitForInputToContinue(Scanner scanner) {
        while (true) {
            logger.info("");
            logger.info("Press <ENTER> to continue:");
            String input = scanner.nextLine();

            if (input == null || input.trim().isEmpty()) {
                logger.info("Continuing with the program...");
                logger.info("");
                break;
            } else {
                logger.info("Invalid input. Please try again.");
            }
        }
    }
}
```
A wrapper class for the CloudWatch SDK methods that the scenario calls.

```
public class CloudWatchActions {

    private static CloudWatchAsyncClient cloudWatchAsyncClient;

    private static final Logger logger = LoggerFactory.getLogger(CloudWatchActions.class);

    /**
     * Retrieves an asynchronous CloudWatch client instance.
     *
     * <p>
     * This method ensures that the CloudWatch client is initialized with the following configurations:
     * <ul>
     *     <li>Maximum concurrency: 100</li>
     *     <li>Connection timeout: 60 seconds</li>
     *     <li>Read timeout: 60 seconds</li>
     *     <li>Write timeout: 60 seconds</li>
     *     <li>API call timeout: 2 minutes</li>
     *     <li>API call attempt timeout: 90 seconds</li>
     *     <li>Retry strategy: STANDARD</li>
     * </ul>
     * </p>
     *
     * @return the asynchronous CloudWatch client instance
     */
    private static CloudWatchAsyncClient getAsyncClient() {
        if (cloudWatchAsyncClient == null) {
            SdkAsyncHttpClient httpClient = NettyNioAsyncHttpClient.builder()
                .maxConcurrency(100)
                .connectionTimeout(Duration.ofSeconds(60))
                .readTimeout(Duration.ofSeconds(60))
                .writeTimeout(Duration.ofSeconds(60))
                .build();

            ClientOverrideConfiguration overrideConfig = ClientOverrideConfiguration.builder()
                .apiCallTimeout(Duration.ofMinutes(2))
                .apiCallAttemptTimeout(Duration.ofSeconds(90))
                .retryStrategy(RetryMode.STANDARD)
                .build();

            cloudWatchAsyncClient = CloudWatchAsyncClient.builder()
                .httpClient(httpClient)
                .overrideConfiguration(overrideConfig)
                .build();
        }
        return cloudWatchAsyncClient;
    }

    /**
     * Returns the Region the client resolved, which a dashboard's metric widgets must name.
     *
     * @return the Region ID, such as us-east-1
     */
    public String getRegion() {
        return getAsyncClient().serviceClientConfiguration().region().id();
    }

    /**
     * Deletes an Anomaly Detector.
     *
     * @param fileName the name of the file containing the Anomaly Detector configuration
     * @return a CompletableFuture that represents the asynchronous deletion of the Anomaly Detector
     */
    public CompletableFuture<DeleteAnomalyDetectorResponse> deleteAnomalyDetectorAsync(String fileName) {
        CompletableFuture<JsonNode> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                return new ObjectMapper().readTree(parser); // Return the root node
            } catch (IOException e) {
                throw new RuntimeException("Failed to read or parse the file", e);
            }
        });

        return readFileFuture.thenCompose(rootNode -> {
            String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
            String customMetricName = rootNode.findValue("customMetricName").asText();

            SingleMetricAnomalyDetector singleMetricAnomalyDetector = SingleMetricAnomalyDetector.builder()
                .metricName(customMetricName)
                .namespace(customMetricNamespace)
                .stat("Maximum")
                .build();

            DeleteAnomalyDetectorRequest request = DeleteAnomalyDetectorRequest.builder()
                .singleMetricAnomalyDetector(singleMetricAnomalyDetector)
                .build();

            return getAsyncClient().deleteAnomalyDetector(request);
        }).whenComplete((result, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Failed to delete the Anomaly Detector", exception);
            } else {
                logger.info("Successfully deleted the Anomaly Detector.");
            }
        });
    }

    /**
     * Deletes a CloudWatch alarm.
     *
     * @param alarmName the name of the alarm to be deleted
     * @return a {@link CompletableFuture} representing the asynchronous operation to delete the alarm
     * the {@link DeleteAlarmsResponse} is returned when the operation completes successfully,
     * or a {@link RuntimeException} is thrown if the operation fails
     */
    public CompletableFuture<DeleteAlarmsResponse> deleteCWAlarmAsync(String alarmName) {
        DeleteAlarmsRequest request = DeleteAlarmsRequest.builder()
            .alarmNames(alarmName)
            .build();

        return getAsyncClient().deleteAlarms(request)
            .whenComplete((response, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Failed to delete the alarm:{} " + alarmName, exception);
                } else {
                    logger.info("Successfully deleted alarm {} ", alarmName);
                }
            });
    }

    /**
     * Deletes the specified dashboard.
     *
     * @param dashboardName the name of the dashboard to be deleted
     * @return a {@link CompletableFuture} representing the asynchronous operation of deleting the dashboard
     * @throws RuntimeException if the dashboard deletion fails
     */
    public CompletableFuture<DeleteDashboardsResponse> deleteDashboardAsync(String dashboardName) {
        DeleteDashboardsRequest dashboardsRequest = DeleteDashboardsRequest.builder()
            .dashboardNames(dashboardName)
            .build();

        return getAsyncClient().deleteDashboards(dashboardsRequest)
            .whenComplete((response, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Failed to delete the dashboard: " + dashboardName, exception);
                } else {
                    logger.info("{} was successfully deleted.", dashboardName);
                }
            });
    }

    /**
     * Retrieves and saves a custom metric image to a file.
     *
     * @param fileName the name of the file to save the metric image to
     * @return a {@link CompletableFuture} that completes when the image has been saved to the file
     */
    public CompletableFuture<Void> downloadAndSaveMetricImageAsync(String fileName) {
        logger.info("Getting Image data for custom metric.");
        String myJSON = """
              {
                  "title": "Example Metric Graph",
                  "view": "timeSeries",
                  "stacked ": false,
                  "period": 10,
                  "width": 1400,
                  "height": 600,
                  "metrics": [
                      [
                      "AWS/Billing",
                      "EstimatedCharges",
                      "Currency",
                      "USD"
                     ]
                  ]
              }
            """;

        GetMetricWidgetImageRequest imageRequest = GetMetricWidgetImageRequest.builder()
            .metricWidget(myJSON)
            .build();

        return getAsyncClient().getMetricWidgetImage(imageRequest)
            .thenCompose(response -> {
                SdkBytes sdkBytes = response.metricWidgetImage();
                byte[] bytes = sdkBytes.asByteArray();
                return CompletableFuture.runAsync(() -> {
                    try {
                        File outputFile = new File(fileName);
                        try (FileOutputStream outputStream = new FileOutputStream(outputFile)) {
                            outputStream.write(bytes);
                        }
                    } catch (IOException e) {
                        throw new RuntimeException("Failed to write image to file", e);
                    }
                });
            })
            .whenComplete((result, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Error getting and saving metric image", exception);
                } else {
                    logger.info("Image data saved successfully to {}", fileName);
                }
            });
    }

    /**
     * Describes the anomaly detectors based on the specified JSON file.
     *
     * @param fileName the name of the JSON file containing the custom metric namespace and name
     * @return a {@link CompletableFuture} that completes when the anomaly detectors have been described
     * @throws RuntimeException if there is a failure during the operation, such as when reading or parsing the JSON file,
     *                          or when describing the anomaly detectors
     */
    public CompletableFuture<Void> describeAnomalyDetectorsAsync(String fileName) {
        CompletableFuture<JsonNode> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                return new ObjectMapper().readTree(parser);
            } catch (IOException e) {
                throw new RuntimeException("Failed to read or parse the file", e);
            }
        });

        return readFileFuture.thenCompose(rootNode -> {
            try {
                String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
                String customMetricName = rootNode.findValue("customMetricName").asText();

                DescribeAnomalyDetectorsRequest detectorsRequest = DescribeAnomalyDetectorsRequest.builder()
                    .maxResults(10)
                    .metricName(customMetricName)
                    .namespace(customMetricNamespace)
                    .build();

                return getAsyncClient().describeAnomalyDetectors(detectorsRequest).thenAccept(response -> {
                    List<AnomalyDetector> anomalyDetectorList = response.anomalyDetectors();
                    for (AnomalyDetector detector : anomalyDetectorList) {
                        logger.info("Metric name: {} ", detector.singleMetricAnomalyDetector().metricName());
                        logger.info("State: {} ", detector.stateValue());
                    }
                });
            } catch (RuntimeException e) {
                throw new RuntimeException("Failed to describe anomaly detectors", e);
            }
        }).whenComplete((result, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Error describing anomaly detectors", exception);
            }
        });
    }

    /**
     * Adds an anomaly detector for the given file.
     *
     * @param fileName the name of the file containing the anomaly detector configuration
     * @return a {@link CompletableFuture} that completes when the anomaly detector has been added
     */
    public CompletableFuture<Void> addAnomalyDetectorAsync(String fileName) {
        CompletableFuture<JsonNode> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                return new ObjectMapper().readTree(parser); // Return the root node
            } catch (IOException e) {
                throw new RuntimeException("Failed to read or parse the file", e);
            }
        });

        return readFileFuture.thenCompose(rootNode -> {
            try {
                String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
                String customMetricName = rootNode.findValue("customMetricName").asText();

                SingleMetricAnomalyDetector singleMetricAnomalyDetector = SingleMetricAnomalyDetector.builder()
                    .metricName(customMetricName)
                    .namespace(customMetricNamespace)
                    .stat("Maximum")
                    .build();

                PutAnomalyDetectorRequest anomalyDetectorRequest = PutAnomalyDetectorRequest.builder()
                    .singleMetricAnomalyDetector(singleMetricAnomalyDetector)
                    .build();

                return getAsyncClient().putAnomalyDetector(anomalyDetectorRequest).thenAccept(response -> {
                    logger.info("Added anomaly detector for metric {}", customMetricName);
                });
            } catch (Exception e) {
                throw new RuntimeException("Failed to create anomaly detector", e);
            }
        }).whenComplete((result, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Error adding anomaly detector", exception);
            }
        });
    }

    /**
     * Retrieves the alarm history for a given alarm name and date range.
     *
     * @param fileName the path to the JSON file containing the alarm name
     * @param date     the date to start the alarm history search (in the format "yyyy-MM-dd'T'HH:mm:ss'Z'")
     * @return a {@code CompletableFuture<Void>} that completes when the alarm history has been retrieved and processed
     */
    public CompletableFuture<Void> getAlarmHistoryAsync(String fileName, String date) {
        CompletableFuture<String> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(parser);
                return rootNode.findValue("exampleAlarmName").asText(); // Return alarmName from the JSON file
            } catch (IOException e) {
                throw new RuntimeException("Failed to read or parse the file", e);
            }
        });

        // Use the alarm name to describe alarm history with a paginator.
        return readFileFuture.thenCompose(alarmName -> {
            try {
                Instant start = Instant.parse(date);
                Instant endDate = Instant.now();
                DescribeAlarmHistoryRequest historyRequest = DescribeAlarmHistoryRequest.builder()
                    .startDate(start)
                    .endDate(endDate)
                    .alarmName(alarmName)
                    .historyItemType(HistoryItemType.ACTION)
                    .build();

                // Use the paginator to paginate through alarm history pages.
                DescribeAlarmHistoryPublisher historyPublisher = getAsyncClient().describeAlarmHistoryPaginator(historyRequest);
                CompletableFuture<Void> future = historyPublisher
                    .subscribe(response -> response.alarmHistoryItems().forEach(item -> {
                        logger.info("History summary: {}", item.historySummary());
                        logger.info("Timestamp: {}", item.timestamp());
                    }))
                    .whenComplete((result, exception) -> {
                        if (exception != null) {
                            logger.error("Error occurred while getting alarm history: " + exception.getMessage(), exception);
                        } else {
                            logger.info("Successfully retrieved all alarm history.");
                        }
                    });

                // Return the future to the calling code for further handling
                return future;
            } catch (Exception e) {
                throw new RuntimeException("Failed to process alarm history", e);
            }
        }).whenComplete((result, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Error completing alarm history processing", exception);
            }
        });
    }

    /**
     * Checks for a metric alarm in AWS CloudWatch.
     *
     * @param fileName the name of the file containing the JSON configuration for the custom metric
     * @return a {@link CompletableFuture} that completes when the check for the metric alarm is complete
     */
    public CompletableFuture<Void> checkForMetricAlarmAsync(String fileName) {
        CompletableFuture<String> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(parser);
                return rootNode.toString(); // Return JSON as a string for further processing
            } catch (IOException e) {
                throw new RuntimeException("Failed to read file", e);
            }
        });

        return readFileFuture.thenCompose(jsonContent -> {
            try {
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(jsonContent);
                String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
                String customMetricName = rootNode.findValue("customMetricName").asText();

                DescribeAlarmsForMetricRequest metricRequest = DescribeAlarmsForMetricRequest.builder()
                    .metricName(customMetricName)
                    .namespace(customMetricNamespace)
                    .build();

                return checkForAlarmAsync(metricRequest, customMetricName, 10);

            } catch (IOException e) {
                throw new RuntimeException("Failed to parse JSON content", e);
            }
        }).whenComplete((result, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Error checking metric alarm", exception);
            }
        });
    }

    // Recursive method to check for the alarm.

    /**
     * Checks for the existence of an alarm asynchronously for the specified metric.
     *
     * @param metricRequest    the request to describe the alarms for the specified metric
     * @param customMetricName the name of the custom metric to check for an alarm
     * @param retries          the number of retries to perform if no alarm is found
     * @return a {@link CompletableFuture} that completes when an alarm is found or the maximum number of retries has been reached
     */
    private static CompletableFuture<Void> checkForAlarmAsync(DescribeAlarmsForMetricRequest metricRequest, String customMetricName, int retries) {
        if (retries == 0) {
            return CompletableFuture.completedFuture(null).thenRun(() ->
                logger.info("No Alarm state found for {} after 10 retries.", customMetricName)
            );
        }

        return (getAsyncClient().describeAlarmsForMetric(metricRequest).thenCompose(response -> {
            if (response.hasMetricAlarms()) {
                logger.info("Alarm state found for {}", customMetricName);
                return CompletableFuture.completedFuture(null); // Alarm found, complete the future
            } else {
                return CompletableFuture.runAsync(() -> {
                    try {
                        Thread.sleep(20000);
                        logger.info(".");
                    } catch (InterruptedException e) {
                        throw new RuntimeException("Interrupted while waiting to retry", e);
                    }
                }).thenCompose(v -> checkForAlarmAsync(metricRequest, customMetricName, retries - 1)); // Recursive call
            }
        }));
    }

    /**
     * Adds metric data for an alarm asynchronously.
     *
     * @param fileName the name of the JSON file containing the metric data
     * @return a CompletableFuture that asynchronously returns the PutMetricDataResponse
     */
    public CompletableFuture<PutMetricDataResponse> addMetricDataForAlarmAsync(String fileName) {
        CompletableFuture<String> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(parser);
                return rootNode.toString(); // Return JSON as a string for further processing
            } catch (IOException e) {
                throw new RuntimeException("Failed to read file", e);
            }
        });

        return readFileFuture.thenCompose(jsonContent -> {
            try {
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(jsonContent);
                String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
                String customMetricName = rootNode.findValue("customMetricName").asText();
                Instant instant = Instant.now();

                // Create MetricDatum objects.
                MetricDatum datum1 = MetricDatum.builder()
                    .metricName(customMetricName)
                    .unit(StandardUnit.NONE)
                    .value(1001.00)
                    .timestamp(instant)
                    .build();

                MetricDatum datum2 = MetricDatum.builder()
                    .metricName(customMetricName)
                    .unit(StandardUnit.NONE)
                    .value(1002.00)
                    .timestamp(instant)
                    .build();

                List<MetricDatum> metricDataList = new ArrayList<>();
                metricDataList.add(datum1);
                metricDataList.add(datum2);

                // Build the PutMetricData request.
                PutMetricDataRequest request = PutMetricDataRequest.builder()
                    .namespace(customMetricNamespace)
                    .metricData(metricDataList)
                    .build();

                // Send the request asynchronously.
                return getAsyncClient().putMetricData(request);

            } catch (IOException e) {
                CompletableFuture<PutMetricDataResponse> failedFuture = new CompletableFuture<>();
                failedFuture.completeExceptionally(new RuntimeException("Failed to parse JSON content", e));
                return failedFuture;
            }
        }).whenComplete((response, exception) -> {
            if (exception != null) {
                logger.error("Failed to put metric data: " + exception.getMessage(), exception);
            } else {
                logger.info("Added metric values for metric.");
            }
        });
    }

    /**
     * Retrieves custom metric data from the AWS CloudWatch service.
     *
     * @param fileName the name of the file containing the custom metric information
     * @return a {@link CompletableFuture} that completes when the metric data has been retrieved
     */
    public CompletableFuture<Void> getCustomMetricDataAsync(String fileName) {
        CompletableFuture<String> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                // Read values from the JSON file.
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(parser);
                return rootNode.toString(); // Return JSON as a string for further processing
            } catch (IOException e) {
                throw new RuntimeException("Failed to read file", e);
            }
        });

        return readFileFuture.thenCompose(jsonContent -> {
            try {
                // Parse the JSON string to extract relevant values.
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(jsonContent);
                String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
                String customMetricName = rootNode.findValue("customMetricName").asText();

                // Set the current time and date range for metric query.
                Instant nowDate = Instant.now();
                long hours = 1;
                long minutes = 30;
                Instant endTime = nowDate.plus(hours, ChronoUnit.HOURS).plus(minutes, ChronoUnit.MINUTES);

                Metric met = Metric.builder()
                    .metricName(customMetricName)
                    .namespace(customMetricNamespace)
                    .build();

                MetricStat metStat = MetricStat.builder()
                    .stat("Maximum")
                    .period(60)  // Assuming period in seconds
                    .metric(met)
                    .build();

                MetricDataQuery dataQuery = MetricDataQuery.builder()
                    .metricStat(metStat)
                    .id("foo2")
                    .returnData(true)
                    .build();

                List<MetricDataQuery> dq = new ArrayList<>();
                dq.add(dataQuery);

                GetMetricDataRequest getMetricDataRequest = GetMetricDataRequest.builder()
                    .maxDatapoints(10)
                    .scanBy(ScanBy.TIMESTAMP_DESCENDING)
                    .startTime(nowDate)
                    .endTime(endTime)
                    .metricDataQueries(dq)
                    .build();

                // Call the async method for CloudWatch data retrieval.
                return getAsyncClient().getMetricData(getMetricDataRequest);

            } catch (IOException e) {
                throw new RuntimeException("Failed to parse JSON content", e);
            }
        }).thenAccept(response -> {
            List<MetricDataResult> data = response.metricDataResults();
            for (MetricDataResult item : data) {
                logger.info("The label is: {}", item.label());
                logger.info("The status code is: {}", item.statusCode().toString());
            }
        }).exceptionally(exception -> {
            throw new RuntimeException("Failed to get metric data", exception);
        });
    }

    /**
     * Describes the CloudWatch alarms of the 'METRIC_ALARM' type.
     *
     * @return a {@link CompletableFuture} that represents the asynchronous operation
     * of describing the CloudWatch alarms. The future completes when the
     * operation is finished, either successfully or with an error.
     */
    public CompletableFuture<Void> describeAlarmsAsync() {
        List<AlarmType> typeList = new ArrayList<>();
        typeList.add(AlarmType.METRIC_ALARM);
        DescribeAlarmsRequest alarmsRequest = DescribeAlarmsRequest.builder()
            .alarmTypes(typeList)
            .maxRecords(10)
            .build();

        return getAsyncClient().describeAlarms(alarmsRequest)
            .thenAccept(response -> {
                List<MetricAlarm> alarmList = response.metricAlarms();
                for (MetricAlarm alarm : alarmList) {
                    logger.info("Alarm name: {}", alarm.alarmName());
                    logger.info("Alarm description: {} ", alarm.alarmDescription());
                }
            })
            .whenComplete((response, ex) -> {
                if (ex != null) {
                    logger.info("Failed to describe alarms: {}", ex.getMessage());
                } else {
                    logger.info("Successfully described alarms.");
                }
            });
    }

    /**
     * Creates an alarm based on the configuration provided in a JSON file.
     *
     * @param fileName the name of the JSON file containing the alarm configuration
     * @return a CompletableFuture that represents the asynchronous operation of creating the alarm
     * @throws RuntimeException if an exception occurs while reading the JSON file or creating the alarm
     */
    public CompletableFuture<String> createAlarmAsync(String fileName) {
        com.fasterxml.jackson.databind.JsonNode rootNode;
        try {
            JsonParser parser = new JsonFactory().createParser(new File(fileName));
            rootNode = new ObjectMapper().readTree(parser);
        } catch (IOException e) {
            throw new RuntimeException("Failed to read the alarm configuration file", e);
        }

        // Extract values from the JSON node.
        String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
        String customMetricName = rootNode.findValue("customMetricName").asText();
        String alarmName = rootNode.findValue("exampleAlarmName").asText();
        String emailTopic = rootNode.findValue("emailTopic").asText();
        String accountId = rootNode.findValue("accountId").asText();
        String region = rootNode.findValue("region").asText();

        // Create a List for alarm actions.
        List<String> alarmActions = new ArrayList<>();
        alarmActions.add("arn:aws:sns:" + region + ":" + accountId + ":" + emailTopic);

        PutMetricAlarmRequest alarmRequest = PutMetricAlarmRequest.builder()
            .alarmActions(alarmActions)
            .alarmDescription("Example metric alarm")
            .alarmName(alarmName)
            .comparisonOperator(ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD)
            .threshold(100.00)
            .metricName(customMetricName)
            .namespace(customMetricNamespace)
            .evaluationPeriods(1)
            .period(10)
            .statistic("Maximum")
            .datapointsToAlarm(1)
            .treatMissingData("ignore")
            .build();

        // Call the putMetricAlarm asynchronously and handle the result.
        return getAsyncClient().putMetricAlarm(alarmRequest)
            .handle((response, ex) -> {
                if (ex != null) {
                    logger.info("Failed to create alarm: {}", ex.getMessage());
                    throw new RuntimeException("Failed to create alarm", ex);
                } else {
                    logger.info("{} was successfully created!", alarmName);
                    return alarmName;
                }
            });
    }

    /**
     * Adds a metric to a dashboard asynchronously.
     *
     * @param fileName      the name of the file containing the dashboard content
     * @param dashboardName the name of the dashboard to be updated
     * @return a {@link CompletableFuture} representing the asynchronous operation, which will complete with a
     * {@link PutDashboardResponse} when the dashboard is successfully updated
     */
    public CompletableFuture<PutDashboardResponse> addMetricToDashboardAsync(String fileName, String dashboardName) {
        String dashboardBody;
        try {
            dashboardBody = readFileAsString(fileName);
        } catch (IOException e) {
            throw new RuntimeException("Failed to read the dashboard file", e);
        }

        PutDashboardRequest dashboardRequest = PutDashboardRequest.builder()
            .dashboardName(dashboardName)
            .dashboardBody(dashboardBody)
            .build();

        return getAsyncClient().putDashboard(dashboardRequest)
            .handle((response, ex) -> {
                if (ex != null) {
                    logger.info("Failed to update dashboard: {}", ex.getMessage());
                    throw new RuntimeException("Error updating dashboard", ex);
                } else {
                    logger.info("{} was successfully updated.", dashboardName);
                    return response;
                }
            });
    }

    /**
     * Creates a new custom metric.
     *
     * @param dataPoint the data point to be added to the custom metric
     * @return a {@link CompletableFuture} representing the asynchronous operation of adding the custom metric
     */
    public CompletableFuture<PutMetricDataResponse> createNewCustomMetricAsync(Double dataPoint) {
        Dimension dimension = Dimension.builder()
            .name("UNIQUE_PAGES")
            .value("URLS")
            .build();

        // Set an Instant object for the current time in UTC.
        String time = ZonedDateTime.now(ZoneOffset.UTC).format(DateTimeFormatter.ISO_INSTANT);
        Instant instant = Instant.parse(time);

        // Create the MetricDatum.
        MetricDatum datum = MetricDatum.builder()
            .metricName("PAGES_VISITED")
            .unit(StandardUnit.NONE)
            .value(dataPoint)
            .timestamp(instant)
            .dimensions(dimension)
            .build();

        PutMetricDataRequest request = PutMetricDataRequest.builder()
            .namespace("SITE/TRAFFIC")
            .metricData(datum)
            .build();

        return getAsyncClient().putMetricData(request)
            .whenComplete((response, ex) -> {
                if (ex != null) {
                    throw new RuntimeException("Error adding custom metric", ex);
                } else {
                    logger.info("Successfully added metric values for PAGES_VISITED.");
                }
            });
    }

    /**
     * Lists the available dashboards.
     *
     * @return a {@link CompletableFuture} that completes when the operation is finished.
     * The future will complete exceptionally if an error occurs while listing the dashboards.
     */
    public CompletableFuture<Void> listDashboardsAsync() {
        ListDashboardsRequest listDashboardsRequest = ListDashboardsRequest.builder().build();
        ListDashboardsPublisher paginator = getAsyncClient().listDashboardsPaginator(listDashboardsRequest);
        return paginator.subscribe(response -> {
            response.dashboardEntries().forEach(entry -> {
                logger.info("Dashboard name is: {} ", entry.dashboardName());
                logger.info("Dashboard ARN is: {} ", entry.dashboardArn());
            });
        }).exceptionally(ex -> {
            logger.info("Failed to list dashboards: {} ", ex.getMessage());
            throw new RuntimeException("Error occurred while listing dashboards", ex);
        });
    }

    /**
     * Creates a new dashboard with the specified name and the metrics described by the given file.
     *
     * @param dashboardName the name of the dashboard to be created
     * @param fileName      the name of the file containing the dashboard body
     * @return a {@link CompletableFuture} representing the asynchronous operation of creating the dashboard
     * @throws IOException if there is an error reading the dashboard body from the file
     */
    public CompletableFuture<PutDashboardResponse> createDashboardWithMetricsAsync(String dashboardName, String fileName) throws IOException {
        return createDashboardAsync(dashboardName, readFileAsString(fileName));
    }

    /**
     * Creates a new dashboard with the specified name and body.
     *
     * @param dashboardName the name of the dashboard to be created
     * @param dashboardBody the dashboard body, as JSON
     * @return a {@link CompletableFuture} representing the asynchronous operation of creating the dashboard
     */
    public CompletableFuture<PutDashboardResponse> createDashboardAsync(String dashboardName, String dashboardBody) {
        PutDashboardRequest dashboardRequest = PutDashboardRequest.builder()
            .dashboardName(dashboardName)
            .dashboardBody(dashboardBody)
            .build();

        return getAsyncClient().putDashboard(dashboardRequest)
            .handle((response, ex) -> {
                if (ex != null) {
                    logger.info("Failed to create dashboard: {}", ex.getMessage());
                    throw new RuntimeException("Dashboard creation failed", ex);
                } else {
                    // Handle the normal response case
                    logger.info("{} was successfully created.", dashboardName);
                    List<DashboardValidationMessage> messages = response.dashboardValidationMessages();
                    if (messages.isEmpty()) {
                        logger.info("There are no messages in the new Dashboard.");
                    } else {
                        for (DashboardValidationMessage message : messages) {
                            logger.info("Message: {}", message.message());
                        }
                    }
                    return response; // Return the response for further use
                }
            });
    }

    /**
     * Retrieves the metric statistics for the "EstimatedCharges" metric in the "AWS/Billing" namespace.
     *
     * @param costDateWeek the start date for the metric statistics, in the format of an ISO-8601 date string (e.g., "2023-04-05")
     * @return a {@link CompletableFuture} that, when completed, contains the {@link GetMetricStatisticsResponse} with the retrieved metric statistics
     * @throws RuntimeException if the metric statistics cannot be retrieved successfully
     */
    public CompletableFuture<GetMetricStatisticsResponse> getMetricStatisticsAsync(String costDateWeek) {
        Instant start = Instant.parse(costDateWeek);
        Instant endDate = Instant.now();

        // Define dimension
        Dimension dimension = Dimension.builder()
            .name("Currency")
            .value("USD")
            .build();

        List<Dimension> dimensionList = new ArrayList<>();
        dimensionList.add(dimension);

        GetMetricStatisticsRequest statisticsRequest = GetMetricStatisticsRequest.builder()
            .metricName("EstimatedCharges")
            .namespace("AWS/Billing")
            .dimensions(dimensionList)
            .statistics(Statistic.MAXIMUM)
            .startTime(start)
            .endTime(endDate)
            .period(86400) // One day period
            .build();

        return getAsyncClient().getMetricStatistics(statisticsRequest)
            .whenComplete((response, exception) -> {
                if (response != null) {
                    List<Datapoint> data = response.datapoints();
                    if (!data.isEmpty()) {
                        for (Datapoint datapoint : data) {
                            logger.info("Timestamp: {} Maximum value: {})", datapoint.timestamp(), datapoint.maximum());
                        }
                    } else {
                        logger.info("The returned data list is empty");
                    }
                } else {
                    throw new RuntimeException("Failed to get metric statistics: " + exception.getMessage(), exception);
                }
            });
    }

    /**
     * Retrieves and displays metric statistics for the specified parameters.
     *
     * @param nameSpace    the namespace for the metric
     * @param metVal       the name of the metric
     * @param metricOption the statistic to retrieve for the metric (e.g., "Maximum", "Average")
     * @param date         the date for which to retrieve the metric statistics, in the format "yyyy-MM-dd'T'HH:mm:ss'Z'"
     * @param myDimension  the dimension(s) to filter the metric statistics by
     * @return a {@link CompletableFuture} that completes when the metric statistics have been retrieved and displayed
     */
    public CompletableFuture<GetMetricStatisticsResponse> getAndDisplayMetricStatisticsAsync(String nameSpace, String metVal,
                                                                                             String metricOption, String date, Dimension myDimension) {

        Instant start = Instant.parse(date);
        Instant endDate = Instant.now();

        // Building the request for metric statistics.
        GetMetricStatisticsRequest statisticsRequest = GetMetricStatisticsRequest.builder()
            .endTime(endDate)
            .startTime(start)
            .dimensions(myDimension)
            .metricName(metVal)
            .namespace(nameSpace)
            .period(86400) // 1 day period
            .statistics(Statistic.fromValue(metricOption))
            .build();

        return getAsyncClient().getMetricStatistics(statisticsRequest)
            .whenComplete((response, exception) -> {
                if (response != null) {
                    List<Datapoint> data = response.datapoints();
                    if (!data.isEmpty()) {
                        for (Datapoint datapoint : data) {
                            logger.info("Timestamp: {} Maximum value: {}", datapoint.timestamp(), datapoint.maximum());
                        }
                    } else {
                        logger.info("The returned data list is empty");
                    }
                } else {
                    logger.info("Failed to get metric statistics: {} ", exception.getMessage());
                }
            })
            .exceptionally(exception -> {
                throw new RuntimeException("Error while getting metric statistics: " + exception.getMessage(), exception);
            });
    }

    /**
     * Retrieves a list of metric names for the specified namespace.
     *
     * @param namespace the namespace for which to retrieve the metric names
     * @return a {@link CompletableFuture} that, when completed, contains an {@link ArrayList} of
     * the metric names in the specified namespace
     * @throws RuntimeException if an error occurs while listing the metrics
     */
    public CompletableFuture<ArrayList<String>> listMetsAsync(String namespace) {
        ListMetricsRequest request = ListMetricsRequest.builder()
            .namespace(namespace)
            .build();

        ListMetricsPublisher metricsPaginator = getAsyncClient().listMetricsPaginator(request);
        Set<String> metSet = new HashSet<>();
        CompletableFuture<Void> future = metricsPaginator.subscribe(response -> {
            response.metrics().forEach(metric -> {
                String metricName = metric.metricName();
                metSet.add(metricName);
            });
        });

        return future
            .thenApply(ignored -> new ArrayList<>(metSet))
            .exceptionally(exception -> {
                throw new RuntimeException("Failed to list metrics: " + exception.getMessage(), exception);
            });
    }

    /**
     * Lists the available namespaces for the current AWS account.
     *
     * @return a {@link CompletableFuture} that, when completed, contains an {@link ArrayList} of the available namespace names.
     * @throws RuntimeException if an error occurs while listing the namespaces.
     */
    public CompletableFuture<ArrayList<String>> listNameSpacesAsync() {
        ArrayList<String> nameSpaceList = new ArrayList<>();
        ListMetricsRequest request = ListMetricsRequest.builder().build();

        ListMetricsPublisher metricsPaginator = getAsyncClient().listMetricsPaginator(request);
        CompletableFuture<Void> future = metricsPaginator.subscribe(response -> {
            response.metrics().forEach(metric -> {
                String namespace = metric.namespace();
                if (!nameSpaceList.contains(namespace)) {
                    nameSpaceList.add(namespace);
                }
            });
        });

        return future
            .thenApply(ignored -> nameSpaceList)
            .exceptionally(exception -> {
                throw new RuntimeException("Failed to list namespaces: " + exception.getMessage(), exception);
            });
    }
    /**
     * Retrieves the specific metric asynchronously.
     *
     * @param namespace the namespace of the metric to retrieve
     * @return a CompletableFuture that completes with the first dimension of the first metric found in the specified namespace,
     * or throws a RuntimeException if an error occurs or no metrics or dimensions are found
     */
    public CompletableFuture<Dimension> getSpecificMetAsync(String namespace) {
        ListMetricsRequest request = ListMetricsRequest.builder()
            .namespace(namespace)
            .build();

        return getAsyncClient().listMetrics(request).handle((response, exception) -> {
            if (exception != null) {
                logger.info("Error occurred while listing metrics: {} ", exception.getMessage());
                throw new RuntimeException("Failed to retrieve specific metric dimension", exception);
            } else {
                List<Metric> myList = response.metrics();
                if (!myList.isEmpty()) {
                    Metric metric = myList.get(0);
                    if (!metric.dimensions().isEmpty()) {
                        return metric.dimensions().get(0); // Return the first dimension
                    }
                }
                throw new RuntimeException("No metrics or dimensions found");
            }
        });
    }

    /**
     * Gets the current OTel enrichment status for the account. Enrichment is what makes
     * CloudWatch attach AWS resource context to incoming OTLP metrics, so the metrics
     * become correlatable with the rest of CloudWatch rather than opaque series.
     *
     * @return a {@link CompletableFuture} that completes with the status, such as
     * {@code Running} or {@code NotStarted}
     */
    public CompletableFuture<String> getOTelEnrichmentStatusAsync() {
        return getAsyncClient().getOTelEnrichment(GetOTelEnrichmentRequest.builder().build())
            .handle((response, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Failed to get OTel enrichment status: "
                        + exception.getMessage(), exception);
                }
                return response.statusAsString();
            });
    }

    /**
     * Turns on OTel enrichment for the account.
     *
     * @return a {@link CompletableFuture} that completes when enrichment has started
     */
    public CompletableFuture<Void> startOTelEnrichmentAsync() {
        return getAsyncClient().startOTelEnrichment(StartOTelEnrichmentRequest.builder().build())
            .handle((response, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Failed to start OTel enrichment: "
                        + exception.getMessage(), exception);
                }
                logger.info("Started OTel enrichment for this account.");
                return null;
            });
    }

    /**
     * Turns off OTel enrichment for the account. Existing PromQL alarms are not deleted,
     * but vended metrics stop being enriched, so queries that select on the added labels
     * stop matching.
     *
     * @return a {@link CompletableFuture} that completes when enrichment has stopped
     */
    public CompletableFuture<Void> stopOTelEnrichmentAsync() {
        return getAsyncClient().stopOTelEnrichment(StopOTelEnrichmentRequest.builder().build())
            .handle((response, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Failed to stop OTel enrichment: "
                        + exception.getMessage(), exception);
                }
                logger.info("Stopped OTel enrichment for this account.");
                return null;
            });
    }

    /**
     * Creates an alarm that evaluates a PromQL query.
     *
     * <p>A PromQL alarm differs from a classic metric alarm in a few ways. The query can
     * match many series at once, and each matching series is tracked separately as a
     * contributor. Instead of counting breaching periods, you specify durations: a
     * contributor moves to ALARM after it breaches continuously for the pending period,
     * and back to OK after it stops breaching for the recovery period. A PromQL alarm
     * starts in the OK state rather than INSUFFICIENT_DATA.
     *
     * <p>{@link EvaluationCriteria} is a union and is mutually exclusive with the classic
     * {@code metricName} and {@code metrics} parameters. When you use it you must also set
     * {@code evaluationInterval}, and you must not set {@code period}, {@code statistic},
     * {@code threshold}, {@code comparisonOperator}, or {@code evaluationPeriods}.
     *
     * @param alarmName          the name of the alarm, unique within the Region
     * @param query              the PromQL query to evaluate. The comparison belongs in
     *                           the query itself; there is no separate threshold.
     * @param evaluationInterval how often, in seconds, to run the query. Valid values are
     *                           10, 20, 30, and any multiple of 60, up to 3600.
     * @param pendingPeriod      how long, in seconds, a contributor must breach
     *                           continuously before it moves to ALARM
     * @param recoveryPeriod     how long, in seconds, a contributor must stop breaching
     *                           before it moves back to OK
     * @return a {@link CompletableFuture} that completes when the alarm is created
     */
    public CompletableFuture<Void> putPromQLMetricAlarmAsync(String alarmName, String query,
            int evaluationInterval, int pendingPeriod, int recoveryPeriod) {
        AlarmPromQLCriteria promQLCriteria = AlarmPromQLCriteria.builder()
            .query(query)
            .pendingPeriod(pendingPeriod)
            .recoveryPeriod(recoveryPeriod)
            .build();

        PutMetricAlarmRequest request = PutMetricAlarmRequest.builder()
            .alarmName(alarmName)
            .alarmDescription("PromQL alarm created by the AWS SDK for Java 2.x Basics scenario.")
            .evaluationCriteria(EvaluationCriteria.builder()
                .promQLCriteria(promQLCriteria)
                .build())
            .evaluationInterval(evaluationInterval)
            .build();

        return getAsyncClient().putMetricAlarm(request).handle((response, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Failed to create PromQL alarm: "
                    + exception.getMessage(), exception);
            }
            logger.info("Created PromQL alarm {} for query {}.", alarmName, query);
            return null;
        });
    }

    /**
     * Gets the contributors for a PromQL alarm. Each contributor is one series that the
     * alarm's query matched, identified by its label set. This is how you find out which
     * hosts, services, or pods are breaching, rather than only that something is.
     *
     * <p>The paging loop continues until the next token is empty. A page can come back
     * empty while still carrying a next token, so stopping at the first empty page would
     * silently drop later results.
     *
     * @param alarmName the name of the PromQL alarm
     * @return a {@link CompletableFuture} that completes with the list of contributors,
     * which is empty when the query matched no series
     */
    public CompletableFuture<List<AlarmContributor>> describeAlarmContributorsAsync(String alarmName) {
        List<AlarmContributor> contributors = new ArrayList<>();
        return collectContributorsPage(alarmName, null, contributors);
    }

    private CompletableFuture<List<AlarmContributor>> collectContributorsPage(String alarmName,
            String nextToken, List<AlarmContributor> accumulated) {
        DescribeAlarmContributorsRequest request = DescribeAlarmContributorsRequest.builder()
            .alarmName(alarmName)
            .nextToken(nextToken)
            .build();

        return getAsyncClient().describeAlarmContributors(request)
            .thenCompose(response -> {
                accumulated.addAll(response.alarmContributors());
                String token = response.nextToken();
                if (token == null || token.isEmpty()) {
                    return CompletableFuture.completedFuture(accumulated);
                }
                return collectContributorsPage(alarmName, token, accumulated);
            })
            .exceptionally(exception -> {
                throw new RuntimeException("Failed to describe alarm contributors: "
                    + exception.getMessage(), exception);
            });
    }

    /**
     * Creates or updates an alarm mute rule. While a mute rule is active the targeted
     * alarms keep evaluating and keep changing state, but their configured actions do not
     * fire. This is the supported way to suppress notifications during planned
     * maintenance, instead of disabling alarm actions and relying on someone to turn them
     * back on.
     *
     * @param name       the name of the mute rule
     * @param expression when the rule activates. For a recurring window, a five-field
     *                   cron expression, {@code cron(Minutes Hours Day-of-month Month
     *                   Day-of-week)}, such as {@code cron(0 2 * * SUN)}. Note that this
     *                   is five fields, not the six that Amazon EventBridge uses. For a
     *                   one-time window, {@code at(yyyy-MM-ddThh:mm)}, such as
     *                   {@code at(2026-09-05T02:00)}, with no seconds.
     * @param duration   how long the window lasts once it activates, as an ISO 8601
     *                   duration from {@code PT1M} to {@code P15D}. For example,
     *                   {@code PT2H} is two hours. Plain forms such as {@code 2h} are
     *                   rejected.
     * @param timezone   a standard timezone identifier. Defaults to UTC when omitted.
     * @param alarmNames the names of up to 100 alarms to mute. If empty, the rule applies
     *                   to every alarm in the account.
     * @return a {@link CompletableFuture} that completes when the rule is written
     */
    public CompletableFuture<Void> putAlarmMuteRuleAsync(String name, String expression,
            String duration, String timezone, List<String> alarmNames) {
        Schedule schedule = Schedule.builder()
            .expression(expression)
            .duration(duration)
            .timezone(timezone)
            .build();

        PutAlarmMuteRuleRequest.Builder request = PutAlarmMuteRuleRequest.builder()
            .name(name)
            .description("Mute rule created by the AWS SDK for Java 2.x Basics scenario.")
            .rule(Rule.builder().schedule(schedule).build());

        if (alarmNames != null && !alarmNames.isEmpty()) {
            request.muteTargets(MuteTargets.builder().alarmNames(alarmNames).build());
        }

        return getAsyncClient().putAlarmMuteRule(request.build()).handle((response, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Failed to put alarm mute rule: "
                    + exception.getMessage(), exception);
            }
            logger.info("Put alarm mute rule {}.", name);
            return null;
        });
    }

    /**
     * Gets the full configuration of an alarm mute rule, including its schedule, the
     * alarms it targets, and its current status.
     *
     * @param name the name of the mute rule
     * @return a {@link CompletableFuture} that completes with the mute rule
     */
    public CompletableFuture<GetAlarmMuteRuleResponse> getAlarmMuteRuleAsync(String name) {
        return getAsyncClient().getAlarmMuteRule(GetAlarmMuteRuleRequest.builder()
                .alarmMuteRuleName(name)
                .build())
            .handle((response, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Failed to get alarm mute rule: "
                        + exception.getMessage(), exception);
                }
                return response;
            });
    }

    /**
     * Lists the alarm mute rules in the account, optionally filtered to the rules that
     * target one alarm.
     *
     * <p>Note that {@link AlarmMuteRuleSummary} carries no name field, only an ARN,
     * status, mute type, and last-updated timestamp. To find a rule by name, match on the
     * ARN suffix.
     *
     * @param alarmName when non-null, only rules that target this alarm are returned
     * @return a {@link CompletableFuture} that completes with the mute rule summaries
     */
    public CompletableFuture<List<AlarmMuteRuleSummary>> listAlarmMuteRulesAsync(String alarmName) {
        List<AlarmMuteRuleSummary> summaries = new ArrayList<>();
        return collectMuteRulesPage(alarmName, null, summaries);
    }

    private CompletableFuture<List<AlarmMuteRuleSummary>> collectMuteRulesPage(String alarmName,
            String nextToken, List<AlarmMuteRuleSummary> accumulated) {
        ListAlarmMuteRulesRequest request = ListAlarmMuteRulesRequest.builder()
            .alarmName(alarmName)
            .nextToken(nextToken)
            .build();

        return getAsyncClient().listAlarmMuteRules(request)
            .thenCompose(response -> {
                accumulated.addAll(response.alarmMuteRuleSummaries());
                String token = response.nextToken();
                if (token == null || token.isEmpty()) {
                    return CompletableFuture.completedFuture(accumulated);
                }
                return collectMuteRulesPage(alarmName, token, accumulated);
            })
            .exceptionally(exception -> {
                throw new RuntimeException("Failed to list alarm mute rules: "
                    + exception.getMessage(), exception);
            });
    }

    /**
     * Deletes an alarm mute rule. The alarms it targeted resume firing their actions.
     *
     * @param name the name of the mute rule
     * @return a {@link CompletableFuture} that completes when the rule is deleted
     */
    public CompletableFuture<Void> deleteAlarmMuteRuleAsync(String name) {
        return getAsyncClient().deleteAlarmMuteRule(DeleteAlarmMuteRuleRequest.builder()
                .alarmMuteRuleName(name)
                .build())
            .handle((response, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Failed to delete alarm mute rule: "
                        + exception.getMessage(), exception);
                }
                logger.info("Deleted alarm mute rule {}.", name);
                return null;
            });
    }

    public static String readFileAsString(String file) throws IOException {
        return new String(Files.readAllBytes(Paths.get(file)));
    }
}
```
+ For API details, see the following topics in *AWS SDK for Java 2.x API Reference*.
  + [DeleteAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAlarmMuteRule)
  + [DeleteAlarms](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAlarms)
  + [DeleteDashboards](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteDashboards)
  + [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarmContributors)
  + [GetAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetAlarmMuteRule)
  + [GetDashboard](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetDashboard)
  + [GetMetricStatistics](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetMetricStatistics)
  + [GetOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetOTelEnrichment)
  + [ListAlarmMuteRules](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListAlarmMuteRules)
  + [ListDashboards](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListDashboards)
  + [ListMetrics](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListMetrics)
  + [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutAlarmMuteRule)
  + [PutDashboard](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutDashboard)
  + [PutMetricAlarm](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutMetricAlarm)
  + [StartOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/StartOTelEnrichment)
  + [StopOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/StopOTelEnrichment)

## Actions
<a name="actions"></a>

### `DeleteAlarmMuteRule`
<a name="cloudwatch_DeleteAlarmMuteRule_java_topic"></a>

The following code example shows how to use `DeleteAlarmMuteRule`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Deletes an alarm mute rule. The alarms it targeted resume firing their actions.
     *
     * @param cw   the CloudWatch client
     * @param name the name of the mute rule
     */
    public static void deleteAlarmMuteRule(CloudWatchClient cw, String name) {
        try {
            cw.deleteAlarmMuteRule(DeleteAlarmMuteRuleRequest.builder()
                    .alarmMuteRuleName(name)
                    .build());

            System.out.printf("Deleted alarm mute rule %s.%n", name);

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [DeleteAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAlarmMuteRule) in *AWS SDK for Java 2.x API Reference*.

### `DeleteAlarms`
<a name="cloudwatch_DeleteAlarms_java_topic"></a>

The following code example shows how to use `DeleteAlarms`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Deletes a CloudWatch alarm.
     *
     * @param alarmName the name of the alarm to be deleted
     * @return a {@link CompletableFuture} representing the asynchronous operation to delete the alarm
     * the {@link DeleteAlarmsResponse} is returned when the operation completes successfully,
     * or a {@link RuntimeException} is thrown if the operation fails
     */
    public CompletableFuture<DeleteAlarmsResponse> deleteCWAlarmAsync(String alarmName) {
        DeleteAlarmsRequest request = DeleteAlarmsRequest.builder()
            .alarmNames(alarmName)
            .build();

        return getAsyncClient().deleteAlarms(request)
            .whenComplete((response, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Failed to delete the alarm:{} " + alarmName, exception);
                } else {
                    logger.info("Successfully deleted alarm {} ", alarmName);
                }
            });
    }
```
+  For API details, see [DeleteAlarms](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAlarms) in *AWS SDK for Java 2.x API Reference*.

### `DeleteAnomalyDetector`
<a name="cloudwatch_DeleteAnomalyDetector_java_topic"></a>

The following code example shows how to use `DeleteAnomalyDetector`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Deletes an Anomaly Detector.
     *
     * @param fileName the name of the file containing the Anomaly Detector configuration
     * @return a CompletableFuture that represents the asynchronous deletion of the Anomaly Detector
     */
    public CompletableFuture<DeleteAnomalyDetectorResponse> deleteAnomalyDetectorAsync(String fileName) {
        CompletableFuture<JsonNode> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                return new ObjectMapper().readTree(parser); // Return the root node
            } catch (IOException e) {
                throw new RuntimeException("Failed to read or parse the file", e);
            }
        });

        return readFileFuture.thenCompose(rootNode -> {
            String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
            String customMetricName = rootNode.findValue("customMetricName").asText();

            SingleMetricAnomalyDetector singleMetricAnomalyDetector = SingleMetricAnomalyDetector.builder()
                .metricName(customMetricName)
                .namespace(customMetricNamespace)
                .stat("Maximum")
                .build();

            DeleteAnomalyDetectorRequest request = DeleteAnomalyDetectorRequest.builder()
                .singleMetricAnomalyDetector(singleMetricAnomalyDetector)
                .build();

            return getAsyncClient().deleteAnomalyDetector(request);
        }).whenComplete((result, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Failed to delete the Anomaly Detector", exception);
            } else {
                logger.info("Successfully deleted the Anomaly Detector.");
            }
        });
    }
```
+  For API details, see [DeleteAnomalyDetector](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAnomalyDetector) in *AWS SDK for Java 2.x API Reference*.

### `DeleteDashboards`
<a name="cloudwatch_DeleteDashboards_java_topic"></a>

The following code example shows how to use `DeleteDashboards`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Deletes the specified dashboard.
     *
     * @param dashboardName the name of the dashboard to be deleted
     * @return a {@link CompletableFuture} representing the asynchronous operation of deleting the dashboard
     * @throws RuntimeException if the dashboard deletion fails
     */
    public CompletableFuture<DeleteDashboardsResponse> deleteDashboardAsync(String dashboardName) {
        DeleteDashboardsRequest dashboardsRequest = DeleteDashboardsRequest.builder()
            .dashboardNames(dashboardName)
            .build();

        return getAsyncClient().deleteDashboards(dashboardsRequest)
            .whenComplete((response, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Failed to delete the dashboard: " + dashboardName, exception);
                } else {
                    logger.info("{} was successfully deleted.", dashboardName);
                }
            });
    }
```
+  For API details, see [DeleteDashboards](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteDashboards) in *AWS SDK for Java 2.x API Reference*.

### `DescribeAlarmContributors`
<a name="cloudwatch_DescribeAlarmContributors_java_topic"></a>

The following code example shows how to use `DescribeAlarmContributors`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Gets the contributors for a PromQL alarm. Each contributor is one series that the
     * alarm's query matched, identified by its label set. This is how you find out which
     * hosts, services, or pods are breaching, rather than only that something is.
     *
     * @param cw        the CloudWatch client
     * @param alarmName the name of the PromQL alarm
     * @return the list of contributors
     */
    public static List<AlarmContributor> describeAlarmContributors(CloudWatchClient cw, String alarmName) {
        List<AlarmContributor> contributors = new ArrayList<>();
        try {
            String nextToken = null;
            do {
                DescribeAlarmContributorsRequest request = DescribeAlarmContributorsRequest.builder()
                        .alarmName(alarmName)
                        .nextToken(nextToken)
                        .build();

                DescribeAlarmContributorsResponse response = cw.describeAlarmContributors(request);
                contributors.addAll(response.alarmContributors());
                nextToken = response.nextToken();
            } while (nextToken != null && !nextToken.isEmpty());

            for (AlarmContributor contributor : contributors) {
                StringBuilder labels = new StringBuilder();
                for (Map.Entry<String, String> attribute : contributor.contributorAttributes().entrySet()) {
                    if (labels.length() > 0) {
                        labels.append(", ");
                    }
                    labels.append(attribute.getKey()).append("=").append(attribute.getValue());
                }
                System.out.printf("%s: %s%n", contributor.contributorId(), labels);
                System.out.printf("  reason: %s%n", contributor.stateReason());
            }
            return contributors;

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
            return contributors;
        }
    }
```
+  For API details, see [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarmContributors) in *AWS SDK for Java 2.x API Reference*.

### `DescribeAlarmHistory`
<a name="cloudwatch_DescribeAlarmHistory_java_topic"></a>

The following code example shows how to use `DescribeAlarmHistory`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Retrieves the alarm history for a given alarm name and date range.
     *
     * @param fileName the path to the JSON file containing the alarm name
     * @param date     the date to start the alarm history search (in the format "yyyy-MM-dd'T'HH:mm:ss'Z'")
     * @return a {@code CompletableFuture<Void>} that completes when the alarm history has been retrieved and processed
     */
    public CompletableFuture<Void> getAlarmHistoryAsync(String fileName, String date) {
        CompletableFuture<String> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(parser);
                return rootNode.findValue("exampleAlarmName").asText(); // Return alarmName from the JSON file
            } catch (IOException e) {
                throw new RuntimeException("Failed to read or parse the file", e);
            }
        });

        // Use the alarm name to describe alarm history with a paginator.
        return readFileFuture.thenCompose(alarmName -> {
            try {
                Instant start = Instant.parse(date);
                Instant endDate = Instant.now();
                DescribeAlarmHistoryRequest historyRequest = DescribeAlarmHistoryRequest.builder()
                    .startDate(start)
                    .endDate(endDate)
                    .alarmName(alarmName)
                    .historyItemType(HistoryItemType.ACTION)
                    .build();

                // Use the paginator to paginate through alarm history pages.
                DescribeAlarmHistoryPublisher historyPublisher = getAsyncClient().describeAlarmHistoryPaginator(historyRequest);
                CompletableFuture<Void> future = historyPublisher
                    .subscribe(response -> response.alarmHistoryItems().forEach(item -> {
                        logger.info("History summary: {}", item.historySummary());
                        logger.info("Timestamp: {}", item.timestamp());
                    }))
                    .whenComplete((result, exception) -> {
                        if (exception != null) {
                            logger.error("Error occurred while getting alarm history: " + exception.getMessage(), exception);
                        } else {
                            logger.info("Successfully retrieved all alarm history.");
                        }
                    });

                // Return the future to the calling code for further handling
                return future;
            } catch (Exception e) {
                throw new RuntimeException("Failed to process alarm history", e);
            }
        }).whenComplete((result, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Error completing alarm history processing", exception);
            }
        });
    }
```
+  For API details, see [DescribeAlarmHistory](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarmHistory) in *AWS SDK for Java 2.x API Reference*.

### `DescribeAlarms`
<a name="cloudwatch_DescribeAlarms_java_topic"></a>

The following code example shows how to use `DescribeAlarms`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Describes the CloudWatch alarms of the 'METRIC_ALARM' type.
     *
     * @return a {@link CompletableFuture} that represents the asynchronous operation
     * of describing the CloudWatch alarms. The future completes when the
     * operation is finished, either successfully or with an error.
     */
    public CompletableFuture<Void> describeAlarmsAsync() {
        List<AlarmType> typeList = new ArrayList<>();
        typeList.add(AlarmType.METRIC_ALARM);
        DescribeAlarmsRequest alarmsRequest = DescribeAlarmsRequest.builder()
            .alarmTypes(typeList)
            .maxRecords(10)
            .build();

        return getAsyncClient().describeAlarms(alarmsRequest)
            .thenAccept(response -> {
                List<MetricAlarm> alarmList = response.metricAlarms();
                for (MetricAlarm alarm : alarmList) {
                    logger.info("Alarm name: {}", alarm.alarmName());
                    logger.info("Alarm description: {} ", alarm.alarmDescription());
                }
            })
            .whenComplete((response, ex) -> {
                if (ex != null) {
                    logger.info("Failed to describe alarms: {}", ex.getMessage());
                } else {
                    logger.info("Successfully described alarms.");
                }
            });
    }
```
+  For API details, see [DescribeAlarms](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarms) in *AWS SDK for Java 2.x API Reference*.

### `DescribeAlarmsForMetric`
<a name="cloudwatch_DescribeAlarmsForMetric_java_topic"></a>

The following code example shows how to use `DescribeAlarmsForMetric`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Checks for a metric alarm in AWS CloudWatch.
     *
     * @param fileName the name of the file containing the JSON configuration for the custom metric
     * @return a {@link CompletableFuture} that completes when the check for the metric alarm is complete
     */
    public CompletableFuture<Void> checkForMetricAlarmAsync(String fileName) {
        CompletableFuture<String> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(parser);
                return rootNode.toString(); // Return JSON as a string for further processing
            } catch (IOException e) {
                throw new RuntimeException("Failed to read file", e);
            }
        });

        return readFileFuture.thenCompose(jsonContent -> {
            try {
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(jsonContent);
                String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
                String customMetricName = rootNode.findValue("customMetricName").asText();

                DescribeAlarmsForMetricRequest metricRequest = DescribeAlarmsForMetricRequest.builder()
                    .metricName(customMetricName)
                    .namespace(customMetricNamespace)
                    .build();

                return checkForAlarmAsync(metricRequest, customMetricName, 10);

            } catch (IOException e) {
                throw new RuntimeException("Failed to parse JSON content", e);
            }
        }).whenComplete((result, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Error checking metric alarm", exception);
            }
        });
    }

    // Recursive method to check for the alarm.

    /**
     * Checks for the existence of an alarm asynchronously for the specified metric.
     *
     * @param metricRequest    the request to describe the alarms for the specified metric
     * @param customMetricName the name of the custom metric to check for an alarm
     * @param retries          the number of retries to perform if no alarm is found
     * @return a {@link CompletableFuture} that completes when an alarm is found or the maximum number of retries has been reached
     */
    private static CompletableFuture<Void> checkForAlarmAsync(DescribeAlarmsForMetricRequest metricRequest, String customMetricName, int retries) {
        if (retries == 0) {
            return CompletableFuture.completedFuture(null).thenRun(() ->
                logger.info("No Alarm state found for {} after 10 retries.", customMetricName)
            );
        }

        return (getAsyncClient().describeAlarmsForMetric(metricRequest).thenCompose(response -> {
            if (response.hasMetricAlarms()) {
                logger.info("Alarm state found for {}", customMetricName);
                return CompletableFuture.completedFuture(null); // Alarm found, complete the future
            } else {
                return CompletableFuture.runAsync(() -> {
                    try {
                        Thread.sleep(20000);
                        logger.info(".");
                    } catch (InterruptedException e) {
                        throw new RuntimeException("Interrupted while waiting to retry", e);
                    }
                }).thenCompose(v -> checkForAlarmAsync(metricRequest, customMetricName, retries - 1)); // Recursive call
            }
        }));
    }
```
+  For API details, see [DescribeAlarmsForMetric](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarmsForMetric) in *AWS SDK for Java 2.x API Reference*.

### `DescribeAnomalyDetectors`
<a name="cloudwatch_DescribeAnomalyDetectors_java_topic"></a>

The following code example shows how to use `DescribeAnomalyDetectors`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Describes the anomaly detectors based on the specified JSON file.
     *
     * @param fileName the name of the JSON file containing the custom metric namespace and name
     * @return a {@link CompletableFuture} that completes when the anomaly detectors have been described
     * @throws RuntimeException if there is a failure during the operation, such as when reading or parsing the JSON file,
     *                          or when describing the anomaly detectors
     */
    public CompletableFuture<Void> describeAnomalyDetectorsAsync(String fileName) {
        CompletableFuture<JsonNode> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                return new ObjectMapper().readTree(parser);
            } catch (IOException e) {
                throw new RuntimeException("Failed to read or parse the file", e);
            }
        });

        return readFileFuture.thenCompose(rootNode -> {
            try {
                String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
                String customMetricName = rootNode.findValue("customMetricName").asText();

                DescribeAnomalyDetectorsRequest detectorsRequest = DescribeAnomalyDetectorsRequest.builder()
                    .maxResults(10)
                    .metricName(customMetricName)
                    .namespace(customMetricNamespace)
                    .build();

                return getAsyncClient().describeAnomalyDetectors(detectorsRequest).thenAccept(response -> {
                    List<AnomalyDetector> anomalyDetectorList = response.anomalyDetectors();
                    for (AnomalyDetector detector : anomalyDetectorList) {
                        logger.info("Metric name: {} ", detector.singleMetricAnomalyDetector().metricName());
                        logger.info("State: {} ", detector.stateValue());
                    }
                });
            } catch (RuntimeException e) {
                throw new RuntimeException("Failed to describe anomaly detectors", e);
            }
        }).whenComplete((result, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Error describing anomaly detectors", exception);
            }
        });
    }
```
+  For API details, see [DescribeAnomalyDetectors](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAnomalyDetectors) in *AWS SDK for Java 2.x API Reference*.

### `DisableAlarmActions`
<a name="cloudwatch_DisableAlarmActions_java_topic"></a>

The following code example shows how to use `DisableAlarmActions`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.cloudwatch.CloudWatchClient;
import software.amazon.awssdk.services.cloudwatch.model.CloudWatchException;
import software.amazon.awssdk.services.cloudwatch.model.DisableAlarmActionsRequest;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class DisableAlarmActions {
    public static void main(String[] args) {
        final String usage = """

                Usage:
                  <alarmName>

                Where:
                  alarmName - An alarm name to disable (for example, MyAlarm).
                """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String alarmName = args[0];
        Region region = Region.US_EAST_1;
        CloudWatchClient cw = CloudWatchClient.builder()
                .region(region)
                .build();

        disableActions(cw, alarmName);
        cw.close();
    }

    public static void disableActions(CloudWatchClient cw, String alarmName) {
        try {
            DisableAlarmActionsRequest request = DisableAlarmActionsRequest.builder()
                    .alarmNames(alarmName)
                    .build();

            cw.disableAlarmActions(request);
            System.out.printf("Successfully disabled actions on alarm %s", alarmName);

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}
```
+  For API details, see [DisableAlarmActions](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DisableAlarmActions) in *AWS SDK for Java 2.x API Reference*.

### `EnableAlarmActions`
<a name="cloudwatch_EnableAlarmActions_java_topic"></a>

The following code example shows how to use `EnableAlarmActions`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.cloudwatch.CloudWatchClient;
import software.amazon.awssdk.services.cloudwatch.model.CloudWatchException;
import software.amazon.awssdk.services.cloudwatch.model.EnableAlarmActionsRequest;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class EnableAlarmActions {
    public static void main(String[] args) {
        final String usage = """

                Usage:
                  <alarmName>

                Where:
                  alarmName - An alarm name to enable (for example, MyAlarm).
                """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String alarm = args[0];
        Region region = Region.US_EAST_1;
        CloudWatchClient cw = CloudWatchClient.builder()
                .region(region)
                .build();

        enableActions(cw, alarm);
        cw.close();
    }

    public static void enableActions(CloudWatchClient cw, String alarm) {
        try {
            EnableAlarmActionsRequest request = EnableAlarmActionsRequest.builder()
                    .alarmNames(alarm)
                    .build();

            cw.enableAlarmActions(request);
            System.out.printf("Successfully enabled actions on alarm %s", alarm);

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}
```
+  For API details, see [EnableAlarmActions](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/EnableAlarmActions) in *AWS SDK for Java 2.x API Reference*.

### `GetAlarmMuteRule`
<a name="cloudwatch_GetAlarmMuteRule_java_topic"></a>

The following code example shows how to use `GetAlarmMuteRule`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Gets the full configuration of an alarm mute rule, including its schedule, the
     * alarms it targets, and whether it is currently SCHEDULED, ACTIVE, or EXPIRED.
     *
     * @param cw   the CloudWatch client
     * @param name the name of the mute rule
     * @return the mute rule
     */
    public static GetAlarmMuteRuleResponse getAlarmMuteRule(CloudWatchClient cw, String name) {
        try {
            GetAlarmMuteRuleResponse response = cw.getAlarmMuteRule(GetAlarmMuteRuleRequest.builder()
                    .alarmMuteRuleName(name)
                    .build());

            System.out.printf("Mute rule %s is %s.%n", response.name(), response.statusAsString());
            return response;

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
            return null;
        }
    }
```
+  For API details, see [GetAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetAlarmMuteRule) in *AWS SDK for Java 2.x API Reference*.

### `GetMetricData`
<a name="cloudwatch_GetMetricData_java_topic"></a>

The following code example shows how to use `GetMetricData`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Retrieves custom metric data from the AWS CloudWatch service.
     *
     * @param fileName the name of the file containing the custom metric information
     * @return a {@link CompletableFuture} that completes when the metric data has been retrieved
     */
    public CompletableFuture<Void> getCustomMetricDataAsync(String fileName) {
        CompletableFuture<String> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                // Read values from the JSON file.
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(parser);
                return rootNode.toString(); // Return JSON as a string for further processing
            } catch (IOException e) {
                throw new RuntimeException("Failed to read file", e);
            }
        });

        return readFileFuture.thenCompose(jsonContent -> {
            try {
                // Parse the JSON string to extract relevant values.
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(jsonContent);
                String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
                String customMetricName = rootNode.findValue("customMetricName").asText();

                // Set the current time and date range for metric query.
                Instant nowDate = Instant.now();
                long hours = 1;
                long minutes = 30;
                Instant endTime = nowDate.plus(hours, ChronoUnit.HOURS).plus(minutes, ChronoUnit.MINUTES);

                Metric met = Metric.builder()
                    .metricName(customMetricName)
                    .namespace(customMetricNamespace)
                    .build();

                MetricStat metStat = MetricStat.builder()
                    .stat("Maximum")
                    .period(60)  // Assuming period in seconds
                    .metric(met)
                    .build();

                MetricDataQuery dataQuery = MetricDataQuery.builder()
                    .metricStat(metStat)
                    .id("foo2")
                    .returnData(true)
                    .build();

                List<MetricDataQuery> dq = new ArrayList<>();
                dq.add(dataQuery);

                GetMetricDataRequest getMetricDataRequest = GetMetricDataRequest.builder()
                    .maxDatapoints(10)
                    .scanBy(ScanBy.TIMESTAMP_DESCENDING)
                    .startTime(nowDate)
                    .endTime(endTime)
                    .metricDataQueries(dq)
                    .build();

                // Call the async method for CloudWatch data retrieval.
                return getAsyncClient().getMetricData(getMetricDataRequest);

            } catch (IOException e) {
                throw new RuntimeException("Failed to parse JSON content", e);
            }
        }).thenAccept(response -> {
            List<MetricDataResult> data = response.metricDataResults();
            for (MetricDataResult item : data) {
                logger.info("The label is: {}", item.label());
                logger.info("The status code is: {}", item.statusCode().toString());
            }
        }).exceptionally(exception -> {
            throw new RuntimeException("Failed to get metric data", exception);
        });
    }
```
+  For API details, see [GetMetricData](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetMetricData) in *AWS SDK for Java 2.x API Reference*.

### `GetMetricStatistics`
<a name="cloudwatch_GetMetricStatistics_java_topic"></a>

The following code example shows how to use `GetMetricStatistics`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Retrieves and displays metric statistics for the specified parameters.
     *
     * @param nameSpace    the namespace for the metric
     * @param metVal       the name of the metric
     * @param metricOption the statistic to retrieve for the metric (e.g., "Maximum", "Average")
     * @param date         the date for which to retrieve the metric statistics, in the format "yyyy-MM-dd'T'HH:mm:ss'Z'"
     * @param myDimension  the dimension(s) to filter the metric statistics by
     * @return a {@link CompletableFuture} that completes when the metric statistics have been retrieved and displayed
     */
    public CompletableFuture<GetMetricStatisticsResponse> getAndDisplayMetricStatisticsAsync(String nameSpace, String metVal,
                                                                                             String metricOption, String date, Dimension myDimension) {

        Instant start = Instant.parse(date);
        Instant endDate = Instant.now();

        // Building the request for metric statistics.
        GetMetricStatisticsRequest statisticsRequest = GetMetricStatisticsRequest.builder()
            .endTime(endDate)
            .startTime(start)
            .dimensions(myDimension)
            .metricName(metVal)
            .namespace(nameSpace)
            .period(86400) // 1 day period
            .statistics(Statistic.fromValue(metricOption))
            .build();

        return getAsyncClient().getMetricStatistics(statisticsRequest)
            .whenComplete((response, exception) -> {
                if (response != null) {
                    List<Datapoint> data = response.datapoints();
                    if (!data.isEmpty()) {
                        for (Datapoint datapoint : data) {
                            logger.info("Timestamp: {} Maximum value: {}", datapoint.timestamp(), datapoint.maximum());
                        }
                    } else {
                        logger.info("The returned data list is empty");
                    }
                } else {
                    logger.info("Failed to get metric statistics: {} ", exception.getMessage());
                }
            })
            .exceptionally(exception -> {
                throw new RuntimeException("Error while getting metric statistics: " + exception.getMessage(), exception);
            });
    }
```
+  For API details, see [GetMetricStatistics](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetMetricStatistics) in *AWS SDK for Java 2.x API Reference*.

### `GetMetricWidgetImage`
<a name="cloudwatch_GetMetricWidgetImage_java_topic"></a>

The following code example shows how to use `GetMetricWidgetImage`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Retrieves and saves a custom metric image to a file.
     *
     * @param fileName the name of the file to save the metric image to
     * @return a {@link CompletableFuture} that completes when the image has been saved to the file
     */
    public CompletableFuture<Void> downloadAndSaveMetricImageAsync(String fileName) {
        logger.info("Getting Image data for custom metric.");
        String myJSON = """
              {
                  "title": "Example Metric Graph",
                  "view": "timeSeries",
                  "stacked ": false,
                  "period": 10,
                  "width": 1400,
                  "height": 600,
                  "metrics": [
                      [
                      "AWS/Billing",
                      "EstimatedCharges",
                      "Currency",
                      "USD"
                     ]
                  ]
              }
            """;

        GetMetricWidgetImageRequest imageRequest = GetMetricWidgetImageRequest.builder()
            .metricWidget(myJSON)
            .build();

        return getAsyncClient().getMetricWidgetImage(imageRequest)
            .thenCompose(response -> {
                SdkBytes sdkBytes = response.metricWidgetImage();
                byte[] bytes = sdkBytes.asByteArray();
                return CompletableFuture.runAsync(() -> {
                    try {
                        File outputFile = new File(fileName);
                        try (FileOutputStream outputStream = new FileOutputStream(outputFile)) {
                            outputStream.write(bytes);
                        }
                    } catch (IOException e) {
                        throw new RuntimeException("Failed to write image to file", e);
                    }
                });
            })
            .whenComplete((result, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Error getting and saving metric image", exception);
                } else {
                    logger.info("Image data saved successfully to {}", fileName);
                }
            });
    }
```
+  For API details, see [GetMetricWidgetImage](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetMetricWidgetImage) in *AWS SDK for Java 2.x API Reference*.

### `GetOTelEnrichment`
<a name="cloudwatch_GetOTelEnrichment_java_topic"></a>

The following code example shows how to use `GetOTelEnrichment`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Gets the current OTel enrichment status for the account.
     *
     * @param cw the CloudWatch client
     * @return the status, either {@code Running} or {@code Stopped}
     */
    public static String getOTelEnrichmentStatus(CloudWatchClient cw) {
        try {
            String status = cw.getOTelEnrichment(GetOTelEnrichmentRequest.builder().build())
                    .statusAsString();
            System.out.printf("OTel enrichment status is %s.%n", status);
            return status;

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
            return null;
        }
    }
```
+  For API details, see [GetOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetOTelEnrichment) in *AWS SDK for Java 2.x API Reference*.

### `ListAlarmMuteRules`
<a name="cloudwatch_ListAlarmMuteRules_java_topic"></a>

The following code example shows how to use `ListAlarmMuteRules`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Lists the alarm mute rules in the account, optionally filtered to the rules that
     * target one alarm.
     *
     * @param cw        the CloudWatch client
     * @param alarmName when non-null, only rules that target this alarm are returned
     * @return the list of mute rule summaries
     */
    public static List<AlarmMuteRuleSummary> listAlarmMuteRules(CloudWatchClient cw, String alarmName) {
        List<AlarmMuteRuleSummary> summaries = new ArrayList<>();
        try {
            String nextToken = null;
            do {
                ListAlarmMuteRulesRequest request = ListAlarmMuteRulesRequest.builder()
                        .alarmName(alarmName)
                        .nextToken(nextToken)
                        .build();

                ListAlarmMuteRulesResponse response = cw.listAlarmMuteRules(request);
                summaries.addAll(response.alarmMuteRuleSummaries());
                nextToken = response.nextToken();
            } while (nextToken != null && !nextToken.isEmpty());

            for (AlarmMuteRuleSummary summary : summaries) {
                System.out.printf("%s (%s)%n", summary.alarmMuteRuleArn(), summary.statusAsString());
            }
            return summaries;

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
            return summaries;
        }
    }
```
+  For API details, see [ListAlarmMuteRules](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListAlarmMuteRules) in *AWS SDK for Java 2.x API Reference*.

### `ListDashboards`
<a name="cloudwatch_ListDashboards_java_topic"></a>

The following code example shows how to use `ListDashboards`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Lists the available dashboards.
     *
     * @return a {@link CompletableFuture} that completes when the operation is finished.
     * The future will complete exceptionally if an error occurs while listing the dashboards.
     */
    public CompletableFuture<Void> listDashboardsAsync() {
        ListDashboardsRequest listDashboardsRequest = ListDashboardsRequest.builder().build();
        ListDashboardsPublisher paginator = getAsyncClient().listDashboardsPaginator(listDashboardsRequest);
        return paginator.subscribe(response -> {
            response.dashboardEntries().forEach(entry -> {
                logger.info("Dashboard name is: {} ", entry.dashboardName());
                logger.info("Dashboard ARN is: {} ", entry.dashboardArn());
            });
        }).exceptionally(ex -> {
            logger.info("Failed to list dashboards: {} ", ex.getMessage());
            throw new RuntimeException("Error occurred while listing dashboards", ex);
        });
    }
```
+  For API details, see [ListDashboards](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListDashboards) in *AWS SDK for Java 2.x API Reference*.

### `ListMetrics`
<a name="cloudwatch_ListMetrics_java_topic"></a>

The following code example shows how to use `ListMetrics`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Retrieves a list of metric names for the specified namespace.
     *
     * @param namespace the namespace for which to retrieve the metric names
     * @return a {@link CompletableFuture} that, when completed, contains an {@link ArrayList} of
     * the metric names in the specified namespace
     * @throws RuntimeException if an error occurs while listing the metrics
     */
    public CompletableFuture<ArrayList<String>> listMetsAsync(String namespace) {
        ListMetricsRequest request = ListMetricsRequest.builder()
            .namespace(namespace)
            .build();

        ListMetricsPublisher metricsPaginator = getAsyncClient().listMetricsPaginator(request);
        Set<String> metSet = new HashSet<>();
        CompletableFuture<Void> future = metricsPaginator.subscribe(response -> {
            response.metrics().forEach(metric -> {
                String metricName = metric.metricName();
                metSet.add(metricName);
            });
        });

        return future
            .thenApply(ignored -> new ArrayList<>(metSet))
            .exceptionally(exception -> {
                throw new RuntimeException("Failed to list metrics: " + exception.getMessage(), exception);
            });
    }
```
+  For API details, see [ListMetrics](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListMetrics) in *AWS SDK for Java 2.x API Reference*.

### `PutAlarmMuteRule`
<a name="cloudwatch_PutAlarmMuteRule_java_topic"></a>

The following code example shows how to use `PutAlarmMuteRule`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Creates or updates an alarm mute rule. While a mute rule is active the targeted
     * alarms keep evaluating and keep transitioning between states, but their configured
     * actions do not fire. This is the supported way to suppress notifications during a
     * known maintenance window instead of disabling alarm actions and hoping someone
     * remembers to turn them back on.
     *
     * @param cw         the CloudWatch client
     * @param name       the name of the mute rule
     * @param expression when the rule activates. For a recurring window, use a
     *                   five-field cron expression,
     *                   {@code cron(Minutes Hours Day-of-month Month Day-of-week)},
     *                   such as {@code cron(0 2 * * SUN)} for every Sunday at 2:00 AM.
     *                   Note that this is five fields, not the six that Amazon
     *                   EventBridge uses. For a one-time window, use
     *                   {@code at(yyyy-MM-ddThh:mm)}, such as
     *                   {@code at(2026-09-05T02:00)}.
     * @param duration   how long the mute window lasts once it activates, in ISO 8601
     *                   duration format, from {@code PT1M} (one minute) to
     *                   {@code P15D} (15 days). For example, {@code PT2H} is two hours
     *                   and {@code P2DT12H} is two days and 12 hours.
     * @param timezone   the time zone the expression is evaluated in, such as
     *                   {@code America/Los_Angeles}
     * @param alarmNames the names of up to 100 alarms to mute. If empty, the rule
     *                   applies to all alarms in the account.
     */
    public static void putAlarmMuteRule(CloudWatchClient cw, String name, String expression, String duration,
            String timezone, List<String> alarmNames) {
        try {
            Schedule schedule = Schedule.builder()
                    .expression(expression)
                    .duration(duration)
                    .timezone(timezone)
                    .build();

            PutAlarmMuteRuleRequest.Builder request = PutAlarmMuteRuleRequest.builder()
                    .name(name)
                    .description("Mute rule created by the AWS SDK for Java 2.x example.")
                    .rule(Rule.builder().schedule(schedule).build());

            if (alarmNames != null && !alarmNames.isEmpty()) {
                request.muteTargets(MuteTargets.builder().alarmNames(alarmNames).build());
            }

            cw.putAlarmMuteRule(request.build());
            System.out.printf("Put alarm mute rule %s.%n", name);

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutAlarmMuteRule) in *AWS SDK for Java 2.x API Reference*.

### `PutAnomalyDetector`
<a name="cloudwatch_PutAnomalyDetector_java_topic"></a>

The following code example shows how to use `PutAnomalyDetector`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Adds an anomaly detector for the given file.
     *
     * @param fileName the name of the file containing the anomaly detector configuration
     * @return a {@link CompletableFuture} that completes when the anomaly detector has been added
     */
    public CompletableFuture<Void> addAnomalyDetectorAsync(String fileName) {
        CompletableFuture<JsonNode> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                return new ObjectMapper().readTree(parser); // Return the root node
            } catch (IOException e) {
                throw new RuntimeException("Failed to read or parse the file", e);
            }
        });

        return readFileFuture.thenCompose(rootNode -> {
            try {
                String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
                String customMetricName = rootNode.findValue("customMetricName").asText();

                SingleMetricAnomalyDetector singleMetricAnomalyDetector = SingleMetricAnomalyDetector.builder()
                    .metricName(customMetricName)
                    .namespace(customMetricNamespace)
                    .stat("Maximum")
                    .build();

                PutAnomalyDetectorRequest anomalyDetectorRequest = PutAnomalyDetectorRequest.builder()
                    .singleMetricAnomalyDetector(singleMetricAnomalyDetector)
                    .build();

                return getAsyncClient().putAnomalyDetector(anomalyDetectorRequest).thenAccept(response -> {
                    logger.info("Added anomaly detector for metric {}", customMetricName);
                });
            } catch (Exception e) {
                throw new RuntimeException("Failed to create anomaly detector", e);
            }
        }).whenComplete((result, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Error adding anomaly detector", exception);
            }
        });
    }
```
+  For API details, see [PutAnomalyDetector](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutAnomalyDetector) in *AWS SDK for Java 2.x API Reference*.

### `PutDashboard`
<a name="cloudwatch_PutDashboard_java_topic"></a>

The following code example shows how to use `PutDashboard`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Creates a new dashboard with the specified name and body.
     *
     * @param dashboardName the name of the dashboard to be created
     * @param dashboardBody the dashboard body, as JSON
     * @return a {@link CompletableFuture} representing the asynchronous operation of creating the dashboard
     */
    public CompletableFuture<PutDashboardResponse> createDashboardAsync(String dashboardName, String dashboardBody) {
        PutDashboardRequest dashboardRequest = PutDashboardRequest.builder()
            .dashboardName(dashboardName)
            .dashboardBody(dashboardBody)
            .build();

        return getAsyncClient().putDashboard(dashboardRequest)
            .handle((response, ex) -> {
                if (ex != null) {
                    logger.info("Failed to create dashboard: {}", ex.getMessage());
                    throw new RuntimeException("Dashboard creation failed", ex);
                } else {
                    // Handle the normal response case
                    logger.info("{} was successfully created.", dashboardName);
                    List<DashboardValidationMessage> messages = response.dashboardValidationMessages();
                    if (messages.isEmpty()) {
                        logger.info("There are no messages in the new Dashboard.");
                    } else {
                        for (DashboardValidationMessage message : messages) {
                            logger.info("Message: {}", message.message());
                        }
                    }
                    return response; // Return the response for further use
                }
            });
    }
```
+  For API details, see [PutDashboard](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutDashboard) in *AWS SDK for Java 2.x API Reference*.

### `PutMetricAlarm`
<a name="cloudwatch_PutMetricAlarm_java_topic"></a>

The following code example shows how to use `PutMetricAlarm`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).
Create an alarm that evaluates a PromQL query against OpenTelemetry metrics.

```
    /**
     * Creates an alarm that evaluates a PromQL query.
     *
     * <p>A PromQL alarm differs from a classic metric alarm in a few ways. The query
     * can match many series at once, and each matching series is tracked separately as
     * a contributor. Instead of counting breaching periods, you specify durations: a
     * contributor moves to ALARM after it breaches continuously for the pending period,
     * and back to OK after it stops breaching for the recovery period. A PromQL alarm
     * starts in the OK state rather than INSUFFICIENT_DATA.
     *
     * <p>{@link EvaluationCriteria} is a union and is mutually exclusive with the
     * classic {@code metricName} and {@code metrics} parameters. When you use it you
     * must also set {@code evaluationInterval}, and you must not set {@code period},
     * {@code statistic}, {@code threshold}, {@code comparisonOperator},
     * {@code evaluationPeriods}, {@code datapointsToAlarm}, or
     * {@code treatMissingData}.
     *
     * @param cw                 the CloudWatch client
     * @param alarmName          the name of the alarm, unique within the Region
     * @param query              the PromQL query to evaluate, such as
     *                           {@code avg(cpu_utilization_percent) > 80}. The
     *                           comparison belongs in the query itself; there is no
     *                           separate threshold parameter.
     * @param evaluationInterval how often, in seconds, to run the query. Valid values
     *                           are 10, 20, 30, and any multiple of 60, up to 3600.
     * @param pendingPeriod      how long, in seconds, a contributor must breach
     *                           continuously before it moves to ALARM
     * @param recoveryPeriod     how long, in seconds, a contributor must stop breaching
     *                           before it moves back to OK
     */
    public static void putPromQLMetricAlarm(CloudWatchClient cw, String alarmName, String query,
            int evaluationInterval, int pendingPeriod, int recoveryPeriod) {
        try {
            AlarmPromQLCriteria promQLCriteria = AlarmPromQLCriteria.builder()
                    .query(query)
                    .pendingPeriod(pendingPeriod)
                    .recoveryPeriod(recoveryPeriod)
                    .build();

            PutMetricAlarmRequest request = PutMetricAlarmRequest.builder()
                    .alarmName(alarmName)
                    .alarmDescription("PromQL alarm created by the AWS SDK for Java 2.x example.")
                    .evaluationCriteria(EvaluationCriteria.builder()
                            .promQLCriteria(promQLCriteria)
                            .build())
                    .evaluationInterval(evaluationInterval)
                    .build();

            cw.putMetricAlarm(request);
            System.out.printf("Created PromQL alarm %s for query %s.%n", alarmName, query);

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
Create an alarm that evaluates a single CloudWatch metric.

```
    /**
     * Creates an alarm based on the configuration provided in a JSON file.
     *
     * @param fileName the name of the JSON file containing the alarm configuration
     * @return a CompletableFuture that represents the asynchronous operation of creating the alarm
     * @throws RuntimeException if an exception occurs while reading the JSON file or creating the alarm
     */
    public CompletableFuture<String> createAlarmAsync(String fileName) {
        com.fasterxml.jackson.databind.JsonNode rootNode;
        try {
            JsonParser parser = new JsonFactory().createParser(new File(fileName));
            rootNode = new ObjectMapper().readTree(parser);
        } catch (IOException e) {
            throw new RuntimeException("Failed to read the alarm configuration file", e);
        }

        // Extract values from the JSON node.
        String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
        String customMetricName = rootNode.findValue("customMetricName").asText();
        String alarmName = rootNode.findValue("exampleAlarmName").asText();
        String emailTopic = rootNode.findValue("emailTopic").asText();
        String accountId = rootNode.findValue("accountId").asText();
        String region = rootNode.findValue("region").asText();

        // Create a List for alarm actions.
        List<String> alarmActions = new ArrayList<>();
        alarmActions.add("arn:aws:sns:" + region + ":" + accountId + ":" + emailTopic);

        PutMetricAlarmRequest alarmRequest = PutMetricAlarmRequest.builder()
            .alarmActions(alarmActions)
            .alarmDescription("Example metric alarm")
            .alarmName(alarmName)
            .comparisonOperator(ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD)
            .threshold(100.00)
            .metricName(customMetricName)
            .namespace(customMetricNamespace)
            .evaluationPeriods(1)
            .period(10)
            .statistic("Maximum")
            .datapointsToAlarm(1)
            .treatMissingData("ignore")
            .build();

        // Call the putMetricAlarm asynchronously and handle the result.
        return getAsyncClient().putMetricAlarm(alarmRequest)
            .handle((response, ex) -> {
                if (ex != null) {
                    logger.info("Failed to create alarm: {}", ex.getMessage());
                    throw new RuntimeException("Failed to create alarm", ex);
                } else {
                    logger.info("{} was successfully created!", alarmName);
                    return alarmName;
                }
            });
    }
```
+  For API details, see [PutMetricAlarm](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutMetricAlarm) in *AWS SDK for Java 2.x API Reference*.

### `PutMetricData`
<a name="cloudwatch_PutMetricData_java_topic"></a>

The following code example shows how to use `PutMetricData`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Adds metric data for an alarm asynchronously.
     *
     * @param fileName the name of the JSON file containing the metric data
     * @return a CompletableFuture that asynchronously returns the PutMetricDataResponse
     */
    public CompletableFuture<PutMetricDataResponse> addMetricDataForAlarmAsync(String fileName) {
        CompletableFuture<String> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(parser);
                return rootNode.toString(); // Return JSON as a string for further processing
            } catch (IOException e) {
                throw new RuntimeException("Failed to read file", e);
            }
        });

        return readFileFuture.thenCompose(jsonContent -> {
            try {
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(jsonContent);
                String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
                String customMetricName = rootNode.findValue("customMetricName").asText();
                Instant instant = Instant.now();

                // Create MetricDatum objects.
                MetricDatum datum1 = MetricDatum.builder()
                    .metricName(customMetricName)
                    .unit(StandardUnit.NONE)
                    .value(1001.00)
                    .timestamp(instant)
                    .build();

                MetricDatum datum2 = MetricDatum.builder()
                    .metricName(customMetricName)
                    .unit(StandardUnit.NONE)
                    .value(1002.00)
                    .timestamp(instant)
                    .build();

                List<MetricDatum> metricDataList = new ArrayList<>();
                metricDataList.add(datum1);
                metricDataList.add(datum2);

                // Build the PutMetricData request.
                PutMetricDataRequest request = PutMetricDataRequest.builder()
                    .namespace(customMetricNamespace)
                    .metricData(metricDataList)
                    .build();

                // Send the request asynchronously.
                return getAsyncClient().putMetricData(request);

            } catch (IOException e) {
                CompletableFuture<PutMetricDataResponse> failedFuture = new CompletableFuture<>();
                failedFuture.completeExceptionally(new RuntimeException("Failed to parse JSON content", e));
                return failedFuture;
            }
        }).whenComplete((response, exception) -> {
            if (exception != null) {
                logger.error("Failed to put metric data: " + exception.getMessage(), exception);
            } else {
                logger.info("Added metric values for metric.");
            }
        });
    }
```
+  For API details, see [PutMetricData](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutMetricData) in *AWS SDK for Java 2.x API Reference*.

### `StartOTelEnrichment`
<a name="cloudwatch_StartOTelEnrichment_java_topic"></a>

The following code example shows how to use `StartOTelEnrichment`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Turns on OTel enrichment for the account. Once enrichment is running, CloudWatch
     * vended metrics that carry a resource identifier dimension, such as the EC2
     * CPUUtilization metric with its InstanceId dimension, are decorated with resource
     * ARN and resource tag labels and become queryable with PromQL.
     *
     * <p>Resource tags on telemetry must already be enabled for the account before you
     * call this operation.
     *
     * @param cw the CloudWatch client
     */
    public static void startOTelEnrichment(CloudWatchClient cw) {
        try {
            cw.startOTelEnrichment(StartOTelEnrichmentRequest.builder().build());
            System.out.println("Started OTel enrichment for this account.");

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [StartOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/StartOTelEnrichment) in *AWS SDK for Java 2.x API Reference*.

### `StopOTelEnrichment`
<a name="cloudwatch_StopOTelEnrichment_java_topic"></a>

The following code example shows how to use `StopOTelEnrichment`.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).

```
    /**
     * Turns off OTel enrichment for the account. Existing PromQL alarms are not
     * deleted, but vended metrics stop being enriched with resource ARN and tag labels,
     * so queries that select on those labels stop matching.
     *
     * @param cw the CloudWatch client
     */
    public static void stopOTelEnrichment(CloudWatchClient cw) {
        try {
            cw.stopOTelEnrichment(StopOTelEnrichmentRequest.builder().build());
            System.out.println("Stopped OTel enrichment for this account.");

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [StopOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/StopOTelEnrichment) in *AWS SDK for Java 2.x API Reference*.

## Scenarios
<a name="scenarios"></a>

### Monitor DynamoDB performance
<a name="cross_MonitorDynamoDB_java_topic"></a>

The following code example shows how to configure an application's use of DynamoDB to monitor performance.

**SDK for Java 2.x**
 This example shows how to configure a Java application to monitor the performance of DynamoDB. The application sends metric data to CloudWatch where you can monitor the performance.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/usecases/monitor_dynamodb).

**Services used in this example**
+ CloudWatch
+ DynamoDB

### Send OpenTelemetry metrics and alarm on them with PromQL
<a name="cloudwatch_Scenario_OTelMetrics_java_topic"></a>

The following code example shows how to:
+ Send OTLP metrics to the CloudWatch metrics endpoint with an OpenTelemetry Collector.
+ Start OpenTelemetry enrichment so CloudWatch correlates those metrics with your resources.
+ Create an alarm that evaluates a PromQL query across every series the query returns.
+ Inspect the individual series, called contributors, that put the alarm in ALARM state.
+ Mute the alarm for a maintenance window, then clean up.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples).
A wrapper class for the CloudWatch OpenTelemetry SDK methods.

```
import software.amazon.awssdk.services.cloudwatch.CloudWatchClient;
import software.amazon.awssdk.services.cloudwatch.model.AlarmContributor;
import software.amazon.awssdk.services.cloudwatch.model.AlarmMuteRuleSummary;
import software.amazon.awssdk.services.cloudwatch.model.AlarmPromQLCriteria;
import software.amazon.awssdk.services.cloudwatch.model.CloudWatchException;
import software.amazon.awssdk.services.cloudwatch.model.DeleteAlarmMuteRuleRequest;
import software.amazon.awssdk.services.cloudwatch.model.DescribeAlarmContributorsRequest;
import software.amazon.awssdk.services.cloudwatch.model.DescribeAlarmContributorsResponse;
import software.amazon.awssdk.services.cloudwatch.model.EvaluationCriteria;
import software.amazon.awssdk.services.cloudwatch.model.GetAlarmMuteRuleRequest;
import software.amazon.awssdk.services.cloudwatch.model.GetAlarmMuteRuleResponse;
import software.amazon.awssdk.services.cloudwatch.model.GetOTelEnrichmentRequest;
import software.amazon.awssdk.services.cloudwatch.model.ListAlarmMuteRulesRequest;
import software.amazon.awssdk.services.cloudwatch.model.ListAlarmMuteRulesResponse;
import software.amazon.awssdk.services.cloudwatch.model.MuteTargets;
import software.amazon.awssdk.services.cloudwatch.model.PutAlarmMuteRuleRequest;
import software.amazon.awssdk.services.cloudwatch.model.PutMetricAlarmRequest;
import software.amazon.awssdk.services.cloudwatch.model.Rule;
import software.amazon.awssdk.services.cloudwatch.model.Schedule;
import software.amazon.awssdk.services.cloudwatch.model.StartOTelEnrichmentRequest;
import software.amazon.awssdk.services.cloudwatch.model.StopOTelEnrichmentRequest;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class CloudWatchOTelActions {

    /**
     * Turns on OTel enrichment for the account. Once enrichment is running, CloudWatch
     * vended metrics that carry a resource identifier dimension, such as the EC2
     * CPUUtilization metric with its InstanceId dimension, are decorated with resource
     * ARN and resource tag labels and become queryable with PromQL.
     *
     * <p>Resource tags on telemetry must already be enabled for the account before you
     * call this operation.
     *
     * @param cw the CloudWatch client
     */
    public static void startOTelEnrichment(CloudWatchClient cw) {
        try {
            cw.startOTelEnrichment(StartOTelEnrichmentRequest.builder().build());
            System.out.println("Started OTel enrichment for this account.");

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }

    /**
     * Gets the current OTel enrichment status for the account.
     *
     * @param cw the CloudWatch client
     * @return the status, either {@code Running} or {@code Stopped}
     */
    public static String getOTelEnrichmentStatus(CloudWatchClient cw) {
        try {
            String status = cw.getOTelEnrichment(GetOTelEnrichmentRequest.builder().build())
                    .statusAsString();
            System.out.printf("OTel enrichment status is %s.%n", status);
            return status;

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
            return null;
        }
    }

    /**
     * Turns off OTel enrichment for the account. Existing PromQL alarms are not
     * deleted, but vended metrics stop being enriched with resource ARN and tag labels,
     * so queries that select on those labels stop matching.
     *
     * @param cw the CloudWatch client
     */
    public static void stopOTelEnrichment(CloudWatchClient cw) {
        try {
            cw.stopOTelEnrichment(StopOTelEnrichmentRequest.builder().build());
            System.out.println("Stopped OTel enrichment for this account.");

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }

    /**
     * Creates an alarm that evaluates a PromQL query.
     *
     * <p>A PromQL alarm differs from a classic metric alarm in a few ways. The query
     * can match many series at once, and each matching series is tracked separately as
     * a contributor. Instead of counting breaching periods, you specify durations: a
     * contributor moves to ALARM after it breaches continuously for the pending period,
     * and back to OK after it stops breaching for the recovery period. A PromQL alarm
     * starts in the OK state rather than INSUFFICIENT_DATA.
     *
     * <p>{@link EvaluationCriteria} is a union and is mutually exclusive with the
     * classic {@code metricName} and {@code metrics} parameters. When you use it you
     * must also set {@code evaluationInterval}, and you must not set {@code period},
     * {@code statistic}, {@code threshold}, {@code comparisonOperator},
     * {@code evaluationPeriods}, {@code datapointsToAlarm}, or
     * {@code treatMissingData}.
     *
     * @param cw                 the CloudWatch client
     * @param alarmName          the name of the alarm, unique within the Region
     * @param query              the PromQL query to evaluate, such as
     *                           {@code avg(cpu_utilization_percent) > 80}. The
     *                           comparison belongs in the query itself; there is no
     *                           separate threshold parameter.
     * @param evaluationInterval how often, in seconds, to run the query. Valid values
     *                           are 10, 20, 30, and any multiple of 60, up to 3600.
     * @param pendingPeriod      how long, in seconds, a contributor must breach
     *                           continuously before it moves to ALARM
     * @param recoveryPeriod     how long, in seconds, a contributor must stop breaching
     *                           before it moves back to OK
     */
    public static void putPromQLMetricAlarm(CloudWatchClient cw, String alarmName, String query,
            int evaluationInterval, int pendingPeriod, int recoveryPeriod) {
        try {
            AlarmPromQLCriteria promQLCriteria = AlarmPromQLCriteria.builder()
                    .query(query)
                    .pendingPeriod(pendingPeriod)
                    .recoveryPeriod(recoveryPeriod)
                    .build();

            PutMetricAlarmRequest request = PutMetricAlarmRequest.builder()
                    .alarmName(alarmName)
                    .alarmDescription("PromQL alarm created by the AWS SDK for Java 2.x example.")
                    .evaluationCriteria(EvaluationCriteria.builder()
                            .promQLCriteria(promQLCriteria)
                            .build())
                    .evaluationInterval(evaluationInterval)
                    .build();

            cw.putMetricAlarm(request);
            System.out.printf("Created PromQL alarm %s for query %s.%n", alarmName, query);

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }

    /**
     * Gets the contributors for a PromQL alarm. Each contributor is one series that the
     * alarm's query matched, identified by its label set. This is how you find out which
     * hosts, services, or pods are breaching, rather than only that something is.
     *
     * @param cw        the CloudWatch client
     * @param alarmName the name of the PromQL alarm
     * @return the list of contributors
     */
    public static List<AlarmContributor> describeAlarmContributors(CloudWatchClient cw, String alarmName) {
        List<AlarmContributor> contributors = new ArrayList<>();
        try {
            String nextToken = null;
            do {
                DescribeAlarmContributorsRequest request = DescribeAlarmContributorsRequest.builder()
                        .alarmName(alarmName)
                        .nextToken(nextToken)
                        .build();

                DescribeAlarmContributorsResponse response = cw.describeAlarmContributors(request);
                contributors.addAll(response.alarmContributors());
                nextToken = response.nextToken();
            } while (nextToken != null && !nextToken.isEmpty());

            for (AlarmContributor contributor : contributors) {
                StringBuilder labels = new StringBuilder();
                for (Map.Entry<String, String> attribute : contributor.contributorAttributes().entrySet()) {
                    if (labels.length() > 0) {
                        labels.append(", ");
                    }
                    labels.append(attribute.getKey()).append("=").append(attribute.getValue());
                }
                System.out.printf("%s: %s%n", contributor.contributorId(), labels);
                System.out.printf("  reason: %s%n", contributor.stateReason());
            }
            return contributors;

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
            return contributors;
        }
    }

    /**
     * Creates or updates an alarm mute rule. While a mute rule is active the targeted
     * alarms keep evaluating and keep transitioning between states, but their configured
     * actions do not fire. This is the supported way to suppress notifications during a
     * known maintenance window instead of disabling alarm actions and hoping someone
     * remembers to turn them back on.
     *
     * @param cw         the CloudWatch client
     * @param name       the name of the mute rule
     * @param expression when the rule activates. For a recurring window, use a
     *                   five-field cron expression,
     *                   {@code cron(Minutes Hours Day-of-month Month Day-of-week)},
     *                   such as {@code cron(0 2 * * SUN)} for every Sunday at 2:00 AM.
     *                   Note that this is five fields, not the six that Amazon
     *                   EventBridge uses. For a one-time window, use
     *                   {@code at(yyyy-MM-ddThh:mm)}, such as
     *                   {@code at(2026-09-05T02:00)}.
     * @param duration   how long the mute window lasts once it activates, in ISO 8601
     *                   duration format, from {@code PT1M} (one minute) to
     *                   {@code P15D} (15 days). For example, {@code PT2H} is two hours
     *                   and {@code P2DT12H} is two days and 12 hours.
     * @param timezone   the time zone the expression is evaluated in, such as
     *                   {@code America/Los_Angeles}
     * @param alarmNames the names of up to 100 alarms to mute. If empty, the rule
     *                   applies to all alarms in the account.
     */
    public static void putAlarmMuteRule(CloudWatchClient cw, String name, String expression, String duration,
            String timezone, List<String> alarmNames) {
        try {
            Schedule schedule = Schedule.builder()
                    .expression(expression)
                    .duration(duration)
                    .timezone(timezone)
                    .build();

            PutAlarmMuteRuleRequest.Builder request = PutAlarmMuteRuleRequest.builder()
                    .name(name)
                    .description("Mute rule created by the AWS SDK for Java 2.x example.")
                    .rule(Rule.builder().schedule(schedule).build());

            if (alarmNames != null && !alarmNames.isEmpty()) {
                request.muteTargets(MuteTargets.builder().alarmNames(alarmNames).build());
            }

            cw.putAlarmMuteRule(request.build());
            System.out.printf("Put alarm mute rule %s.%n", name);

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }

    /**
     * Gets the full configuration of an alarm mute rule, including its schedule, the
     * alarms it targets, and whether it is currently SCHEDULED, ACTIVE, or EXPIRED.
     *
     * @param cw   the CloudWatch client
     * @param name the name of the mute rule
     * @return the mute rule
     */
    public static GetAlarmMuteRuleResponse getAlarmMuteRule(CloudWatchClient cw, String name) {
        try {
            GetAlarmMuteRuleResponse response = cw.getAlarmMuteRule(GetAlarmMuteRuleRequest.builder()
                    .alarmMuteRuleName(name)
                    .build());

            System.out.printf("Mute rule %s is %s.%n", response.name(), response.statusAsString());
            return response;

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
            return null;
        }
    }

    /**
     * Lists the alarm mute rules in the account, optionally filtered to the rules that
     * target one alarm.
     *
     * @param cw        the CloudWatch client
     * @param alarmName when non-null, only rules that target this alarm are returned
     * @return the list of mute rule summaries
     */
    public static List<AlarmMuteRuleSummary> listAlarmMuteRules(CloudWatchClient cw, String alarmName) {
        List<AlarmMuteRuleSummary> summaries = new ArrayList<>();
        try {
            String nextToken = null;
            do {
                ListAlarmMuteRulesRequest request = ListAlarmMuteRulesRequest.builder()
                        .alarmName(alarmName)
                        .nextToken(nextToken)
                        .build();

                ListAlarmMuteRulesResponse response = cw.listAlarmMuteRules(request);
                summaries.addAll(response.alarmMuteRuleSummaries());
                nextToken = response.nextToken();
            } while (nextToken != null && !nextToken.isEmpty());

            for (AlarmMuteRuleSummary summary : summaries) {
                System.out.printf("%s (%s)%n", summary.alarmMuteRuleArn(), summary.statusAsString());
            }
            return summaries;

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
            return summaries;
        }
    }

    /**
     * Deletes an alarm mute rule. The alarms it targeted resume firing their actions.
     *
     * @param cw   the CloudWatch client
     * @param name the name of the mute rule
     */
    public static void deleteAlarmMuteRule(CloudWatchClient cw, String name) {
        try {
            cw.deleteAlarmMuteRule(DeleteAlarmMuteRuleRequest.builder()
                    .alarmMuteRuleName(name)
                    .build());

            System.out.printf("Deleted alarm mute rule %s.%n", name);

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}
```
+ For API details, see the following topics in *AWS SDK for Java 2.x API Reference*.
  + [DeleteAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAlarmMuteRule)
  + [DeleteAlarms](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAlarms)
  + [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarmContributors)
  + [GetAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetAlarmMuteRule)
  + [GetOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetOTelEnrichment)
  + [ListAlarmMuteRules](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListAlarmMuteRules)
  + [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutAlarmMuteRule)
  + [PutMetricAlarm](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutMetricAlarm)
  + [StartOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/StartOTelEnrichment)
  + [StopOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/StopOTelEnrichment)
