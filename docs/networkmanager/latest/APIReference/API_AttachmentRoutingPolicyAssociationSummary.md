---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_AttachmentRoutingPolicyAssociationSummary.html
---

# AttachmentRoutingPolicyAssociationSummary
<a name="API_AttachmentRoutingPolicyAssociationSummary"></a>

Summary information about routing policy associations for an attachment.

## Contents
<a name="API_AttachmentRoutingPolicyAssociationSummary_Contents"></a>

 ** AssociatedRoutingPolicies **   <a name="networkmanager-Type-AttachmentRoutingPolicyAssociationSummary-AssociatedRoutingPolicies"></a>
The list of routing policies currently associated with the attachment.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** AttachmentId **   <a name="networkmanager-Type-AttachmentRoutingPolicyAssociationSummary-AttachmentId"></a>
The ID of the attachment associated with the routing policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^attachment-([0-9a-f]{8,17})$`
Required: No

 ** PendingRoutingPolicies **   <a name="networkmanager-Type-AttachmentRoutingPolicyAssociationSummary-PendingRoutingPolicies"></a>
The list of routing policies that are pending association with the attachment.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** RoutingPolicyLabel **   <a name="networkmanager-Type-AttachmentRoutingPolicyAssociationSummary-RoutingPolicyLabel"></a>
The routing policy label associated with the attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_AttachmentRoutingPolicyAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/AttachmentRoutingPolicyAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/AttachmentRoutingPolicyAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/AttachmentRoutingPolicyAssociationSummary)
