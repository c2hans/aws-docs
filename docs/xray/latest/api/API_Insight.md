---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_Insight.html
---

# Insight
<a name="API_Insight"></a>

When fault rates go outside of the expected range, X-Ray creates an insight. Insights tracks emergent issues within your applications.

## Contents
<a name="API_Insight_Contents"></a>

 ** Categories **   <a name="xray-Type-Insight-Categories"></a>
The categories that label and describe the type of insight.
Type: Array of strings
Valid Values: `FAULT`
Required: No

 ** ClientRequestImpactStatistics **   <a name="xray-Type-Insight-ClientRequestImpactStatistics"></a>
The impact statistics of the client side service. This includes the number of requests to the client service and whether the requests were faults or okay.
Type: [RequestImpactStatistics](API_RequestImpactStatistics.md) object
Required: No

 ** EndTime **   <a name="xray-Type-Insight-EndTime"></a>
The time, in Unix seconds, at which the insight ended.
Type: Timestamp
Required: No

 ** GroupARN **   <a name="xray-Type-Insight-GroupARN"></a>
The Amazon Resource Name (ARN) of the group that the insight belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: No

 ** GroupName **   <a name="xray-Type-Insight-GroupName"></a>
The name of the group that the insight belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** InsightId **   <a name="xray-Type-Insight-InsightId"></a>
The insights unique identifier.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`
Required: No

 ** RootCauseServiceId **   <a name="xray-Type-Insight-RootCauseServiceId"></a>

Type: [ServiceId](API_ServiceId.md) object
Required: No

 ** RootCauseServiceRequestImpactStatistics **   <a name="xray-Type-Insight-RootCauseServiceRequestImpactStatistics"></a>
The impact statistics of the root cause service. This includes the number of requests to the client service and whether the requests were faults or okay.
Type: [RequestImpactStatistics](API_RequestImpactStatistics.md) object
Required: No

 ** StartTime **   <a name="xray-Type-Insight-StartTime"></a>
The time, in Unix seconds, at which the insight began.
Type: Timestamp
Required: No

 ** State **   <a name="xray-Type-Insight-State"></a>
The current state of the insight.
Type: String
Valid Values: `ACTIVE | CLOSED`
Required: No

 ** Summary **   <a name="xray-Type-Insight-Summary"></a>
A brief description of the insight.
Type: String
Required: No

 ** TopAnomalousServices **   <a name="xray-Type-Insight-TopAnomalousServices"></a>
The service within the insight that is most impacted by the incident.
Type: Array of [AnomalousService](API_AnomalousService.md) objects
Required: No

## See Also
<a name="API_Insight_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/Insight)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/Insight)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/Insight)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
