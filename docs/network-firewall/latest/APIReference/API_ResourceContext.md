---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ResourceContext.html
---

# ResourceContext

A resource that a context store records, which `ListResourcesInContextStore` returns.

## Contents
<a name="API_ResourceContext_Contents"></a>

 ** PublicId **   <a name="networkfirewall-Type-ResourceContext-PublicId"></a>
The identifier of the resource, for example `vpc-1234567890abcdef0`, `subnet-1234567890abcdef0`, `sg-1234567890abcdef0`, or `tgw-attach-1234567890abcdef0`.
Type: String
Required: Yes

 ** AttachmentType **   <a name="networkfirewall-Type-ResourceContext-AttachmentType"></a>
The type of the transit gateway attachment. Present for attachments.
Type: String
Required: No

 ** AvailabilityZone **   <a name="networkfirewall-Type-ResourceContext-AvailabilityZone"></a>
The Availability Zone of the resource. Present for subnets.
Type: String
Required: No

 ** ContextType **   <a name="networkfirewall-Type-ResourceContext-ContextType"></a>
The kind of context that the context store records for the resource. Valid values:
+  `ResourceId` - A VPC.
+  `SegmentId` - A security group.
+  `Subnet` - A subnet.
+  `Attachment` - A transit gateway attachment.
Type: String
Valid Values: `ResourceId | SegmentId | Subnet | Attachment`
Required: No

 ** Region **   <a name="networkfirewall-Type-ResourceContext-Region"></a>
The AWS Region of the resource.
Type: String
Pattern: `^[a-z]{2}(-[a-z]+)+-\d+$`
Required: No

## See Also
<a name="API_ResourceContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ResourceContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ResourceContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ResourceContext)
