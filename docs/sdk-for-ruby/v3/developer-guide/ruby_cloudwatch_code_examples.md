---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/ruby_cloudwatch_code_examples.html
---

# CloudWatch examples using SDK for Ruby
<a name="ruby_cloudwatch_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Ruby with CloudWatch.

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Basics](#basics)
+ [Actions](#actions)
+ [Scenarios](#scenarios)

## Basics
<a name="basics"></a>

### Learn the basics
<a name="cloudwatch_GetStartedMetricsDashboardsAlarms_ruby_topic"></a>

The following code example shows how to:
+ List CloudWatch namespaces and metrics.
+ Start OpenTelemetry enrichment so CloudWatch correlates incoming OTLP metrics with the resources that produced them.
+ See how OTLP metrics reach the CloudWatch metrics endpoint. Metric ingestion over OTLP is not an AWS SDK operation.
+ Create an alarm that evaluates a PromQL query.
+ Inspect the alarm's contributors, the individual series that the query matched.
+ Get statistics for a metric and chart it on a dashboard.
+ Mute the alarm for a maintenance window, then clean up.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples).
Run an interactive scenario demonstrating the CloudWatch OpenTelemetry experience.

```
DASHES = ('-' * 80).freeze
DEFAULT_QUERY = 'avg by (host) (system_cpu_utilization) > 80'.freeze

# Valid evaluation intervals are 10, 20, 30, or any multiple of 60 up to 3600 seconds.
EVALUATION_INTERVAL = 60
PENDING_PERIOD = 300
RECOVERY_PERIOD = 120

# Lists the metrics and namespaces already present in the account, to orient the reader
# before any configuration happens.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @return [Hash] A hash of namespace to the metrics found in it, most populated first.
def metrics_by_namespace(cloudwatch_client)
  by_namespace = {}
  metric_count = 0

  cloudwatch_client.list_metrics.each_page do |page|
    page.metrics.each do |metric|
      (by_namespace[metric.namespace] ||= []) << metric
      metric_count += 1
    end
    # This account may have a very large number of metrics, so stop once we have enough
    # to give the reader a sense of what is there.
    break if metric_count >= 500
  end

  puts "\tFound #{metric_count} metrics across #{by_namespace.size} namespaces:"
  by_namespace
    .sort_by { |_namespace, metrics| -metrics.size }
    .first(10)
    .each { |namespace, metrics| puts "\t  #{namespace} (#{metrics.size} metrics)" }

  if by_namespace.empty?
    puts "\tNo metrics found in this account. The statistics and dashboard steps later"
    puts "\ton need an existing metric, so they will be skipped."
  end

  by_namespace
rescue StandardError => e
  puts "Error listing metrics: #{e.message}"
  {}
end

# Turns on OTel enrichment, but only if it is not already running. Enrichment is an
# account-wide setting, so this scenario only turns it off again if it was the thing that
# turned it on.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @return [Boolean] true if this run started enrichment; otherwise, false.
def enrichment_started_by_example?(cloudwatch_client)
  # The Ruby SDK renders the OTel prefix as +o_tel+, so the methods are
  # +get_o_tel_enrichment+ and +start_o_tel_enrichment+.
  status = cloudwatch_client.get_o_tel_enrichment.status
  puts "\tEnrichment status: #{status}"

  if status == 'Running'
    puts
    puts "\tEnrichment was already running, so we will leave it alone. The cleanup step"
    puts "\twill not stop it, because other workloads in this account may depend on it."
    return false
  end

  cloudwatch_client.start_o_tel_enrichment
  puts "\tEnrichment status: #{cloudwatch_client.get_o_tel_enrichment.status}"
  puts
  puts "\tNote: this run started enrichment, so the cleanup step will stop it again."
  true
rescue StandardError => e
  puts "Error starting OTel enrichment: #{e.message}"
  false
end

# Creates an alarm whose evaluation is a PromQL query.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String] The name of the alarm to create.
# @param query [String] The PromQL query to evaluate.
# @return [Boolean] true if the alarm was created; otherwise, false.
def promql_alarm_created?(cloudwatch_client, alarm_name, query)
  # The comparison belongs in the query itself. A PromQL alarm has no separate threshold,
  # comparison operator, statistic, period, or evaluation periods. Note that the Ruby SDK
  # spells the criteria member +prom_ql_criteria+.
  cloudwatch_client.put_metric_alarm(
    alarm_name: alarm_name,
    alarm_description: 'A PromQL alarm created by the AWS SDK for Ruby Basics scenario.',
    evaluation_criteria: {
      prom_ql_criteria: {
        query: query,
        pending_period: PENDING_PERIOD,
        recovery_period: RECOVERY_PERIOD
      }
    },
    evaluation_interval: EVALUATION_INTERVAL
  )
  true
rescue StandardError => e
  puts "Error creating PromQL alarm: #{e.message}"
  false
end

# Prints the contributors to a PromQL alarm. Each contributor is one series the query
# matched, identified by its label set.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String] The name of the PromQL alarm.
# @return [void]
def report_alarm_contributors(cloudwatch_client, alarm_name)
  contributors = []
  next_token = nil

  loop do
    response = cloudwatch_client.describe_alarm_contributors(
      alarm_name: alarm_name,
      next_token: next_token
    )
    contributors.concat(response.alarm_contributors)
    next_token = response.next_token
    # A page can come back empty while still carrying a token, so keep going until the
    # token itself is gone rather than stopping at the first empty page.
    break if next_token.nil? || next_token.empty?
  end

  if contributors.empty?
    puts "\tNo contributors yet. The query matched no series, which usually means no"
    puts "\tOTel metrics with these labels have arrived. Once your collector is sending"
    puts "\tdata, each matching series appears here with its labels and why it breached."
    return
  end

  puts "\tFound #{contributors.size} contributors:"
  contributors.each do |contributor|
    labels = contributor.contributor_attributes.sort.map { |k, v| "#{k}=#{v}" }.join(', ')
    puts "\t  #{contributor.contributor_id}: #{labels}"
    puts "\t    reason: #{contributor.state_reason}"
  end
rescue StandardError => e
  puts "Error describing alarm contributors: #{e.message}"
end

# Builds a single-widget dashboard body that charts the given metric.
#
# @param metric [Aws::CloudWatch::Types::Metric] The metric to chart.
# @param region [String] The region the metric is in. A metric widget must name its
#   region, because a dashboard can chart metrics from several.
# @return [String] The dashboard body, as JSON.
def dashboard_body(metric, region)
  metric_spec = [metric.namespace, metric.metric_name]
  metric.dimensions.each { |dimension| metric_spec.push(dimension.name, dimension.value) }

  {
    widgets: [
      {
        type: 'text',
        x: 0, y: 0, width: 24, height: 2,
        properties: {
          markdown: 'This dashboard was created programmatically by an AWS SDK code example.'
        }
      },
      {
        type: 'metric',
        x: 0, y: 2, width: 12, height: 6,
        properties: {
          metrics: [metric_spec],
          view: 'timeSeries',
          stat: 'Average',
          period: 300,
          region: region,
          title: metric.metric_name
        }
      }
    ]
  }.to_json
end

# Gets statistics for an existing metric and charts it on a dashboard, so the reader can
# see what the alarm is evaluating.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param dashboard_name [String] The name of the dashboard to create.
# @param by_namespace [Hash] The namespaces and metrics discovered in step 1.
# @return [Boolean] true if a dashboard was created; otherwise, false.
def chart_metric_on_dashboard(cloudwatch_client, dashboard_name, by_namespace)
  if by_namespace.empty?
    puts "\tSkipping statistics and dashboard because no metrics exist yet."
    return false
  end

  metric = by_namespace.max_by { |_namespace, metrics| metrics.size }.last.first

  stats = cloudwatch_client.get_metric_statistics(
    namespace: metric.namespace,
    metric_name: metric.metric_name,
    dimensions: metric.dimensions,
    start_time: Time.now - (60 * 60 * 24),
    end_time: Time.now,
    period: 3600,
    statistics: %w[Average Maximum]
  )
  puts "\tStatistics for #{metric.namespace} #{metric.metric_name} over the last day:"
  puts "\t  Datapoints: #{stats.datapoints.size}"
  stats.datapoints.first(3).each do |datapoint|
    puts "\t  #{datapoint.timestamp} average #{datapoint.average}, maximum #{datapoint.maximum}"
  end

  response = cloudwatch_client.put_dashboard(
    dashboard_name: dashboard_name,
    dashboard_body: dashboard_body(metric, cloudwatch_client.config.region)
  )
  response.dashboard_validation_messages.each do |message|
    puts "\tDashboard validation message: #{message.message}"
  end
  puts "\tCreated dashboard #{dashboard_name}."

  stored = cloudwatch_client.get_dashboard(dashboard_name: dashboard_name)
  puts "\tRead the dashboard back, #{stored.dashboard_body.length} characters of widget JSON."
  true
rescue StandardError => e
  puts "Error getting statistics or creating the dashboard: #{e.message}"
  false
end

# Creates a mute rule so the alarm's actions are suppressed during a maintenance window,
# then reads it back and finds it in the account's rules.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param mute_rule_name [String] The name of the mute rule to create.
# @param alarm_name [String] The name of the alarm to mute.
# @return [void]
def mute_alarm_for_maintenance(cloudwatch_client, mute_rule_name, alarm_name)
  # The expression is a five-field cron expression,
  # cron(Minutes Hours Day-of-month Month Day-of-week). Note that this is five fields, not
  # the six that Amazon EventBridge uses. For a one-time window, use at(yyyy-MM-ddThh:mm),
  # with no seconds. The duration is an ISO 8601 duration from PT1M to P15D, so PT2H
  # rather than 2h.
  expression = 'cron(0 2 * * SUN)'
  duration = 'PT2H'
  timezone = 'America/Los_Angeles'

  cloudwatch_client.put_alarm_mute_rule(
    name: mute_rule_name,
    description: 'A mute rule created by the AWS SDK for Ruby Basics scenario.',
    rule: {
      schedule: {
        expression: expression,
        duration: duration,
        timezone: timezone
      }
    },
    # Target up to 100 alarms. If mute_targets is omitted, the rule applies to every alarm
    # in the account.
    mute_targets: { alarm_names: [alarm_name] }
  )

  puts "\tCreated mute rule #{mute_rule_name}:"
  puts "\t  schedule: #{expression} for #{duration}"
  puts "\t  timezone: #{timezone}"
  puts "\t  targets:  #{alarm_name}"
  puts
  puts "\tNote the two formats here. The expression is a five-field cron expression, five"
  puts "\trather than the six Amazon EventBridge uses. The duration is an ISO 8601"
  puts "\tduration, so 'PT2H' and not '2h'."
  puts
  puts "\tAlso note that mute_targets is set explicitly. If you leave it out, the rule"
  puts "\tapplies to every alarm in the account."

  rule = cloudwatch_client.get_alarm_mute_rule(alarm_mute_rule_name: mute_rule_name)
  puts "\tRead the rule back: status #{rule.status}, mute type #{rule.mute_type}."

  summaries = cloudwatch_client.list_alarm_mute_rules(alarm_name: alarm_name)
                               .alarm_mute_rule_summaries
  puts "\tFound #{summaries.size} mute rules targeting this alarm."
  # Mute rule summaries carry no name field, only an ARN, so match on the ARN suffix.
  match = summaries.find do |summary|
    summary.alarm_mute_rule_arn.end_with?("/#{mute_rule_name}", ":#{mute_rule_name}")
  end
  puts "\t  matched by ARN: #{match.alarm_mute_rule_arn} (#{match.status})" if match
rescue StandardError => e
  puts "Error muting the alarm: #{e.message}"
end

# Deletes the resources the scenario created. Each deletion is attempted independently so
# that one failure does not leave the remaining resources behind.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param names [Hash] The alarm, dashboard, and mute rule names to delete.
# @param started_here [Boolean] Whether this run turned OTel enrichment on.
# @return [void]
def clean_up(cloudwatch_client, names, started_here)
  begin
    cloudwatch_client.delete_alarm_mute_rule(alarm_mute_rule_name: names[:mute_rule])
    puts "\tDeleted mute rule #{names[:mute_rule]}."
  rescue StandardError => e
    puts "\tCould not delete the mute rule: #{e.message}"
  end

  begin
    cloudwatch_client.delete_alarms(alarm_names: [names[:alarm]])
    puts "\tDeleted alarm #{names[:alarm]}."
  rescue StandardError => e
    puts "\tCould not delete the alarm: #{e.message}"
  end

  if names[:dashboard]
    begin
      cloudwatch_client.delete_dashboards(dashboard_names: [names[:dashboard]])
      puts "\tDeleted dashboard #{names[:dashboard]}."
    rescue StandardError => e
      puts "\tCould not delete the dashboard: #{e.message}"
    end
  end

  unless started_here
    puts "\tLeft OTel enrichment running, because it was already on before this run."
    return
  end

  begin
    cloudwatch_client.stop_o_tel_enrichment
    puts "\tStopped OTel enrichment, because this run started it."
  rescue StandardError => e
    puts "\tCould not stop OTel enrichment: #{e.message}"
  end
end

# Prints the scenario's introduction.
#
# @return [void]
def print_intro
  puts DASHES
  puts 'Welcome to the Amazon CloudWatch Basics scenario.'
  puts
  puts 'CloudWatch now ingests OpenTelemetry metrics natively. This scenario walks through'
  puts 'that experience: it turns on OTel enrichment so CloudWatch can correlate incoming'
  puts 'OTLP metrics with the resources that produced them, alarms on those metrics with a'
  puts 'PromQL query, and shows you which individual series drove the alarm.'
  puts
  puts 'A PromQL alarm works differently from a classic metric alarm. Rather than watching'
  puts 'one metric and counting breaching periods, it evaluates a query that can match many'
  puts 'series at once, and tracks each one separately as a contributor.'
  puts DASHES
end

# Explains that OTLP metric ingestion is not an AWS SDK operation. This step makes no
# service call; naming the gap explicitly is the point.
#
# @return [void]
def explain_otlp_ingestion
  puts '3. Send OTLP metrics to CloudWatch'
  puts
  puts 'This step is not an AWS SDK operation, and that\'s worth being explicit about.'
  puts 'Metrics reach CloudWatch over the OTLP protocol, through the CloudWatch agent, an'
  puts 'OpenTelemetry Collector, or an ADOT SDK. There is no PutOTelMetrics API to call.'
  puts
  puts 'Point your collector at the CloudWatch metrics endpoint, which follows the pattern'
  puts "\thttps://monitoring.<region>.amazonaws.com/v1/metrics"
  puts
  puts 'The endpoint is HTTP/1.1 only and does not support gRPC, so use an otlphttp'
  puts 'exporter rather than otlp. The metrics endpoint signs as "monitoring".'
  puts DASHES
end

# Prompts for a PromQL query and creates an alarm that evaluates it.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String] The name of the alarm to create.
# @return [void]
def create_promql_alarm_step(cloudwatch_client, alarm_name)
  puts '4. Create a PromQL alarm'
  puts
  puts 'Now we alarm on those metrics. The comparison goes inside the query itself: a'
  puts 'PromQL alarm has no separate threshold, comparison operator, statistic, or period.'
  puts
  print "Enter a PromQL query, or press ENTER for [#{DEFAULT_QUERY}]: "
  input = $stdin.gets
  query = input.nil? || input.strip.empty? ? DEFAULT_QUERY : input.strip

  if promql_alarm_created?(cloudwatch_client, alarm_name, query)
    puts "\tCreated alarm #{alarm_name}:"
    puts "\t  query:              #{query}"
    puts "\t  evaluationInterval: #{EVALUATION_INTERVAL} seconds"
    puts "\t  pendingPeriod:      #{PENDING_PERIOD} seconds"
    puts "\t  recoveryPeriod:     #{RECOVERY_PERIOD} seconds"
    puts
    puts "\tA PromQL alarm starts in the OK state rather than INSUFFICIENT_DATA, which is"
    puts "\tanother way it differs from a classic alarm."
  end
  puts DASHES
end

# Runs the eight steps of the scenario in order.
def run_me
  region = 'us-east-1'
  cloudwatch_client = Aws::CloudWatch::Client.new(region: region)

  # Suffix the resource names so repeated runs do not collide.
  suffix = rand(1000..9999)
  alarm_name = "doc-example-promql-alarm-#{suffix}"
  dashboard_name = "doc-example-dashboard-#{suffix}"
  mute_rule_name = "doc-example-mute-rule-#{suffix}"

  print_intro

  puts '1. List metrics and namespaces'
  puts
  puts 'Before configuring anything, let\'s see what CloudWatch is already collecting in'
  puts 'this account by calling ListMetrics.'
  puts
  by_namespace = metrics_by_namespace(cloudwatch_client)
  puts DASHES

  puts '2. Start OpenTelemetry enrichment'
  puts
  puts 'Enrichment is what lets CloudWatch attach AWS resource context to the OTLP metrics'
  puts 'you send it. Without it, your metrics arrive as opaque series with no connection to'
  puts 'the resources that emitted them.'
  puts
  puts 'We check the current state first, and only start enrichment if it isn\'t already on.'
  puts
  started_here = enrichment_started_by_example?(cloudwatch_client)
  puts DASHES

  explain_otlp_ingestion
  create_promql_alarm_step(cloudwatch_client, alarm_name)

  puts '5. Inspect the alarm\'s contributors'
  puts
  puts 'Each contributor is one series the query matched, identified by its label set. This'
  puts 'is how you find out which host is unhealthy rather than only that something is.'
  puts 'Classic alarms have no equivalent.'
  puts
  report_alarm_contributors(cloudwatch_client, alarm_name)
  puts DASHES

  puts '6. Get statistics and chart the metric on a dashboard'
  puts
  puts 'Statistics and dashboards are how you see what the alarm is evaluating.'
  puts
  dashboard_created = chart_metric_on_dashboard(cloudwatch_client, dashboard_name, by_namespace)
  puts DASHES

  mute_alarm_step(cloudwatch_client, mute_rule_name, alarm_name)

  clean_up_step(
    cloudwatch_client,
    { alarm: alarm_name, dashboard: dashboard_created ? dashboard_name : nil,
      mute_rule: mute_rule_name },
    started_here
  )

  puts 'This concludes the Amazon CloudWatch Basics scenario.'
end

# Explains what a mute rule does, then creates one for the scenario's alarm.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param mute_rule_name [String] The name of the mute rule to create.
# @param alarm_name [String] The name of the alarm to mute.
# @return [void]
def mute_alarm_step(cloudwatch_client, mute_rule_name, alarm_name)
  puts '7. Mute the alarm for a maintenance window'
  puts
  puts 'While a mute rule is active the targeted alarms keep evaluating and keep changing'
  puts 'state, but their actions do not fire. This is the supported way to suppress'
  puts 'notifications during planned maintenance, instead of disabling alarm actions and'
  puts 'hoping someone remembers to turn them back on.'
  puts
  mute_alarm_for_maintenance(cloudwatch_client, mute_rule_name, alarm_name)
  puts DASHES
end

# Asks whether to delete the resources the scenario created, and deletes them if so.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param names [Hash] The alarm, dashboard, and mute rule names to delete.
# @param started_here [Boolean] Whether this run turned OTel enrichment on.
# @return [void]
def clean_up_step(cloudwatch_client, names, started_here)
  puts '8. Clean up'
  print 'Delete the resources this scenario created? (y/n) '
  answer = $stdin.gets
  if answer.nil? || answer.strip.downcase != 'y'
    puts "\tSkipping cleanup. Note that the alarm, dashboard, and mute rule are still in"
    puts "\tyour account, and enrichment may still be running."
  else
    clean_up(cloudwatch_client, names, started_here)
  end
  puts DASHES
end
```
+ For API details, see the following topics in *AWS SDK for Ruby API Reference*.
  + [DeleteAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteAlarmMuteRule)
  + [DeleteAlarms](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteAlarms)
  + [DeleteDashboards](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteDashboards)
  + [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarmContributors)
  + [GetAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetAlarmMuteRule)
  + [GetDashboard](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetDashboard)
  + [GetMetricStatistics](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetMetricStatistics)
  + [GetOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetOTelEnrichment)
  + [ListAlarmMuteRules](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListAlarmMuteRules)
  + [ListDashboards](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListDashboards)
  + [ListMetrics](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListMetrics)
  + [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutAlarmMuteRule)
  + [PutDashboard](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutDashboard)
  + [PutMetricAlarm](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutMetricAlarm)
  + [StartOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/StartOTelEnrichment)
  + [StopOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/StopOTelEnrichment)

## Actions
<a name="actions"></a>

### `DeleteAlarmMuteRule`
<a name="cloudwatch_DeleteAlarmMuteRule_ruby_topic"></a>

The following code example shows how to use `DeleteAlarmMuteRule`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples).

```
# Deletes an alarm mute rule. The alarms it targeted resume firing their actions.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param name [String] The name of the mute rule.
# @return [Boolean] true if the mute rule was deleted; otherwise, false.
def alarm_mute_rule_deleted?(cloudwatch_client, name)
  cloudwatch_client.delete_alarm_mute_rule(alarm_mute_rule_name: name)
  true
rescue StandardError => e
  puts "Error deleting alarm mute rule: #{e.message}"
  false
end
```
+  For API details, see [DeleteAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteAlarmMuteRule) in *AWS SDK for Ruby API Reference*.

### `DescribeAlarmContributors`
<a name="cloudwatch_DescribeAlarmContributors_ruby_topic"></a>

The following code example shows how to use `DescribeAlarmContributors`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples).

