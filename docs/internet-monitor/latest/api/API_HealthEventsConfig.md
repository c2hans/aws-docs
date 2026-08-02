---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_HealthEventsConfig.html
---

# HealthEventsConfig
<a name="API_HealthEventsConfig"></a>

A complex type with the configuration information that determines the threshold and other conditions for when Internet Monitor creates a health event for an overall performance or availability issue, across an application's geographies.

Defines the percentages, for overall performance scores and availability scores for an application, that are the thresholds for when Internet Monitor creates a health event. You can override the defaults to set a custom threshold for overall performance or availability scores, or both.

You can also set thresholds for local health scores,, where Internet Monitor creates a health event when scores cross a threshold for one or more city-networks, in addition to creating an event when an overall score crosses a threshold.

If you don't set a health event threshold, the default value is 95%.

For local thresholds, you also set a minimum percentage of overall traffic that is impacted by an issue before Internet Monitor creates an event. In addition, you can disable local thresholds, for performance scores, availability scores, or both.

For more information, see [ Change health event thresholds](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-overview.html#IMUpdateThresholdFromOverview) in the Internet Monitor section of the *CloudWatch User Guide*.

## Contents
<a name="API_HealthEventsConfig_Contents"></a>

 ** AvailabilityLocalHealthEventsConfig **   <a name="internetmonitor-Type-HealthEventsConfig-AvailabilityLocalHealthEventsConfig"></a>
The configuration that determines the threshold and other conditions for when Internet Monitor creates a health event for a local availability issue.
Type: [LocalHealthEventsConfig](API_LocalHealthEventsConfig.md) object
Required: No

 ** AvailabilityScoreThreshold **   <a name="internetmonitor-Type-HealthEventsConfig-AvailabilityScoreThreshold"></a>
The health event threshold percentage set for availability scores.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** PerformanceLocalHealthEventsConfig **   <a name="internetmonitor-Type-HealthEventsConfig-PerformanceLocalHealthEventsConfig"></a>
The configuration that determines the threshold and other conditions for when Internet Monitor creates a health event for a local performance issue.
Type: [LocalHealthEventsConfig](API_LocalHealthEventsConfig.md) object
Required: No

 ** PerformanceScoreThreshold **   <a name="internetmonitor-Type-HealthEventsConfig-PerformanceScoreThreshold"></a>
The health event threshold percentage set for performance scores.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_HealthEventsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/HealthEventsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/HealthEventsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/HealthEventsConfig)
