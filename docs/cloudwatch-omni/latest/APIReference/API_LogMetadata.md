---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_LogMetadata.html
---

# LogMetadata
<a name="API_LogMetadata"></a>

One LOGS query selector block on a node. The `attributes` map's keys are AND'd; each selects with `col = value`. Deliberately RAW/un-normalized so the selector matches the store, not the node's merged identity.

## Contents
<a name="API_LogMetadata_Contents"></a>

 ** attributes **   <a name="cloudwatchomni-Type-LogMetadata-attributes"></a>
One LOGS query-selector block: EXACT store column -> raw SCALAR value (mirroring the scalar MetadataAttributeMap). Keyed by the store column that carries the value (e.g. `resource.attributes['service.name']`, `attributes['aws.local.service']`, `@logGroupName`) so the selector matches the emitted signal. A dimension seen under several values (a service under two namespaces, several log groups) becomes several blocks with the same columns and different values, which the console ORs. Dedicated to the LOGS selector so its cap evolves independently of the metric attribute map and the TRACES map. Selector caps are deliberately DISTINCT from the metric caps.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_LogMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/LogMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/LogMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/LogMetadata)