```
# Gets the contributors for a PromQL alarm. Each contributor is one series that the
# alarm's query matched, identified by its label set. This is how you find out which
# hosts, services, or pods are breaching, rather than only that something is.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String] The name of the PromQL alarm.
# @return [Array] The contributors, as Aws::CloudWatch::Types::AlarmContributor.
def alarm_contributors(cloudwatch_client, alarm_name)
  contributors = []
  next_token = nil

  loop do
    response = cloudwatch_client.describe_alarm_contributors(
      alarm_name: alarm_name,
      next_token: next_token
    )
    contributors.concat(response.alarm_contributors)
    next_token = response.next_token
    break if next_token.nil? || next_token.empty?
  end

  contributors
rescue StandardError => e
  puts "Error getting alarm contributors: #{e.message}"
  []
end
```
+  For API details, see [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarmContributors) in *AWS SDK for Ruby API Reference*.

### `DescribeAlarms`
<a name="cloudwatch_DescribeAlarms_ruby_topic"></a>

The following code example shows how to use `DescribeAlarms`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples).

```
require 'aws-sdk-cloudwatch'

# Lists the names of available Amazon CloudWatch alarms.
#
# @param cloudwatch_client [Aws::CloudWatch::Client]
#   An initialized CloudWatch client.
# @example
#   list_alarms(Aws::CloudWatch::Client.new(region: 'us-east-1'))
def list_alarms(cloudwatch_client)
  response = cloudwatch_client.describe_alarms
  if response.metric_alarms.count.positive?
    response.metric_alarms.each do |alarm|
      puts alarm.alarm_name
    end
  else
    puts 'No alarms found.'
  end
rescue StandardError => e
  puts "Error getting information about alarms: #{e.message}"
end
```
+  For API details, see [DescribeAlarms](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarms) in *AWS SDK for Ruby API Reference*.

