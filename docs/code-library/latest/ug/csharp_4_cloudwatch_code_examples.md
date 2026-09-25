---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/csharp_4_cloudwatch_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# CloudWatch examples using SDK for .NET (v4)
<a name="csharp_4_cloudwatch_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for .NET (v4) with CloudWatch.

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
<a name="cloudwatch_Hello_csharp_4_topic"></a>

The following code example shows how to get started using CloudWatch.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
using Amazon.CloudWatch;
using Amazon.CloudWatch.Model;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace CloudWatchActions;

public static class HelloCloudWatch
{
    static async Task Main(string[] args)
    {
        // Use the AWS .NET Core Setup package to set up dependency injection for the Amazon CloudWatch service.
        // Use your AWS profile name, or leave it blank to use the default profile.
        using var host = Host.CreateDefaultBuilder(args)
            .ConfigureServices((_, services) =>
                services.AddAWSService<IAmazonCloudWatch>()
            ).Build();

        // Now the client is available for injection.
        var cloudWatchClient = host.Services.GetRequiredService<IAmazonCloudWatch>();

        // You can use await and any of the async methods to get a response.
        var metricNamespace = "AWS/Billing";
        var response = await cloudWatchClient.ListMetricsAsync(new ListMetricsRequest
        {
            Namespace = metricNamespace
        });
        Console.WriteLine($"Hello Amazon CloudWatch! Following are some metrics available in the {metricNamespace} namespace:");
        Console.WriteLine();
        if (response.Metrics != null)
        {
            foreach (var metric in response.Metrics.Take(5))
            {
                Console.WriteLine($"\tMetric: {metric.MetricName}");
                Console.WriteLine($"\tNamespace: {metric.Namespace}");
                Console.WriteLine(
                    $"\tDimensions: {string.Join(", ", metric.Dimensions.Select(m => $"{m.Name}:{m.Value}"))}");
                Console.WriteLine();
            }
        }
    }
}
```
+  For API details, see [ListMetrics](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/ListMetrics) in *AWS SDK for .NET API Reference*.

## Basics
<a name="basics"></a>

### Learn the basics
<a name="cloudwatch_GetStartedMetricsDashboardsAlarms_csharp_4_topic"></a>

The following code example shows how to:
+ List CloudWatch namespaces and metrics.
+ Start OpenTelemetry enrichment so CloudWatch correlates incoming OTLP metrics with the resources that produced them.
+ See how OTLP metrics reach the CloudWatch metrics endpoint. Metric ingestion over OTLP is not an AWS SDK operation.
+ Create an alarm that evaluates a PromQL query.
+ Inspect the alarm's contributors, the individual series that the query matched.
+ Get statistics for a metric and chart it on a dashboard.
+ Mute the alarm for a maintenance window, then clean up.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).
Run an interactive scenario at a command prompt.

```
public class CloudWatchScenario
{
    /*
    Before running this .NET code example, set up your development environment, including your credentials.

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

    This .NET example performs the following tasks:
        1. List metrics and namespaces from CloudWatch.
        2. Start OpenTelemetry enrichment for the account.
        3. Explain how OTLP metrics reach CloudWatch.
        4. Create an alarm that evaluates a PromQL query.
        5. Inspect the contributors to the PromQL alarm.
        6. Get metric statistics and chart the metric on a dashboard.
        7. Mute the alarm for a maintenance window.
        8. Clean up resources.
    */

    private static ILogger logger = null!;
    private static CloudWatchWrapper _cloudWatchWrapper = null!;
    private static CloudWatchOTelWrapper _otelWrapper = null!;
    private static IConfiguration _configuration = null!;

    private const string DefaultQuery = "avg by (host) (system_cpu_utilization) > 80";

    // Valid evaluation intervals are 10, 20, 30, or any multiple of 60 up to 3600 seconds.
    private const int EvaluationInterval = 60;
    private const int PendingPeriod = 300;
    private const int RecoveryPeriod = 120;

    private static string _alarmName = null!;
    private static string _dashboardName = null!;
    private static string _muteRuleName = null!;

    // Tracks whether this run turned enrichment on, so that cleanup only turns off
    // enrichment that this run started.
    private static bool _startedEnrichment;
    private static bool _dashboardCreated;
    private static string _region = null!;

    static async Task Main(string[] args)
    {
        // Set up dependency injection for the Amazon service.
        using var host = Host.CreateDefaultBuilder(args)
            .ConfigureLogging(logging =>
                logging.AddFilter("System", LogLevel.Debug)
                    .AddFilter<DebugLoggerProvider>("Microsoft", LogLevel.Information)
                    .AddFilter<ConsoleLoggerProvider>("Microsoft", LogLevel.Trace))
            .ConfigureServices((_, services) =>
            services.AddAWSService<IAmazonCloudWatch>()
            .AddTransient<CloudWatchWrapper>()
            .AddTransient<CloudWatchOTelWrapper>()
        )
        .Build();

        _configuration = new ConfigurationBuilder()
            .SetBasePath(Directory.GetCurrentDirectory())
            .AddJsonFile("settings.json") // Load settings from .json file.
            .AddJsonFile("settings.local.json",
                true) // Optionally, load local settings.
            .Build();

        logger = LoggerFactory.Create(builder => { builder.AddConsole(); })
            .CreateLogger<CloudWatchScenario>();

        _cloudWatchWrapper = host.Services.GetRequiredService<CloudWatchWrapper>();
        _otelWrapper = host.Services.GetRequiredService<CloudWatchOTelWrapper>();

        // A metric widget must name its region, because a dashboard can chart
        // metrics from several.
        _region = host.Services.GetRequiredService<IAmazonCloudWatch>()
            .Config.RegionEndpoint.SystemName;

        // Suffix the resource names so repeated runs do not collide.
        var suffix = Random.Shared.Next(1000, 9999).ToString();
        _alarmName = $"doc-example-promql-alarm-{suffix}";
        _dashboardName = $"doc-example-dashboard-{suffix}";
        _muteRuleName = $"doc-example-mute-rule-{suffix}";

        Console.WriteLine(new string('-', 80));
        Console.WriteLine("Welcome to the Amazon CloudWatch Basics scenario.");
        Console.WriteLine(new string('-', 80));
        Console.WriteLine(
            "\nCloudWatch now ingests OpenTelemetry metrics natively. This scenario walks through" +
            "\nthat experience: it turns on OTel enrichment so CloudWatch can correlate incoming" +
            "\nOTLP metrics with the resources that produced them, alarms on those metrics with a" +
            "\nPromQL query, and shows you which individual series drove the alarm." +
            "\n" +
            "\nA PromQL alarm works differently from a classic metric alarm. Rather than watching" +
            "\none metric and counting breaching periods, it evaluates a query that can match many" +
            "\nseries at once, and tracks each one separately as a contributor.\n");

        try
        {
            var namespaces = await ListMetricsAndNamespaces();
            await StartOTelEnrichment();
            ExplainOtlpIngestion();
            await CreatePromQlAlarm();
            await InspectAlarmContributors();
            await GetStatisticsAndChartMetric(namespaces);
            await MuteAlarmForMaintenance();
            await CleanUp();

            Console.WriteLine(new string('-', 80));
            Console.WriteLine("CloudWatch Basics scenario is complete.");
            Console.WriteLine(new string('-', 80));
        }
        catch (Exception ex)
        {
            Console.WriteLine(new string('-', 80));
            logger.LogError(ex, "There was a problem executing the scenario.");
            await CleanUp();
            Console.WriteLine(new string('-', 80));
        }
    }

    /// <summary>
    /// List the metrics and namespaces already present in the account, to orient the
    /// reader before any configuration happens.
    /// </summary>
    /// <returns>The distinct namespaces found.</returns>
    private static async Task<List<string>> ListMetricsAndNamespaces()
    {
        Console.WriteLine(new string('-', 80));
        Console.WriteLine("1. List metrics and namespaces");
        Console.WriteLine(
            "\nBefore configuring anything, let's see what CloudWatch is already collecting in" +
            "\nthis account by calling ListMetrics.\n");

        var metrics = await _cloudWatchWrapper.ListMetrics();

        // Order by metric count descending, so the most-populated namespace comes first.
        // Step 6 charts a metric from that namespace, and a busy namespace is the one most
        // likely to have datapoints worth looking at.
        var namespaceCounts = metrics
            .GroupBy(m => m.Namespace)
            .Select(g => new { Namespace = g.Key, Count = g.Count() })
            .OrderByDescending(n => n.Count)
            .ToList();
        var namespaces = namespaceCounts.Select(n => n.Namespace).ToList();

        Console.WriteLine($"\tFound {metrics.Count} metrics across {namespaces.Count} namespaces:");
        foreach (var entry in namespaceCounts.Take(10))
        {
            Console.WriteLine($"\t  {entry.Namespace} ({entry.Count} metrics)");
        }

        if (!namespaces.Any())
        {
            Console.WriteLine(
                "\tNo metrics found in this account. The statistics and dashboard steps later on" +
                "\n\tneed an existing metric, so they will be skipped.");
        }

        Console.WriteLine(new string('-', 80));
        return namespaces;
    }

    /// <summary>
    /// Start OTel enrichment, but only if it is not already running. Enrichment is what
    /// makes CloudWatch attach AWS resource context to incoming OTLP metrics.
    /// </summary>
    private static async Task StartOTelEnrichment()
    {
        Console.WriteLine(new string('-', 80));
        Console.WriteLine("2. Start OpenTelemetry enrichment");
        Console.WriteLine(
            "\nEnrichment is what lets CloudWatch attach AWS resource context to the OTLP metrics" +
            "\nyou send it. Without it, your metrics arrive as opaque series with no connection to" +
            "\nthe resources that emitted them." +
            "\n" +
            "\nWe check the current state first, and only start enrichment if it isn't already on.\n");

        var status = await _otelWrapper.GetOTelEnrichmentStatus();
        Console.WriteLine($"\tEnrichment status: {status}");

        if (status != OTelEnrichmentStatus.Running)
        {
            // Record the attempt before making it. We already know enrichment was not running,
            // so stopping it during cleanup is always safe, and a call that starts enrichment
            // but then fails to report back (a timeout, say) would otherwise leave it running.
            _startedEnrichment = true;
            await _otelWrapper.StartOTelEnrichment();

            status = await _otelWrapper.GetOTelEnrichmentStatus();
            Console.WriteLine($"\tEnrichment status: {status}");
            Console.WriteLine(
                "\n\tNote: this run started enrichment, so the cleanup step will stop it again.");
        }
        else
        {
            Console.WriteLine(
                "\n\tEnrichment was already running, so we will leave it alone. The cleanup step" +
                "\n\twill not stop it, because other workloads in this account may depend on it.");
        }

        Console.WriteLine(new string('-', 80));
    }

    /// <summary>
    /// Explain that OTLP metric ingestion is not an AWS SDK operation. This step makes no
    /// service call; naming the gap explicitly is the point.
    /// </summary>
    private static void ExplainOtlpIngestion()
    {
        Console.WriteLine(new string('-', 80));
        Console.WriteLine("3. Send OTLP metrics to CloudWatch");
        Console.WriteLine(
            "\nThis step is not an AWS SDK operation, and that's worth being explicit about." +
            "\nMetrics reach CloudWatch over the OTLP protocol, through the CloudWatch agent, an" +
            "\nOpenTelemetry Collector, or an ADOT SDK. There is no PutOTelMetrics API to call." +
            "\n" +
            "\nPoint your collector at the CloudWatch metrics endpoint, which follows the pattern" +
            "\n\thttps://monitoring.<region>.amazonaws.com/v1/metrics" +
            "\n" +
            "\nThe endpoint is HTTP/1.1 only and does not support gRPC, so use an otlphttp" +
            "\nexporter rather than otlp. The metrics endpoint signs as \"monitoring\".\n");
        Console.WriteLine(new string('-', 80));
    }

