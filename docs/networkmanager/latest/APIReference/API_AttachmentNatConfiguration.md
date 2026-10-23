---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_AttachmentNatConfiguration.html
---

# AttachmentNatConfiguration
<a name="API_AttachmentNatConfiguration"></a>

Describes the NAT configuration of a core network attachment.

## Contents
<a name="API_AttachmentNatConfiguration_Contents"></a>

 ** AttachmentId **   <a name="networkmanager-Type-AttachmentNatConfiguration-AttachmentId"></a>
The ID of the attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^attachment-([0-9a-f]{8,17})$`
Required: No

 ** NatGatewayRules **   <a name="networkmanager-Type-AttachmentNatConfiguration-NatGatewayRules"></a>
The NAT rules of the attachment.
Type: Array of [NatRule](API_NatRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** NatGatewaySupport **   <a name="networkmanager-Type-AttachmentNatConfiguration-NatGatewaySupport"></a>
The state of NAT gateway support on the attachment.
Type: String
Valid Values: `ENABLED | ENABLING | DISABLED | DISABLING | PENDING_ATTACHMENT_ACCEPTANCE`
Required: No

 ** NatSystemRouteSupport **   <a name="networkmanager-Type-AttachmentNatConfiguration-NatSystemRouteSupport"></a>
Indicates whether the core network installs system routes for the NAT CIDR blocks of the attachment's NAT rules.
Type: Boolean
Required: No

## See Also
<a name="API_AttachmentNatConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/AttachmentNatConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/AttachmentNatConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/AttachmentNatConfiguration)
