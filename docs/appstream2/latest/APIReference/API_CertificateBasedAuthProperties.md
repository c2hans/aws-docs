---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CertificateBasedAuthProperties.html
---

# CertificateBasedAuthProperties
<a name="API_CertificateBasedAuthProperties"></a>

The certificate-based authentication properties used to authenticate SAML 2.0 Identity Provider (IdP) user identities to Active Directory domain-joined streaming instances. Fallback is turned on by default when certificate-based authentication is **Enabled** . Fallback allows users to log in using their AD domain password if certificate-based authentication is unsuccessful, or to unlock a desktop lock screen. **Enabled\_no\_directory\_login\_fallback** enables certificate-based authentication, but does not allow users to log in using their AD domain password. Users will be disconnected to re-authenticate using certificates.

## Contents
<a name="API_CertificateBasedAuthProperties_Contents"></a>

 ** CertificateAuthorityArn **   <a name="WorkSpacesApplications-Type-CertificateBasedAuthProperties-CertificateAuthorityArn"></a>
The ARN of the AWS Certificate Manager Private CA resource.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** Status **   <a name="WorkSpacesApplications-Type-CertificateBasedAuthProperties-Status"></a>
The status of the certificate-based authentication properties.
Type: String
Valid Values: `DISABLED | ENABLED | ENABLED_NO_DIRECTORY_LOGIN_FALLBACK`
Required: No

## See Also
<a name="API_CertificateBasedAuthProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/CertificateBasedAuthProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/CertificateBasedAuthProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/CertificateBasedAuthProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