    /// <summary>
    /// Create an alarm whose evaluation is a PromQL query.
    /// </summary>
    private static async Task CreatePromQlAlarm()
    {
        Console.WriteLine(new string('-', 80));
        Console.WriteLine("4. Create a PromQL alarm");
        Console.WriteLine(
            "\nNow we alarm on those metrics. The comparison goes inside the query itself: a" +
            "\nPromQL alarm has no separate threshold, comparison operator, statistic, or period.\n");

        Console.WriteLine($"Enter a PromQL query, or press <ENTER> for the default\n[{DefaultQuery}]:");
        var input = Console.ReadLine();
        var query = string.IsNullOrWhiteSpace(input) ? DefaultQuery : input.Trim();

        await _otelWrapper.PutPromQLMetricAlarm(_alarmName, query,
            EvaluationInterval, PendingPeriod, RecoveryPeriod);

        Console.WriteLine($"\tCreated alarm {_alarmName}:");
        Console.WriteLine($"\t  query:              {query}");
        Console.WriteLine($"\t  evaluationInterval: {EvaluationInterval} seconds");
        Console.WriteLine($"\t  pendingPeriod:      {PendingPeriod} seconds");
        Console.WriteLine($"\t  recoveryPeriod:     {RecoveryPeriod} seconds");
        Console.WriteLine(
            "\n\tA PromQL alarm starts in the OK state rather than INSUFFICIENT_DATA, which is" +
            "\n\tanother way it differs from a classic alarm.");

        Console.WriteLine(new string('-', 80));
    }

    /// <summary>
    /// Show which individual series the alarm's query matched. This is the step with no
    /// classic-alarm equivalent.
    /// </summary>
    private static async Task InspectAlarmContributors()
    {
        Console.WriteLine(new string('-', 80));
        Console.WriteLine("5. Inspect the alarm's contributors");
        Console.WriteLine(
            "\nEach contributor is one series the query matched, identified by its label set." +
            "\nThis is how you find out which host is unhealthy rather than only that something" +
            "\nis. Classic alarms have no equivalent.\n");

        var contributors = await _otelWrapper.DescribeAlarmContributors(_alarmName);

        if (!contributors.Any())
        {
            Console.WriteLine(
                "\tNo contributors yet. The query matched no series, which usually means no OTel" +
                "\n\tmetrics with these labels have arrived. Once your collector is sending data," +
                "\n\teach matching series appears here with its labels and why it breached.");
        }
        else
        {
            Console.WriteLine($"\tFound {contributors.Count} contributors:");
            foreach (var contributor in contributors)
            {
                var labels = string.Join(", ",
                    contributor.ContributorAttributes.Select(a => $"{a.Key}={a.Value}"));
                Console.WriteLine($"\t  {contributor.ContributorId}: {labels}");
                Console.WriteLine($"\t    reason: {contributor.StateReason}");
            }
        }

        Console.WriteLine(new string('-', 80));
    }

    /// <summary>
    /// Get statistics for an existing metric and chart it on a dashboard, so the reader can
    /// see what the alarm is evaluating.
    /// </summary>
    /// <param name="namespaces">The namespaces discovered in step 1.</param>
    private static async Task GetStatisticsAndChartMetric(List<string> namespaces)
    {
        Console.WriteLine(new string('-', 80));
        Console.WriteLine("6. Get statistics and chart the metric on a dashboard");
        Console.WriteLine("\nStatistics and dashboards are how you see what the alarm is evaluating.\n");

        if (!namespaces.Any())
        {
            Console.WriteLine("\tSkipping statistics and dashboard because no metrics exist yet.");
            Console.WriteLine(new string('-', 80));
            return;
        }

        var metricNamespace = namespaces.First();
        var metrics = await _cloudWatchWrapper.ListMetrics(metricNamespace);
        var metric = metrics.FirstOrDefault();

        if (metric != null)
        {
            var datapoints = await _cloudWatchWrapper.GetMetricStatistics(
                metricNamespace, metric.MetricName, new List<string> { "Average", "Maximum" },
                metric.Dimensions, 1, 3600);

            Console.WriteLine(
                $"\tStatistics for {metricNamespace} {metric.MetricName} over the last day:");
            Console.WriteLine($"\t  Datapoints: {datapoints.Count}");
            foreach (var datapoint in datapoints.Take(3))
            {
                Console.WriteLine(
                    $"\t  {datapoint.Timestamp:u} average {datapoint.Average}, maximum {datapoint.Maximum}");
            }

            var dashboardBody = BuildDashboardBody(metricNamespace, metric, _region);
            var validationMessages = await _cloudWatchWrapper.PutDashboard(_dashboardName, dashboardBody);
            _dashboardCreated = true;

            if (validationMessages.Any())
            {
                foreach (var message in validationMessages)
                {
                    Console.WriteLine($"\tDashboard validation message: {message.Message}");
                }
            }

            Console.WriteLine($"\tCreated dashboard {_dashboardName}.");

            var dashboard = await _cloudWatchWrapper.GetDashboard(_dashboardName);
            Console.WriteLine($"\tRead the dashboard back, {dashboard.Length} characters of widget JSON.");
        }
        else
        {
            Console.WriteLine($"\tNo metrics found in namespace {metricNamespace}, skipping.");
        }

        Console.WriteLine(new string('-', 80));
    }

    /// <summary>
    /// Build a single-widget dashboard body that charts the given metric.
    /// </summary>
    /// <param name="metricNamespace">The namespace of the metric to chart.</param>
    /// <param name="metric">The metric to chart.</param>
    /// <param name="region">The region the metric is in. A metric widget must name its
    /// region, because a dashboard can chart metrics from several.</param>
    internal static string BuildDashboardBody(string metricNamespace, Metric metric, string region)
    {
        var dimensionParts = string.Concat(
            metric.Dimensions.Select(d => $", \"{d.Name}\", \"{d.Value}\""));

        return $@"{{
    ""widgets"": [
        {{
            ""type"": ""text"",
            ""x"": 0, ""y"": 0, ""width"": 24, ""height"": 2,
            ""properties"": {{
                ""markdown"": ""This dashboard was created programmatically by an AWS SDK code example.""
            }}
        }},
        {{
            ""type"": ""metric"",
            ""x"": 0, ""y"": 2, ""width"": 12, ""height"": 6,
            ""properties"": {{
                ""metrics"": [[ ""{metricNamespace}"", ""{metric.MetricName}""{dimensionParts} ]],
                ""view"": ""timeSeries"",
                ""stat"": ""Average"",
                ""period"": 300,
                ""region"": ""{region}"",
                ""title"": ""{metric.MetricName}""
            }}
        }}
    ]
}}";
    }

    /// <summary>
    /// Create a mute rule so the alarm's actions are suppressed during a maintenance
    /// window, then read it back and find it in the account's rules.
    /// </summary>
    private static async Task MuteAlarmForMaintenance()
    {
        Console.WriteLine(new string('-', 80));
        Console.WriteLine("7. Mute the alarm for a maintenance window");
        Console.WriteLine(
            "\nWhile a mute rule is active the targeted alarms keep evaluating and keep changing" +
            "\nstate, but their actions do not fire. This is the supported way to suppress" +
            "\nnotifications during planned maintenance, instead of disabling alarm actions and" +
            "\nhoping someone remembers to turn them back on.\n");

        // The expression is a five-field cron expression,
        // cron(Minutes Hours Day-of-month Month Day-of-week). Note that this is five fields,
        // not the six that Amazon EventBridge uses. For a one-time window, use
        // at(yyyy-MM-ddThh:mm), with no seconds. The duration is an ISO 8601 duration from
        // PT1M to P15D, so PT2H rather than 2h.
        const string expression = "cron(0 2 * * SUN)";
        const string duration = "PT2H";
        const string timezone = "America/Los_Angeles";

        await _otelWrapper.PutAlarmMuteRule(_muteRuleName, expression, duration, timezone,
            new List<string> { _alarmName });

        Console.WriteLine($"\tCreated mute rule {_muteRuleName}:");
        Console.WriteLine($"\t  schedule: {expression} for {duration}");
        Console.WriteLine($"\t  timezone: {timezone}");
        Console.WriteLine($"\t  targets:  {_alarmName}");
        Console.WriteLine(
            "\n\tNote the two formats here. The expression is a five-field cron expression, five" +
            "\n\trather than the six Amazon EventBridge uses. The duration is an ISO 8601" +
            "\n\tduration, so 'PT2H' and not '2h'." +
            "\n" +
            "\n\tAlso note that MuteTargets is set explicitly. If you leave it out, the rule" +
            "\n\tapplies to every alarm in the account.");

        var muteRule = await _otelWrapper.GetAlarmMuteRule(_muteRuleName);
        Console.WriteLine(
            $"\tRead the rule back: status {muteRule.Status}, mute type {muteRule.MuteType}.");

        var summaries = await _otelWrapper.ListAlarmMuteRules(_alarmName);
        Console.WriteLine($"\tFound {summaries.Count} mute rules targeting this alarm.");

        // Mute rule summaries carry no name field, only an ARN, so match on the ARN suffix.
        var match = summaries.FirstOrDefault(s =>
            s.AlarmMuteRuleArn.EndsWith($"/{_muteRuleName}") ||
            s.AlarmMuteRuleArn.EndsWith($":{_muteRuleName}"));

        if (match != null)
        {
            Console.WriteLine($"\t  matched by ARN: {match.AlarmMuteRuleArn} ({match.Status})");
        }

        Console.WriteLine(new string('-', 80));
    }

    /// <summary>
    /// Delete the resources the scenario created. Each deletion is attempted independently
    /// so that one failure does not leave the remaining resources behind.
    /// </summary>
    private static async Task CleanUp()
    {
        Console.WriteLine(new string('-', 80));
        Console.WriteLine("8. Clean up");
        Console.WriteLine("\nDelete the resources this scenario created? (y/n)");

        var response = Console.ReadLine();
        if (!string.Equals(response?.Trim(), "y", StringComparison.OrdinalIgnoreCase))
        {
            Console.WriteLine(
                "\tSkipping cleanup. Note that the alarm, dashboard, and mute rule are still in" +
                "\n\tyour account, and enrichment may still be running.");
            Console.WriteLine(new string('-', 80));
            return;
        }

        try
        {
            await _otelWrapper.DeleteAlarmMuteRule(_muteRuleName);
            Console.WriteLine($"\tDeleted mute rule {_muteRuleName}.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"\tCould not delete the mute rule: {ex.Message}");
        }

        try
        {
            await _cloudWatchWrapper.DeleteAlarms(new List<string> { _alarmName });
            Console.WriteLine($"\tDeleted alarm {_alarmName}.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"\tCould not delete the alarm: {ex.Message}");
        }

        if (_dashboardCreated)
        {
            try
            {
                await _cloudWatchWrapper.DeleteDashboards(new List<string> { _dashboardName });
                Console.WriteLine($"\tDeleted dashboard {_dashboardName}.");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"\tCould not delete the dashboard: {ex.Message}");
            }
        }

        if (_startedEnrichment)
        {
            try
            {
                await _otelWrapper.StopOTelEnrichment();
                Console.WriteLine("\tStopped OTel enrichment, because this run started it.");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"\tCould not stop OTel enrichment: {ex.Message}");
            }
        }
        else
        {
            Console.WriteLine(
                "\tLeft OTel enrichment running, because it was already on before this run.");
        }

        Console.WriteLine(new string('-', 80));
    }
}
```
Wrapper methods used by the scenario for the CloudWatch OpenTelemetry actions.

```
/// <summary>
/// Wrapper class for the OpenTelemetry features of Amazon CloudWatch: turning on OTel
/// enrichment so that CloudWatch vended metrics are queryable with PromQL, alarming on a
/// PromQL query, inspecting the individual series (contributors) that put a PromQL alarm
/// into ALARM, and muting alarm actions on a schedule.
///
/// Note that OTLP metric ingestion is not an AWS SDK operation. To send OpenTelemetry
/// metrics to CloudWatch, point an OpenTelemetry collector or the AWS Distro for
/// OpenTelemetry (ADOT) SDK at the CloudWatch OTLP metrics endpoint,
/// https://monitoring.{region}.amazonaws.com/v1/metrics. The operations here cover
/// everything you do after those metrics land in CloudWatch.
/// </summary>
public class CloudWatchOTelWrapper
{
    private readonly IAmazonCloudWatch _amazonCloudWatch;
    private readonly ILogger<CloudWatchOTelWrapper> _logger;

