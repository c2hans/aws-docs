---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_cloudwatch_code_examples.html
---

# CloudWatch examples using SDK for Kotlin
<a name="kotlin_cloudwatch_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Kotlin with CloudWatch.

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Get started](#get_started)
+ [Basics](#basics)
+ [Actions](#actions)

## Get started
<a name="get_started"></a>

### Hello CloudWatch
<a name="cloudwatch_Hello_kotlin_topic"></a>

The following code example shows how to get started using CloudWatch.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
/**
Before running this Kotlin code example, set up your development environment,
including your credentials.

For more information, see the following documentation topic:
https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/setup.html
 */
suspend fun main(args: Array<String>) {
    val usage = """
        Usage:
           <namespace>
        Where:
           namespace - The namespace to filter against (for example, AWS/EC2).
    """

    if (args.size != 1) {
        println(usage)
        exitProcess(0)
    }

    val namespace = args[0]
    listAllMets(namespace)
}

suspend fun listAllMets(namespaceVal: String?) {
    val request =
        ListMetricsRequest {
            namespace = namespaceVal
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient
            .listMetricsPaginated(request)
            .transform { it.metrics?.forEach { obj -> emit(obj) } }
            .collect { obj ->
                println("Name is ${obj.metricName}")
                println("Namespace is ${obj.namespace}")
            }
    }
}
```
+  For API details, see [ListMetrics](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

## Basics
<a name="basics"></a>

### Learn the basics
<a name="cloudwatch_GetStartedMetricsDashboardsAlarms_kotlin_topic"></a>

The following code example shows how to:
+ List CloudWatch namespaces and metrics.
+ Start OpenTelemetry enrichment so CloudWatch correlates incoming OTLP metrics with the resources that produced them.
+ See how OTLP metrics reach the CloudWatch metrics endpoint. Metric ingestion over OTLP is not an AWS SDK operation.
+ Create an alarm that evaluates a PromQL query.
+ Inspect the alarm's contributors, the individual series that the query matched.
+ Get statistics for a metric and chart it on a dashboard.
+ Mute the alarm for a maintenance window, then clean up.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).
Run an interactive scenario demonstrating the CloudWatch OpenTelemetry experience.

```
/**
 Before running this Kotlin code example, set up your development environment,
 including your credentials.

 For more information, see the following documentation topic:
 https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/setup.html

 This scenario demonstrates the Amazon CloudWatch OpenTelemetry (OTel) experience.
 CloudWatch ingests OpenTelemetry metrics natively, and this example walks through what
 you do with them: turning on enrichment so CloudWatch can correlate incoming OTLP
 metrics with the resources that produced them, alarming on those metrics with a PromQL
 query, and finding out which individual series drove the alarm.

 A PromQL alarm works differently from a classic metric alarm. Rather than watching one
 metric and counting breaching periods, it evaluates a query that can match many series
 at once, and tracks each matching series separately as a contributor.

 Note that sending OTLP metrics to CloudWatch is not an AWS SDK operation. Metrics
 arrive over the OTLP protocol through the CloudWatch agent, an OpenTelemetry
 Collector, or an ADOT SDK. Everything this scenario does is configuration and querying
 around that ingestion path.

 This Kotlin code example performs the following tasks:

 1. List metrics and namespaces from Amazon CloudWatch.
 2. Start OpenTelemetry enrichment for the account.
 3. Explain how OTLP metrics reach CloudWatch.
 4. Create an alarm that evaluates a PromQL query.
 5. Inspect the contributors to the PromQL alarm.
 6. Get metric statistics and chart the metric on a dashboard.
 7. Mute the alarm for a maintenance window.
 8. Clean up the Amazon CloudWatch resources.
 */

val DASHES: String = "-".repeat(80)

private const val REGION = "us-east-1"

private const val DEFAULT_QUERY = "avg by (host) (system_cpu_utilization) > 80"

// Valid evaluation intervals are 10, 20, 30, or any multiple of 60 up to 3600 seconds.
private const val EVALUATION_INTERVAL = 60
private const val PENDING_PERIOD = 300
private const val RECOVERY_PERIOD = 120

val scenarioScanner = Scanner(System.`in`)

suspend fun main() {
    // Suffix the resource names so repeated runs do not collide.
    val suffix = (Random().nextInt(9000) + 1000).toString()
    val alarmName = "doc-example-promql-alarm-$suffix"
    val dashboardName = "doc-example-dashboard-$suffix"
    val muteRuleName = "doc-example-mute-rule-$suffix"

    println(DASHES)
    println("Welcome to the Amazon CloudWatch Basics scenario.")
    println(
        """
        CloudWatch now ingests OpenTelemetry metrics natively. This scenario walks through
        that experience: it turns on OTel enrichment so CloudWatch can correlate incoming
        OTLP metrics with the resources that produced them, alarms on those metrics with a
        PromQL query, and shows you which individual series drove the alarm.

        A PromQL alarm works differently from a classic metric alarm. Rather than watching
        one metric and counting breaching periods, it evaluates a query that can match many
        series at once, and tracks each one separately as a contributor.

        Let's get started...
        """.trimIndent(),
    )
    waitForInputToContinue()

    // Tracks whether this run turned enrichment on, so that cleanup only turns off
    // enrichment that this run started.
    var startedEnrichment = false
    var dashboardCreated = false

    println(DASHES)
    println(
        """
        1. List metrics and namespaces

        Before configuring anything, let's see what CloudWatch is already collecting in
        this account by calling ListMetrics.
        """.trimIndent(),
    )
    waitForInputToContinue()

    val namespaces = listNameSpaces()
    println("Found ${namespaces.size} namespaces in this account:")
    namespaces.take(10).forEach { println("  $it") }
    if (namespaces.isEmpty()) {
        println(
            """
            No metrics found in this account. The statistics and dashboard steps later on
            need an existing metric, so they will be skipped.
            """.trimIndent(),
        )
    }
    waitForInputToContinue()

    println(DASHES)
    println(
        """
        2. Start OpenTelemetry enrichment

        Enrichment is what lets CloudWatch attach AWS resource context to the OTLP metrics
        you send it. Without it, your metrics arrive as opaque series with no connection to
        the resources that emitted them.

        We check the current state first, and only start enrichment if it isn't already on.
        """.trimIndent(),
    )
    waitForInputToContinue()

    val status = getOTelEnrichmentStatus()
    if (status !is OTelEnrichmentStatus.Running) {
        // Record the attempt before making it. We already know enrichment was not running, so
        // stopping it during cleanup is always safe, and a start that succeeds but fails to
        // report back would otherwise leave it running.
        startedEnrichment = true
        startOTelEnrichment()

        val newStatus = getOTelEnrichmentStatus()
        println(
            "Note: this run started enrichment (status is now ${newStatus?.value}), so the " +
                "cleanup step will stop it again.",
        )
    } else {
        println(
            """
            Enrichment was already running, so we will leave it alone. The cleanup step
            will not stop it, because other workloads in this account may depend on it.
            """.trimIndent(),
        )
    }
    waitForInputToContinue()

    println(DASHES)
    println(
        """
        3. Send OTLP metrics to CloudWatch

        This step is not an AWS SDK operation, and that's worth being explicit about.
        Metrics reach CloudWatch over the OTLP protocol, through the CloudWatch agent, an
        OpenTelemetry Collector, or an ADOT SDK. There is no PutOTelMetrics API to call.

        Point your collector at the CloudWatch metrics endpoint, which follows the pattern
        https://monitoring.<region>.amazonaws.com/v1/metrics

        The endpoint is HTTP/1.1 only and does not support gRPC, so use an otlphttp
        exporter rather than otlp. The metrics endpoint signs as "monitoring".
        """.trimIndent(),
    )
    waitForInputToContinue()

    println(DASHES)
    println(
        """
        4. Create a PromQL alarm

        Now we alarm on those metrics. The comparison goes inside the query itself: a
        PromQL alarm has no separate threshold, comparison operator, statistic, or period.
        """.trimIndent(),
    )
    println("Enter a PromQL query, or press <ENTER> for the default")
    println("[$DEFAULT_QUERY]:")
    val queryInput = scenarioScanner.nextLine()
    val query = if (queryInput.isBlank()) DEFAULT_QUERY else queryInput.trim()

    putPromQlMetricAlarm(alarmName, query, EVALUATION_INTERVAL, PENDING_PERIOD, RECOVERY_PERIOD)
    println("Created alarm $alarmName:")
    println("  query:              $query")
    println("  evaluationInterval: $EVALUATION_INTERVAL seconds")
    println("  pendingPeriod:      $PENDING_PERIOD seconds")
    println("  recoveryPeriod:     $RECOVERY_PERIOD seconds")
    println(
        """
        A PromQL alarm starts in the OK state rather than INSUFFICIENT_DATA, which is
        another way it differs from a classic alarm.
        """.trimIndent(),
    )
    waitForInputToContinue()

    println(DASHES)
    println(
        """
        5. Inspect the alarm's contributors

        Each contributor is one series the query matched, identified by its label set. This
        is how you find out which host is unhealthy rather than only that something is.
        Classic alarms have no equivalent.
        """.trimIndent(),
    )
    waitForInputToContinue()

    describeAlarmContributors(alarmName)
    waitForInputToContinue()

    println(DASHES)
    println(
        """
        6. Get statistics and chart the metric on a dashboard

        Statistics and dashboards are how you see what the alarm is evaluating.
        """.trimIndent(),
    )
    waitForInputToContinue()

    if (namespaces.isNotEmpty()) {
        val namespace = namespaces[0]
        val metrics = listMets(namespace)
        if (metrics != null && metrics.isNotEmpty()) {
            val metricName = metrics[0]
            val startDate = Instant.now().minus(24, ChronoUnit.HOURS).toString()
            var dimension: Dimension? = null
            try {
                dimension = getSpecificMet(namespace)
                if (dimension != null) {
                    getAndDisplayMetricStatistics(namespace, metricName, "Average", startDate, dimension)
                }
            } catch (e: Exception) {
                println("Could not get statistics for $namespace/$metricName: ${e.message}")
            }

            // Chart the metric this run just discovered. Reading the widgets from a file
            // would chart metrics that may not exist in this account.
            try {
                createDashboard(dashboardName, buildDashboardBody(namespace, metricName, dimension, REGION))
                dashboardCreated = true
                listDashboards()
            } catch (e: Exception) {
                println("Could not create the dashboard: ${e.message}")
            }
        } else {
            println("No metrics found in namespace $namespace, skipping statistics and the dashboard.")
        }
    } else {
        println("Skipping statistics and dashboard because no metrics exist yet.")
    }
    waitForInputToContinue()

    println(DASHES)
    println(
        """
        7. Mute the alarm for a maintenance window

        While a mute rule is active the targeted alarms keep evaluating and keep changing
        state, but their actions do not fire. This is the supported way to suppress
        notifications during planned maintenance, instead of disabling alarm actions and
        hoping someone remembers to turn them back on.
        """.trimIndent(),
    )
    waitForInputToContinue()

    // The expression is a five-field cron expression,
    // cron(Minutes Hours Day-of-month Month Day-of-week). Note that this is five fields,
    // not the six that Amazon EventBridge uses. For a one-time window, use
    // at(yyyy-MM-ddThh:mm), with no seconds. The duration is an ISO 8601 duration from
    // PT1M to P15D, so PT2H rather than 2h.
    val expression = "cron(0 2 * * SUN)"
    val duration = "PT2H"
    val timezone = "America/Los_Angeles"

    putAlarmMuteRule(muteRuleName, expression, duration, listOf(alarmName), timezone)
    println("Created mute rule $muteRuleName:")
    println("  schedule: $expression for $duration")
    println("  timezone: $timezone")
    println("  targets:  $alarmName")
    println(
        """
        Note the two formats here. The expression is a five-field cron expression, five
        rather than the six Amazon EventBridge uses. The duration is an ISO 8601 duration,
        so 'PT2H' and not '2h'.

        Also note that muteTargets is set explicitly. If you leave it out, the rule applies
        to every alarm in the account.
        """.trimIndent(),
    )

    val muteRule = getAlarmMuteRule(muteRuleName)
    println("Read the rule back: status ${muteRule.status?.value}, mute type ${muteRule.muteType}.")

    val summaries = listAlarmMuteRules(alarmName)
    println("Found ${summaries.size} mute rules targeting this alarm.")
    // Mute rule summaries carry no name field, only an ARN, so match on the ARN suffix.
    summaries
        .firstOrNull { summary ->
            summary.alarmMuteRuleArn?.endsWith("/$muteRuleName") == true ||
                summary.alarmMuteRuleArn?.endsWith(":$muteRuleName") == true
        }?.let { summary ->
            println("  matched by ARN: ${summary.alarmMuteRuleArn} (${summary.status?.value})")
        }
    waitForInputToContinue()

    println(DASHES)
    println("8. Clean up")
    println("Delete the resources this scenario created? (y/n)")
    val cleanUp = scenarioScanner.nextLine()
    if (!cleanUp.trim().equals("y", ignoreCase = true)) {
        println(
            """
            Skipping cleanup. Note that the alarm, dashboard, and mute rule are still in
            your account, and enrichment may still be running.
            """.trimIndent(),
        )
        println(DASHES)
        println("This concludes the Amazon CloudWatch Basics scenario.")
        return
    }

    // Each deletion is attempted independently so that one failure does not leave the
    // remaining resources behind.
    try {
        deleteAlarmMuteRule(muteRuleName)
    } catch (e: Exception) {
        println("Could not delete the mute rule: ${e.message}")
    }

    try {
        deleteAlarm(alarmName)
    } catch (e: Exception) {
        println("Could not delete the alarm: ${e.message}")
    }

    if (dashboardCreated) {
        try {
            deleteDashboard(dashboardName)
        } catch (e: Exception) {
            println("Could not delete the dashboard: ${e.message}")
        }
    }

    if (startedEnrichment) {
        try {
            stopOTelEnrichment()
            println("Stopped OTel enrichment, because this run started it.")
        } catch (e: Exception) {
            println("Could not stop OTel enrichment: ${e.message}")
        }
    } else {
        println("Left OTel enrichment running, because it was already on before this run.")
    }

    println(DASHES)
    println("This concludes the Amazon CloudWatch Basics scenario.")
    println(DASHES)
}

private fun waitForInputToContinue() {
    while (true) {
        println("")
        println("Press <ENTER> to continue:")
        val input = scenarioScanner.nextLine()
        if (input.trim().isEmpty()) {
            println("Continuing with the program...")
            println("")
            break
        }
        println("Invalid input. Please try again.")
    }
}

suspend fun deleteAlarm(alarmNameVal: String) {
    val request =
        DeleteAlarmsRequest {
            alarmNames = listOf(alarmNameVal)
        }

    CloudWatchClient.fromEnvironment { region = REGION }.use { cwClient ->
        cwClient.deleteAlarms(request)
        println("Successfully deleted alarm $alarmNameVal")
    }
}

suspend fun deleteDashboard(dashboardName: String) {
    val dashboardsRequest =
        DeleteDashboardsRequest {
            dashboardNames = listOf(dashboardName)
        }
    CloudWatchClient.fromEnvironment { region = REGION }.use { cwClient ->
        cwClient.deleteDashboards(dashboardsRequest)
        println("$dashboardName was successfully deleted.")
    }
}

suspend fun listDashboards() {
    CloudWatchClient { region = "us-east-1" }.use { cwClient ->
        cwClient
            .listDashboardsPaginated({})
            .transform { it.dashboardEntries?.forEach { obj -> emit(obj) } }
            .collect { obj ->
                println("Name is ${obj.dashboardName}")
                println("Dashboard ARN is ${obj.dashboardArn}")
            }
    }
}

suspend fun createDashboard(
    dashboardNameVal: String,
    dashboardBodyVal: String,
) {
    val dashboardRequest =
        PutDashboardRequest {
            dashboardName = dashboardNameVal
            dashboardBody = dashboardBodyVal
        }

    CloudWatchClient.fromEnvironment { region = REGION }.use { cwClient ->
        val response = cwClient.putDashboard(dashboardRequest)
        println("$dashboardNameVal was successfully created.")
        val messages = response.dashboardValidationMessages
        if (messages != null) {
            if (messages.isEmpty()) {
                println("There are no messages in the new Dashboard")
            } else {
                for (message in messages) {
                    println("Message is: ${message.message}")
                }
            }
        }
    }
}

/**
 * Builds a single-widget dashboard body that charts the given metric.
 *
 * A metric widget must name its Region, because a dashboard can chart metrics from several.
 */
fun buildDashboardBody(
    metricNamespace: String,
    metricName: String,
    dimension: Dimension?,
    region: String,
): String {
    val dimensionParts =
        if (dimension == null) "" else ", \"${dimension.name}\", \"${dimension.value}\""

    return """
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
                        "metrics": [[ "$metricNamespace", "$metricName"$dimensionParts ]],
                        "view": "timeSeries",
                        "stat": "Average",
                        "period": 300,
                        "region": "$region",
                        "title": "$metricName"
                    }
                }
            ]
        }
    """.trimIndent()
}

suspend fun getAndDisplayMetricStatistics(
    nameSpaceVal: String,
    metVal: String,
    metricOption: String,
    date: String,
    myDimension: Dimension,
) {
    val start = Instant.parse(date)
    val endDate = Instant.now()
    val statisticsRequest =
        GetMetricStatisticsRequest {
            endTime =
                aws.smithy.kotlin.runtime.time
                    .Instant(endDate)
            startTime =
                aws.smithy.kotlin.runtime.time
                    .Instant(start)
            dimensions = listOf(myDimension)
            metricName = metVal
            namespace = nameSpaceVal
            period = 86400
            statistics = listOf(Statistic.fromValue(metricOption))
        }

    CloudWatchClient { region = "us-east-1" }.use { cwClient ->
        val response = cwClient.getMetricStatistics(statisticsRequest)
        val data = response.datapoints
        if (data != null) {
            if (data.isNotEmpty()) {
                for (datapoint in data) {
                    println("Timestamp: ${datapoint.timestamp} Maximum value: ${datapoint.maximum}")
                }
            } else {
                println("The returned data list is empty")
            }
        }
    }
}

suspend fun listMets(namespaceVal: String?): ArrayList<String>? {
    val metList = ArrayList<String>()
    val request =
        ListMetricsRequest {
            namespace = namespaceVal
        }
    CloudWatchClient.fromEnvironment { region = REGION }.use { cwClient ->
        val reponse = cwClient.listMetrics(request)
        reponse.metrics?.forEach { metrics ->
            val data = metrics.metricName
            if (!metList.contains(data)) {
                metList.add(data!!)
            }
        }
    }
    return metList
}

suspend fun getSpecificMet(namespaceVal: String?): Dimension? {
    val request =
        ListMetricsRequest {
            namespace = namespaceVal
        }
    CloudWatchClient.fromEnvironment { region = REGION }.use { cwClient ->
        val response = cwClient.listMetrics(request)
        val myList = response.metrics
        if (myList != null) {
            return myList[0].dimensions?.get(0)
        }
    }
    return null
}

suspend fun listNameSpaces(): ArrayList<String> {
    val nameSpaceList = ArrayList<String>()
    CloudWatchClient.fromEnvironment { region = REGION }.use { cwClient ->
        val response = cwClient.listMetrics(ListMetricsRequest {})
        response.metrics?.forEach { metrics ->
            val data = metrics.namespace
            if (!nameSpaceList.contains(data)) {
                nameSpaceList.add(data!!)
            }
        }
    }
    return nameSpaceList
}
```
The OpenTelemetry functions that the scenario calls.

```
suspend fun getOTelEnrichmentStatus(): OTelEnrichmentStatus? {
    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        val response = cwClient.getOTelEnrichment(GetOTelEnrichmentRequest {})
        val status = response.status
        when (status) {
            is OTelEnrichmentStatus.Running ->
                println("OTel enrichment is running. Vended metrics are queryable with PromQL")
            is OTelEnrichmentStatus.Stopped ->
                println("OTel enrichment is stopped. Start it to enrich vended metrics")
            else -> println("OTel enrichment status is ${status?.value}")
        }
        return status
    }
}

suspend fun startOTelEnrichment() {
    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.startOTelEnrichment(StartOTelEnrichmentRequest {})
        println("Successfully started OTel enrichment for this account")
    }
}

suspend fun putPromQlMetricAlarm(
    alarmNameVal: String,
    queryVal: String,
    evaluationIntervalVal: Int = 60,
    pendingPeriodVal: Int = 300,
    recoveryPeriodVal: Int = 120,
) {
    // The comparison belongs in the query itself. A PromQL alarm has no separate
    // threshold, comparison operator, statistic, period, or evaluation periods.
    //
    // Note that the Kotlin SDK spells this AlarmPromQlCriteria, with a lowercase l in
    // "Ql". Every other AWS SDK spells it PromQL, so don't be thrown by the difference
    // when comparing this example against the other language versions.
    val promQlCriteria =
        AlarmPromQlCriteria {
            query = queryVal
            pendingPeriod = pendingPeriodVal
            recoveryPeriod = recoveryPeriodVal
        }

    // EvaluationCriteria is a union and is mutually exclusive with the classic
    // metricName and metrics parameters. When you use it, you must also set
    // evaluationInterval.
    val request =
        PutMetricAlarmRequest {
            alarmName = alarmNameVal
            alarmDescription = "A PromQL alarm created by the Kotlin SDK"
            evaluationCriteria = EvaluationCriteria.PromQlCriteria(promQlCriteria)
            evaluationInterval = evaluationIntervalVal
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.putMetricAlarm(request)
        println("Successfully created PromQL alarm $alarmNameVal for query $queryVal")
    }
}

suspend fun describeAlarmContributors(alarmNameVal: String): List<AlarmContributor> {
    val contributors = mutableListOf<AlarmContributor>()

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        var token: String? = null
        do {
            val response =
                cwClient.describeAlarmContributors(
                    DescribeAlarmContributorsRequest {
                        alarmName = alarmNameVal
                        nextToken = token
                    },
                )

            response.alarmContributors?.let { contributors.addAll(it) }
            token = response.nextToken
        } while (token != null)

        if (contributors.isEmpty()) {
            println(
                "No contributors yet. The query matched no series, which usually means no " +
                    "OTel metrics with these labels have arrived",
            )
        }

        contributors.forEach { contributor ->
            val labels =
                contributor.contributorAttributes
                    ?.entries
                    ?.sortedBy { it.key }
                    ?.joinToString(", ") { "${it.key}=${it.value}" }
            println("${contributor.contributorId}: $labels")
            println("  reason: ${contributor.stateReason}")
        }
    }
    return contributors
}

