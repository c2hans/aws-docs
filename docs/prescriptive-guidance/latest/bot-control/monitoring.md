---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/bot-control/monitoring.html
---

# Guidelines for monitoring your bot control strategy
<a name="monitoring"></a>

For bot traffic and web application traffic, monitoring and visibility is of great importance. It helps you prioritize activities as well as security operations. If detailed logging or using a SIEM system are not possible, then a good starting point is monitoring basic metrics provided by your selected solution or vendor.

This visibility is useful for threat intelligence, hardening rules, troubleshooting false positives, and responding to an incident. There are multiple monitoring options available with AWS WAF. For high-level monitoring, AWS WAF provides traffic overview information in the AWS Management Console. This is available for all traffic as well as a detailed view for bot traffic, when the Bot Control rule group is enabled in your web ACL.

AWS WAF provides different options for detailed [logging of web ACL traffic](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html). You can also add labels to requests, which you can use to facilitate log analysis and configure bot evaluation rules. By integrating [Amazon CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html), you can query the AWS WAF logs and visualize the results.

If you turn on detailed logging, AWS WAF provides additional visibility beyond the preconfigured **Bot control dashboard**. Using AWS WAF logs to visualize traffic, as well as ad-hoc investigations, can provide in-depth understanding of traffic patterns and options for mitigation for a web application.

You can integrate AWS WAF log data with Amazon CloudWatch Logs, Amazon Simple Storage Service (Amazon S3), or Amazon Data Firehose. For more information, see [Turn on AWS WAF logging and send logs to CloudWatch, Amazon S3, or Amazon Data Firehose](https://repost.aws/knowledge-center/waf-turn-on-logging). You can also send logs to various targets for analysis, including to Amazon OpenSearch Service or an [AWS Marketplace](https://aws.amazon.com/marketplace) solution. For more information, see [Destination settings](https://docs.aws.amazon.com/firehose/latest/dev/create-destination.html) in the Firehose documentation. If multiple log sources are used, a centralized logging solution is recommended to correlate sources.

Next, this guide provides recommendations for how to start monitoring bot traffic and gain visibility by using Amazon CloudWatch.

## Tracking top rules
<a name="top-rules"></a>

Tracking the top-hit rules can highlight trends and potentially anomalous activities. Increased rates for a specific rule might indicate a potential false positive or targeted activity that you should investigate. The most common rule for tracking would be [IP-based rules](static-controls.md#ip-based-controls), geo-blocking rules (a spike here can show traffic from unusual countries, which might not be automatically blocked), and rate-based rules. These rules would always have inherent variation, but an anomaly in the traffic pattern can be indicative of bot activity. Take this into consideration if you're manually setting the thresholds.

## Tracking top labels and namespaces
<a name="top-labels"></a>

By using CloudWatch metrics to track the top [labels](https://docs.aws.amazon.com/waf/latest/developerguide/waf-labels.html), you can see which AWS WAF rules are frequently being invoked. This helps you detect anomalies, such as an increase in scraper activity, traffic from suspicious sources, or attempted abuse of the application login page or API.

The following are example labels that might be of interest:
+ `awswaf:managed:aws:bot-control:signal:non_browser_user_agent `
+ `awswaf:managed:aws:bot-control:bot:category:http_library`
+ `awswaf:managed:aws:bot-control:bot:name:curl`
+ `awswaf:managed:aws:atp:signal:credential_compromised`
+ `awswaf:managed:aws:core-rule-set:NoUserAgent_Header`
+ `awswaf:managed:token:rejected`

The following are example label namespaces that might be of interest:
+ `awswaf:managed:aws:bot-control:`
+ `awswaf:managed:aws:atp:`
+ `awswaf:managed:aws:anonymous-ip-list:`

## Creating math expressions
<a name="math-expressions"></a>

In Amazon CloudWatch, you can create [math expressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) for any or all rules. If you set alerts on math expressions, you will be notified regarding anomalies in rates, not quantities, of certain metrics. This is an important tool to reduce alert fatigue.

Create a custom metric built out of a math expression. Look at the relative rates for rules, out of the overall number of requests to an application. The following is a common math expression:

`[ruleX count * 100]/[All allowed requests + All blocked requests]`

This math expression provides a percentage so that you can track a specific rule and visualize its trend over time.

## Using anomaly detection
<a name="anomaly-detection"></a>

Using [CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) on any CloudWatch metric can provide alerts on abnormally low or high trends, without setting up the actual threshold manually. These algorithms continuously analyze metrics of systems and applications, determine normal baselines, and surface anomalies with minimal user intervention. CloudWatch applies statistical and ML algorithms in its anomaly detection feature.

## Using Amazon CloudWatch metrics
<a name="cloudwatch-metrics"></a>

AWS WAF processes traffic and adds labels to requests that match the rules defined in the web ACL. Each label creates a [metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) in CloudWatch. At the same time, each web ACL rule also creates metrics for each of its possible actions. Use these label and action metrics to gain a high-level understanding of bot traffic. This is a cost-effective approach to visualizing trends. For more information, see [View available metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.html) and [Graphing metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph_metrics.html) in the CloudWatch documentation.

CloudWatch provides the option to send data to a log collector or aggregator, be it an AWS service or a third-party solution. Ingesting data from CloudWatch can provide a more consolidated security observability experience, where you can correlate data from multiple sources. This can help you investigate, view, or set up your alerts and security automations.

## Building a dashboard
<a name="dashboard"></a>

After identifying the important metrics to track, create a dashboard that contains the most relevant metrics. Displaying them side-by-side, under a single pane of glass can provide additional visibility and control.

It is always preferable to configure alerts and automation rules for anomalous metric values. Do not rely on humans to identify anomalies by looking at a dashboard. However, dashboards can be useful for investigation purposes after an alert has been received.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
