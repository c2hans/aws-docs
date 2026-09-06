---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DescribedSecurityPolicy.html
---

# DescribedSecurityPolicy
<a name="API_DescribedSecurityPolicy"></a>

Describes the properties of a security policy that you specify. For more information about security policies, see [Working with security policies for servers](https://docs.aws.amazon.com/transfer/latest/userguide/security-policies.html) or [Working with security policies for SFTP connectors](https://docs.aws.amazon.com/transfer/latest/userguide/security-policies-connectors.html).

## Contents
<a name="API_DescribedSecurityPolicy_Contents"></a>

 ** SecurityPolicyName **   <a name="TransferFamily-Type-DescribedSecurityPolicy-SecurityPolicyName"></a>
The text name of the specified security policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `Transfer[A-Za-z0-9]*SecurityPolicy-[A-Za-z0-9-]+`
Required: Yes

 ** Fips **   <a name="TransferFamily-Type-DescribedSecurityPolicy-Fips"></a>
Specifies whether this policy enables Federal Information Processing Standards (FIPS). This parameter applies to both server and connector security policies.
Type: Boolean
Required: No

 ** Protocols **   <a name="TransferFamily-Type-DescribedSecurityPolicy-Protocols"></a>
Lists the file transfer protocols that the security policy applies to.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `SFTP | FTPS`
Required: No

 ** SshCiphers **   <a name="TransferFamily-Type-DescribedSecurityPolicy-SshCiphers"></a>
Lists the enabled Secure Shell (SSH) cipher encryption algorithms in the security policy that is attached to the server or connector. This parameter applies to both server and connector security policies.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: No

 ** SshHostKeyAlgorithms **   <a name="TransferFamily-Type-DescribedSecurityPolicy-SshHostKeyAlgorithms"></a>
Lists the host key algorithms for the security policy.
This parameter only applies to security policies for connectors.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: No

 ** SshKexs **   <a name="TransferFamily-Type-DescribedSecurityPolicy-SshKexs"></a>
Lists the enabled SSH key exchange (KEX) encryption algorithms in the security policy that is attached to the server or connector. This parameter applies to both server and connector security policies.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: No

 ** SshMacs **   <a name="TransferFamily-Type-DescribedSecurityPolicy-SshMacs"></a>
Lists the enabled SSH message authentication code (MAC) encryption algorithms in the security policy that is attached to the server or connector. This parameter applies to both server and connector security policies.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: No

 ** TlsCiphers **   <a name="TransferFamily-Type-DescribedSecurityPolicy-TlsCiphers"></a>
Lists the enabled Transport Layer Security (TLS) cipher encryption algorithms in the security policy that is attached to the server.
This parameter only applies to security policies for servers.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: No

 ** Type **   <a name="TransferFamily-Type-DescribedSecurityPolicy-Type"></a>
The resource type to which the security policy applies, either server or connector.
Type: String
Valid Values: `SERVER | CONNECTOR`
Required: No

## See Also
<a name="API_DescribedSecurityPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DescribedSecurityPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DescribedSecurityPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DescribedSecurityPolicy)
