---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html
---

# UpdatePackageVersionsStatus
<a name="API_UpdatePackageVersionsStatus"></a>

 Updates the status of one or more versions of a package. Using `UpdatePackageVersionsStatus`, you can update the status of package versions to `Archived`, `Published`, or `Unlisted`. To set the status of a package version to `Disposed`, use [DisposePackageVersions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DisposePackageVersions.html).

## Request Syntax
<a name="API_UpdatePackageVersionsStatus_RequestSyntax"></a>

```
POST /v1/package/versions/update_status?domain={{domain}}&domain-owner={{domainOwner}}&format={{format}}&namespace={{namespace}}&package={{package}}&repository={{repository}} HTTP/1.1
Content-type: application/json

{
   "expectedStatus": "{{string}}",
   "targetStatus": "{{string}}",
   "versionRevisions": {
      "{{string}}" : "{{string}}"
   },
   "versions": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdatePackageVersionsStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_UpdatePackageVersionsStatus_RequestSyntax) **   <a name="codeartifact-UpdatePackageVersionsStatus-request-uri-domain"></a>
 The name of the domain that contains the repository that contains the package versions with a status to be updated.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_UpdatePackageVersionsStatus_RequestSyntax) **   <a name="codeartifact-UpdatePackageVersionsStatus-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [format](#API_UpdatePackageVersionsStatus_RequestSyntax) **   <a name="codeartifact-UpdatePackageVersionsStatus-request-uri-format"></a>
 A format that specifies the type of the package with the statuses to update.
Valid Values: `npm | pypi | maven | nuget | generic | ruby | swift | cargo`
Required: Yes

 ** [namespace](#API_UpdatePackageVersionsStatus_RequestSyntax) **   <a name="codeartifact-UpdatePackageVersionsStatus-request-uri-namespace"></a>
The namespace of the package version to be updated. The package component that specifies its namespace depends on its type. For example:
+  The namespace of a Maven package version is its `groupId`.
+  The namespace of an npm or Swift package version is its `scope`.
+ The namespace of a generic package is its `namespace`.
+  Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [package](#API_UpdatePackageVersionsStatus_RequestSyntax) **   <a name="codeartifact-UpdatePackageVersionsStatus-request-uri-package"></a>
 The name of the package with the version statuses to update.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

 ** [repository](#API_UpdatePackageVersionsStatus_RequestSyntax) **   <a name="codeartifact-UpdatePackageVersionsStatus-request-uri-repository"></a>
 The repository that contains the package versions with the status you want to update.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

## Request Body
<a name="API_UpdatePackageVersionsStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [expectedStatus](#API_UpdatePackageVersionsStatus_RequestSyntax) **   <a name="codeartifact-UpdatePackageVersionsStatus-request-expectedStatus"></a>
 The package version’s expected status before it is updated. If `expectedStatus` is provided, the package version's status is updated only if its status at the time `UpdatePackageVersionsStatus` is called matches `expectedStatus`.
Type: String
Valid Values: `Archived | Published | Unlisted | Unfinished`
Required: No

 ** [targetStatus](#API_UpdatePackageVersionsStatus_RequestSyntax) **   <a name="codeartifact-UpdatePackageVersionsStatus-request-targetStatus"></a>
 The status you want to change the package version status to.
Type: String
Valid Values: `Archived | Published | Unlisted`
Required: Yes

 ** [versionRevisions](#API_UpdatePackageVersionsStatus_RequestSyntax) **   <a name="codeartifact-UpdatePackageVersionsStatus-request-versionRevisions"></a>
 A map of package versions and package version revisions. The map `key` is the package version (for example, `3.5.2`), and the map `value` is the package version revision.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[^#/\s]+`
Value Length Constraints: Minimum length of 1. Maximum length of 50.
Value Pattern: `\S+`
Required: No

 ** [versions](#API_UpdatePackageVersionsStatus_RequestSyntax) **   <a name="codeartifact-UpdatePackageVersionsStatus-request-versions"></a>
 An array of strings that specify the versions of the package with the statuses to update.
Type: Array of strings
Array Members: Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

## Response Syntax
<a name="API_UpdatePackageVersionsStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failedVersions": {
      "string" : {
         "errorCode": "string",
         "errorMessage": "string"
      }
   },
   "successfulVersions": {
      "string" : {
         "revision": "string",
         "status": "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdatePackageVersionsStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedVersions](#API_UpdatePackageVersionsStatus_ResponseSyntax) **   <a name="codeartifact-UpdatePackageVersionsStatus-response-failedVersions"></a>
 A list of `SuccessfulPackageVersionInfo` objects, one for each package version with a status that successfully updated.
Type: String to [PackageVersionError](API_PackageVersionError.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[^#/\s]+`

 ** [successfulVersions](#API_UpdatePackageVersionsStatus_ResponseSyntax) **   <a name="codeartifact-UpdatePackageVersionsStatus-response-successfulVersions"></a>
 A list of `PackageVersionError` objects, one for each package version with a status that failed to update.
Type: String to [SuccessfulPackageVersionInfo](API_SuccessfulPackageVersionInfo.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[^#/\s]+`

## Errors
<a name="API_UpdatePackageVersionsStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The operation did not succeed because of an unauthorized access attempt.
HTTP Status Code: 403

 ** ConflictException **
 The operation did not succeed because prerequisites are not met.
 ** resourceId **
 The ID of the resource.
 ** resourceType **
 The type of AWS resource.
HTTP Status Code: 409

 ** InternalServerException **
 The operation did not succeed because of an error that occurred inside AWS CodeArtifact.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The operation did not succeed because the resource requested is not found in the service.
 ** resourceId **
 The ID of the resource.
 ** resourceType **
 The type of AWS resource.
HTTP Status Code: 404

 ** ThrottlingException **
 The operation did not succeed because too many requests are sent to the service.
 ** retryAfterSeconds **
 The time period, in seconds, to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
 The operation did not succeed because a parameter in the request was sent with an invalid value.
 ** reason **

HTTP Status Code: 400

## See Also
<a name="API_UpdatePackageVersionsStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/UpdatePackageVersionsStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/UpdatePackageVersionsStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/UpdatePackageVersionsStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/UpdatePackageVersionsStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/UpdatePackageVersionsStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/UpdatePackageVersionsStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/UpdatePackageVersionsStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/UpdatePackageVersionsStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/UpdatePackageVersionsStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/UpdatePackageVersionsStatus)