### `DescribeAlarmsForMetric`
<a name="cloudwatch_DescribeAlarmsForMetric_ruby_topic"></a>

The following code example shows how to use `DescribeAlarmsForMetric`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples).

```
#
# @param cloudwatch_client [Aws::CloudWatch::Client]
#   An initialized CloudWatch client.
# @example
#   describe_metric_alarms(Aws::CloudWatch::Client.new(region: 'us-east-1'))
def describe_metric_alarms(cloudwatch_client)
  response = cloudwatch_client.describe_alarms

  if response.metric_alarms.count.positive?
    response.metric_alarms.each do |alarm|
      puts '-' * 16
      puts "Name:           #{alarm.alarm_name}"
      puts "State value:    #{alarm.state_value}"
      puts "State reason:   #{alarm.state_reason}"
      puts "Metric:         #{alarm.metric_name}"
      puts "Namespace:      #{alarm.namespace}"
      puts "Statistic:      #{alarm.statistic}"
      puts "Period:         #{alarm.period}"
      puts "Unit:           #{alarm.unit}"
      puts "Eval. periods:  #{alarm.evaluation_periods}"
      puts "Threshold:      #{alarm.threshold}"
      puts "Comp. operator: #{alarm.comparison_operator}"

      if alarm.key?(:ok_actions) && alarm.ok_actions.count.positive?
        puts 'OK actions:'
        alarm.ok_actions.each do |a|
          puts "  #{a}"
        end
      end

      if alarm.key?(:alarm_actions) && alarm.alarm_actions.count.positive?
        puts 'Alarm actions:'
        alarm.alarm_actions.each do |a|
          puts "  #{a}"
        end
      end

      if alarm.key?(:insufficient_data_actions) &&
         alarm.insufficient_data_actions.count.positive?
        puts 'Insufficient data actions:'
        alarm.insufficient_data_actions.each do |a|
          puts "  #{a}"
        end
      end

      puts 'Dimensions:'
      if alarm.key?(:dimensions) && alarm.dimensions.count.positive?
        alarm.dimensions.each do |d|
          puts "  Name: #{d.name}, Value: #{d.value}"
        end
      else
        puts '  None for this alarm.'
      end
    end
  else
    puts 'No alarms found.'
  end
rescue StandardError => e
  puts "Error getting information about alarms: #{e.message}"
end

# Example usage:
def run_me
  region = ''

  # Print usage information and then stop.
  if ARGV[0] == '--help' || ARGV[0] == '-h'
    puts 'Usage:   ruby cw-ruby-example-show-alarms.rb REGION'
    puts 'Example: ruby cw-ruby-example-show-alarms.rb us-east-1'
    exit 1
  # If no values are specified at the command prompt, use these default values.
  elsif ARGV.count.zero?
    region = 'us-east-1'
  # Otherwise, use the values as specified at the command prompt.
  else
    region = ARGV[0]
  end

  cloudwatch_client = Aws::CloudWatch::Client.new(region: region)
  puts 'Available alarms:'
  describe_metric_alarms(cloudwatch_client)
end

run_me if $PROGRAM_NAME == __FILE__
```
+  For API details, see [DescribeAlarmsForMetric](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarmsForMetric) in *AWS SDK for Ruby API Reference*.

