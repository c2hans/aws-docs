---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_AvailabilityMeasurement.html
---

# AvailabilityMeasurement
<a name="API_AvailabilityMeasurement"></a>

Internet Monitor calculates measurements about the availability for your application's internet traffic between client locations and AWS. AWS has substantial historical data about internet performance and availability between AWS services and different network providers and geographies. By applying statistical analysis to the data, Internet Monitor can detect when the performance and availability for your application has dropped, compared to an estimated baseline that's already calculated. To make it easier to see those drops, we report that information to you in the form of health scores: a performance score and an availability score.

Availability in Internet Monitor represents the estimated percentage of traffic that is not seeing an availability drop. For example, an availability score of 99% for an end user and service location pair is equivalent to 1% of the traffic experiencing an availability drop for that pair.

For more information, see [How Internet Monitor calculates performance and availability scores](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html#IMExperienceScores) in the Internet Monitor section of the *Amazon CloudWatch User Guide*.

## Contents
<a name="API_AvailabilityMeasurement_Contents"></a>

 ** ExperienceScore **   <a name="internetmonitor-Type-AvailabilityMeasurement-ExperienceScore"></a>
Experience scores, or health scores are calculated for different geographic and network provider combinations (that is, different granularities) and also summed into global scores. If you view performance or availability scores without filtering for any specific geography or service provider, Internet Monitor provides global health scores.
The Internet Monitor chapter in the *CloudWatch User Guide* includes detailed information about how Internet Monitor calculates health scores, including performance and availability scores, and when it creates and resolves health events. For more information, see [How AWS calculates performance and availability scores](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html#IMExperienceScores) in the Internet Monitor section of the *CloudWatch User Guide*.
Type: Double
Required: No

 ** PercentOfClientLocationImpacted **   <a name="internetmonitor-Type-AvailabilityMeasurement-PercentOfClientLocationImpacted"></a>
The percentage of impact caused by a health event for client location traffic globally.
For information about how Internet Monitor calculates impact, see [Inside Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html) in the Internet Monitor section of the Amazon CloudWatch User Guide.
Type: Double
Required: No

 ** PercentOfTotalTrafficImpacted **   <a name="internetmonitor-Type-AvailabilityMeasurement-PercentOfTotalTrafficImpacted"></a>
The impact on total traffic that a health event has, in increased latency or reduced availability. This is the percentage of how much latency has increased or availability has decreased during the event, compared to what is typical for traffic from this client location to the AWS location using this client network.
For information about how Internet Monitor calculates impact, see [How Internet Monitor works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html) in the Internet Monitor section of the Amazon CloudWatch User Guide.
Type: Double
Required: No

## See Also
<a name="API_AvailabilityMeasurement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/AvailabilityMeasurement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/AvailabilityMeasurement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/AvailabilityMeasurement)
