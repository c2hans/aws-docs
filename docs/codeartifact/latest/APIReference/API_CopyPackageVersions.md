---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_CopyPackageVersions.html
---

# CopyPackageVersions
<a name="API_CopyPackageVersions"></a>

 Copies package versions from one repository to another repository in the same domain.

**Note**
 You must specify `versions` or `versionRevisions`. You cannot specify both.

## Request Syntax
<a name="API_CopyPackageVersions_RequestSyntax"></a>

```
POST /v1/package/versions/copy?destination-repository={{destinationRepository}}&domain={{domain}}&domain-owner={{domainOwner}}&format={{format}}&namespace={{namespace}}&package={{package}}&source-repository={{sourceRepository}} HTTP/1.1
Content-type: application/json

{
   "allowOverwrite": {{boolean}},
   "includeFromUpstream": {{boolean}},
   "versionRevisions": {
      "{{string}}" : "{{string}}"
   },
   "versions": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_CopyPackageVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [destinationRepository](#API_CopyPackageVersions_RequestSyntax) **   <a name="codeartifact-CopyPackageVersions-request-uri-destinationRepository"></a>
 The name of the repository into which package versions are copied.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

 ** [domain](#API_CopyPackageVersions_RequestSyntax) **   <a name="codeartifact-CopyPackageVersions-request-uri-domain"></a>
 The name of the domain that contains the source and destination repositories.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_CopyPackageVersions_RequestSyntax) **   <a name="codeartifact-CopyPackageVersions-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [format](#API_CopyPackageVersions_RequestSyntax) **   <a name="codeartifact-CopyPackageVersions-request-uri-format"></a>
 The format of the package versions to be copied.
Valid Values: `npm | pypi | maven | nuget | generic | ruby | swift | cargo`
Required: Yes

 ** [namespace](#API_CopyPackageVersions_RequestSyntax) **   <a name="codeartifact-CopyPackageVersions-request-uri-namespace"></a>
The namespace of the package versions to be copied. The package component that specifies its namespace depends on its type. For example:
The namespace is required when copying package versions of the following formats:
+ Maven
+ Swift
+ generic
+  The namespace of a Maven package version is its `groupId`.
+  The namespace of an npm or Swift package version is its `scope`.
+ The namespace of a generic package is its `namespace`.
+  Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [package](#API_CopyPackageVersions_RequestSyntax) **   <a name="codeartifact-CopyPackageVersions-request-uri-package"></a>
 The name of the package that contains the versions to be copied.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

 ** [sourceRepository](#API_CopyPackageVersions_RequestSyntax) **   <a name="codeartifact-CopyPackageVersions-request-uri-sourceRepository"></a>
 The name of the repository that contains the package versions to be copied.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

## Request Body
<a name="API_CopyPackageVersions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [allowOverwrite](#API_CopyPackageVersions_RequestSyntax) **   <a name="codeartifact-CopyPackageVersions-request-allowOverwrite"></a>
 Set to true to overwrite a package version that already exists in the destination repository. If set to false and the package version already exists in the destination repository, the package version is returned in the `failedVersions` field of the response with an `ALREADY_EXISTS` error code.
Type: Boolean
Required: No

 ** [includeFromUpstream](#API_CopyPackageVersions_RequestSyntax) **   <a name="codeartifact-CopyPackageVersions-request-includeFromUpstream"></a>
 Set to true to copy packages from repositories that are upstream from the source repository to the destination repository. The default setting is false. For more information, see [Working with upstream repositories](https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html).
Type: Boolean
Required: No

 ** [versionRevisions](#API_CopyPackageVersions_RequestSyntax) **   <a name="codeartifact-CopyPackageVersions-request-versionRevisions"></a>
 A list of key-value pairs. The keys are package versions and the values are package version revisions. A `CopyPackageVersion` operation succeeds if the specified versions in the source repository match the specified package version revision.
 You must specify `versions` or `versionRevisions`. You cannot specify both.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[^#/\s]+`
Value Length Constraints: Minimum length of 1. Maximum length of 50.
Value Pattern: `\S+`
Required: No

 ** [versions](#API_CopyPackageVersions_RequestSyntax) **   <a name="codeartifact-CopyPackageVersions-request-versions"></a>
 The versions of the package to be copied.
 You must specify `versions` or `versionRevisions`. You cannot specify both.
Type: Array of strings
Array Members: Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: No

## Response Syntax
<a name="API_CopyPackageVersions_ResponseSyntax"></a>

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
<a name="API_CopyPackageVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedVersions](#API_CopyPackageVersions_ResponseSyntax) **   <a name="codeartifact-CopyPackageVersions-response-failedVersions"></a>
 A map of package versions that failed to copy and their error codes. The possible error codes are in the `PackageVersionError` data type. They are:
+  `ALREADY_EXISTS`
+  `MISMATCHED_REVISION`
+  `MISMATCHED_STATUS`
+  `NOT_ALLOWED`
+  `NOT_FOUND`
+  `SKIPPED`
Type: String to [PackageVersionError](API_PackageVersionError.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[^#/\s]+`

 ** [successfulVersions](#API_CopyPackageVersions_ResponseSyntax) **   <a name="codeartifact-CopyPackageVersions-response-successfulVersions"></a>
 A list of the package versions that were successfully copied to your repository.
Type: String to [SuccessfulPackageVersionInfo](API_SuccessfulPackageVersionInfo.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[^#/\s]+`

## Errors
<a name="API_CopyPackageVersions_Errors"></a>

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

 ** ServiceQuotaExceededException **
 The operation did not succeed because it would have exceeded a service limit for your account.
 ** resourceId **
 The ID of the resource.
 ** resourceType **
 The type of AWS resource.
HTTP Status Code: 402

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
<a name="API_CopyPackageVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/CopyPackageVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/CopyPackageVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/CopyPackageVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/CopyPackageVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/CopyPackageVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/CopyPackageVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/CopyPackageVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/CopyPackageVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/CopyPackageVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/CopyPackageVersions)
