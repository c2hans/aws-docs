---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_InternetHealth.html
---

# InternetHealth
<a name="API_InternetHealth"></a>

Internet health includes measurements calculated by Internet Monitor about the performance and availability for your application on the internet. AWS has substantial historical data about internet performance and availability between AWS services and different network providers and geographies. By applying statistical analysis to the data, Internet Monitor can detect when the performance and availability for your application has dropped, compared to an estimated baseline that's already calculated. To make it easier to see those drops, Internet Monitor reports the information to you in the form of health scores: a performance score and an availability score.

## Contents
<a name="API_InternetHealth_Contents"></a>

 ** Availability **   <a name="internetmonitor-Type-InternetHealth-Availability"></a>
Availability in Internet Monitor represents the estimated percentage of traffic that is not seeing an availability drop. For example, an availability score of 99% for an end user and service location pair is equivalent to 1% of the traffic experiencing an availability drop for that pair.
For more information, see [How Internet Monitor calculates performance and availability scores](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html#IMExperienceScores) in the Internet Monitor section of the *CloudWatch User Guide*.
Type: [AvailabilityMeasurement](API_AvailabilityMeasurement.md) object
Required: No

 ** Performance **   <a name="internetmonitor-Type-InternetHealth-Performance"></a>
Performance in Internet Monitor represents the estimated percentage of traffic that is not seeing a performance drop. For example, a performance score of 99% for an end user and service location pair is equivalent to 1% of the traffic experiencing a performance drop for that pair.
For more information, see [How Internet Monitor calculates performance and availability scores](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html#IMExperienceScores) in the Internet Monitor section of the *CloudWatch User Guide*.
Type: [PerformanceMeasurement](API_PerformanceMeasurement.md) object
Required: No

## See Also
<a name="API_InternetHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/InternetHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/InternetHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/InternetHealth)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Internet Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query internet-monitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