### `DisableAlarmActions`
<a name="cloudwatch_DisableAlarmActions_ruby_topic"></a>

The following code example shows how to use `DisableAlarmActions`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples).

```
# Disables an alarm in Amazon CloudWatch.
#
# Prerequisites.
#
# - The alarm to disable.
#
# @param cloudwatch_client [Aws::CloudWatch::Client]
#   An initialized CloudWatch client.
# @param alarm_name [String] The name of the alarm to disable.
# @return [Boolean] true if the alarm was disabled; otherwise, false.
# @example
#   exit 1 unless alarm_actions_disabled?(
#     Aws::CloudWatch::Client.new(region: 'us-east-1'),
#     'ObjectsInBucket'
#   )
def alarm_actions_disabled?(cloudwatch_client, alarm_name)
  cloudwatch_client.disable_alarm_actions(alarm_names: [alarm_name])
  true
rescue StandardError => e
  puts "Error disabling alarm actions: #{e.message}"
  false
end

# Example usage:
def run_me
  alarm_name = 'ObjectsInBucket'
  alarm_description = 'Objects exist in this bucket for more than 1 day.'
  metric_name = 'NumberOfObjects'
  # Notify this Amazon Simple Notification Service (Amazon SNS) topic when
  # the alarm transitions to the ALARM state.
  alarm_actions = ['arn:aws:sns:us-east-1:111111111111:Default_CloudWatch_Alarms_Topic']
  namespace = 'AWS/S3'
  statistic = 'Average'
  dimensions = [
    {
      name: "BucketName",
      value: "amzn-s3-demo-bucket"
    },
    {
      name: 'StorageType',
      value: 'AllStorageTypes'
    }
  ]
  period = 86_400 # Daily (24 hours * 60 minutes * 60 seconds = 86400 seconds).
  unit = 'Count'
  evaluation_periods = 1 # More than one day.
  threshold = 1 # One object.
  comparison_operator = 'GreaterThanThreshold' # More than one object.
  # Replace us-west-2 with the AWS Region you're using for Amazon CloudWatch.
  region = 'us-east-1'

  cloudwatch_client = Aws::CloudWatch::Client.new(region: region)

  if alarm_created_or_updated?(
    cloudwatch_client,
    alarm_name,
    alarm_description,
    metric_name,
    alarm_actions,
    namespace,
    statistic,
    dimensions,
    period,
    unit,
    evaluation_periods,
    threshold,
    comparison_operator
  )
    puts "Alarm '#{alarm_name}' created or updated."
  else
    puts "Could not create or update alarm '#{alarm_name}'."
  end

  if alarm_actions_disabled?(cloudwatch_client, alarm_name)
    puts "Alarm '#{alarm_name}' disabled."
  else
    puts "Could not disable alarm '#{alarm_name}'."
  end
end

run_me if $PROGRAM_NAME == __FILE__
```
+  For API details, see [DisableAlarmActions](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DisableAlarmActions) in *AWS SDK for Ruby API Reference*.

### `GetAlarmMuteRule`
<a name="cloudwatch_GetAlarmMuteRule_ruby_topic"></a>

The following code example shows how to use `GetAlarmMuteRule`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples).

```
# Gets the full configuration of an alarm mute rule, including its schedule, the alarms
# it targets, and whether it is currently SCHEDULED, ACTIVE, or EXPIRED.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param name [String] The name of the mute rule.
# @return [Aws::CloudWatch::Types::GetAlarmMuteRuleOutput, nil] The mute rule, or nil on
#   error.
def alarm_mute_rule(cloudwatch_client, name)
  cloudwatch_client.get_alarm_mute_rule(alarm_mute_rule_name: name)
rescue StandardError => e
  puts "Error getting alarm mute rule: #{e.message}"
  nil
end
```
+  For API details, see [GetAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetAlarmMuteRule) in *AWS SDK for Ruby API Reference*.