    /// <summary>
    /// Constructor for the CloudWatch OpenTelemetry wrapper.
    /// </summary>
    /// <param name="amazonCloudWatch">The injected CloudWatch client.</param>
    /// <param name="logger">The injected logger for the wrapper.</param>
    public CloudWatchOTelWrapper(IAmazonCloudWatch amazonCloudWatch, ILogger<CloudWatchOTelWrapper> logger)
    {
        _logger = logger;
        _amazonCloudWatch = amazonCloudWatch;
    }
```
Wrapper methods used by the scenario for the metric, statistic, and dashboard actions.

```
/// <summary>
/// Wrapper class for Amazon CloudWatch methods.
/// </summary>
public class CloudWatchWrapper
{
    private readonly IAmazonCloudWatch _amazonCloudWatch;
    private readonly ILogger<CloudWatchWrapper> _logger;

    /// <summary>
    /// Constructor for the CloudWatch wrapper.
    /// </summary>
    /// <param name="amazonCloudWatch">The injected CloudWatch client.</param>
    /// <param name="logger">The injected logger for the wrapper.</param>
    public CloudWatchWrapper(IAmazonCloudWatch amazonCloudWatch, ILogger<CloudWatchWrapper> logger)

    {
        _logger = logger;
        _amazonCloudWatch = amazonCloudWatch;
    }

    /// <summary>
    /// List metrics available, optionally within a namespace.
    /// </summary>
    /// <param name="metricNamespace">Optional CloudWatch namespace to use when listing metrics.</param>
    /// <param name="filter">Optional dimension filter.</param>
    /// <param name="metricName">Optional metric name filter.</param>
    /// <returns>The list of metrics.</returns>
    public async Task<List<Metric>> ListMetrics(string? metricNamespace = null, DimensionFilter? filter = null, string? metricName = null)
    {
        var results = new List<Metric>();
        var paginateMetrics = _amazonCloudWatch.Paginators.ListMetrics(
            new ListMetricsRequest
            {
                Namespace = metricNamespace,
                Dimensions = filter != null ? new List<DimensionFilter> { filter } : null,
                MetricName = metricName
            });
        // Get the entire list using the paginator.
        await foreach (var metric in paginateMetrics.Metrics)
        {
            results.Add(metric);
        }

        return results;
    }

    /// <summary>
    /// Wrapper to get statistics for a specific CloudWatch metric.
    /// </summary>
    /// <param name="metricNamespace">The namespace of the metric.</param>
    /// <param name="metricName">The name of the metric.</param>
    /// <param name="statistics">The list of statistics to include.</param>
    /// <param name="dimensions">The list of dimensions to include.</param>
    /// <param name="days">The number of days in the past to include.</param>
    /// <param name="period">The period for the data.</param>
    /// <returns>A list of DataPoint objects for the statistics.</returns>
    public async Task<List<Datapoint>> GetMetricStatistics(string metricNamespace,
        string metricName, List<string> statistics, List<Dimension> dimensions, int days, int period)
    {
        var metricStatistics = await _amazonCloudWatch.GetMetricStatisticsAsync(
            new GetMetricStatisticsRequest()
            {
                Namespace = metricNamespace,
                MetricName = metricName,
                Dimensions = dimensions,
                Statistics = statistics,
                StartTime = DateTime.UtcNow.AddDays(-days),
                EndTime = DateTime.UtcNow,
                Period = period
            });

        return metricStatistics.Datapoints ?? new List<Datapoint>();
    }

    /// <summary>
    /// Wrapper to create or add to a dashboard with metrics.
    /// </summary>
    /// <param name="dashboardName">The name for the dashboard.</param>
    /// <param name="dashboardBody">The metric data in JSON for the dashboard.</param>
    /// <returns>A list of validation messages for the dashboard.</returns>
    public async Task<List<DashboardValidationMessage>> PutDashboard(string dashboardName,
        string dashboardBody)
    {
        // Updating a dashboard replaces all contents.
        // Best practice is to include a text widget indicating this dashboard was created programmatically.
        var dashboardResponse = await _amazonCloudWatch.PutDashboardAsync(
            new PutDashboardRequest()
            {
                DashboardName = dashboardName,
                DashboardBody = dashboardBody
            });

        return dashboardResponse.DashboardValidationMessages ?? new List<DashboardValidationMessage>();
    }

    /// <summary>
    /// Get information on a dashboard.
    /// </summary>
    /// <param name="dashboardName">The name of the dashboard.</param>
    /// <returns>A JSON object with dashboard information.</returns>
    public async Task<string> GetDashboard(string dashboardName)
    {
        var dashboardResponse = await _amazonCloudWatch.GetDashboardAsync(
            new GetDashboardRequest()
            {
                DashboardName = dashboardName
            });

        return dashboardResponse.DashboardBody;
    }

    /// <summary>
    /// Get a list of dashboards.
    /// </summary>
    /// <returns>A list of DashboardEntry objects.</returns>
    public async Task<List<DashboardEntry>> ListDashboards()
    {
        var results = new List<DashboardEntry>();
        var paginateDashboards = _amazonCloudWatch.Paginators.ListDashboards(
            new ListDashboardsRequest());
        // Get the entire list using the paginator.
        await foreach (var data in paginateDashboards.DashboardEntries)
        {
            results.Add(data);
        }

        return results;
    }

    /// <summary>
    /// Wrapper to add metric data to a CloudWatch metric.
    /// </summary>
    /// <param name="metricNamespace">The namespace of the metric.</param>
    /// <param name="metricData">A data object for the metric data.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> PutMetricData(string metricNamespace,
        List<MetricDatum> metricData)
    {
        var putDataResponse = await _amazonCloudWatch.PutMetricDataAsync(
            new PutMetricDataRequest()
            {
                MetricData = metricData,
                Namespace = metricNamespace,
            });

        return putDataResponse.HttpStatusCode == HttpStatusCode.OK;
    }

    /// <summary>
    /// Get an image for a metric graphed over time.
    /// </summary>
    /// <param name="metricNamespace">The namespace of the metric.</param>
    /// <param name="metric">The name of the metric.</param>
    /// <param name="stat">The name of the stat to chart.</param>
    /// <param name="period">The period to use for the chart.</param>
    /// <returns>A memory stream for the chart image.</returns>
    public async Task<MemoryStream> GetTimeSeriesMetricImage(string metricNamespace, string metric, string stat, int period)
    {
        var metricImageWidget = new
        {
            title = "Example Metric Graph",
            view = "timeSeries",
            stacked = false,
            period = period,
            width = 1400,
            height = 600,
            metrics = new List<List<object>>
                { new() { metricNamespace, metric, new { stat } } }
        };

        var metricImageWidgetString = JsonSerializer.Serialize(metricImageWidget);
        var imageResponse = await _amazonCloudWatch.GetMetricWidgetImageAsync(
            new GetMetricWidgetImageRequest()
            {
                MetricWidget = metricImageWidgetString
            });

        return imageResponse.MetricWidgetImage;
    }

    /// <summary>
    /// Save a metric image to a file.
    /// </summary>
    /// <param name="memoryStream">The MemoryStream for the metric image.</param>
    /// <param name="metricName">The name of the metric.</param>
    /// <returns>The path to the file.</returns>
    public string SaveMetricImage(MemoryStream memoryStream, string metricName)
    {
        var metricFileName = $"{metricName}_{DateTime.Now.Ticks}.png";
        using var sr = new StreamReader(memoryStream);
        // Writes the memory stream to a file.
        File.WriteAllBytes(metricFileName, memoryStream.ToArray());
        var filePath = Path.Join(AppDomain.CurrentDomain.BaseDirectory,
            metricFileName);
        return filePath;
    }

    /// <summary>
    /// Get data for CloudWatch metrics.
    /// </summary>
    /// <param name="minutesOfData">The number of minutes of data to include.</param>
    /// <param name="useDescendingTime">True to return the data descending by time.</param>
    /// <param name="endDateUtc">The end date for the data, in UTC.</param>
    /// <param name="maxDataPoints">The maximum data points to include.</param>
    /// <param name="dataQueries">Optional data queries to include.</param>
    /// <returns>A list of the requested metric data.</returns>
    public async Task<List<MetricDataResult>> GetMetricData(int minutesOfData, bool useDescendingTime, DateTime? endDateUtc = null,
        int maxDataPoints = 0, List<MetricDataQuery>? dataQueries = null)
    {
        var metricData = new List<MetricDataResult>();
        // If no end time is provided, use the current time for the end time.
        endDateUtc ??= DateTime.UtcNow;
        var timeZoneOffset = TimeZoneInfo.Local.GetUtcOffset(endDateUtc.Value.ToLocalTime());
        var startTimeUtc = endDateUtc.Value.AddMinutes(-minutesOfData);
        // The timezone string should be in the format +0000, so use the timezone offset to format it correctly.
        var timeZoneString = $"{timeZoneOffset.Hours:D2}{timeZoneOffset.Minutes:D2}";
        // Add the plus sign for positive offsets.
        timeZoneString = timeZoneString.StartsWith('-') ? timeZoneString : "+" + timeZoneString;
        var paginatedMetricData = _amazonCloudWatch.Paginators.GetMetricData(
            new GetMetricDataRequest()
            {
                StartTime = startTimeUtc,
                EndTime = endDateUtc.Value,
                LabelOptions = new LabelOptions { Timezone = timeZoneString },
                ScanBy = useDescendingTime ? ScanBy.TimestampDescending : ScanBy.TimestampAscending,
                MaxDatapoints = maxDataPoints,
                MetricDataQueries = dataQueries,
            });

        if (paginatedMetricData.MetricDataResults != null)
        {
            await foreach (var data in paginatedMetricData.MetricDataResults)
            {
                metricData.Add(data);
            }
        }

        return metricData;
    }

