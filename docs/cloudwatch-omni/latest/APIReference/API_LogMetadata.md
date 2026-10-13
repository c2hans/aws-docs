---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_LogMetadata.html
---

# LogMetadata
<a name="API_LogMetadata"></a>

One LOGS query selector block on a node. The `attributes` map's keys are AND'd; each selects with `col = value`. Deliberately RAW/un-normalized so the selector matches the store, not the node's merged identity.

## Contents
<a name="API_LogMetadata_Contents"></a>

 ** attributes **   <a name="cloudwatchomni-Type-LogMetadata-attributes"></a>
One LOGS query-selector block: an exact log-store column mapped to the raw value it carries, so the selector matches the emitted signal. Keys are store column names, not bare attribute names. Every block carries "@logGroupName"; alongside it a block carries either the entity columns ("`@entities`.KeyAttributes.Name", ".Type", ".Environment", "`@entities`.Attributes.PlatformType") or OTel columns ("resource.attributes['service.name']", "resource.attributes['service.namespace']", "resource.attributes['cloud.provider'\|'cloud.account.id'\|'cloud.region']"). A dimension seen under several values — several log groups, or a service under two namespaces — becomes several blocks with the same columns and different values, to be OR'd together.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_LogMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/LogMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/LogMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/LogMetadata)