### `GetOTelEnrichment`
<a name="cloudwatch_GetOTelEnrichment_ruby_topic"></a>

The following code example shows how to use `GetOTelEnrichment`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples).

```
# Gets the current OTel enrichment status for the account.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @return [String, nil] 'Running' or 'Stopped', or nil if the status could not be read.
def otel_enrichment_status(cloudwatch_client)
  cloudwatch_client.get_o_tel_enrichment.status
rescue StandardError => e
  puts "Error getting OTel enrichment status: #{e.message}"
  nil
end
```
+  For API details, see [GetOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetOTelEnrichment) in *AWS SDK for Ruby API Reference*.

### `ListAlarmMuteRules`
<a name="cloudwatch_ListAlarmMuteRules_ruby_topic"></a>

The following code example shows how to use `ListAlarmMuteRules`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples).

```
# Lists the alarm mute rules in the account, optionally filtered to the rules that
# target one alarm.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String, nil] When given, only rules that target this alarm are
#   returned.
# @return [Array] The mute rule summaries, as
#   Aws::CloudWatch::Types::AlarmMuteRuleSummary.
def alarm_mute_rules(cloudwatch_client, alarm_name = nil)
  summaries = []
  next_token = nil

  loop do
    response = cloudwatch_client.list_alarm_mute_rules(
      alarm_name: alarm_name,
      next_token: next_token
    )
    summaries.concat(response.alarm_mute_rule_summaries)
    next_token = response.next_token
    break if next_token.nil? || next_token.empty?
  end

  summaries
rescue StandardError => e
  puts "Error listing alarm mute rules: #{e.message}"
  []
end
```
+  For API details, see [ListAlarmMuteRules](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListAlarmMuteRules) in *AWS SDK for Ruby API Reference*.

### `ListMetrics`
<a name="cloudwatch_ListMetrics_ruby_topic"></a>

The following code example shows how to use `ListMetrics`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples).

```
# Lists available metrics for a metric namespace in Amazon CloudWatch.
#
# @param cloudwatch_client [Aws::CloudWatch::Client]
#   An initialized CloudWatch client.
# @param metric_namespace [String] The namespace of the metric.
# @example
#   list_metrics_for_namespace(
#     Aws::CloudWatch::Client.new(region: 'us-east-1'),
#     'SITE/TRAFFIC'
#   )
def list_metrics_for_namespace(cloudwatch_client, metric_namespace)
  response = cloudwatch_client.list_metrics(namespace: metric_namespace)

  if response.metrics.count.positive?
    response.metrics.each do |metric|
      puts "  Metric name: #{metric.metric_name}"
      if metric.dimensions.count.positive?
        puts '    Dimensions:'
        metric.dimensions.each do |dimension|
          puts "      Name: #{dimension.name}, Value: #{dimension.value}"
        end
      else
        puts 'No dimensions found.'
      end
    end
  else
    puts "No metrics found for namespace '#{metric_namespace}'. " \
      'Note that it could take up to 15 minutes for recently-added metrics ' \
      'to become available.'
  end
end

# Example usage:
def run_me
  metric_namespace = 'SITE/TRAFFIC'
  # Replace us-west-2 with the AWS Region you're using for Amazon CloudWatch.
  region = 'us-east-1'

  cloudwatch_client = Aws::CloudWatch::Client.new(region: region)

  # Add three datapoints.
  puts 'Continuing...' unless datapoint_added_to_metric?(
    cloudwatch_client,
    metric_namespace,
    'UniqueVisitors',
    'SiteName',
    'example.com',
    5_885.0,
    'Count'
  )

  puts 'Continuing...' unless datapoint_added_to_metric?(
    cloudwatch_client,
    metric_namespace,
    'UniqueVisits',
    'SiteName',
    'example.com',
    8_628.0,
    'Count'
  )

  puts 'Continuing...' unless datapoint_added_to_metric?(
    cloudwatch_client,
    metric_namespace,
    'PageViews',
    'PageURL',
    'example.html',
    18_057.0,
    'Count'
  )

  puts "Metrics for namespace '#{metric_namespace}':"
  list_metrics_for_namespace(cloudwatch_client, metric_namespace)
end

run_me if $PROGRAM_NAME == __FILE__
```
+  For API details, see [ListMetrics](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListMetrics) in *AWS SDK for Ruby API Reference*.

### `PutAlarmMuteRule`
<a name="cloudwatch_PutAlarmMuteRule_ruby_topic"></a>

The following code example shows how to use `PutAlarmMuteRule`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples).

```
# Creates or updates an alarm mute rule. While a mute rule is active the targeted alarms
# keep evaluating and keep transitioning between states, but their configured actions do
# not fire. This is the supported way to suppress notifications during a known
# maintenance window, instead of disabling alarm actions and relying on someone to turn
# them back on.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param name [String] The name of the mute rule.
# @param schedule [Hash] The mute window, mirroring the +rule.schedule+ shape:
#   * +:expression+ [String] When the rule activates. For a recurring window, use a
#     five-field cron expression,
#     'cron(Minutes Hours Day-of-month Month Day-of-week)', such as
#     'cron(0 2 * * SUN)' for every Sunday at 2:00 AM. Note that this is five fields,
#     not the six that Amazon EventBridge uses. For a one-time window, use
#     'at(yyyy-MM-ddThh:mm)', such as 'at(2026-09-05T02:00)'.
#   * +:duration+ [String] How long the mute window lasts once it activates, in ISO 8601
#     duration format, from 'PT1M' (one minute) to 'P15D' (15 days). For example,
#     'PT2H' is two hours and 'P2DT12H' is two days and 12 hours.
#   * +:timezone+ [String] The time zone the expression is evaluated in, such as
#     'America/Los_Angeles'.
# @param alarm_names [Array] The names of up to 100 alarms to mute. If empty, the rule
#   applies to all alarms in the account.
# @param description [String] A description of the mute rule.
# @return [Boolean] true if the mute rule was created or updated; otherwise, false.
def alarm_mute_rule_created_or_updated?(
  cloudwatch_client,
  name,
  schedule,
  alarm_names,
  description
)
  params = {
    name: name,
    description: description,
    rule: {
      schedule: {
        expression: schedule[:expression],
        duration: schedule[:duration],
        timezone: schedule[:timezone]
      }
    }
  }
  params[:mute_targets] = { alarm_names: alarm_names } unless alarm_names.empty?

  cloudwatch_client.put_alarm_mute_rule(params)
  true
rescue StandardError => e
  puts "Error putting alarm mute rule: #{e.message}"
  false
end
```
+  For API details, see [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutAlarmMuteRule) in *AWS SDK for Ruby API Reference*.

### `PutMetricAlarm`
<a name="cloudwatch_PutMetricAlarm_ruby_topic"></a>

The following code example shows how to use `PutMetricAlarm`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples).
Create an alarm that evaluates a PromQL query against OpenTelemetry metrics.

