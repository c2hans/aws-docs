---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ClientVpnAuthenticationRequest.html
---

# ClientVpnAuthenticationRequest
<a name="API_ClientVpnAuthenticationRequest"></a>

Describes the authentication method to be used by a Client VPN endpoint. For more information, see [Authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/authentication-authrization.html#client-authentication) in the * AWS Client VPN Administrator Guide*.

## Contents
<a name="API_ClientVpnAuthenticationRequest_Contents"></a>

 ** ActiveDirectory **
Information about the Active Directory to be used, if applicable. You must provide this information if **Type** is `directory-service-authentication`.
Type: [DirectoryServiceAuthenticationRequest](API_DirectoryServiceAuthenticationRequest.md) object
Required: No

 ** FederatedAuthentication **
Information about the IAM SAML identity provider to be used, if applicable. You must provide this information if **Type** is `federated-authentication`.
Type: [FederatedAuthenticationRequest](API_FederatedAuthenticationRequest.md) object
Required: No

 ** MutualAuthentication **
Information about the authentication certificates to be used, if applicable. You must provide this information if **Type** is `certificate-authentication`.
Type: [CertificateAuthenticationRequest](API_CertificateAuthenticationRequest.md) object
Required: No

 ** Type **
The type of client authentication to be used.
Type: String
Valid Values: `certificate-authentication | directory-service-authentication | federated-authentication`
Required: No

## See Also
<a name="API_ClientVpnAuthenticationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ClientVpnAuthenticationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ClientVpnAuthenticationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ClientVpnAuthenticationRequest)