suspend fun putAlarmMuteRule(
    muteRuleName: String,
    expressionVal: String,
    durationVal: String,
    alarmNamesVal: List<String>,
    timezoneVal: String = "America/Los_Angeles",
) {
    // For a recurring window, use a five-field cron expression,
    // cron(Minutes Hours Day-of-month Month Day-of-week), such as cron(0 2 * * SUN).
    // Note that this is five fields, not the six that Amazon EventBridge uses. For a
    // one-time window, use at(yyyy-MM-ddThh:mm), such as at(2026-09-05T02:00). The
    // duration is in ISO 8601 duration format, from PT1M (one minute) to P15D (15 days).
    val scheduleOb =
        Schedule {
            expression = expressionVal
            duration = durationVal
            timezone = timezoneVal
        }

    val request =
        PutAlarmMuteRuleRequest {
            name = muteRuleName
            description = "A mute rule created by the Kotlin SDK"
            rule =
                Rule {
                    schedule = scheduleOb
                }
            // Target up to 100 alarms. If muteTargets is omitted, the rule applies to
            // every alarm in the account.
            if (alarmNamesVal.isNotEmpty()) {
                muteTargets =
                    MuteTargets {
                        alarmNames = alarmNamesVal
                    }
            }
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.putAlarmMuteRule(request)
        println("Successfully put alarm mute rule $muteRuleName")
    }
}