```
# Creates or updates an alarm that evaluates a PromQL query.
#
# A PromQL alarm differs from a classic metric alarm in a few ways. The query can match
# many series at once, and each matching series is tracked separately as a contributor.
# Instead of counting breaching periods, you specify durations: a contributor moves to
# ALARM after it breaches continuously for the pending period, and back to OK after it
# stops breaching for the recovery period. A PromQL alarm starts in the OK state rather
# than INSUFFICIENT_DATA.
#
# The +evaluation_criteria+ union is mutually exclusive with the classic +metric_name+
# and +metrics+ parameters. When you use it you must also set +evaluation_interval+, and
# you must not set +period+, +statistic+, +threshold+, +comparison_operator+,
# +evaluation_periods+, +datapoints_to_alarm+, or +treat_missing_data+.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String] The name of the alarm, unique within the Region.
# @param criteria [Hash] The PromQL criteria, mirroring the +prom_ql_criteria+ shape:
#   * +:query+ [String] The PromQL query to evaluate, such as
#     'avg(cpu_utilization_percent) > 80'. The comparison belongs in the query itself;
#     there is no separate threshold parameter.
#   * +:pending_period+ [Integer] How long, in seconds, a contributor must breach
#     continuously before it moves to ALARM.
#   * +:recovery_period+ [Integer] How long, in seconds, a contributor must stop
#     breaching before it moves back to OK.
# @param evaluation_interval [Integer] How often, in seconds, to run the query. Valid
#   values are 10, 20, 30, and any multiple of 60, up to 3600.
# @param alarm_description [String] A description of the alarm.
# @return [Boolean] true if the alarm was created or updated; otherwise, false.
def promql_alarm_created_or_updated?(
  cloudwatch_client,
  alarm_name,
  criteria,
  evaluation_interval,
  alarm_description
)
  cloudwatch_client.put_metric_alarm(
    alarm_name: alarm_name,
    alarm_description: alarm_description,
    evaluation_criteria: {
      prom_ql_criteria: {
        query: criteria[:query],
        pending_period: criteria[:pending_period],
        recovery_period: criteria[:recovery_period]
      }
    },
    evaluation_interval: evaluation_interval
  )
  true
rescue StandardError => e
  puts "Error creating PromQL alarm: #{e.message}"
  false
end
```
Create an alarm that evaluates a single CloudWatch metric.

```
# Creates or updates an alarm in Amazon CloudWatch.
#
# @param cloudwatch_client [Aws::CloudWatch::Client]
#   An initialized CloudWatch client.
# @param alarm_name [String] The name of the alarm.
# @param alarm_description [String] A description about the alarm.
# @param metric_name [String] The name of the metric associated with the alarm.
# @param alarm_actions [Array] A list of Strings representing the
#   Amazon Resource Names (ARNs) to execute when the alarm transitions to the
#   ALARM state.
# @param namespace [String] The namespace for the metric to alarm on.
# @param statistic [String] The statistic for the metric.
# @param dimensions [Array] A list of dimensions for the metric, specified as
#   Aws::CloudWatch::Types::Dimension.
# @param period [Integer] The number of seconds before re-evaluating the metric.
# @param unit [String] The unit of measure for the statistic.
# @param evaluation_periods [Integer] The number of periods over which data is
#   compared to the specified threshold.
# @param theshold [Float] The value against which the specified statistic is compared.
# @param comparison_operator [String] The arithmetic operation to use when
#   comparing the specified statistic and threshold.
# @return [Boolean] true if the alarm was created or updated; otherwise, false.
# @example
#   exit 1 unless alarm_created_or_updated?(
#     Aws::CloudWatch::Client.new(region: 'us-east-1'),
#     'ObjectsInBucket',
#     'Objects exist in this bucket for more than 1 day.',
#     'NumberOfObjects',
#     ['arn:aws:sns:us-east-1:111111111111:Default_CloudWatch_Alarms_Topic'],
#     'AWS/S3',
#     'Average',
#     [
#       {
#         name: 'BucketName',
#         value: 'amzn-s3-demo-bucket'
#       },
#       {
#         name: 'StorageType',
#         value: 'AllStorageTypes'
#       }
#     ],
#     86_400,
#     'Count',
#     1,
#     1,
#     'GreaterThanThreshold'
#   )
def alarm_created_or_updated?(
  cloudwatch_client,
  alarm_name,
  alarm_description,
  metric_name,
  alarm_actions,
  namespace,
  statistic,
  dimensions,
  period,
  unit,
  evaluation_periods,
  threshold,
  comparison_operator
)
  cloudwatch_client.put_metric_alarm(
    alarm_name: alarm_name,
    alarm_description: alarm_description,
    metric_name: metric_name,
    alarm_actions: alarm_actions,
    namespace: namespace,
    statistic: statistic,
    dimensions: dimensions,
    period: period,
    unit: unit,
    evaluation_periods: evaluation_periods,
    threshold: threshold,
    comparison_operator: comparison_operator
  )
  true
rescue StandardError => e
  puts "Error creating alarm: #{e.message}"
  false
end
```
+  For API details, see [PutMetricAlarm](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutMetricAlarm) in *AWS SDK for Ruby API Reference*.

### `PutMetricData`
<a name="cloudwatch_PutMetricData_ruby_topic"></a>

The following code example shows how to use `PutMetricData`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples).

```
require 'aws-sdk-cloudwatch'

# Adds a datapoint to a metric in Amazon CloudWatch.
#
# @param cloudwatch_client [Aws::CloudWatch::Client]
#   An initialized CloudWatch client.
# @param metric_namespace [String] The namespace of the metric to add the
#   datapoint to.
# @param metric_name [String] The name of the metric to add the datapoint to.
# @param dimension_name [String] The name of the dimension to add the
#   datapoint to.
# @param dimension_value [String] The value of the dimension to add the
#   datapoint to.
# @param metric_value [Float] The value of the datapoint.
# @param metric_unit [String] The unit of measurement for the datapoint.
# @return [Boolean]
# @example
#   exit 1 unless datapoint_added_to_metric?(
#     Aws::CloudWatch::Client.new(region: 'us-east-1'),
#     'SITE/TRAFFIC',
#     'UniqueVisitors',
#     'SiteName',
#     'example.com',
#     5_885.0,
#     'Count'
#   )
def datapoint_added_to_metric?(
  cloudwatch_client,
  metric_namespace,
  metric_name,
  dimension_name,
  dimension_value,
  metric_value,
  metric_unit
)
  cloudwatch_client.put_metric_data(
    namespace: metric_namespace,
    metric_data: [
      {
        metric_name: metric_name,
        dimensions: [
          {
            name: dimension_name,
            value: dimension_value
          }
        ],
        value: metric_value,
        unit: metric_unit
      }
    ]
  )
  puts "Added data about '#{metric_name}' to namespace " \
    "'#{metric_namespace}'."
  true
rescue StandardError => e
  puts "Error adding data about '#{metric_name}' to namespace " \
    "'#{metric_namespace}': #{e.message}"
  false
end
```
+  For API details, see [PutMetricData](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutMetricData) in *AWS SDK for Ruby API Reference*.

### `StartOTelEnrichment`
<a name="cloudwatch_StartOTelEnrichment_ruby_topic"></a>

The following code example shows how to use `StartOTelEnrichment`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples).

```
# Turns on OTel enrichment for the account. Once enrichment is running, CloudWatch vended
# metrics that carry a resource identifier dimension, such as the Amazon EC2
# CPUUtilization metric with its InstanceId dimension, are decorated with resource ARN
# and resource tag labels and become queryable with PromQL.
#
# Resource tags on telemetry must already be enabled for the account before you call
# this operation.
#
# Note that the Ruby SDK renders the OTel prefix as +o_tel+, so the method is
# +start_o_tel_enrichment+ rather than +start_otel_enrichment+.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @return [Boolean] true if enrichment was started; otherwise, false.
def otel_enrichment_started?(cloudwatch_client)
  cloudwatch_client.start_o_tel_enrichment
  true
rescue StandardError => e
  puts "Error starting OTel enrichment: #{e.message}"
  false
end
```
+  For API details, see [StartOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/StartOTelEnrichment) in *AWS SDK for Ruby API Reference*.

### `StopOTelEnrichment`
<a name="cloudwatch_StopOTelEnrichment_ruby_topic"></a>

The following code example shows how to use `StopOTelEnrichment`.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples).

