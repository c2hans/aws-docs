---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_NodeFilters.html
---

# NodeFilters
<a name="API_NodeFilters"></a>

Criteria for selecting nodes in a context graph query.

## Contents
<a name="API_NodeFilters_Contents"></a>

 ** category **   <a name="cloudwatchomni-Type-NodeFilters-category"></a>
Match nodes of any of these categories.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Valid Values: `GEN_AI_AGENT | GEN_AI_MODEL | DATABASE | MESSAGING_QUEUE | COMPUTE | STORAGE | NETWORK`
Required: No

 ** cloudProvider **   <a name="cloudwatchomni-Type-NodeFilters-cloudProvider"></a>
Match nodes on any of these cloud providers.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** name **   <a name="cloudwatchomni-Type-NodeFilters-name"></a>
Match only nodes with this name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** namespace **   <a name="cloudwatchomni-Type-NodeFilters-namespace"></a>
Match nodes in any of these logical service groupings.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** nodeId **   <a name="cloudwatchomni-Type-NodeFilters-nodeId"></a>
Match only the node with this identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** nodeType **   <a name="cloudwatchomni-Type-NodeFilters-nodeType"></a>
Match only nodes of this type.
Type: String
Valid Values: `SERVICE | RESOURCE | REMOTE_SERVICE`
Required: No

 ** region **   <a name="cloudwatchomni-Type-NodeFilters-region"></a>
Match nodes in any of these regions.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** sourceAccountId **   <a name="cloudwatchomni-Type-NodeFilters-sourceAccountId"></a>
Match nodes discovered from telemetry produced by any of these accounts.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** sources **   <a name="cloudwatchomni-Type-NodeFilters-sources"></a>
Match nodes contributed by any of these discovery sources.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Valid Values: `VPC_FLOW_LOG | CLOUDTRAIL | IAM_POLICY | CODE_SEMANTICS | TELEMETRY | AZURE_VNET_FLOW_LOG | ELB_ACCESS_LOG | CLOUDFRONT_ACCESS_LOG | S3_ACCESS_LOG | WAF_ACCESS_LOG | AWS_INTEGRATION | CONFIG`
Required: No

 ** stage **   <a name="cloudwatchomni-Type-NodeFilters-stage"></a>
Match nodes observed in any of these deployment environments.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** tags **   <a name="cloudwatchomni-Type-NodeFilters-tags"></a>
Match nodes by the tags on the underlying resource.
Type: Array of [KeyFilter](API_KeyFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** telemetryAttributes **   <a name="cloudwatchomni-Type-NodeFilters-telemetryAttributes"></a>
Match nodes by their OpenTelemetry (OTel) telemetry attributes.
Type: Array of [KeyFilter](API_KeyFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## See Also
<a name="API_NodeFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/NodeFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/NodeFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/NodeFilters)
