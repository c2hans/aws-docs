---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Filters.html
---

# Filters
<a name="API_Filters"></a>

Contains the filter to apply when retrieving metrics.

## Contents
<a name="API_Filters_Contents"></a>

 ** AgentStatuses **   <a name="connect-Type-Filters-AgentStatuses"></a>
A list of up to 50 agent status IDs or ARNs.
Type: Array of strings
Required: No

 ** Channels **   <a name="connect-Type-Filters-Channels"></a>
The channel to use to filter the metrics.
Type: Array of strings
Array Members: Maximum number of 4 items.
Valid Values: `VOICE | CHAT | TASK | EMAIL`
Required: No

 ** Queues **   <a name="connect-Type-Filters-Queues"></a>
The queues to use to filter the metrics. You should specify at least one queue, and can specify up to 100 queues per request. The `GetCurrentMetricsData` API in particular requires a queue when you include a `Filter` in your request.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** RoutingProfiles **   <a name="connect-Type-Filters-RoutingProfiles"></a>
A list of up to 100 routing profile IDs or ARNs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** RoutingStepExpressions **   <a name="connect-Type-Filters-RoutingStepExpressions"></a>
A list of expressions as a filter, in which an expression is an object of a step in a routing criteria. Accepts filter values up to 3,000 characters in length. Filter values are case-sensitive. JSON object key order and whitespace may be arbitrary; array order and tree structure must be preserved.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 3000.
Required: No

 ** Subtypes **   <a name="connect-Type-Filters-Subtypes"></a>
A list of up to 10 subtypes can be provided.
Type: Array of strings
Array Members: Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** ValidationTestTypes **   <a name="connect-Type-Filters-ValidationTestTypes"></a>
A list of up to 10 validationTestTypes can be provided.
Type: Array of strings
Array Members: Maximum number of 10 items.
Required: No

## See Also
<a name="API_Filters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Filters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Filters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Filters)