    /// <summary>
    /// Add a metric alarm to send an email when the metric passes a threshold.
    /// </summary>
    /// <param name="alarmDescription">A description of the alarm.</param>
    /// <param name="alarmName">The name for the alarm.</param>
    /// <param name="comparison">The type of comparison to use.</param>
    /// <param name="metricName">The name of the metric for the alarm.</param>
    /// <param name="metricNamespace">The namespace of the metric.</param>
    /// <param name="threshold">The threshold value for the alarm.</param>
    /// <param name="alarmActions">Optional actions to execute when in an alarm state.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> PutMetricEmailAlarm(string alarmDescription, string alarmName, ComparisonOperator comparison,
        string metricName, string metricNamespace, double threshold, List<string> alarmActions = null!)
    {
        try
        {
            var putEmailAlarmResponse = await _amazonCloudWatch.PutMetricAlarmAsync(
                new PutMetricAlarmRequest()
                {
                    AlarmActions = alarmActions,
                    AlarmDescription = alarmDescription,
                    AlarmName = alarmName,
                    ComparisonOperator = comparison,
                    Threshold = threshold,
                    Namespace = metricNamespace,
                    MetricName = metricName,
                    EvaluationPeriods = 1,
                    Period = 10,
                    Statistic = new Statistic("Maximum"),
                    DatapointsToAlarm = 1,
                    TreatMissingData = "ignore"
                });
            return putEmailAlarmResponse.HttpStatusCode == HttpStatusCode.OK;
        }
        catch (LimitExceededException lex)
        {
            _logger.LogError(lex, $"Unable to add alarm {alarmName}. Alarm quota has already been reached.");
        }

        return false;
    }

    /// <summary>
    /// Add specific email actions to a list of action strings for a CloudWatch alarm.
    /// </summary>
    /// <param name="accountId">The AccountId for the alarm.</param>
    /// <param name="region">The region for the alarm.</param>
    /// <param name="emailTopicName">An Amazon Simple Notification Service (SNS) topic for the alarm email.</param>
    /// <param name="alarmActions">Optional list of existing alarm actions to append to.</param>
    /// <returns>A list of string actions for an alarm.</returns>
    public List<string> AddEmailAlarmAction(string accountId, string region,
        string emailTopicName, List<string>? alarmActions = null)
    {
        alarmActions ??= new List<string>();
        var snsAlarmAction = $"arn:aws:sns:{region}:{accountId}:{emailTopicName}";
        alarmActions.Add(snsAlarmAction);
        return alarmActions;
    }

    /// <summary>
    /// Describe the current alarms, optionally filtered by state.
    /// </summary>
    /// <param name="stateValue">Optional filter for alarm state.</param>
    /// <returns>The list of alarm data.</returns>
    public async Task<List<MetricAlarm>> DescribeAlarms(StateValue? stateValue = null)
    {
        List<MetricAlarm> alarms = new List<MetricAlarm>();
        var paginatedDescribeAlarms = _amazonCloudWatch.Paginators.DescribeAlarms(
            new DescribeAlarmsRequest()
            {
                StateValue = stateValue
            });

        await foreach (var data in paginatedDescribeAlarms.MetricAlarms)
        {
            alarms.Add(data);
        }
        return alarms;
    }

    /// <summary>
    /// Describe the current alarms for a specific metric.
    /// </summary>
    /// <param name="metricNamespace">The namespace of the metric.</param>
    /// <param name="metricName">The name of the metric.</param>
    /// <returns>The list of alarm data.</returns>
    public async Task<List<MetricAlarm>> DescribeAlarmsForMetric(string metricNamespace, string metricName)
    {
        var alarmsResult = await _amazonCloudWatch.DescribeAlarmsForMetricAsync(
            new DescribeAlarmsForMetricRequest()
            {
                Namespace = metricNamespace,
                MetricName = metricName
            });

        return alarmsResult.MetricAlarms ?? new List<MetricAlarm>();
    }

    /// <summary>
    /// Describe the history of an alarm for a number of days in the past.
    /// </summary>
    /// <param name="alarmName">The name of the alarm.</param>
    /// <param name="historyDays">The number of days in the past.</param>
    /// <returns>The list of alarm history data.</returns>
    public async Task<List<AlarmHistoryItem>> DescribeAlarmHistory(string alarmName, int historyDays)
    {
        List<AlarmHistoryItem> alarmHistory = new List<AlarmHistoryItem>();
        var paginatedAlarmHistory = _amazonCloudWatch.Paginators.DescribeAlarmHistory(
            new DescribeAlarmHistoryRequest()
            {
                AlarmName = alarmName,
                EndDate = DateTime.UtcNow,
                HistoryItemType = HistoryItemType.StateUpdate,
                StartDate = DateTime.UtcNow.AddDays(-historyDays)
            });

        await foreach (var data in paginatedAlarmHistory.AlarmHistoryItems)
        {
            alarmHistory.Add(data);
        }
        return alarmHistory;
    }

    /// <summary>
    /// Delete a list of alarms from CloudWatch.
    /// </summary>
    /// <param name="alarmNames">A list of names of alarms to delete.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DeleteAlarms(List<string> alarmNames)
    {
        var deleteAlarmsResult = await _amazonCloudWatch.DeleteAlarmsAsync(
            new DeleteAlarmsRequest()
            {
                AlarmNames = alarmNames
            });

        return deleteAlarmsResult.HttpStatusCode == HttpStatusCode.OK;
    }

    /// <summary>
    /// Disable the actions for a list of alarms from CloudWatch.
    /// </summary>
    /// <param name="alarmNames">A list of names of alarms.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DisableAlarmActions(List<string> alarmNames)
    {
        var disableAlarmActionsResult = await _amazonCloudWatch.DisableAlarmActionsAsync(
            new DisableAlarmActionsRequest()
            {
                AlarmNames = alarmNames
            });

        return disableAlarmActionsResult.HttpStatusCode == HttpStatusCode.OK;
    }

    /// <summary>
    /// Enable the actions for a list of alarms from CloudWatch.
    /// </summary>
    /// <param name="alarmNames">A list of names of alarms.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> EnableAlarmActions(List<string> alarmNames)
    {
        var enableAlarmActionsResult = await _amazonCloudWatch.EnableAlarmActionsAsync(
            new EnableAlarmActionsRequest()
            {
                AlarmNames = alarmNames
            });

        return enableAlarmActionsResult.HttpStatusCode == HttpStatusCode.OK;
    }

    /// <summary>
    /// Add an anomaly detector for a single metric.
    /// </summary>
    /// <param name="anomalyDetector">A single metric anomaly detector.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> PutAnomalyDetector(SingleMetricAnomalyDetector anomalyDetector)
    {
        var putAlarmDetectorResult = await _amazonCloudWatch.PutAnomalyDetectorAsync(
            new PutAnomalyDetectorRequest()
            {
                SingleMetricAnomalyDetector = anomalyDetector
            });

        return putAlarmDetectorResult.HttpStatusCode == HttpStatusCode.OK;
    }

    /// <summary>
    /// Describe anomaly detectors for a metric and namespace.
    /// </summary>
    /// <param name="metricNamespace">The namespace of the metric.</param>
    /// <param name="metricName">The metric of the anomaly detectors.</param>
    /// <returns>The list of detectors.</returns>
    public async Task<List<AnomalyDetector>> DescribeAnomalyDetectors(string metricNamespace, string metricName)
    {
        List<AnomalyDetector> detectors = new List<AnomalyDetector>();
        var paginatedDescribeAnomalyDetectors = _amazonCloudWatch.Paginators.DescribeAnomalyDetectors(
            new DescribeAnomalyDetectorsRequest()
            {
                MetricName = metricName,
                Namespace = metricNamespace
            });

        await foreach (var data in paginatedDescribeAnomalyDetectors.AnomalyDetectors)
        {
            detectors.Add(data);
        }

        return detectors;
    }

    /// <summary>
    /// Delete a single metric anomaly detector.
    /// </summary>
    /// <param name="anomalyDetector">The anomaly detector to delete.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DeleteAnomalyDetector(SingleMetricAnomalyDetector anomalyDetector)
    {
        var deleteAnomalyDetectorResponse = await _amazonCloudWatch.DeleteAnomalyDetectorAsync(
            new DeleteAnomalyDetectorRequest()
            {
                SingleMetricAnomalyDetector = anomalyDetector
            });

        return deleteAnomalyDetectorResponse.HttpStatusCode == HttpStatusCode.OK;
    }

    /// <summary>
    /// Delete a list of CloudWatch dashboards.
    /// </summary>
    /// <param name="dashboardNames">List of dashboard names to delete.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DeleteDashboards(List<string> dashboardNames)
    {
        var deleteDashboardsResponse = await _amazonCloudWatch.DeleteDashboardsAsync(
            new DeleteDashboardsRequest()
            {
                DashboardNames = dashboardNames
            });

        return deleteDashboardsResponse.HttpStatusCode == HttpStatusCode.OK;
    }
}
```
Example settings.json values for the scenario.

```
{
  "dashboardName": "example-new-dashboard",
  "exampleAlarmName": "example-metric-alarm",
  "accountId": "1234567890",
  "region": "us-east-1",
  "emailTopic": "Default_CloudWatch_Alarms_Topic",
  "customMetricNamespace": "example-namespace",
  "customMetricName": "example-custom-metric",
  "dashboardExampleBody": {
    "widgets": [
      {
        "height": 6,
        "width": 6,
        "y": 0,
        "x": 0,
        "type": "text",
        "properties": {
          "markdown": "# Code Example Dashboard \nThis dashboard was created by example code.\n"
        }
      },
      {
        "height": 8,
        "width": 8,
        "y": 0,
        "x": 6,
        "type": "metric",
        "properties": {
          "metrics": [
            [
              "AWS/Billing",
              "EstimatedCharges",
              "Currency",
              "USD",
              { "region": "us-east-1" }
            ]
          ],
          "view": "timeSeries",
          "region": "us-east-1",
          "stat": "Maximum",
          "period": 86400,
          "yAxis": {
            "left": {
              "min": 0,
              "max": 100
            }
          },
          "stacked": false,
          "title": "Estimated Billing",
          "setPeriodToTimeRange": false,
          "liveData": true,
          "sparkline": true,
          "trend": true
        }
      },
      {
        "height": 8,
        "width": 8,
        "y": 0,
        "x": 14,
        "type": "metric",
        "properties": {
          "metrics": [
            [ "AWS/Usage", "CallCount", "Type", "API", "Resource", "ListMetrics", "Service", "CloudWatch", "Class", "None" ],
            [ "...", "GetMetricStatistics", ".", ".", ".", "." ],
            [ "...", "GetMetricData", ".", ".", ".", "." ],
            [ "...", "PutDashboard", ".", ".", ".", "." ],
            [ "...", "PutMetricData", ".", ".", ".", "." ]
          ],
          "view": "timeSeries",
          "yAxis": {
            "left": {
              "min": 0,
              "max": 200
            }
          },
          "stacked": false,
          "region": "us-east-1",
          "stat": "Sum",
          "period": 300,
          "title": "CloudWatch Usage",
          "setPeriodToTimeRange": false,
          "liveData": true,
          "sparkline": true,
          "trend": true
        }
      }
    ]
  }
}
```
+ For API details, see the following topics in *AWS SDK for .NET API Reference*.
  + [DeleteAlarmMuteRule](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DeleteAlarmMuteRule)
  + [DeleteAlarms](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DeleteAlarms)
  + [DeleteDashboards](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DeleteDashboards)
  + [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DescribeAlarmContributors)
  + [GetAlarmMuteRule](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetAlarmMuteRule)
  + [GetDashboard](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetDashboard)
  + [GetMetricStatistics](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetMetricStatistics)
  + [GetOTelEnrichment](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetOTelEnrichment)
  + [ListAlarmMuteRules](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/ListAlarmMuteRules)
  + [ListDashboards](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/ListDashboards)
  + [ListMetrics](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/ListMetrics)
  + [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutAlarmMuteRule)
  + [PutDashboard](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutDashboard)
  + [PutMetricAlarm](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutMetricAlarm)
  + [StartOTelEnrichment](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/StartOTelEnrichment)
  + [StopOTelEnrichment](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/StopOTelEnrichment)

## Actions
<a name="actions"></a>

### `DeleteAlarmMuteRule`
<a name="cloudwatch_DeleteAlarmMuteRule_csharp_4_topic"></a>

The following code example shows how to use `DeleteAlarmMuteRule`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Delete an alarm mute rule. The alarms it targeted resume firing their actions.
    /// </summary>
    /// <param name="name">The name of the mute rule.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DeleteAlarmMuteRule(string name)
    {
        var response = await _amazonCloudWatch.DeleteAlarmMuteRuleAsync(
            new DeleteAlarmMuteRuleRequest
            {
                AlarmMuteRuleName = name
            });

        _logger.LogInformation($"Deleted alarm mute rule {name}.");
        return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
    }
```
+  For API details, see [DeleteAlarmMuteRule](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DeleteAlarmMuteRule) in *AWS SDK for .NET API Reference*.