```
# Turns off OTel enrichment for the account. Existing PromQL alarms are not deleted, but
# vended metrics stop being enriched with resource ARN and tag labels, so queries that
# select on those labels stop matching.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @return [Boolean] true if enrichment was stopped; otherwise, false.
def otel_enrichment_stopped?(cloudwatch_client)
  cloudwatch_client.stop_o_tel_enrichment
  true
rescue StandardError => e
  puts "Error stopping OTel enrichment: #{e.message}"
  false
end
```
+  For API details, see [StopOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/StopOTelEnrichment) in *AWS SDK for Ruby API Reference*.

## Scenarios
<a name="scenarios"></a>

### Send OpenTelemetry metrics and alarm on them with PromQL
<a name="cloudwatch_Scenario_OTelMetrics_ruby_topic"></a>

The following code example shows how to:
+ Send OTLP metrics to the CloudWatch metrics endpoint with an OpenTelemetry Collector.
+ Start OpenTelemetry enrichment so CloudWatch correlates those metrics with your resources.
+ Create an alarm that evaluates a PromQL query across every series the query returns.
+ Inspect the individual series, called contributors, that put the alarm in ALARM state.
+ Mute the alarm for a maintenance window, then clean up.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples).
Define methods that call the CloudWatch OpenTelemetry operations.

```
# Turns on OTel enrichment for the account. Once enrichment is running, CloudWatch vended
# metrics that carry a resource identifier dimension, such as the Amazon EC2
# CPUUtilization metric with its InstanceId dimension, are decorated with resource ARN
# and resource tag labels and become queryable with PromQL.
#
# Resource tags on telemetry must already be enabled for the account before you call
# this operation.
#
# Note that the Ruby SDK renders the OTel prefix as +o_tel+, so the method is
# +start_o_tel_enrichment+ rather than +start_otel_enrichment+.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @return [Boolean] true if enrichment was started; otherwise, false.
def otel_enrichment_started?(cloudwatch_client)
  cloudwatch_client.start_o_tel_enrichment
  true
rescue StandardError => e
  puts "Error starting OTel enrichment: #{e.message}"
  false
end

# Gets the current OTel enrichment status for the account.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @return [String, nil] 'Running' or 'Stopped', or nil if the status could not be read.
def otel_enrichment_status(cloudwatch_client)
  cloudwatch_client.get_o_tel_enrichment.status
rescue StandardError => e
  puts "Error getting OTel enrichment status: #{e.message}"
  nil
end

# Creates or updates an alarm that evaluates a PromQL query.
#
# A PromQL alarm differs from a classic metric alarm in a few ways. The query can match
# many series at once, and each matching series is tracked separately as a contributor.
# Instead of counting breaching periods, you specify durations: a contributor moves to
# ALARM after it breaches continuously for the pending period, and back to OK after it
# stops breaching for the recovery period. A PromQL alarm starts in the OK state rather
# than INSUFFICIENT_DATA.
#
# The +evaluation_criteria+ union is mutually exclusive with the classic +metric_name+
# and +metrics+ parameters. When you use it you must also set +evaluation_interval+, and
# you must not set +period+, +statistic+, +threshold+, +comparison_operator+,
# +evaluation_periods+, +datapoints_to_alarm+, or +treat_missing_data+.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String] The name of the alarm, unique within the Region.
# @param criteria [Hash] The PromQL criteria, mirroring the +prom_ql_criteria+ shape:
#   * +:query+ [String] The PromQL query to evaluate, such as
#     'avg(cpu_utilization_percent) > 80'. The comparison belongs in the query itself;
#     there is no separate threshold parameter.
#   * +:pending_period+ [Integer] How long, in seconds, a contributor must breach
#     continuously before it moves to ALARM.
#   * +:recovery_period+ [Integer] How long, in seconds, a contributor must stop
#     breaching before it moves back to OK.
# @param evaluation_interval [Integer] How often, in seconds, to run the query. Valid
#   values are 10, 20, 30, and any multiple of 60, up to 3600.
# @param alarm_description [String] A description of the alarm.
# @return [Boolean] true if the alarm was created or updated; otherwise, false.
def promql_alarm_created_or_updated?(
  cloudwatch_client,
  alarm_name,
  criteria,
  evaluation_interval,
  alarm_description
)
  cloudwatch_client.put_metric_alarm(
    alarm_name: alarm_name,
    alarm_description: alarm_description,
    evaluation_criteria: {
      prom_ql_criteria: {
        query: criteria[:query],
        pending_period: criteria[:pending_period],
        recovery_period: criteria[:recovery_period]
      }
    },
    evaluation_interval: evaluation_interval
  )
  true
rescue StandardError => e
  puts "Error creating PromQL alarm: #{e.message}"
  false
end

# Gets the contributors for a PromQL alarm. Each contributor is one series that the
# alarm's query matched, identified by its label set. This is how you find out which
# hosts, services, or pods are breaching, rather than only that something is.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String] The name of the PromQL alarm.
# @return [Array] The contributors, as Aws::CloudWatch::Types::AlarmContributor.
def alarm_contributors(cloudwatch_client, alarm_name)
  contributors = []
  next_token = nil

  loop do
    response = cloudwatch_client.describe_alarm_contributors(
      alarm_name: alarm_name,
      next_token: next_token
    )
    contributors.concat(response.alarm_contributors)
    next_token = response.next_token
    break if next_token.nil? || next_token.empty?
  end

  contributors
rescue StandardError => e
  puts "Error getting alarm contributors: #{e.message}"
  []
end

# Creates or updates an alarm mute rule. While a mute rule is active the targeted alarms
# keep evaluating and keep transitioning between states, but their configured actions do
# not fire. This is the supported way to suppress notifications during a known
# maintenance window, instead of disabling alarm actions and relying on someone to turn
# them back on.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param name [String] The name of the mute rule.
# @param schedule [Hash] The mute window, mirroring the +rule.schedule+ shape:
#   * +:expression+ [String] When the rule activates. For a recurring window, use a
#     five-field cron expression,
#     'cron(Minutes Hours Day-of-month Month Day-of-week)', such as
#     'cron(0 2 * * SUN)' for every Sunday at 2:00 AM. Note that this is five fields,
#     not the six that Amazon EventBridge uses. For a one-time window, use
#     'at(yyyy-MM-ddThh:mm)', such as 'at(2026-09-05T02:00)'.
#   * +:duration+ [String] How long the mute window lasts once it activates, in ISO 8601
#     duration format, from 'PT1M' (one minute) to 'P15D' (15 days). For example,
#     'PT2H' is two hours and 'P2DT12H' is two days and 12 hours.
#   * +:timezone+ [String] The time zone the expression is evaluated in, such as
#     'America/Los_Angeles'.
# @param alarm_names [Array] The names of up to 100 alarms to mute. If empty, the rule
#   applies to all alarms in the account.
# @param description [String] A description of the mute rule.
# @return [Boolean] true if the mute rule was created or updated; otherwise, false.
def alarm_mute_rule_created_or_updated?(
  cloudwatch_client,
  name,
  schedule,
  alarm_names,
  description
)
  params = {
    name: name,
    description: description,
    rule: {
      schedule: {
        expression: schedule[:expression],
        duration: schedule[:duration],
        timezone: schedule[:timezone]
      }
    }
  }
  params[:mute_targets] = { alarm_names: alarm_names } unless alarm_names.empty?

  cloudwatch_client.put_alarm_mute_rule(params)
  true
rescue StandardError => e
  puts "Error putting alarm mute rule: #{e.message}"
  false
end

# Gets the full configuration of an alarm mute rule, including its schedule, the alarms
# it targets, and whether it is currently SCHEDULED, ACTIVE, or EXPIRED.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param name [String] The name of the mute rule.
# @return [Aws::CloudWatch::Types::GetAlarmMuteRuleOutput, nil] The mute rule, or nil on
#   error.
def alarm_mute_rule(cloudwatch_client, name)
  cloudwatch_client.get_alarm_mute_rule(alarm_mute_rule_name: name)
rescue StandardError => e
  puts "Error getting alarm mute rule: #{e.message}"
  nil
end

# Lists the alarm mute rules in the account, optionally filtered to the rules that
# target one alarm.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String, nil] When given, only rules that target this alarm are
#   returned.
# @return [Array] The mute rule summaries, as
#   Aws::CloudWatch::Types::AlarmMuteRuleSummary.
def alarm_mute_rules(cloudwatch_client, alarm_name = nil)
  summaries = []
  next_token = nil

  loop do
    response = cloudwatch_client.list_alarm_mute_rules(
      alarm_name: alarm_name,
      next_token: next_token
    )
    summaries.concat(response.alarm_mute_rule_summaries)
    next_token = response.next_token
    break if next_token.nil? || next_token.empty?
  end

  summaries
rescue StandardError => e
  puts "Error listing alarm mute rules: #{e.message}"
  []
end

# Deletes an alarm mute rule. The alarms it targeted resume firing their actions.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param name [String] The name of the mute rule.
# @return [Boolean] true if the mute rule was deleted; otherwise, false.
def alarm_mute_rule_deleted?(cloudwatch_client, name)
  cloudwatch_client.delete_alarm_mute_rule(alarm_mute_rule_name: name)
  true
rescue StandardError => e
  puts "Error deleting alarm mute rule: #{e.message}"
  false
end

# Turns off OTel enrichment for the account. Existing PromQL alarms are not deleted, but
# vended metrics stop being enriched with resource ARN and tag labels, so queries that
# select on those labels stop matching.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @return [Boolean] true if enrichment was stopped; otherwise, false.
def otel_enrichment_stopped?(cloudwatch_client)
  cloudwatch_client.stop_o_tel_enrichment
  true
rescue StandardError => e
  puts "Error stopping OTel enrichment: #{e.message}"
  false
end
```
Alarm on OpenTelemetry metrics with a PromQL query, inspect the contributors to the alarm, and mute it.

