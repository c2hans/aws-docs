---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_InsightEvent.html
---

# InsightEvent
<a name="API_InsightEvent"></a>

X-Ray reevaluates insights periodically until they are resolved, and records each intermediate state in an event. You can review incident events in the Impact Timeline on the Inspect page in the X-Ray console.

## Contents
<a name="API_InsightEvent_Contents"></a>

 ** ClientRequestImpactStatistics **   <a name="xray-Type-InsightEvent-ClientRequestImpactStatistics"></a>
The impact statistics of the client side service. This includes the number of requests to the client service and whether the requests were faults or okay.
Type: [RequestImpactStatistics](API_RequestImpactStatistics.md) object
Required: No

 ** EventTime **   <a name="xray-Type-InsightEvent-EventTime"></a>
The time, in Unix seconds, at which the event was recorded.
Type: Timestamp
Required: No

 ** RootCauseServiceRequestImpactStatistics **   <a name="xray-Type-InsightEvent-RootCauseServiceRequestImpactStatistics"></a>
The impact statistics of the root cause service. This includes the number of requests to the client service and whether the requests were faults or okay.
Type: [RequestImpactStatistics](API_RequestImpactStatistics.md) object
Required: No

 ** Summary **   <a name="xray-Type-InsightEvent-Summary"></a>
A brief description of the event.
Type: String
Required: No

 ** TopAnomalousServices **   <a name="xray-Type-InsightEvent-TopAnomalousServices"></a>
The service during the event that is most impacted by the incident.
Type: Array of [AnomalousService](API_AnomalousService.md) objects
Required: No

## See Also
<a name="API_InsightEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/InsightEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/InsightEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/InsightEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