suspend fun getAlarmMuteRule(muteRuleName: String): GetAlarmMuteRuleResponse {
    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        val response =
            cwClient.getAlarmMuteRule(
                GetAlarmMuteRuleRequest {
                    alarmMuteRuleName = muteRuleName
                },
            )

        println("Mute rule ${response.name} is ${response.status?.value}")
        println("  ARN: ${response.alarmMuteRuleArn}")
        println("  schedule: ${response.rule?.schedule?.expression} for ${response.rule?.schedule?.duration}")
        response.muteTargets?.alarmNames?.let { println("  muted alarms: ${it.joinToString(", ")}") }
        return response
    }
}

suspend fun listAlarmMuteRules(alarmNameVal: String? = null): List<AlarmMuteRuleSummary> {
    val summaries = mutableListOf<AlarmMuteRuleSummary>()

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        var token: String? = null
        do {
            val response =
                cwClient.listAlarmMuteRules(
                    ListAlarmMuteRulesRequest {
                        alarmName = alarmNameVal
                        nextToken = token
                    },
                )

            response.alarmMuteRuleSummaries?.let { summaries.addAll(it) }
            token = response.nextToken
        } while (token != null)

        summaries.forEach { summary ->
            println("${summary.alarmMuteRuleArn} (${summary.status?.value})")
        }
    }
    return summaries
}

