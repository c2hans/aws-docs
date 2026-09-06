---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_HealthEvent.html
---

# HealthEvent
<a name="API_HealthEvent"></a>

Information about a health event created in a monitor in Internet Monitor.

## Contents
<a name="API_HealthEvent_Contents"></a>

 ** EventArn **   <a name="internetmonitor-Type-HealthEvent-EventArn"></a>
The Amazon Resource Name (ARN) of the event.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** EventId **   <a name="internetmonitor-Type-HealthEvent-EventId"></a>
The internally-generated identifier of a specific network traffic impairment health event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9/_.-]+`
Required: Yes

 ** ImpactedLocations **   <a name="internetmonitor-Type-HealthEvent-ImpactedLocations"></a>
The locations impacted by the health event.
Type: Array of [ImpactedLocation](API_ImpactedLocation.md) objects
Required: Yes

 ** ImpactType **   <a name="internetmonitor-Type-HealthEvent-ImpactType"></a>
The type of impairment for a health event.
Type: String
Valid Values: `AVAILABILITY | PERFORMANCE | LOCAL_AVAILABILITY | LOCAL_PERFORMANCE`
Required: Yes

 ** LastUpdatedAt **   <a name="internetmonitor-Type-HealthEvent-LastUpdatedAt"></a>
When the health event was last updated.
Type: Timestamp
Required: Yes

 ** StartedAt **   <a name="internetmonitor-Type-HealthEvent-StartedAt"></a>
When a health event started.
Type: Timestamp
Required: Yes

 ** Status **   <a name="internetmonitor-Type-HealthEvent-Status"></a>
The status of a health event.
Type: String
Valid Values: `ACTIVE | RESOLVED`
Required: Yes

 ** CreatedAt **   <a name="internetmonitor-Type-HealthEvent-CreatedAt"></a>
When the health event was created.
Type: Timestamp
Required: No

 ** EndedAt **   <a name="internetmonitor-Type-HealthEvent-EndedAt"></a>
The time when a health event ended. If the health event is still active, then the end time is not set.
Type: Timestamp
Required: No

 ** HealthScoreThreshold **   <a name="internetmonitor-Type-HealthEvent-HealthScoreThreshold"></a>
The value of the threshold percentage for performance or availability that was configured when Internet Monitor created the health event.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** PercentOfTotalTrafficImpacted **   <a name="internetmonitor-Type-HealthEvent-PercentOfTotalTrafficImpacted"></a>
The impact on total traffic that a health event has, in increased latency or reduced availability. This is the percentage of how much latency has increased or availability has decreased during the event, compared to what is typical for traffic from this client location to the AWS location using this client network.
Type: Double
Required: No

## See Also
<a name="API_HealthEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/HealthEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/HealthEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/HealthEvent)
