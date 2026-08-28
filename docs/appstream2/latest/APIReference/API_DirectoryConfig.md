---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DirectoryConfig.html
---

# DirectoryConfig
<a name="API_DirectoryConfig"></a>

Describes the configuration information required to join fleets and image builders to Microsoft Active Directory domains.

## Contents
<a name="API_DirectoryConfig_Contents"></a>

 ** DirectoryName **   <a name="WorkSpacesApplications-Type-DirectoryConfig-DirectoryName"></a>
The fully qualified name of the directory (for example, corp.example.com).
Type: String
Required: Yes

 ** CertificateBasedAuthProperties **   <a name="WorkSpacesApplications-Type-DirectoryConfig-CertificateBasedAuthProperties"></a>
The certificate-based authentication properties used to authenticate SAML 2.0 Identity Provider (IdP) user identities to Active Directory domain-joined streaming instances. Fallback is turned on by default when certificate-based authentication is **Enabled** . Fallback allows users to log in using their AD domain password if certificate-based authentication is unsuccessful, or to unlock a desktop lock screen. **Enabled\_no\_directory\_login\_fallback** enables certificate-based authentication, but does not allow users to log in using their AD domain password. Users will be disconnected to re-authenticate using certificates.
Type: [CertificateBasedAuthProperties](API_CertificateBasedAuthProperties.md) object
Required: No

 ** CreatedTime **   <a name="WorkSpacesApplications-Type-DirectoryConfig-CreatedTime"></a>
The time the directory configuration was created.
Type: Timestamp
Required: No

 ** OrganizationalUnitDistinguishedNames **   <a name="WorkSpacesApplications-Type-DirectoryConfig-OrganizationalUnitDistinguishedNames"></a>
The distinguished names of the organizational units for computer accounts.
Type: Array of strings
Length Constraints: Maximum length of 2000.
Required: No

 ** ServiceAccountCredentials **   <a name="WorkSpacesApplications-Type-DirectoryConfig-ServiceAccountCredentials"></a>
The credentials for the service account used by the fleet or image builder to connect to the directory.
Type: [ServiceAccountCredentials](API_ServiceAccountCredentials.md) object
Required: No

## See Also
<a name="API_DirectoryConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DirectoryConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DirectoryConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DirectoryConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