suspend fun deleteAlarmMuteRule(muteRuleName: String) {
    val request =
        DeleteAlarmMuteRuleRequest {
            alarmMuteRuleName = muteRuleName
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.deleteAlarmMuteRule(request)
        println("Successfully deleted alarm mute rule $muteRuleName")
    }
}

suspend fun stopOTelEnrichment() {
    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.stopOTelEnrichment(StopOTelEnrichmentRequest {})
        println("Successfully stopped OTel enrichment for this account")
    }
}
```
+ For API details, see the following topics in *AWS SDK for Kotlin API reference*.
  + [DeleteAlarmMuteRule](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [DeleteAlarms](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [DeleteDashboards](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [DescribeAlarmContributors](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [GetAlarmMuteRule](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [GetDashboard](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [GetMetricStatistics](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [GetOTelEnrichment](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [ListAlarmMuteRules](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [ListDashboards](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [ListMetrics](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [PutAlarmMuteRule](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [PutDashboard](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [PutMetricAlarm](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [StartOTelEnrichment](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [StopOTelEnrichment](https://sdk.amazonaws.com/kotlin/api/latest/index.html)

## Actions
<a name="actions"></a>

### `DeleteAlarmMuteRule`
<a name="cloudwatch_DeleteAlarmMuteRule_kotlin_topic"></a>

The following code example shows how to use `DeleteAlarmMuteRule`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun deleteAlarmMuteRule(muteRuleName: String) {
    val request =
        DeleteAlarmMuteRuleRequest {
            alarmMuteRuleName = muteRuleName
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.deleteAlarmMuteRule(request)
        println("Successfully deleted alarm mute rule $muteRuleName")
    }
}
```
+  For API details, see [DeleteAlarmMuteRule](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `DeleteAlarms`
<a name="cloudwatch_DeleteAlarms_kotlin_topic"></a>

The following code example shows how to use `DeleteAlarms`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun deleteAlarm(alarmNameVal: String) {
    val request =
        DeleteAlarmsRequest {
            alarmNames = listOf(alarmNameVal)
        }

    CloudWatchClient.fromEnvironment { region = REGION }.use { cwClient ->
        cwClient.deleteAlarms(request)
        println("Successfully deleted alarm $alarmNameVal")
    }
}
```
+  For API details, see [DeleteAlarms](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `DeleteAnomalyDetector`
<a name="cloudwatch_DeleteAnomalyDetector_kotlin_topic"></a>

The following code example shows how to use `DeleteAnomalyDetector`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun deleteAnomalyDetector(
    namespaceVal: String,
    metricNameVal: String,
) {
    val singleMetricAnomalyDetectorVal =
        SingleMetricAnomalyDetector {
            namespace = namespaceVal
            metricName = metricNameVal
            stat = "Maximum"
        }

    val request =
        DeleteAnomalyDetectorRequest {
            singleMetricAnomalyDetector = singleMetricAnomalyDetectorVal
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.deleteAnomalyDetector(request)
        println("Successfully deleted the anomaly detector for metric $metricNameVal.")
    }
}
```
+  For API details, see [DeleteAnomalyDetector](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `DeleteDashboards`
<a name="cloudwatch_DeleteDashboards_kotlin_topic"></a>

The following code example shows how to use `DeleteDashboards`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun deleteDashboard(dashboardName: String) {
    val dashboardsRequest =
        DeleteDashboardsRequest {
            dashboardNames = listOf(dashboardName)
        }
    CloudWatchClient.fromEnvironment { region = REGION }.use { cwClient ->
        cwClient.deleteDashboards(dashboardsRequest)
        println("$dashboardName was successfully deleted.")
    }
}
```
+  For API details, see [DeleteDashboards](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `DescribeAlarmContributors`
<a name="cloudwatch_DescribeAlarmContributors_kotlin_topic"></a>

The following code example shows how to use `DescribeAlarmContributors`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun describeAlarmContributors(alarmNameVal: String): List<AlarmContributor> {
    val contributors = mutableListOf<AlarmContributor>()

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        var token: String? = null
        do {
            val response =
                cwClient.describeAlarmContributors(
                    DescribeAlarmContributorsRequest {
                        alarmName = alarmNameVal
                        nextToken = token
                    },
                )

            response.alarmContributors?.let { contributors.addAll(it) }
            token = response.nextToken
        } while (token != null)

        if (contributors.isEmpty()) {
            println(
                "No contributors yet. The query matched no series, which usually means no " +
                    "OTel metrics with these labels have arrived",
            )
        }

        contributors.forEach { contributor ->
            val labels =
                contributor.contributorAttributes
                    ?.entries
                    ?.sortedBy { it.key }
                    ?.joinToString(", ") { "${it.key}=${it.value}" }
            println("${contributor.contributorId}: $labels")
            println("  reason: ${contributor.stateReason}")
        }
    }
    return contributors
}
```
+  For API details, see [DescribeAlarmContributors](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `DescribeAlarmHistory`
<a name="cloudwatch_DescribeAlarmHistory_kotlin_topic"></a>

The following code example shows how to use `DescribeAlarmHistory`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun getAlarmHistory(
    alarmNameVal: String,
    startDateVal: String,
) {
    val request =
        DescribeAlarmHistoryRequest {
            alarmName = alarmNameVal
            startDate =
                aws.smithy.kotlin.runtime.time.Instant
                    .fromIso8601(startDateVal)
            endDate =
                aws.smithy.kotlin.runtime.time.Instant
                    .now()
            historyItemType = HistoryItemType.Action
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        val response = cwClient.describeAlarmHistory(request)
        val historyItems = response.alarmHistoryItems
        if (historyItems.isNullOrEmpty()) {
            println("No alarm history data found for $alarmNameVal.")
        } else {
            for (item in historyItems) {
                println("History summary: ${item.historySummary}")
                println("Time stamp: ${item.timestamp}")
            }
        }
    }
}
```
+  For API details, see [DescribeAlarmHistory](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `DescribeAlarms`
<a name="cloudwatch_DescribeAlarms_kotlin_topic"></a>

The following code example shows how to use `DescribeAlarms`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun desCWAlarms() {
    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        val response = cwClient.describeAlarms(DescribeAlarmsRequest {})
        response.metricAlarms?.forEach { alarm ->
            println("Retrieved alarm ${alarm.alarmName}")
        }
    }
}
```
+  For API details, see [DescribeAlarms](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `DescribeAlarmsForMetric`
<a name="cloudwatch_DescribeAlarmsForMetric_kotlin_topic"></a>

The following code example shows how to use `DescribeAlarmsForMetric`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun describeAlarmsForMetric(
    namespaceVal: String,
    metricNameVal: String,
) {
    val request =
        DescribeAlarmsForMetricRequest {
            namespace = namespaceVal
            metricName = metricNameVal
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        val response = cwClient.describeAlarmsForMetric(request)
        val alarms = response.metricAlarms
        if (alarms.isNullOrEmpty()) {
            println("No alarms found for $metricNameVal in $namespaceVal.")
        } else {
            for (alarm in alarms) {
                println("Alarm name: ${alarm.alarmName}")
                println("Alarm state: ${alarm.stateValue}")
            }
        }
    }
}
```
+  For API details, see [DescribeAlarmsForMetric](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `DescribeAnomalyDetectors`
<a name="cloudwatch_DescribeAnomalyDetectors_kotlin_topic"></a>

The following code example shows how to use `DescribeAnomalyDetectors`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun describeAnomalyDetectors(
    namespaceVal: String,
    metricNameVal: String,
) {
    val request =
        DescribeAnomalyDetectorsRequest {
            maxResults = 10
            namespace = namespaceVal
            metricName = metricNameVal
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        val response = cwClient.describeAnomalyDetectors(request)
        response.anomalyDetectors?.forEach { detector ->
            println("Metric name: ${detector.singleMetricAnomalyDetector?.metricName}")
            println("State: ${detector.stateValue}")
        }
    }
}
```
+  For API details, see [DescribeAnomalyDetectors](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `DisableAlarmActions`
<a name="cloudwatch_DisableAlarmActions_kotlin_topic"></a>

The following code example shows how to use `DisableAlarmActions`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun disableActions(alarmName: String) {
    val request =
        DisableAlarmActionsRequest {
            alarmNames = listOf(alarmName)
        }
    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.disableAlarmActions(request)
        println("Successfully disabled actions on alarm $alarmName")
    }
}
```
+  For API details, see [DisableAlarmActions](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `EnableAlarmActions`
<a name="cloudwatch_EnableAlarmActions_kotlin_topic"></a>

The following code example shows how to use `EnableAlarmActions`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun enableActions(alarm: String) {
    val request =
        EnableAlarmActionsRequest {
            alarmNames = listOf(alarm)
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.enableAlarmActions(request)
        println("Successfully enabled actions on alarm $alarm")
    }
}
```
+  For API details, see [EnableAlarmActions](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `GetAlarmMuteRule`
<a name="cloudwatch_GetAlarmMuteRule_kotlin_topic"></a>

The following code example shows how to use `GetAlarmMuteRule`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun getAlarmMuteRule(muteRuleName: String): GetAlarmMuteRuleResponse {
    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        val response =
            cwClient.getAlarmMuteRule(
                GetAlarmMuteRuleRequest {
                    alarmMuteRuleName = muteRuleName
                },
            )

        println("Mute rule ${response.name} is ${response.status?.value}")
        println("  ARN: ${response.alarmMuteRuleArn}")
        println("  schedule: ${response.rule?.schedule?.expression} for ${response.rule?.schedule?.duration}")
        response.muteTargets?.alarmNames?.let { println("  muted alarms: ${it.joinToString(", ")}") }
        return response
    }
}
```
+  For API details, see [GetAlarmMuteRule](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `GetMetricData`
<a name="cloudwatch_GetMetricData_kotlin_topic"></a>

The following code example shows how to use `GetMetricData`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun getMetData() {
    val start =
        aws.smithy.kotlin.runtime.time.Instant
            .fromIso8601("2019-10-23T10:12:35Z")
    val endDate =
        aws.smithy.kotlin.runtime.time.Instant
            .now()
    val met =
        Metric {
            metricName = "DiskReadBytes"
            namespace = "AWS/EC2"
        }

    val metStat =
        MetricStat {
            stat = "Minimum"
            period = 60
            metric = met
        }

    val dataQUery =
        MetricDataQuery {
            metricStat = metStat
            id = "foo2"
            returnData = true
        }

    val dq = mutableListOf<MetricDataQuery>()
    dq.add(dataQUery)

    val request =
        GetMetricDataRequest {
            maxDatapoints = 100
            startTime = start
            endTime = endDate
            metricDataQueries = dq
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        val response = cwClient.getMetricData(request)
        response.metricDataResults?.forEach { item ->
            println("The label is ${item.label}")
            println("The status code is ${item.statusCode}")
        }
    }
}
```
+  For API details, see [GetMetricData](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `GetMetricStatistics`
<a name="cloudwatch_GetMetricStatistics_kotlin_topic"></a>

The following code example shows how to use `GetMetricStatistics`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun getAndDisplayMetricStatistics(
    nameSpaceVal: String,
    metVal: String,
    metricOption: String,
    date: String,
    myDimension: Dimension,
) {
    val start = Instant.parse(date)
    val endDate = Instant.now()
    val statisticsRequest =
        GetMetricStatisticsRequest {
            endTime =
                aws.smithy.kotlin.runtime.time
                    .Instant(endDate)
            startTime =
                aws.smithy.kotlin.runtime.time
                    .Instant(start)
            dimensions = listOf(myDimension)
            metricName = metVal
            namespace = nameSpaceVal
            period = 86400
            statistics = listOf(Statistic.fromValue(metricOption))
        }

    CloudWatchClient { region = "us-east-1" }.use { cwClient ->
        val response = cwClient.getMetricStatistics(statisticsRequest)
        val data = response.datapoints
        if (data != null) {
            if (data.isNotEmpty()) {
                for (datapoint in data) {
                    println("Timestamp: ${datapoint.timestamp} Maximum value: ${datapoint.maximum}")
                }
            } else {
                println("The returned data list is empty")
            }
        }
    }
}
```
+  For API details, see [GetMetricStatistics](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `GetMetricWidgetImage`
<a name="cloudwatch_GetMetricWidgetImage_kotlin_topic"></a>

The following code example shows how to use `GetMetricWidgetImage`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun getAndOpenMetricImage(fileName: String) {
    println("Getting image data for a custom metric.")
    val myJSON = """{
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
        }"""

    val request =
        GetMetricWidgetImageRequest {
            metricWidget = myJSON
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        val response = cwClient.getMetricWidgetImage(request)
        val bytes = response.metricWidgetImage
        if (bytes != null) {
            File(fileName).writeBytes(bytes)
            println("You have successfully written data to $fileName.")
        }
    }
}
```
+  For API details, see [GetMetricWidgetImage](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `GetOTelEnrichment`
<a name="cloudwatch_GetOTelEnrichment_kotlin_topic"></a>

The following code example shows how to use `GetOTelEnrichment`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun getOTelEnrichmentStatus(): OTelEnrichmentStatus? {
    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        val response = cwClient.getOTelEnrichment(GetOTelEnrichmentRequest {})
        val status = response.status
        when (status) {
            is OTelEnrichmentStatus.Running ->
                println("OTel enrichment is running. Vended metrics are queryable with PromQL")
            is OTelEnrichmentStatus.Stopped ->
                println("OTel enrichment is stopped. Start it to enrich vended metrics")
            else -> println("OTel enrichment status is ${status?.value}")
        }
        return status
    }
}
```
+  For API details, see [GetOTelEnrichment](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `ListAlarmMuteRules`
<a name="cloudwatch_ListAlarmMuteRules_kotlin_topic"></a>

The following code example shows how to use `ListAlarmMuteRules`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun listAlarmMuteRules(alarmNameVal: String? = null): List<AlarmMuteRuleSummary> {
    val summaries = mutableListOf<AlarmMuteRuleSummary>()

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        var token: String? = null
        do {
            val response =
                cwClient.listAlarmMuteRules(
                    ListAlarmMuteRulesRequest {
                        alarmName = alarmNameVal
                        nextToken = token
                    },
                )

            response.alarmMuteRuleSummaries?.let { summaries.addAll(it) }
            token = response.nextToken
        } while (token != null)

        summaries.forEach { summary ->
            println("${summary.alarmMuteRuleArn} (${summary.status?.value})")
        }
    }
    return summaries
}
```
+  For API details, see [ListAlarmMuteRules](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `ListDashboards`
<a name="cloudwatch_ListDashboards_kotlin_topic"></a>

The following code example shows how to use `ListDashboards`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun listDashboards() {
    CloudWatchClient { region = "us-east-1" }.use { cwClient ->
        cwClient
            .listDashboardsPaginated({})
            .transform { it.dashboardEntries?.forEach { obj -> emit(obj) } }
            .collect { obj ->
                println("Name is ${obj.dashboardName}")
                println("Dashboard ARN is ${obj.dashboardArn}")
            }
    }
}
```
+  For API details, see [ListDashboards](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `ListMetrics`
<a name="cloudwatch_ListMetrics_kotlin_topic"></a>

The following code example shows how to use `ListMetrics`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun listMets(namespaceVal: String?): ArrayList<String>? {
    val metList = ArrayList<String>()
    val request =
        ListMetricsRequest {
            namespace = namespaceVal
        }
    CloudWatchClient.fromEnvironment { region = REGION }.use { cwClient ->
        val reponse = cwClient.listMetrics(request)
        reponse.metrics?.forEach { metrics ->
            val data = metrics.metricName
            if (!metList.contains(data)) {
                metList.add(data!!)
            }
        }
    }
    return metList
}
```
+  For API details, see [ListMetrics](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `PutAlarmMuteRule`
<a name="cloudwatch_PutAlarmMuteRule_kotlin_topic"></a>

The following code example shows how to use `PutAlarmMuteRule`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun putAlarmMuteRule(
    muteRuleName: String,
    expressionVal: String,
    durationVal: String,
    alarmNamesVal: List<String>,
    timezoneVal: String = "America/Los_Angeles",
) {
    // For a recurring window, use a five-field cron expression,
    // cron(Minutes Hours Day-of-month Month Day-of-week), such as cron(0 2 * * SUN).
    // Note that this is five fields, not the six that Amazon EventBridge uses. For a
    // one-time window, use at(yyyy-MM-ddThh:mm), such as at(2026-09-05T02:00). The
    // duration is in ISO 8601 duration format, from PT1M (one minute) to P15D (15 days).
    val scheduleOb =
        Schedule {
            expression = expressionVal
            duration = durationVal
            timezone = timezoneVal
        }

    val request =
        PutAlarmMuteRuleRequest {
            name = muteRuleName
            description = "A mute rule created by the Kotlin SDK"
            rule =
                Rule {
                    schedule = scheduleOb
                }
            // Target up to 100 alarms. If muteTargets is omitted, the rule applies to
            // every alarm in the account.
            if (alarmNamesVal.isNotEmpty()) {
                muteTargets =
                    MuteTargets {
                        alarmNames = alarmNamesVal
                    }
            }
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.putAlarmMuteRule(request)
        println("Successfully put alarm mute rule $muteRuleName")
    }
}
```
+  For API details, see [PutAlarmMuteRule](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `PutAnomalyDetector`
<a name="cloudwatch_PutAnomalyDetector_kotlin_topic"></a>

The following code example shows how to use `PutAnomalyDetector`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun addAnomalyDetector(
    namespaceVal: String,
    metricNameVal: String,
) {
    val singleMetricAnomalyDetectorVal =
        SingleMetricAnomalyDetector {
            namespace = namespaceVal
            metricName = metricNameVal
            stat = "Maximum"
        }

    val request =
        PutAnomalyDetectorRequest {
            singleMetricAnomalyDetector = singleMetricAnomalyDetectorVal
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.putAnomalyDetector(request)
        println("Added an anomaly detector for metric $metricNameVal.")
    }
}
```
+  For API details, see [PutAnomalyDetector](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `PutDashboard`
<a name="cloudwatch_PutDashboard_kotlin_topic"></a>

The following code example shows how to use `PutDashboard`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun createDashboard(
    dashboardNameVal: String,
    dashboardBodyVal: String,
) {
    val dashboardRequest =
        PutDashboardRequest {
            dashboardName = dashboardNameVal
            dashboardBody = dashboardBodyVal
        }

    CloudWatchClient.fromEnvironment { region = REGION }.use { cwClient ->
        val response = cwClient.putDashboard(dashboardRequest)
        println("$dashboardNameVal was successfully created.")
        val messages = response.dashboardValidationMessages
        if (messages != null) {
            if (messages.isEmpty()) {
                println("There are no messages in the new Dashboard")
            } else {
                for (message in messages) {
                    println("Message is: ${message.message}")
                }
            }
        }
    }
}
```
+  For API details, see [PutDashboard](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `PutMetricAlarm`
<a name="cloudwatch_PutMetricAlarm_kotlin_topic"></a>

The following code example shows how to use `PutMetricAlarm`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).
Create an alarm that evaluates a PromQL query against OpenTelemetry metrics.

```
suspend fun putPromQlMetricAlarm(
    alarmNameVal: String,
    queryVal: String,
    evaluationIntervalVal: Int = 60,
    pendingPeriodVal: Int = 300,
    recoveryPeriodVal: Int = 120,
) {
    // The comparison belongs in the query itself. A PromQL alarm has no separate
    // threshold, comparison operator, statistic, period, or evaluation periods.
    //
    // Note that the Kotlin SDK spells this AlarmPromQlCriteria, with a lowercase l in
    // "Ql". Every other AWS SDK spells it PromQL, so don't be thrown by the difference
    // when comparing this example against the other language versions.
    val promQlCriteria =
        AlarmPromQlCriteria {
            query = queryVal
            pendingPeriod = pendingPeriodVal
            recoveryPeriod = recoveryPeriodVal
        }

    // EvaluationCriteria is a union and is mutually exclusive with the classic
    // metricName and metrics parameters. When you use it, you must also set
    // evaluationInterval.
    val request =
        PutMetricAlarmRequest {
            alarmName = alarmNameVal
            alarmDescription = "A PromQL alarm created by the Kotlin SDK"
            evaluationCriteria = EvaluationCriteria.PromQlCriteria(promQlCriteria)
            evaluationInterval = evaluationIntervalVal
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.putMetricAlarm(request)
        println("Successfully created PromQL alarm $alarmNameVal for query $queryVal")
    }
}
```
Create an alarm that evaluates a single CloudWatch metric.

```
suspend fun putMetricAlarm(
    alarmNameVal: String,
    instanceIdVal: String,
) {
    val dimensionOb =
        Dimension {
            name = "InstanceId"
            value = instanceIdVal
        }

    val request =
        PutMetricAlarmRequest {
            alarmName = alarmNameVal
            comparisonOperator = ComparisonOperator.GreaterThanThreshold
            evaluationPeriods = 1
            metricName = "CPUUtilization"
            namespace = "AWS/EC2"
            period = 60
            statistic = Statistic.fromValue("Average")
            threshold = 70.0
            actionsEnabled = false
            alarmDescription = "An Alarm created by the Kotlin SDK when server CPU utilization exceeds 70%"
            unit = StandardUnit.fromValue("Seconds")
            dimensions = listOf(dimensionOb)
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.putMetricAlarm(request)
        println("Successfully created an alarm with name $alarmNameVal")
    }
}
```
+  For API details, see [PutMetricAlarm](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `PutMetricData`
<a name="cloudwatch_PutMetricData_kotlin_topic"></a>

The following code example shows how to use `PutMetricData`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun addMetricData(
    namespaceVal: String,
    metricNameVal: String,
) {
    val time =
        aws.smithy.kotlin.runtime.time.Instant
            .now()

    val datum =
        MetricDatum {
            metricName = metricNameVal
            unit = StandardUnit.None
            value = 1001.00
            timestamp = time
        }

    val datum2 =
        MetricDatum {
            metricName = metricNameVal
            unit = StandardUnit.None
            value = 1002.00
            timestamp = time
        }

    val request =
        PutMetricDataRequest {
            namespace = namespaceVal
            metricData = listOf(datum, datum2)
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.putMetricData(request)
        println("Added metric values for metric $metricNameVal.")
    }
}
```
+  For API details, see [PutMetricData](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `StartOTelEnrichment`
<a name="cloudwatch_StartOTelEnrichment_kotlin_topic"></a>

The following code example shows how to use `StartOTelEnrichment`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun startOTelEnrichment() {
    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.startOTelEnrichment(StartOTelEnrichmentRequest {})
        println("Successfully started OTel enrichment for this account")
    }
}
```
+  For API details, see [StartOTelEnrichment](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

### `StopOTelEnrichment`
<a name="cloudwatch_StopOTelEnrichment_kotlin_topic"></a>

The following code example shows how to use `StopOTelEnrichment`.

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples).

```
suspend fun stopOTelEnrichment() {
    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.stopOTelEnrichment(StopOTelEnrichmentRequest {})
        println("Successfully stopped OTel enrichment for this account")
    }
}
```
+  For API details, see [StopOTelEnrichment](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.
