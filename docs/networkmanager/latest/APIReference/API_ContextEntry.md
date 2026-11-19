---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ContextEntry.html
---

# ContextEntry

Describes a context entry in a context store. A context entry describes a resource, such as a security group, subnet, or attachment.

## Contents
<a name="API_ContextEntry_Contents"></a>

 ** AttachmentType **   <a name="networkmanager-Type-ContextEntry-AttachmentType"></a>
The type of the attachment, for example `VPC`. Network Manager returns this value only when the context type is `Attachment`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** AvailabilityZone **   <a name="networkmanager-Type-ContextEntry-AvailabilityZone"></a>
The ID of the Availability Zone of the resource, for example `use1-az2`. Network Manager returns this value only when the context type is `Subnet`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** ContextId **   <a name="networkmanager-Type-ContextEntry-ContextId"></a>
The ID of the context entry.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** ContextType **   <a name="networkmanager-Type-ContextEntry-ContextType"></a>
The type of the context entry, for example `SegmentId`, `Subnet`, or `Attachment`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** PublicId **   <a name="networkmanager-Type-ContextEntry-PublicId"></a>
The ID of the resource, for example a security group ID, subnet ID, or transit gateway attachment ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** Region **   <a name="networkmanager-Type-ContextEntry-Region"></a>
The Amazon Web Services Region of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: No

 ** SegmentType **   <a name="networkmanager-Type-ContextEntry-SegmentType"></a>
The type of the segment, for example `SecurityGroup`. Network Manager returns this value only when the context type is `SegmentId`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_ContextEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ContextEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ContextEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ContextEntry)
