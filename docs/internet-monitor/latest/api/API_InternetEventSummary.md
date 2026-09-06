---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_InternetEventSummary.html
---

# InternetEventSummary
<a name="API_InternetEventSummary"></a>

A summary of information about an internet event in Internet Monitor. Internet events are issues that cause performance degradation or availability problems for impacted AWS client locations. Internet Monitor displays information about recent global health events, called internet events, on a global outages map that is available to all AWS customers.

## Contents
<a name="API_InternetEventSummary_Contents"></a>

 ** ClientLocation **   <a name="internetmonitor-Type-InternetEventSummary-ClientLocation"></a>
The impacted location, such as a city, that AWS clients access application resources from.
Type: [ClientLocation](API_ClientLocation.md) object
Required: Yes

 ** EventArn **   <a name="internetmonitor-Type-InternetEventSummary-EventArn"></a>
The Amazon Resource Name (ARN) of the internet event.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** EventId **   <a name="internetmonitor-Type-InternetEventSummary-EventId"></a>
The internally-generated identifier of an internet event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** EventStatus **   <a name="internetmonitor-Type-InternetEventSummary-EventStatus"></a>
The status of an internet event.
Type: String
Valid Values: `ACTIVE | RESOLVED`
Required: Yes

 ** EventType **   <a name="internetmonitor-Type-InternetEventSummary-EventType"></a>
The type of network impairment.
Type: String
Valid Values: `AVAILABILITY | PERFORMANCE`
Required: Yes

 ** StartedAt **   <a name="internetmonitor-Type-InternetEventSummary-StartedAt"></a>
The time when an internet event started.
Type: Timestamp
Required: Yes

 ** EndedAt **   <a name="internetmonitor-Type-InternetEventSummary-EndedAt"></a>
The time when an internet event ended. If the event hasn't ended yet, this value is empty.
Type: Timestamp
Required: No

## See Also
<a name="API_InternetEventSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/InternetEventSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/InternetEventSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/InternetEventSummary)
