---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_LocalHealthEventsConfig.html
---

# LocalHealthEventsConfig
<a name="API_LocalHealthEventsConfig"></a>

A complex type with the configuration information that determines the threshold and other conditions for when Internet Monitor creates a health event for a local performance or availability issue, when scores cross a threshold for one or more city-networks.

Defines the percentages, for performance scores or availability scores, that are the local thresholds for when Internet Monitor creates a health event. Also defines whether a local threshold is enabled or disabled, and the minimum percentage of overall traffic that must be impacted by an issue before Internet Monitor creates an event when a threshold is crossed for a local health score.

If you don't set a local health event threshold, the default value is 60%.

For more information, see [ Change health event thresholds](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-overview.html#IMUpdateThresholdFromOverview) in the Internet Monitor section of the *CloudWatch User Guide*.

## Contents
<a name="API_LocalHealthEventsConfig_Contents"></a>

 ** HealthScoreThreshold **   <a name="internetmonitor-Type-LocalHealthEventsConfig-HealthScoreThreshold"></a>
The health event threshold percentage set for a local health score.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** MinTrafficImpact **   <a name="internetmonitor-Type-LocalHealthEventsConfig-MinTrafficImpact"></a>
The minimum percentage of overall traffic for an application that must be impacted by an issue before Internet Monitor creates an event when a threshold is crossed for a local health score.
If you don't set a minimum traffic impact threshold, the default value is 0.1%.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Status **   <a name="internetmonitor-Type-LocalHealthEventsConfig-Status"></a>
The status of whether Internet Monitor creates a health event based on a threshold percentage set for a local health score. The status can be `ENABLED` or `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_LocalHealthEventsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/LocalHealthEventsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/LocalHealthEventsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/LocalHealthEventsConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Internet Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query internet-monitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