### `DeleteAlarms`
<a name="cloudwatch_DeleteAlarms_csharp_4_topic"></a>

The following code example shows how to use `DeleteAlarms`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Delete a list of alarms from CloudWatch.
    /// </summary>
    /// <param name="alarmNames">A list of names of alarms to delete.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DeleteAlarms(List<string> alarmNames)
    {
        var deleteAlarmsResult = await _amazonCloudWatch.DeleteAlarmsAsync(
            new DeleteAlarmsRequest()
            {
                AlarmNames = alarmNames
            });

        return deleteAlarmsResult.HttpStatusCode == HttpStatusCode.OK;
    }
```
+  For API details, see [DeleteAlarms](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DeleteAlarms) in *AWS SDK for .NET API Reference*.

### `DeleteAnomalyDetector`
<a name="cloudwatch_DeleteAnomalyDetector_csharp_4_topic"></a>

The following code example shows how to use `DeleteAnomalyDetector`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Delete a single metric anomaly detector.
    /// </summary>
    /// <param name="anomalyDetector">The anomaly detector to delete.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DeleteAnomalyDetector(SingleMetricAnomalyDetector anomalyDetector)
    {
        var deleteAnomalyDetectorResponse = await _amazonCloudWatch.DeleteAnomalyDetectorAsync(
            new DeleteAnomalyDetectorRequest()
            {
                SingleMetricAnomalyDetector = anomalyDetector
            });

        return deleteAnomalyDetectorResponse.HttpStatusCode == HttpStatusCode.OK;
    }
```
+  For API details, see [DeleteAnomalyDetector](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DeleteAnomalyDetector) in *AWS SDK for .NET API Reference*.

### `DeleteDashboards`
<a name="cloudwatch_DeleteDashboards_csharp_4_topic"></a>

The following code example shows how to use `DeleteDashboards`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Delete a list of CloudWatch dashboards.
    /// </summary>
    /// <param name="dashboardNames">List of dashboard names to delete.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DeleteDashboards(List<string> dashboardNames)
    {
        var deleteDashboardsResponse = await _amazonCloudWatch.DeleteDashboardsAsync(
            new DeleteDashboardsRequest()
            {
                DashboardNames = dashboardNames
            });

        return deleteDashboardsResponse.HttpStatusCode == HttpStatusCode.OK;
    }
```
+  For API details, see [DeleteDashboards](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DeleteDashboards) in *AWS SDK for .NET API Reference*.

### `DescribeAlarmContributors`
<a name="cloudwatch_DescribeAlarmContributors_csharp_4_topic"></a>

The following code example shows how to use `DescribeAlarmContributors`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Get the contributors for a PromQL alarm. Each contributor is one series that the
    /// alarm's query matched, identified by its label set. This is how you find out which
    /// hosts, services, or pods are breaching, rather than only that something is.
    /// </summary>
    /// <param name="alarmName">The name of the PromQL alarm.</param>
    /// <returns>The list of contributors.</returns>
    public async Task<List<AlarmContributor>> DescribeAlarmContributors(string alarmName)
    {
        var results = new List<AlarmContributor>();
        string? nextToken = null;

        do
        {
            var response = await _amazonCloudWatch.DescribeAlarmContributorsAsync(
                new DescribeAlarmContributorsRequest
                {
                    AlarmName = alarmName,
                    NextToken = nextToken
                });

            if (response.AlarmContributors != null)
            {
                results.AddRange(response.AlarmContributors);
            }

            nextToken = response.NextToken;
        } while (!string.IsNullOrEmpty(nextToken));

        _logger.LogInformation($"Got {results.Count} contributors for alarm {alarmName}.");
        return results;
    }
```
+  For API details, see [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DescribeAlarmContributors) in *AWS SDK for .NET API Reference*.

### `DescribeAlarmHistory`
<a name="cloudwatch_DescribeAlarmHistory_csharp_4_topic"></a>

The following code example shows how to use `DescribeAlarmHistory`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Describe the history of an alarm for a number of days in the past.
    /// </summary>
    /// <param name="alarmName">The name of the alarm.</param>
    /// <param name="historyDays">The number of days in the past.</param>
    /// <returns>The list of alarm history data.</returns>
    public async Task<List<AlarmHistoryItem>> DescribeAlarmHistory(string alarmName, int historyDays)
    {
        List<AlarmHistoryItem> alarmHistory = new List<AlarmHistoryItem>();
        var paginatedAlarmHistory = _amazonCloudWatch.Paginators.DescribeAlarmHistory(
            new DescribeAlarmHistoryRequest()
            {
                AlarmName = alarmName,
                EndDate = DateTime.UtcNow,
                HistoryItemType = HistoryItemType.StateUpdate,
                StartDate = DateTime.UtcNow.AddDays(-historyDays)
            });

        await foreach (var data in paginatedAlarmHistory.AlarmHistoryItems)
        {
            alarmHistory.Add(data);
        }
        return alarmHistory;
    }
```
+  For API details, see [DescribeAlarmHistory](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DescribeAlarmHistory) in *AWS SDK for .NET API Reference*.

### `DescribeAlarms`
<a name="cloudwatch_DescribeAlarms_csharp_4_topic"></a>

The following code example shows how to use `DescribeAlarms`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Describe the current alarms, optionally filtered by state.
    /// </summary>
    /// <param name="stateValue">Optional filter for alarm state.</param>
    /// <returns>The list of alarm data.</returns>
    public async Task<List<MetricAlarm>> DescribeAlarms(StateValue? stateValue = null)
    {
        List<MetricAlarm> alarms = new List<MetricAlarm>();
        var paginatedDescribeAlarms = _amazonCloudWatch.Paginators.DescribeAlarms(
            new DescribeAlarmsRequest()
            {
                StateValue = stateValue
            });

        await foreach (var data in paginatedDescribeAlarms.MetricAlarms)
        {
            alarms.Add(data);
        }
        return alarms;
    }
```
+  For API details, see [DescribeAlarms](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DescribeAlarms) in *AWS SDK for .NET API Reference*.

### `DescribeAlarmsForMetric`
<a name="cloudwatch_DescribeAlarmsForMetric_csharp_4_topic"></a>

The following code example shows how to use `DescribeAlarmsForMetric`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Describe the current alarms for a specific metric.
    /// </summary>
    /// <param name="metricNamespace">The namespace of the metric.</param>
    /// <param name="metricName">The name of the metric.</param>
    /// <returns>The list of alarm data.</returns>
    public async Task<List<MetricAlarm>> DescribeAlarmsForMetric(string metricNamespace, string metricName)
    {
        var alarmsResult = await _amazonCloudWatch.DescribeAlarmsForMetricAsync(
            new DescribeAlarmsForMetricRequest()
            {
                Namespace = metricNamespace,
                MetricName = metricName
            });

        return alarmsResult.MetricAlarms ?? new List<MetricAlarm>();
    }
```
+  For API details, see [DescribeAlarmsForMetric](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DescribeAlarmsForMetric) in *AWS SDK for .NET API Reference*.

### `DescribeAnomalyDetectors`
<a name="cloudwatch_DescribeAnomalyDetectors_csharp_4_topic"></a>

The following code example shows how to use `DescribeAnomalyDetectors`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Describe anomaly detectors for a metric and namespace.
    /// </summary>
    /// <param name="metricNamespace">The namespace of the metric.</param>
    /// <param name="metricName">The metric of the anomaly detectors.</param>
    /// <returns>The list of detectors.</returns>
    public async Task<List<AnomalyDetector>> DescribeAnomalyDetectors(string metricNamespace, string metricName)
    {
        List<AnomalyDetector> detectors = new List<AnomalyDetector>();
        var paginatedDescribeAnomalyDetectors = _amazonCloudWatch.Paginators.DescribeAnomalyDetectors(
            new DescribeAnomalyDetectorsRequest()
            {
                MetricName = metricName,
                Namespace = metricNamespace
            });

        await foreach (var data in paginatedDescribeAnomalyDetectors.AnomalyDetectors)
        {
            detectors.Add(data);
        }

        return detectors;
    }
```
+  For API details, see [DescribeAnomalyDetectors](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DescribeAnomalyDetectors) in *AWS SDK for .NET API Reference*.

### `DisableAlarmActions`
<a name="cloudwatch_DisableAlarmActions_csharp_4_topic"></a>

The following code example shows how to use `DisableAlarmActions`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Disable the actions for a list of alarms from CloudWatch.
    /// </summary>
    /// <param name="alarmNames">A list of names of alarms.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DisableAlarmActions(List<string> alarmNames)
    {
        var disableAlarmActionsResult = await _amazonCloudWatch.DisableAlarmActionsAsync(
            new DisableAlarmActionsRequest()
            {
                AlarmNames = alarmNames
            });

        return disableAlarmActionsResult.HttpStatusCode == HttpStatusCode.OK;
    }
```
+  For API details, see [DisableAlarmActions](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DisableAlarmActions) in *AWS SDK for .NET API Reference*.

### `EnableAlarmActions`
<a name="cloudwatch_EnableAlarmActions_csharp_4_topic"></a>

The following code example shows how to use `EnableAlarmActions`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Enable the actions for a list of alarms from CloudWatch.
    /// </summary>
    /// <param name="alarmNames">A list of names of alarms.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> EnableAlarmActions(List<string> alarmNames)
    {
        var enableAlarmActionsResult = await _amazonCloudWatch.EnableAlarmActionsAsync(
            new EnableAlarmActionsRequest()
            {
                AlarmNames = alarmNames
            });

        return enableAlarmActionsResult.HttpStatusCode == HttpStatusCode.OK;
    }
```
+  For API details, see [EnableAlarmActions](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/EnableAlarmActions) in *AWS SDK for .NET API Reference*.

### `GetAlarmMuteRule`
<a name="cloudwatch_GetAlarmMuteRule_csharp_4_topic"></a>

The following code example shows how to use `GetAlarmMuteRule`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Get the full configuration of an alarm mute rule, including its schedule, the
    /// alarms it targets, and whether it is currently SCHEDULED, ACTIVE, or EXPIRED.
    /// </summary>
    /// <param name="name">The name of the mute rule.</param>
    /// <returns>The mute rule.</returns>
    public async Task<GetAlarmMuteRuleResponse> GetAlarmMuteRule(string name)
    {
        var response = await _amazonCloudWatch.GetAlarmMuteRuleAsync(
            new GetAlarmMuteRuleRequest
            {
                AlarmMuteRuleName = name
            });

        _logger.LogInformation($"Mute rule {response.Name} is {response.Status}.");
        return response;
    }
