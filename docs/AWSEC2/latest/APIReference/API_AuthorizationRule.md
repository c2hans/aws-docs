---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizationRule.html
---

# AuthorizationRule
<a name="API_AuthorizationRule"></a>

Information about an authorization rule.

## Contents
<a name="API_AuthorizationRule_Contents"></a>

 ** accessAll **
Indicates whether the authorization rule grants access to all clients.
Type: Boolean
Required: No

 ** clientVpnEndpointId **
The ID of the Client VPN endpoint with which the authorization rule is associated.
Type: String
Required: No

 ** description **
A brief description of the authorization rule.
Type: String
Required: No

 ** destinationCidr **
The IPv4 address range, in CIDR notation, of the network to which the authorization rule applies.
Type: String
Required: No

 ** groupId **
The ID of the Active Directory group to which the authorization rule grants access.
Type: String
Required: No

 ** status **
The current state of the authorization rule.
Type: [ClientVpnAuthorizationRuleStatus](API_ClientVpnAuthorizationRuleStatus.md) object
Required: No

## See Also
<a name="API_AuthorizationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AuthorizationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AuthorizationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AuthorizationRule)
