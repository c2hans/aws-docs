---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ClientVpnAuthentication.html
---

# ClientVpnAuthentication
<a name="API_ClientVpnAuthentication"></a>

Describes the authentication methods used by a Client VPN endpoint. For more information, see [Authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-authentication.html) in the * AWS Client VPN Administrator Guide*.

## Contents
<a name="API_ClientVpnAuthentication_Contents"></a>

 ** activeDirectory **
Information about the Active Directory, if applicable.
Type: [DirectoryServiceAuthentication](API_DirectoryServiceAuthentication.md) object
Required: No

 ** federatedAuthentication **
Information about the IAM SAML identity provider, if applicable.
Type: [FederatedAuthentication](API_FederatedAuthentication.md) object
Required: No

 ** mutualAuthentication **
Information about the authentication certificates, if applicable.
Type: [CertificateAuthentication](API_CertificateAuthentication.md) object
Required: No

 ** type **
The authentication type used.
Type: String
Valid Values: `certificate-authentication | directory-service-authentication | federated-authentication`
Required: No

## See Also
<a name="API_ClientVpnAuthentication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ClientVpnAuthentication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ClientVpnAuthentication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ClientVpnAuthentication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