```
+  For API details, see [GetAlarmMuteRule](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetAlarmMuteRule) in *AWS SDK for .NET API Reference*.

### `GetDashboard`
<a name="cloudwatch_GetDashboard_csharp_4_topic"></a>

The following code example shows how to use `GetDashboard`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Get information on a dashboard.
    /// </summary>
    /// <param name="dashboardName">The name of the dashboard.</param>
    /// <returns>A JSON object with dashboard information.</returns>
    public async Task<string> GetDashboard(string dashboardName)
    {
        var dashboardResponse = await _amazonCloudWatch.GetDashboardAsync(
            new GetDashboardRequest()
            {
                DashboardName = dashboardName
            });

        return dashboardResponse.DashboardBody;
    }
```
+  For API details, see [GetDashboard](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetDashboard) in *AWS SDK for .NET API Reference*.

### `GetMetricData`
<a name="cloudwatch_GetMetricData_csharp_4_topic"></a>

The following code example shows how to use `GetMetricData`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Get data for CloudWatch metrics.
    /// </summary>
    /// <param name="minutesOfData">The number of minutes of data to include.</param>
    /// <param name="useDescendingTime">True to return the data descending by time.</param>
    /// <param name="endDateUtc">The end date for the data, in UTC.</param>
    /// <param name="maxDataPoints">The maximum data points to include.</param>
    /// <param name="dataQueries">Optional data queries to include.</param>
    /// <returns>A list of the requested metric data.</returns>
    public async Task<List<MetricDataResult>> GetMetricData(int minutesOfData, bool useDescendingTime, DateTime? endDateUtc = null,
        int maxDataPoints = 0, List<MetricDataQuery>? dataQueries = null)
    {
        var metricData = new List<MetricDataResult>();
        // If no end time is provided, use the current time for the end time.
        endDateUtc ??= DateTime.UtcNow;
        var timeZoneOffset = TimeZoneInfo.Local.GetUtcOffset(endDateUtc.Value.ToLocalTime());
        var startTimeUtc = endDateUtc.Value.AddMinutes(-minutesOfData);
        // The timezone string should be in the format +0000, so use the timezone offset to format it correctly.
        var timeZoneString = $"{timeZoneOffset.Hours:D2}{timeZoneOffset.Minutes:D2}";
        // Add the plus sign for positive offsets.
        timeZoneString = timeZoneString.StartsWith('-') ? timeZoneString : "+" + timeZoneString;
        var paginatedMetricData = _amazonCloudWatch.Paginators.GetMetricData(
            new GetMetricDataRequest()
            {
                StartTime = startTimeUtc,
                EndTime = endDateUtc.Value,
                LabelOptions = new LabelOptions { Timezone = timeZoneString },
                ScanBy = useDescendingTime ? ScanBy.TimestampDescending : ScanBy.TimestampAscending,
                MaxDatapoints = maxDataPoints,
                MetricDataQueries = dataQueries,
            });

        if (paginatedMetricData.MetricDataResults != null)
        {
            await foreach (var data in paginatedMetricData.MetricDataResults)
            {
                metricData.Add(data);
            }
        }

        return metricData;
    }
```
+  For API details, see [GetMetricData](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetMetricData) in *AWS SDK for .NET API Reference*.

### `GetMetricStatistics`
<a name="cloudwatch_GetMetricStatistics_csharp_4_topic"></a>

The following code example shows how to use `GetMetricStatistics`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Wrapper to get statistics for a specific CloudWatch metric.
    /// </summary>
    /// <param name="metricNamespace">The namespace of the metric.</param>
    /// <param name="metricName">The name of the metric.</param>
    /// <param name="statistics">The list of statistics to include.</param>
    /// <param name="dimensions">The list of dimensions to include.</param>
    /// <param name="days">The number of days in the past to include.</param>
    /// <param name="period">The period for the data.</param>
    /// <returns>A list of DataPoint objects for the statistics.</returns>
    public async Task<List<Datapoint>> GetMetricStatistics(string metricNamespace,
        string metricName, List<string> statistics, List<Dimension> dimensions, int days, int period)
    {
        var metricStatistics = await _amazonCloudWatch.GetMetricStatisticsAsync(
            new GetMetricStatisticsRequest()
            {
                Namespace = metricNamespace,
                MetricName = metricName,
                Dimensions = dimensions,
                Statistics = statistics,
                StartTime = DateTime.UtcNow.AddDays(-days),
                EndTime = DateTime.UtcNow,
                Period = period
            });

        return metricStatistics.Datapoints ?? new List<Datapoint>();
    }
```
+  For API details, see [GetMetricStatistics](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetMetricStatistics) in *AWS SDK for .NET API Reference*.

### `GetMetricWidgetImage`
<a name="cloudwatch_GetMetricWidgetImage_csharp_4_topic"></a>

The following code example shows how to use `GetMetricWidgetImage`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Get an image for a metric graphed over time.
    /// </summary>
    /// <param name="metricNamespace">The namespace of the metric.</param>
    /// <param name="metric">The name of the metric.</param>
    /// <param name="stat">The name of the stat to chart.</param>
    /// <param name="period">The period to use for the chart.</param>
    /// <returns>A memory stream for the chart image.</returns>
    public async Task<MemoryStream> GetTimeSeriesMetricImage(string metricNamespace, string metric, string stat, int period)
    {
        var metricImageWidget = new
        {
            title = "Example Metric Graph",
            view = "timeSeries",
            stacked = false,
            period = period,
            width = 1400,
            height = 600,
            metrics = new List<List<object>>
                { new() { metricNamespace, metric, new { stat } } }
        };

        var metricImageWidgetString = JsonSerializer.Serialize(metricImageWidget);
        var imageResponse = await _amazonCloudWatch.GetMetricWidgetImageAsync(
            new GetMetricWidgetImageRequest()
            {
                MetricWidget = metricImageWidgetString
            });

        return imageResponse.MetricWidgetImage;
    }

    /// <summary>
    /// Save a metric image to a file.
    /// </summary>
    /// <param name="memoryStream">The MemoryStream for the metric image.</param>
    /// <param name="metricName">The name of the metric.</param>
    /// <returns>The path to the file.</returns>
    public string SaveMetricImage(MemoryStream memoryStream, string metricName)
    {
        var metricFileName = $"{metricName}_{DateTime.Now.Ticks}.png";
        using var sr = new StreamReader(memoryStream);
        // Writes the memory stream to a file.
        File.WriteAllBytes(metricFileName, memoryStream.ToArray());
        var filePath = Path.Join(AppDomain.CurrentDomain.BaseDirectory,
            metricFileName);
        return filePath;
    }
```
+  For API details, see [GetMetricWidgetImage](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetMetricWidgetImage) in *AWS SDK for .NET API Reference*.

### `GetOTelEnrichment`
<a name="cloudwatch_GetOTelEnrichment_csharp_4_topic"></a>

The following code example shows how to use `GetOTelEnrichment`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Get the current OTel enrichment status for the account.
    /// </summary>
    /// <returns>The status, either Running or Stopped.</returns>
    public async Task<OTelEnrichmentStatus> GetOTelEnrichmentStatus()
    {
        var response = await _amazonCloudWatch.GetOTelEnrichmentAsync(
            new GetOTelEnrichmentRequest());

        _logger.LogInformation($"OTel enrichment status is {response.Status}.");
        return response.Status;
    }
```
+  For API details, see [GetOTelEnrichment](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetOTelEnrichment) in *AWS SDK for .NET API Reference*.

### `ListAlarmMuteRules`
<a name="cloudwatch_ListAlarmMuteRules_csharp_4_topic"></a>

The following code example shows how to use `ListAlarmMuteRules`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// List the alarm mute rules in the account, optionally filtered to the rules that
    /// target one alarm.
    /// </summary>
    /// <param name="alarmName">When specified, only rules that target this alarm are
    /// returned.</param>
    /// <returns>The list of mute rule summaries.</returns>
    public async Task<List<AlarmMuteRuleSummary>> ListAlarmMuteRules(string? alarmName = null)
    {
        var results = new List<AlarmMuteRuleSummary>();
        string? nextToken = null;

        do
        {
            var response = await _amazonCloudWatch.ListAlarmMuteRulesAsync(
                new ListAlarmMuteRulesRequest
                {
                    AlarmName = alarmName,
                    NextToken = nextToken
                });

            if (response.AlarmMuteRuleSummaries != null)
            {
                results.AddRange(response.AlarmMuteRuleSummaries);
            }

            nextToken = response.NextToken;
        } while (!string.IsNullOrEmpty(nextToken));

        _logger.LogInformation($"Got {results.Count} alarm mute rules.");
        return results;
    }
```
+  For API details, see [ListAlarmMuteRules](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/ListAlarmMuteRules) in *AWS SDK for .NET API Reference*.

### `ListDashboards`
<a name="cloudwatch_ListDashboards_csharp_4_topic"></a>

The following code example shows how to use `ListDashboards`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Get a list of dashboards.
    /// </summary>
    /// <returns>A list of DashboardEntry objects.</returns>
    public async Task<List<DashboardEntry>> ListDashboards()
    {
        var results = new List<DashboardEntry>();
        var paginateDashboards = _amazonCloudWatch.Paginators.ListDashboards(
            new ListDashboardsRequest());
        // Get the entire list using the paginator.
        await foreach (var data in paginateDashboards.DashboardEntries)
        {
            results.Add(data);
        }

        return results;
    }
```
+  For API details, see [ListDashboards](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/ListDashboards) in *AWS SDK for .NET API Reference*.

### `ListMetrics`
<a name="cloudwatch_ListMetrics_csharp_4_topic"></a>

The following code example shows how to use `ListMetrics`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// List metrics available, optionally within a namespace.
    /// </summary>
    /// <param name="metricNamespace">Optional CloudWatch namespace to use when listing metrics.</param>
    /// <param name="filter">Optional dimension filter.</param>
    /// <param name="metricName">Optional metric name filter.</param>
    /// <returns>The list of metrics.</returns>
    public async Task<List<Metric>> ListMetrics(string? metricNamespace = null, DimensionFilter? filter = null, string? metricName = null)
    {
        var results = new List<Metric>();
        var paginateMetrics = _amazonCloudWatch.Paginators.ListMetrics(
            new ListMetricsRequest
            {
                Namespace = metricNamespace,
                Dimensions = filter != null ? new List<DimensionFilter> { filter } : null,
                MetricName = metricName
            });
        // Get the entire list using the paginator.
        await foreach (var metric in paginateMetrics.Metrics)
        {
            results.Add(metric);
        }

        return results;
    }
```
+  For API details, see [ListMetrics](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/ListMetrics) in *AWS SDK for .NET API Reference*.

### `PutAlarmMuteRule`
<a name="cloudwatch_PutAlarmMuteRule_csharp_4_topic"></a>

The following code example shows how to use `PutAlarmMuteRule`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Create or update an alarm mute rule. While a mute rule is active the targeted
    /// alarms keep evaluating and keep transitioning between states, but their configured
    /// actions do not fire. This is the supported way to suppress notifications during a
    /// known maintenance window, instead of disabling alarm actions and relying on
    /// someone to turn them back on.
    /// </summary>
    /// <param name="name">The name of the mute rule.</param>
    /// <param name="expression">When the rule activates. For a recurring window, use a
    /// five-field cron expression, cron(Minutes Hours Day-of-month Month Day-of-week),
    /// such as cron(0 2 * * SUN) for every Sunday at 2:00 AM. Note that this is five
    /// fields, not the six that Amazon EventBridge uses. For a one-time window, use
    /// at(yyyy-MM-ddThh:mm), such as at(2026-09-05T02:00).</param>
    /// <param name="duration">How long the mute window lasts once it activates, in
    /// ISO 8601 duration format, from PT1M (one minute) to P15D (15 days). For example,
    /// PT2H is two hours and P2DT12H is two days and 12 hours.</param>
    /// <param name="timezone">The time zone the expression is evaluated in, such as
    /// America/Los_Angeles.</param>
    /// <param name="alarmNames">The names of up to 100 alarms to mute. If null or empty,
    /// the rule applies to all alarms in the account.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> PutAlarmMuteRule(string name, string expression, string duration,
        string timezone, List<string>? alarmNames = null)
    {
        var request = new PutAlarmMuteRuleRequest
        {
            Name = name,
            Description = "A mute rule created by the AWS SDK for .NET example.",
            Rule = new Rule
            {
                Schedule = new Schedule
                {
                    Expression = expression,
                    Duration = duration,
                    Timezone = timezone
                }
            }
        };

        if (alarmNames != null && alarmNames.Any())
        {
            request.MuteTargets = new MuteTargets { AlarmNames = alarmNames };
        }

        var response = await _amazonCloudWatch.PutAlarmMuteRuleAsync(request);

        _logger.LogInformation($"Put alarm mute rule {name}.");
        return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
    }
```
+  For API details, see [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutAlarmMuteRule) in *AWS SDK for .NET API Reference*.

