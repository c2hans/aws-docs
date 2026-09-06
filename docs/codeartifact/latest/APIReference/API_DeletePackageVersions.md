---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeletePackageVersions.html
---

# DeletePackageVersions
<a name="API_DeletePackageVersions"></a>

 Deletes one or more versions of a package. A deleted package version cannot be restored in your repository. If you want to remove a package version from your repository and be able to restore it later, set its status to `Archived`. Archived packages cannot be downloaded from a repository and don't show up with list package APIs (for example, [ListPackageVersions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html)), but you can restore them using [UpdatePackageVersionsStatus](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html).

## Request Syntax
<a name="API_DeletePackageVersions_RequestSyntax"></a>

```
POST /v1/package/versions/delete?domain={{domain}}&domain-owner={{domainOwner}}&format={{format}}&namespace={{namespace}}&package={{package}}&repository={{repository}} HTTP/1.1
Content-type: application/json

{
   "expectedStatus": "{{string}}",
   "versions": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DeletePackageVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_DeletePackageVersions_RequestSyntax) **   <a name="codeartifact-DeletePackageVersions-request-uri-domain"></a>
 The name of the domain that contains the package to delete.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_DeletePackageVersions_RequestSyntax) **   <a name="codeartifact-DeletePackageVersions-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [format](#API_DeletePackageVersions_RequestSyntax) **   <a name="codeartifact-DeletePackageVersions-request-uri-format"></a>
 The format of the package versions to delete.
Valid Values: `npm | pypi | maven | nuget | generic | ruby | swift | cargo`
Required: Yes

 ** [namespace](#API_DeletePackageVersions_RequestSyntax) **   <a name="codeartifact-DeletePackageVersions-request-uri-namespace"></a>
The namespace of the package versions to be deleted. The package component that specifies its namespace depends on its type. For example:
The namespace is required when deleting package versions of the following formats:
+ Maven
+ Swift
+ generic
+  The namespace of a Maven package version is its `groupId`.
+  The namespace of an npm or Swift package version is its `scope`.
+ The namespace of a generic package is its `namespace`.
+  Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [package](#API_DeletePackageVersions_RequestSyntax) **   <a name="codeartifact-DeletePackageVersions-request-uri-package"></a>
 The name of the package with the versions to delete.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

 ** [repository](#API_DeletePackageVersions_RequestSyntax) **   <a name="codeartifact-DeletePackageVersions-request-uri-repository"></a>
 The name of the repository that contains the package versions to delete.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

## Request Body
<a name="API_DeletePackageVersions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [expectedStatus](#API_DeletePackageVersions_RequestSyntax) **   <a name="codeartifact-DeletePackageVersions-request-expectedStatus"></a>
 The expected status of the package version to delete.
Type: String
Valid Values: `Archived | Disposed | Published | Unfinished | Unlisted`
Required: No

 ** [versions](#API_DeletePackageVersions_RequestSyntax) **   <a name="codeartifact-DeletePackageVersions-request-versions"></a>
 An array of strings that specify the versions of the package to delete.
Type: Array of strings
Array Members: Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

## Response Syntax
<a name="API_DeletePackageVersions_ResponseSyntax"></a>

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
<a name="API_DeletePackageVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedVersions](#API_DeletePackageVersions_ResponseSyntax) **   <a name="codeartifact-DeletePackageVersions-response-failedVersions"></a>
 A `PackageVersionError` object that contains a map of errors codes for the deleted package that failed. The possible error codes are:
+  `ALREADY_EXISTS`
+  `MISMATCHED_REVISION`
+  `MISMATCHED_STATUS`
+  `NOT_ALLOWED`
+  `NOT_FOUND`
+  `SKIPPED`
Type: String to [PackageVersionError](API_PackageVersionError.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[^#/\s]+`

 ** [successfulVersions](#API_DeletePackageVersions_ResponseSyntax) **   <a name="codeartifact-DeletePackageVersions-response-successfulVersions"></a>
 A list of the package versions that were successfully deleted. The status of every successful version will be `Deleted`.
Type: String to [SuccessfulPackageVersionInfo](API_SuccessfulPackageVersionInfo.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[^#/\s]+`

## Errors
<a name="API_DeletePackageVersions_Errors"></a>

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
<a name="API_DeletePackageVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/DeletePackageVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/DeletePackageVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/DeletePackageVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/DeletePackageVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/DeletePackageVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/DeletePackageVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/DeletePackageVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/DeletePackageVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/DeletePackageVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/DeletePackageVersions)
