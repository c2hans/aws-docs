---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateDirectoryConfig.html
---

# UpdateDirectoryConfig
<a name="API_UpdateDirectoryConfig"></a>

Updates the specified Directory Config object in WorkSpaces Applications. This object includes the configuration information required to join fleets and image builders to Microsoft Active Directory domains.

## Request Syntax
<a name="API_UpdateDirectoryConfig_RequestSyntax"></a>

```
{
   "CertificateBasedAuthProperties": {
      "CertificateAuthorityArn": "{{string}}",
      "Status": "{{string}}"
   },
   "DirectoryName": "{{string}}",
   "OrganizationalUnitDistinguishedNames": [ "{{string}}" ],
   "ServiceAccountCredentials": {
      "AccountName": "{{string}}",
      "AccountPassword": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateDirectoryConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CertificateBasedAuthProperties](#API_UpdateDirectoryConfig_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateDirectoryConfig-request-CertificateBasedAuthProperties"></a>
The certificate-based authentication properties used to authenticate SAML 2.0 Identity Provider (IdP) user identities to Active Directory domain-joined streaming instances. Fallback is turned on by default when certificate-based authentication is **Enabled** . Fallback allows users to log in using their AD domain password if certificate-based authentication is unsuccessful, or to unlock a desktop lock screen. **Enabled\_no\_directory\_login\_fallback** enables certificate-based authentication, but does not allow users to log in using their AD domain password. Users will be disconnected to re-authenticate using certificates.
Type: [CertificateBasedAuthProperties](API_CertificateBasedAuthProperties.md) object
Required: No

 ** [DirectoryName](#API_UpdateDirectoryConfig_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateDirectoryConfig-request-DirectoryName"></a>
The name of the Directory Config object.
Type: String
Required: Yes

 ** [OrganizationalUnitDistinguishedNames](#API_UpdateDirectoryConfig_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateDirectoryConfig-request-OrganizationalUnitDistinguishedNames"></a>
The distinguished names of the organizational units for computer accounts.
Type: Array of strings
Length Constraints: Maximum length of 2000.
Required: No

 ** [ServiceAccountCredentials](#API_UpdateDirectoryConfig_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateDirectoryConfig-request-ServiceAccountCredentials"></a>
The credentials for the service account used by the fleet or image builder to connect to the directory.
Type: [ServiceAccountCredentials](API_ServiceAccountCredentials.md) object
Required: No

## Response Syntax
<a name="API_UpdateDirectoryConfig_ResponseSyntax"></a>

```
{
   "DirectoryConfig": {
      "CertificateBasedAuthProperties": {
         "CertificateAuthorityArn": "string",
         "Status": "string"
      },
      "CreatedTime": number,
      "DirectoryName": "string",
      "OrganizationalUnitDistinguishedNames": [ "string" ],
      "ServiceAccountCredentials": {
         "AccountName": "string",
         "AccountPassword": "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdateDirectoryConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DirectoryConfig](#API_UpdateDirectoryConfig_ResponseSyntax) **   <a name="WorkSpacesApplications-UpdateDirectoryConfig-response-DirectoryConfig"></a>
Information about the Directory Config object.
Type: [DirectoryConfig](API_DirectoryConfig.md) object

## Errors
<a name="API_UpdateDirectoryConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** IncompatibleImageException **
The image can't be updated because it's not compatible for updates.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidRoleException **
The specified role is invalid.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceInUseException **
The specified resource is in use.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateDirectoryConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/UpdateDirectoryConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/UpdateDirectoryConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/UpdateDirectoryConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/UpdateDirectoryConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/UpdateDirectoryConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/UpdateDirectoryConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/UpdateDirectoryConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/UpdateDirectoryConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/UpdateDirectoryConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/UpdateDirectoryConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
