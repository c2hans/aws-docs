---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_Attachment.html
---

# Attachment
<a name="API_Attachment"></a>

Describes a core network attachment.

## Contents
<a name="API_Attachment_Contents"></a>

 ** AttachmentId **   <a name="networkmanager-Type-Attachment-AttachmentId"></a>
The ID of the attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^attachment-([0-9a-f]{8,17})$`
Required: No

 ** AttachmentPolicyRuleNumber **   <a name="networkmanager-Type-Attachment-AttachmentPolicyRuleNumber"></a>
The policy rule number associated with the attachment.
Type: Integer
Required: No

 ** AttachmentType **   <a name="networkmanager-Type-Attachment-AttachmentType"></a>
The type of attachment.
Type: String
Valid Values: `CONNECT | SITE_TO_SITE_VPN | VPC | DIRECT_CONNECT_GATEWAY | TRANSIT_GATEWAY_ROUTE_TABLE`
Required: No

 ** CoreNetworkArn **   <a name="networkmanager-Type-Attachment-CoreNetworkArn"></a>
The ARN of a core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

 ** CoreNetworkId **   <a name="networkmanager-Type-Attachment-CoreNetworkId"></a>
The ID of a core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: No

 ** CreatedAt **   <a name="networkmanager-Type-Attachment-CreatedAt"></a>
The timestamp when the attachment was created.
Type: Timestamp
Required: No

 ** EdgeLocation **   <a name="networkmanager-Type-Attachment-EdgeLocation"></a>
The Region where the edge is located. This is returned for all attachment types except a Direct Connect gateway attachment, which instead returns `EdgeLocations`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: No

 ** EdgeLocations **   <a name="networkmanager-Type-Attachment-EdgeLocations"></a>
The edge locations that the Direct Connect gateway is associated with. This is returned only for Direct Connect gateway attachments. All other attachment types retrun `EdgeLocation`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: No

 ** LastModificationErrors **   <a name="networkmanager-Type-Attachment-LastModificationErrors"></a>
Describes the error associated with the attachment request.
Type: Array of [AttachmentError](API_AttachmentError.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** NetworkFunctionGroupName **   <a name="networkmanager-Type-Attachment-NetworkFunctionGroupName"></a>
The name of the network function group.
Type: String
Pattern: `[\s\S]*`
Required: No

 ** OwnerAccountId **   <a name="networkmanager-Type-Attachment-OwnerAccountId"></a>
The ID of the attachment account owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[\s\S]*`
Required: No

 ** ProposedNetworkFunctionGroupChange **   <a name="networkmanager-Type-Attachment-ProposedNetworkFunctionGroupChange"></a>
Describes a proposed change to a network function group associated with the attachment.
Type: [ProposedNetworkFunctionGroupChange](API_ProposedNetworkFunctionGroupChange.md) object
Required: No

 ** ProposedSegmentChange **   <a name="networkmanager-Type-Attachment-ProposedSegmentChange"></a>
The attachment to move from one segment to another.
Type: [ProposedSegmentChange](API_ProposedSegmentChange.md) object
Required: No

 ** ResourceArn **   <a name="networkmanager-Type-Attachment-ResourceArn"></a>
The attachment resource ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1500.
Pattern: `[\s\S]*`
Required: No

 ** SegmentName **   <a name="networkmanager-Type-Attachment-SegmentName"></a>
The name of the segment attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** State **   <a name="networkmanager-Type-Attachment-State"></a>
The state of the attachment.
Type: String
Valid Values: `REJECTED | PENDING_ATTACHMENT_ACCEPTANCE | CREATING | FAILED | AVAILABLE | UPDATING | PENDING_NETWORK_UPDATE | PENDING_TAG_ACCEPTANCE | DELETING`
Required: No

 ** Tags **   <a name="networkmanager-Type-Attachment-Tags"></a>
The tags associated with the attachment.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** UpdatedAt **   <a name="networkmanager-Type-Attachment-UpdatedAt"></a>
The timestamp when the attachment was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Attachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Attachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Attachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Attachment)
