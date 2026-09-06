---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_Insight.html
---

# Insight
<a name="API_Insight"></a>

Represents an insight returned by the `ListInsights` operation. An insight is a notification about a domain event or recommendation that helps you optimize your Amazon OpenSearch Service domain.

## Contents
<a name="API_Insight_Contents"></a>

 ** CreationTime **   <a name="opensearchservice-Type-Insight-CreationTime"></a>
The timestamp when the insight was created, in epoch milliseconds.
Type: Timestamp
Required: No

 ** DisplayName **   <a name="opensearchservice-Type-Insight-DisplayName"></a>
The display name of the insight.
Type: String
Required: No

 ** InsightId **   <a name="opensearchservice-Type-Insight-InsightId"></a>
The unique identifier of the insight.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `\p{XDigit}{8}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{12}`
Required: No

 ** IsExperimental **   <a name="opensearchservice-Type-Insight-IsExperimental"></a>
Indicates whether the insight is experimental.
Type: Boolean
Required: No

 ** Priority **   <a name="opensearchservice-Type-Insight-Priority"></a>
The priority level of the insight. Possible values are `CRITICAL`, `HIGH`, `MEDIUM`, and `LOW`.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW`
Required: No

 ** Status **   <a name="opensearchservice-Type-Insight-Status"></a>
The current status of the insight. Possible values are `ACTIVE`, `RESOLVED`, and `DISMISSED`.
Type: String
Valid Values: `ACTIVE | RESOLVED | DISMISSED`
Required: No

 ** Type **   <a name="opensearchservice-Type-Insight-Type"></a>
The type of the insight. Possible values are `EVENT` and `RECOMMENDATION`.
Type: String
Valid Values: `EVENT | RECOMMENDATION`
Required: No

 ** UpdateTime **   <a name="opensearchservice-Type-Insight-UpdateTime"></a>
The timestamp when the insight was last updated, in epoch milliseconds.
Type: Timestamp
Required: No

## See Also
<a name="API_Insight_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/Insight)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/Insight)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/Insight)