### `PutAnomalyDetector`
<a name="cloudwatch_PutAnomalyDetector_csharp_4_topic"></a>

The following code example shows how to use `PutAnomalyDetector`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Add an anomaly detector for a single metric.
    /// </summary>
    /// <param name="anomalyDetector">A single metric anomaly detector.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> PutAnomalyDetector(SingleMetricAnomalyDetector anomalyDetector)
    {
        var putAlarmDetectorResult = await _amazonCloudWatch.PutAnomalyDetectorAsync(
            new PutAnomalyDetectorRequest()
            {
                SingleMetricAnomalyDetector = anomalyDetector
            });

        return putAlarmDetectorResult.HttpStatusCode == HttpStatusCode.OK;
    }
```
+  For API details, see [PutAnomalyDetector](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutAnomalyDetector) in *AWS SDK for .NET API Reference*.

### `PutDashboard`
<a name="cloudwatch_PutDashboard_csharp_4_topic"></a>

The following code example shows how to use `PutDashboard`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Wrapper to create or add to a dashboard with metrics.
    /// </summary>
    /// <param name="dashboardName">The name for the dashboard.</param>
    /// <param name="dashboardBody">The metric data in JSON for the dashboard.</param>
    /// <returns>A list of validation messages for the dashboard.</returns>
    public async Task<List<DashboardValidationMessage>> PutDashboard(string dashboardName,
        string dashboardBody)
    {
        // Updating a dashboard replaces all contents.
        // Best practice is to include a text widget indicating this dashboard was created programmatically.
        var dashboardResponse = await _amazonCloudWatch.PutDashboardAsync(
            new PutDashboardRequest()
            {
                DashboardName = dashboardName,
                DashboardBody = dashboardBody
            });

        return dashboardResponse.DashboardValidationMessages ?? new List<DashboardValidationMessage>();
    }
```
+  For API details, see [PutDashboard](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutDashboard) in *AWS SDK for .NET API Reference*.

### `PutMetricAlarm`
<a name="cloudwatch_PutMetricAlarm_csharp_4_topic"></a>

The following code example shows how to use `PutMetricAlarm`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).
Create an alarm that evaluates a PromQL query against OpenTelemetry metrics.

```
    /// <summary>
    /// Create an alarm that evaluates a PromQL query.
    ///
    /// A PromQL alarm differs from a classic metric alarm in a few ways. The query can
    /// match many series at once, and each matching series is tracked separately as a
    /// contributor. Instead of counting breaching periods, you specify durations: a
    /// contributor moves to ALARM after it breaches continuously for the pending period,
    /// and back to OK after it stops breaching for the recovery period. A PromQL alarm
    /// starts in the OK state rather than INSUFFICIENT_DATA.
    ///
    /// EvaluationCriteria is a union and is mutually exclusive with the classic
    /// MetricName and Metrics properties. When you use it you must also set
    /// EvaluationInterval, and you must not set Period, Statistic, Threshold,
    /// ComparisonOperator, EvaluationPeriods, DatapointsToAlarm, or TreatMissingData.
    /// </summary>
    /// <param name="alarmName">The name of the alarm, unique within the Region.</param>
    /// <param name="query">The PromQL query to evaluate, such as
    /// avg(cpu_utilization_percent) &gt; 80. The comparison belongs in the query itself;
    /// there is no separate threshold property.</param>
    /// <param name="evaluationInterval">How often, in seconds, to run the query. Valid
    /// values are 10, 20, 30, and any multiple of 60, up to 3600.</param>
    /// <param name="pendingPeriod">How long, in seconds, a contributor must breach
    /// continuously before it moves to ALARM.</param>
    /// <param name="recoveryPeriod">How long, in seconds, a contributor must stop
    /// breaching before it moves back to OK.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> PutPromQLMetricAlarm(string alarmName, string query,
        int evaluationInterval = 60, int pendingPeriod = 300, int recoveryPeriod = 120)
    {
        var response = await _amazonCloudWatch.PutMetricAlarmAsync(
            new PutMetricAlarmRequest
            {
                AlarmName = alarmName,
                AlarmDescription = "A PromQL alarm created by the AWS SDK for .NET example.",
                EvaluationCriteria = new EvaluationCriteria
                {
                    PromQLCriteria = new AlarmPromQLCriteria
                    {
                        Query = query,
                        PendingPeriod = pendingPeriod,
                        RecoveryPeriod = recoveryPeriod
                    }
                },
                EvaluationInterval = evaluationInterval
            });

        _logger.LogInformation($"Created PromQL alarm {alarmName} for query {query}.");
        return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
    }
```
Create an alarm that evaluates a single CloudWatch metric.

```
    /// <summary>
    /// Add a metric alarm to send an email when the metric passes a threshold.
    /// </summary>
    /// <param name="alarmDescription">A description of the alarm.</param>
    /// <param name="alarmName">The name for the alarm.</param>
    /// <param name="comparison">The type of comparison to use.</param>
    /// <param name="metricName">The name of the metric for the alarm.</param>
    /// <param name="metricNamespace">The namespace of the metric.</param>
    /// <param name="threshold">The threshold value for the alarm.</param>
    /// <param name="alarmActions">Optional actions to execute when in an alarm state.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> PutMetricEmailAlarm(string alarmDescription, string alarmName, ComparisonOperator comparison,
        string metricName, string metricNamespace, double threshold, List<string> alarmActions = null!)
    {
        try
        {
            var putEmailAlarmResponse = await _amazonCloudWatch.PutMetricAlarmAsync(
                new PutMetricAlarmRequest()
                {
                    AlarmActions = alarmActions,
                    AlarmDescription = alarmDescription,
                    AlarmName = alarmName,
                    ComparisonOperator = comparison,
                    Threshold = threshold,
                    Namespace = metricNamespace,
                    MetricName = metricName,
                    EvaluationPeriods = 1,
                    Period = 10,
                    Statistic = new Statistic("Maximum"),
                    DatapointsToAlarm = 1,
                    TreatMissingData = "ignore"
                });
            return putEmailAlarmResponse.HttpStatusCode == HttpStatusCode.OK;
        }
        catch (LimitExceededException lex)
        {
            _logger.LogError(lex, $"Unable to add alarm {alarmName}. Alarm quota has already been reached.");
        }

        return false;
    }

    /// <summary>
    /// Add specific email actions to a list of action strings for a CloudWatch alarm.
    /// </summary>
    /// <param name="accountId">The AccountId for the alarm.</param>
    /// <param name="region">The region for the alarm.</param>
    /// <param name="emailTopicName">An Amazon Simple Notification Service (SNS) topic for the alarm email.</param>
    /// <param name="alarmActions">Optional list of existing alarm actions to append to.</param>
    /// <returns>A list of string actions for an alarm.</returns>
    public List<string> AddEmailAlarmAction(string accountId, string region,
        string emailTopicName, List<string>? alarmActions = null)
    {
        alarmActions ??= new List<string>();
        var snsAlarmAction = $"arn:aws:sns:{region}:{accountId}:{emailTopicName}";
        alarmActions.Add(snsAlarmAction);
        return alarmActions;
    }
```
+  For API details, see [PutMetricAlarm](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutMetricAlarm) in *AWS SDK for .NET API Reference*.

### `PutMetricData`
<a name="cloudwatch_PutMetricData_csharp_4_topic"></a>

The following code example shows how to use `PutMetricData`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Wrapper to add metric data to a CloudWatch metric.
    /// </summary>
    /// <param name="metricNamespace">The namespace of the metric.</param>
    /// <param name="metricData">A data object for the metric data.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> PutMetricData(string metricNamespace,
        List<MetricDatum> metricData)
    {
        var putDataResponse = await _amazonCloudWatch.PutMetricDataAsync(
            new PutMetricDataRequest()
            {
                MetricData = metricData,
                Namespace = metricNamespace,
            });

        return putDataResponse.HttpStatusCode == HttpStatusCode.OK;
    }
```
+  For API details, see [PutMetricData](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutMetricData) in *AWS SDK for .NET API Reference*.

### `StartOTelEnrichment`
<a name="cloudwatch_StartOTelEnrichment_csharp_4_topic"></a>

The following code example shows how to use `StartOTelEnrichment`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Turn on OTel enrichment for the account. Once enrichment is running, CloudWatch
    /// vended metrics that carry a resource identifier dimension, such as the Amazon EC2
    /// CPUUtilization metric with its InstanceId dimension, are decorated with resource
    /// ARN and resource tag labels and become queryable with PromQL.
    ///
    /// Resource tags on telemetry must already be enabled for the account before you
    /// call this operation.
    /// </summary>
    /// <returns>True if successful.</returns>
    public async Task<bool> StartOTelEnrichment()
    {
        var response = await _amazonCloudWatch.StartOTelEnrichmentAsync(
            new StartOTelEnrichmentRequest());

        _logger.LogInformation("Started OTel enrichment for this account.");
        return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
    }
```
+  For API details, see [StartOTelEnrichment](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/StartOTelEnrichment) in *AWS SDK for .NET API Reference*.

### `StopOTelEnrichment`
<a name="cloudwatch_StopOTelEnrichment_csharp_4_topic"></a>

The following code example shows how to use `StopOTelEnrichment`.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).

```
    /// <summary>
    /// Turn off OTel enrichment for the account. Existing PromQL alarms are not deleted,
    /// but vended metrics stop being enriched with resource ARN and tag labels, so
    /// queries that select on those labels stop matching.
    /// </summary>
    /// <returns>True if successful.</returns>
    public async Task<bool> StopOTelEnrichment()
    {
        var response = await _amazonCloudWatch.StopOTelEnrichmentAsync(
            new StopOTelEnrichmentRequest());

        _logger.LogInformation("Stopped OTel enrichment for this account.");
        return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
    }
```
+  For API details, see [StopOTelEnrichment](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/StopOTelEnrichment) in *AWS SDK for .NET API Reference*.

## Scenarios
<a name="scenarios"></a>

### Send OpenTelemetry metrics and alarm on them with PromQL
<a name="cloudwatch_Scenario_OTelMetrics_csharp_4_topic"></a>

The following code example shows how to:
+ Send OTLP metrics to the CloudWatch metrics endpoint with an OpenTelemetry Collector.
+ Start OpenTelemetry enrichment so CloudWatch correlates those metrics with your resources.
+ Create an alarm that evaluates a PromQL query across every series the query returns.
+ Inspect the individual series, called contributors, that put the alarm in ALARM state.
+ Mute the alarm for a maintenance window, then clean up.

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples).
Wrapper methods for the CloudWatch OpenTelemetry actions.

