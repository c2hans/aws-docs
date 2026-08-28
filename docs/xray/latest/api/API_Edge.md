---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_Edge.html
---

# Edge
<a name="API_Edge"></a>

Information about a connection between two services. An edge can be a synchronous connection, such as typical call between client and service, or an asynchronous link, such as a Lambda function which retrieves an event from an SNS queue.

## Contents
<a name="API_Edge_Contents"></a>

 ** Aliases **   <a name="xray-Type-Edge-Aliases"></a>
Aliases for the edge.
Type: Array of [Alias](API_Alias.md) objects
Required: No

 ** EdgeType **   <a name="xray-Type-Edge-EdgeType"></a>
Describes an asynchronous connection, with a value of `link`.
Type: String
Required: No

 ** EndTime **   <a name="xray-Type-Edge-EndTime"></a>
The end time of the last segment on the edge.
Type: Timestamp
Required: No

 ** ReceivedEventAgeHistogram **   <a name="xray-Type-Edge-ReceivedEventAgeHistogram"></a>
A histogram that maps the spread of event age when received by consumers. Age is calculated each time an event is received. Only populated when *EdgeType* is `link`.
Type: Array of [HistogramEntry](API_HistogramEntry.md) objects
Required: No

 ** ReferenceId **   <a name="xray-Type-Edge-ReferenceId"></a>
Identifier of the edge. Unique within a service map.
Type: Integer
Required: No

 ** ResponseTimeHistogram **   <a name="xray-Type-Edge-ResponseTimeHistogram"></a>
A histogram that maps the spread of client response times on an edge. Only populated for synchronous edges.
Type: Array of [HistogramEntry](API_HistogramEntry.md) objects
Required: No

 ** StartTime **   <a name="xray-Type-Edge-StartTime"></a>
The start time of the first segment on the edge.
Type: Timestamp
Required: No

 ** SummaryStatistics **   <a name="xray-Type-Edge-SummaryStatistics"></a>
Response statistics for segments on the edge.
Type: [EdgeStatistics](API_EdgeStatistics.md) object
Required: No

## See Also
<a name="API_Edge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/Edge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/Edge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/Edge)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
