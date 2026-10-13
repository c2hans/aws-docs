---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_TraceMetadata.html
---

# TraceMetadata
<a name="API_TraceMetadata"></a>

One TRACES query selector block on a node/edge (see LogMetadata).

## Contents
<a name="API_TraceMetadata_Contents"></a>

 ** attributes **   <a name="cloudwatchomni-Type-TraceMetadata-attributes"></a>
One TRACES query-selector block: an exact span-store column mapped to the raw value it carries. Keys are store column names, not bare attribute names — the service identity and cloud dimensions arrive as "resource.attributes['service.name']", "resource.attributes['service.namespace']", "resource.attributes['cloud.provider']", "resource.attributes['cloud.account.id']", "resource.attributes['cloud.region']" and "resource.attributes['deployment.environment']", and span-level identity as "attributes['aws.local.service']" and "attributes['aws.local.environment']". Not every column is present on every block; which ones appear depends on what the span carried.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_TraceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/TraceMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/TraceMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/TraceMetadata)
