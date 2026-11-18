---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ContextFilters.html
---

# ContextFilters
<a name="API_ContextFilters"></a>

Filters for `ListResourcesInContextStore`. Both filters are optional. If you specify both, Network Firewall returns only the resources that match both.

## Contents
<a name="API_ContextFilters_Contents"></a>

 ** Region **   <a name="networkfirewall-Type-ContextFilters-Region"></a>
The AWS Region of the resources to return, for example `us-east-1`.
Type: String
Pattern: `^[a-z]{2}(-[a-z]+)+-\d+$`
Required: No

 ** ResourceType **   <a name="networkfirewall-Type-ContextFilters-ResourceType"></a>
The type of resource to return. Each resource type corresponds to the `ContextType` that Network Firewall reports for the resource:
+  `SecurityGroup` - Security groups. Reported with the `SegmentId` context type.
+  `VPC` - VPCs. Reported with the `ResourceId` context type.
+  `Subnet` - Subnets. Reported with the `Subnet` context type.
+  `TGWAttachment` - Transit gateway attachments. Reported with the `Attachment` context type.
Type: String
Valid Values: `SecurityGroup | VPC | Subnet | TGWAttachment`
Required: No

## See Also
<a name="API_ContextFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ContextFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ContextFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ContextFilters)