```
/// <summary>
/// Wrapper class for the OpenTelemetry features of Amazon CloudWatch: turning on OTel
/// enrichment so that CloudWatch vended metrics are queryable with PromQL, alarming on a
/// PromQL query, inspecting the individual series (contributors) that put a PromQL alarm
/// into ALARM, and muting alarm actions on a schedule.
///
/// Note that OTLP metric ingestion is not an AWS SDK operation. To send OpenTelemetry
/// metrics to CloudWatch, point an OpenTelemetry collector or the AWS Distro for
/// OpenTelemetry (ADOT) SDK at the CloudWatch OTLP metrics endpoint,
/// https://monitoring.{region}.amazonaws.com/v1/metrics. The operations here cover
/// everything you do after those metrics land in CloudWatch.
/// </summary>
public class CloudWatchOTelWrapper
{
    private readonly IAmazonCloudWatch _amazonCloudWatch;
    private readonly ILogger<CloudWatchOTelWrapper> _logger;

    /// <summary>
    /// Constructor for the CloudWatch OpenTelemetry wrapper.
    /// </summary>
    /// <param name="amazonCloudWatch">The injected CloudWatch client.</param>
    /// <param name="logger">The injected logger for the wrapper.</param>
    public CloudWatchOTelWrapper(IAmazonCloudWatch amazonCloudWatch, ILogger<CloudWatchOTelWrapper> logger)
    {
        _logger = logger;
        _amazonCloudWatch = amazonCloudWatch;
    }

    /// <summary>
    /// Turn on OTel enrichment for the account. Once enrichment is running, CloudWatch
    /// vended metrics that carry a resource identifier dimension, such as the Amazon EC2
    /// CPUUtilization metric with its InstanceId dimension, are decorated with resource
    /// ARN and resource tag labels and become queryable with PromQL.
    ///
    /// Resource tags on telemetry must already be enabled for the account before you
    /// call this operation.
    /// </summary>
    /// <returns>True if successful.</returns>
    public async Task<bool> StartOTelEnrichment()
    {
        var response = await _amazonCloudWatch.StartOTelEnrichmentAsync(
            new StartOTelEnrichmentRequest());

        _logger.LogInformation("Started OTel enrichment for this account.");
        return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
    }

    /// <summary>
    /// Get the current OTel enrichment status for the account.
    /// </summary>
    /// <returns>The status, either Running or Stopped.</returns>
    public async Task<OTelEnrichmentStatus> GetOTelEnrichmentStatus()
    {
        var response = await _amazonCloudWatch.GetOTelEnrichmentAsync(
            new GetOTelEnrichmentRequest());

        _logger.LogInformation($"OTel enrichment status is {response.Status}.");
        return response.Status;
    }

    /// <summary>
    /// Create an alarm that evaluates a PromQL query.
    ///
    /// A PromQL alarm differs from a classic metric alarm in a few ways. The query can
    /// match many series at once, and each matching series is tracked separately as a
    /// contributor. Instead of counting breaching periods, you specify durations: a
    /// contributor moves to ALARM after it breaches continuously for the pending period,
    /// and back to OK after it stops breaching for the recovery period. A PromQL alarm
    /// starts in the OK state rather than INSUFFICIENT_DATA.
    ///
    /// EvaluationCriteria is a union and is mutually exclusive with the classic
    /// MetricName and Metrics properties. When you use it you must also set
    /// EvaluationInterval, and you must not set Period, Statistic, Threshold,
    /// ComparisonOperator, EvaluationPeriods, DatapointsToAlarm, or TreatMissingData.
    /// </summary>
    /// <param name="alarmName">The name of the alarm, unique within the Region.</param>
    /// <param name="query">The PromQL query to evaluate, such as
    /// avg(cpu_utilization_percent) &gt; 80. The comparison belongs in the query itself;
    /// there is no separate threshold property.</param>
    /// <param name="evaluationInterval">How often, in seconds, to run the query. Valid
    /// values are 10, 20, 30, and any multiple of 60, up to 3600.</param>
    /// <param name="pendingPeriod">How long, in seconds, a contributor must breach
    /// continuously before it moves to ALARM.</param>
    /// <param name="recoveryPeriod">How long, in seconds, a contributor must stop
    /// breaching before it moves back to OK.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> PutPromQLMetricAlarm(string alarmName, string query,
        int evaluationInterval = 60, int pendingPeriod = 300, int recoveryPeriod = 120)
    {
        var response = await _amazonCloudWatch.PutMetricAlarmAsync(
            new PutMetricAlarmRequest
            {
                AlarmName = alarmName,
                AlarmDescription = "A PromQL alarm created by the AWS SDK for .NET example.",
                EvaluationCriteria = new EvaluationCriteria
                {
                    PromQLCriteria = new AlarmPromQLCriteria
                    {
                        Query = query,
                        PendingPeriod = pendingPeriod,
                        RecoveryPeriod = recoveryPeriod
                    }
                },
                EvaluationInterval = evaluationInterval
            });

        _logger.LogInformation($"Created PromQL alarm {alarmName} for query {query}.");
        return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
    }

    /// <summary>
    /// Get the contributors for a PromQL alarm. Each contributor is one series that the
    /// alarm's query matched, identified by its label set. This is how you find out which
    /// hosts, services, or pods are breaching, rather than only that something is.
    /// </summary>
    /// <param name="alarmName">The name of the PromQL alarm.</param>
    /// <returns>The list of contributors.</returns>
    public async Task<List<AlarmContributor>> DescribeAlarmContributors(string alarmName)
    {
        var results = new List<AlarmContributor>();
        string? nextToken = null;

        do
        {
            var response = await _amazonCloudWatch.DescribeAlarmContributorsAsync(
                new DescribeAlarmContributorsRequest
                {
                    AlarmName = alarmName,
                    NextToken = nextToken
                });

            if (response.AlarmContributors != null)
            {
                results.AddRange(response.AlarmContributors);
            }

            nextToken = response.NextToken;
        } while (!string.IsNullOrEmpty(nextToken));

        _logger.LogInformation($"Got {results.Count} contributors for alarm {alarmName}.");
        return results;
    }

    /// <summary>
    /// Create or update an alarm mute rule. While a mute rule is active the targeted
    /// alarms keep evaluating and keep transitioning between states, but their configured
    /// actions do not fire. This is the supported way to suppress notifications during a
    /// known maintenance window, instead of disabling alarm actions and relying on
    /// someone to turn them back on.
    /// </summary>
    /// <param name="name">The name of the mute rule.</param>
    /// <param name="expression">When the rule activates. For a recurring window, use a
    /// five-field cron expression, cron(Minutes Hours Day-of-month Month Day-of-week),
    /// such as cron(0 2 * * SUN) for every Sunday at 2:00 AM. Note that this is five
    /// fields, not the six that Amazon EventBridge uses. For a one-time window, use
    /// at(yyyy-MM-ddThh:mm), such as at(2026-09-05T02:00).</param>
    /// <param name="duration">How long the mute window lasts once it activates, in
    /// ISO 8601 duration format, from PT1M (one minute) to P15D (15 days). For example,
    /// PT2H is two hours and P2DT12H is two days and 12 hours.</param>
    /// <param name="timezone">The time zone the expression is evaluated in, such as
    /// America/Los_Angeles.</param>
    /// <param name="alarmNames">The names of up to 100 alarms to mute. If null or empty,
    /// the rule applies to all alarms in the account.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> PutAlarmMuteRule(string name, string expression, string duration,
        string timezone, List<string>? alarmNames = null)
    {
        var request = new PutAlarmMuteRuleRequest
        {
            Name = name,
            Description = "A mute rule created by the AWS SDK for .NET example.",
            Rule = new Rule
            {
                Schedule = new Schedule
                {
                    Expression = expression,
                    Duration = duration,
                    Timezone = timezone
                }
            }
        };

        if (alarmNames != null && alarmNames.Any())
        {
            request.MuteTargets = new MuteTargets { AlarmNames = alarmNames };
        }

        var response = await _amazonCloudWatch.PutAlarmMuteRuleAsync(request);

        _logger.LogInformation($"Put alarm mute rule {name}.");
        return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
    }

    /// <summary>
    /// Get the full configuration of an alarm mute rule, including its schedule, the
    /// alarms it targets, and whether it is currently SCHEDULED, ACTIVE, or EXPIRED.
    /// </summary>
    /// <param name="name">The name of the mute rule.</param>
    /// <returns>The mute rule.</returns>
    public async Task<GetAlarmMuteRuleResponse> GetAlarmMuteRule(string name)
    {
        var response = await _amazonCloudWatch.GetAlarmMuteRuleAsync(
            new GetAlarmMuteRuleRequest
            {
                AlarmMuteRuleName = name
            });

        _logger.LogInformation($"Mute rule {response.Name} is {response.Status}.");
        return response;
    }

    /// <summary>
    /// List the alarm mute rules in the account, optionally filtered to the rules that
    /// target one alarm.
    /// </summary>
    /// <param name="alarmName">When specified, only rules that target this alarm are
    /// returned.</param>
    /// <returns>The list of mute rule summaries.</returns>
    public async Task<List<AlarmMuteRuleSummary>> ListAlarmMuteRules(string? alarmName = null)
    {
        var results = new List<AlarmMuteRuleSummary>();
        string? nextToken = null;

        do
        {
            var response = await _amazonCloudWatch.ListAlarmMuteRulesAsync(
                new ListAlarmMuteRulesRequest
                {
                    AlarmName = alarmName,
                    NextToken = nextToken
                });

            if (response.AlarmMuteRuleSummaries != null)
            {
                results.AddRange(response.AlarmMuteRuleSummaries);
            }

            nextToken = response.NextToken;
        } while (!string.IsNullOrEmpty(nextToken));

        _logger.LogInformation($"Got {results.Count} alarm mute rules.");
        return results;
    }

    /// <summary>
    /// Delete an alarm mute rule. The alarms it targeted resume firing their actions.
    /// </summary>
    /// <param name="name">The name of the mute rule.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DeleteAlarmMuteRule(string name)
    {
        var response = await _amazonCloudWatch.DeleteAlarmMuteRuleAsync(
            new DeleteAlarmMuteRuleRequest
            {
                AlarmMuteRuleName = name
            });

        _logger.LogInformation($"Deleted alarm mute rule {name}.");
        return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
    }

    /// <summary>
    /// Turn off OTel enrichment for the account. Existing PromQL alarms are not deleted,
    /// but vended metrics stop being enriched with resource ARN and tag labels, so
    /// queries that select on those labels stop matching.
    /// </summary>
    /// <returns>True if successful.</returns>
    public async Task<bool> StopOTelEnrichment()
    {
        var response = await _amazonCloudWatch.StopOTelEnrichmentAsync(
            new StopOTelEnrichmentRequest());

        _logger.LogInformation("Stopped OTel enrichment for this account.");
        return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
    }
```
+ For API details, see the following topics in *AWS SDK for .NET API Reference*.
  + [DeleteAlarmMuteRule](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DeleteAlarmMuteRule)
  + [DeleteAlarms](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DeleteAlarms)
  + [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DescribeAlarmContributors)
  + [GetAlarmMuteRule](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetAlarmMuteRule)
  + [GetOTelEnrichment](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetOTelEnrichment)
  + [ListAlarmMuteRules](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/ListAlarmMuteRules)
  + [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutAlarmMuteRule)
  + [PutMetricAlarm](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutMetricAlarm)
  + [StartOTelEnrichment](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/StartOTelEnrichment)
  + [StopOTelEnrichment](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/StopOTelEnrichment)