```
# Turns on OpenTelemetry enrichment if the account doesn't already have it on. Enrichment
# is an account-wide setting, so an example should only turn it off again if it was the
# one that turned it on.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @return [Boolean] true if this call started enrichment; otherwise, false.
def enrichment_started_by_example?(cloudwatch_client)
  puts 'Checking whether OTel enrichment is on for this account.'
  status = otel_enrichment_status(cloudwatch_client)
  if status == 'Stopped'
    puts 'Enrichment is stopped. Starting it so vended metrics accept PromQL.'
    return otel_enrichment_started?(cloudwatch_client)
  end

  puts "Enrichment status is '#{status}'. Leaving it alone."
  false
end

# Prints the contributors to a PromQL alarm, one line per matched series.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String] The name of the PromQL alarm.
def report_alarm_contributors(cloudwatch_client, alarm_name)
  puts "\nContributors for '#{alarm_name}':"
  contributors = alarm_contributors(cloudwatch_client, alarm_name)
  if contributors.empty?
    puts '  None yet. The query matched no series, which usually means no OTel metrics ' \
         'with these labels have arrived.'
    return
  end

  contributors.each do |contributor|
    labels = contributor.contributor_attributes.sort.map { |k, v| "#{k}=#{v}" }.join(', ')
    puts "  #{contributor.contributor_id}: #{labels}"
    puts "    reason: #{contributor.state_reason}"
  end
end

# Mutes an alarm for a recurring weekly maintenance window.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param mute_rule_name [String] The name of the mute rule to create.
# @param alarm_name [String] The name of the alarm to mute.
def mute_alarm_for_maintenance(cloudwatch_client, mute_rule_name, alarm_name)
  puts "\nMuting '#{alarm_name}' for a weekly two-hour maintenance window."
  schedule = {
    expression: 'cron(0 2 * * SUN)',
    duration: 'PT2H',
    timezone: 'America/Los_Angeles'
  }
  return unless alarm_mute_rule_created_or_updated?(
    cloudwatch_client,
    mute_rule_name,
    schedule,
    [alarm_name],
    'Suppress checkout CPU pages during Sunday patching.'
  )

  rule = alarm_mute_rule(cloudwatch_client, mute_rule_name)
  puts "Mute rule status is #{rule.status}." unless rule.nil?
  puts 'While the window is active the alarm keeps evaluating and still changes ' \
       'state; only its actions are suppressed.'
end

# Removes the mute rule and the alarm, and stops enrichment if this example started it.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String] The name of the alarm to delete.
# @param mute_rule_name [String] The name of the mute rule to delete.
# @param started_here [Boolean] Whether this example started OTel enrichment.
def clean_up(cloudwatch_client, alarm_name, mute_rule_name, started_here)
  puts "\nCleaning up."
  alarm_mute_rule_deleted?(cloudwatch_client, mute_rule_name)
  cloudwatch_client.delete_alarms(alarm_names: [alarm_name])
  return unless started_here

  puts 'Stopping OTel enrichment, since this example started it.'
  otel_enrichment_stopped?(cloudwatch_client)
end

# Walks through the OpenTelemetry metrics workflow in CloudWatch: turn on enrichment,
# alarm on a PromQL query, inspect the contributors that matched, mute the alarm for a
# maintenance window, then clean up.
#
# This scenario assumes OpenTelemetry metrics are already flowing into the account,
# either from an OpenTelemetry collector, the CloudWatch agent, or the ADOT SDK.
def run_me
  alarm_name = 'doc-example-promql-high-cpu'
  mute_rule_name = 'doc-example-maintenance-window'
  query = 'avg by (host_name) (cpu_utilization_percent{service_name="checkout"}) > 80'
  # Replace us-east-1 with the AWS Region you're using for Amazon CloudWatch.
  region = 'us-east-1'

  cloudwatch_client = Aws::CloudWatch::Client.new(region: region)
  started_here = enrichment_started_by_example?(cloudwatch_client)

  puts "\nCreating a PromQL alarm on: #{query}"
  criteria = { query: query, pending_period: 300, recovery_period: 120 }
  unless promql_alarm_created_or_updated?(
    cloudwatch_client,
    alarm_name,
    criteria,
    30,
    'Average CPU over 80% per host for the checkout service.'
  )
    puts "Could not create alarm '#{alarm_name}'. Stopping."
    return
  end
  puts 'The alarm evaluates every 30 seconds. A host moves to ALARM after breaching ' \
       'for 300 seconds straight, and back to OK after 120 seconds clean.'

  report_alarm_contributors(cloudwatch_client, alarm_name)
  mute_alarm_for_maintenance(cloudwatch_client, mute_rule_name, alarm_name)

  puts "\nMute rules targeting '#{alarm_name}':"
  alarm_mute_rules(cloudwatch_client, alarm_name).each do |summary|
    puts "  #{summary.alarm_mute_rule_arn} (#{summary.status})"
  end

  clean_up(cloudwatch_client, alarm_name, mute_rule_name, started_here)
end
```
+ For API details, see the following topics in *AWS SDK for Ruby API Reference*.
  + [DeleteAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteAlarmMuteRule)
  + [DeleteAlarms](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteAlarms)
  + [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarmContributors)
  + [GetAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetAlarmMuteRule)
  + [GetOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetOTelEnrichment)
  + [ListAlarmMuteRules](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListAlarmMuteRules)
  + [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutAlarmMuteRule)
  + [PutMetricAlarm](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutMetricAlarm)
  + [StartOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/StartOTelEnrichment)
  + [StopOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/StopOTelEnrichment)
