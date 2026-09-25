---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_EdgeFilters.html
---

# EdgeFilters
<a name="API_EdgeFilters"></a>

Criteria for filtering edges in a context graph query.

## Contents
<a name="API_EdgeFilters_Contents"></a>

 ** edgeId **   <a name="cloudwatchomni-Type-EdgeFilters-edgeId"></a>
Match only the edge with this identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** edgeType **   <a name="cloudwatchomni-Type-EdgeFilters-edgeType"></a>
Match only edges of this relationship kind.
Type: String
Valid Values: `CALLS | ACCESSES | RUNS_ON`
Required: No

 ** from **   <a name="cloudwatchomni-Type-EdgeFilters-from"></a>
Match only edges originating from this node identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** operations **   <a name="cloudwatchomni-Type-EdgeFilters-operations"></a>
Match edges carrying any of these operations.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** sources **   <a name="cloudwatchomni-Type-EdgeFilters-sources"></a>
Match edges contributed by any of these discovery sources.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Valid Values: `VPC_FLOW_LOG | CLOUDTRAIL | IAM_POLICY | CODE_SEMANTICS | TELEMETRY | AZURE_VNET_FLOW_LOG | ELB_ACCESS_LOG | CLOUDFRONT_ACCESS_LOG | S3_ACCESS_LOG | WAF_ACCESS_LOG | AWS_INTEGRATION | CONFIG`
Required: No

 ** telemetryAttributes **   <a name="cloudwatchomni-Type-EdgeFilters-telemetryAttributes"></a>
Match edges by their OpenTelemetry (OTel) telemetry attributes. Not yet enforced: currently accepted but ignored (does not filter), matching nodeFilters.telemetryAttributes.
Type: Array of [KeyFilter](API_KeyFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** to **   <a name="cloudwatchomni-Type-EdgeFilters-to"></a>
Match only edges pointing to this node identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_EdgeFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/EdgeFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/EdgeFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/EdgeFilters)
