---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetPackageVersionAsset.html
---

# GetPackageVersionAsset
<a name="API_GetPackageVersionAsset"></a>

 Returns an asset (or file) that is in a package. For example, for a Maven package version, use `GetPackageVersionAsset` to download a `JAR` file, a `POM` file, or any other assets in the package version.

## Request Syntax
<a name="API_GetPackageVersionAsset_RequestSyntax"></a>

```
GET /v1/package/version/asset?asset={{asset}}&domain={{domain}}&domain-owner={{domainOwner}}&format={{format}}&namespace={{namespace}}&package={{package}}&repository={{repository}}&revision={{packageVersionRevision}}&version={{packageVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPackageVersionAsset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [asset](#API_GetPackageVersionAsset_RequestSyntax) **   <a name="codeartifact-GetPackageVersionAsset-request-uri-asset"></a>
 The name of the requested asset.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\P{C}+`
Required: Yes

 ** [domain](#API_GetPackageVersionAsset_RequestSyntax) **   <a name="codeartifact-GetPackageVersionAsset-request-uri-domain"></a>
 The name of the domain that contains the repository that contains the package version with the requested asset.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_GetPackageVersionAsset_RequestSyntax) **   <a name="codeartifact-GetPackageVersionAsset-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [format](#API_GetPackageVersionAsset_RequestSyntax) **   <a name="codeartifact-GetPackageVersionAsset-request-uri-format"></a>
 A format that specifies the type of the package version with the requested asset file.
Valid Values: `npm | pypi | maven | nuget | generic | ruby | swift | cargo`
Required: Yes

 ** [namespace](#API_GetPackageVersionAsset_RequestSyntax) **   <a name="codeartifact-GetPackageVersionAsset-request-uri-namespace"></a>
The namespace of the package version with the requested asset file. The package component that specifies its namespace depends on its type. For example:
The namespace is required when requesting assets from package versions of the following formats:
+ Maven
+ Swift
+ generic
+  The namespace of a Maven package version is its `groupId`.
+  The namespace of an npm or Swift package version is its `scope`.
+ The namespace of a generic package is its `namespace`.
+  Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [package](#API_GetPackageVersionAsset_RequestSyntax) **   <a name="codeartifact-GetPackageVersionAsset-request-uri-package"></a>
 The name of the package that contains the requested asset.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

 ** [packageVersion](#API_GetPackageVersionAsset_RequestSyntax) **   <a name="codeartifact-GetPackageVersionAsset-request-uri-packageVersion"></a>
 A string that contains the package version (for example, `3.5.2`).
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

 ** [packageVersionRevision](#API_GetPackageVersionAsset_RequestSyntax) **   <a name="codeartifact-GetPackageVersionAsset-request-uri-packageVersionRevision"></a>
 The name of the package version revision that contains the requested asset.
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `\S+`

 ** [repository](#API_GetPackageVersionAsset_RequestSyntax) **   <a name="codeartifact-GetPackageVersionAsset-request-uri-repository"></a>
 The repository that contains the package version with the requested asset.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

## Request Body
<a name="API_GetPackageVersionAsset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPackageVersionAsset_ResponseSyntax"></a>

```
HTTP/1.1 200
X-AssetName: {{assetName}}
X-PackageVersion: {{packageVersion}}
X-PackageVersionRevision: {{packageVersionRevision}}

{{asset}}
```

## Response Elements
<a name="API_GetPackageVersionAsset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [assetName](#API_GetPackageVersionAsset_ResponseSyntax) **   <a name="codeartifact-GetPackageVersionAsset-response-assetName"></a>
 The name of the asset that is downloaded.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\P{C}+`

 ** [packageVersion](#API_GetPackageVersionAsset_ResponseSyntax) **   <a name="codeartifact-GetPackageVersionAsset-response-packageVersion"></a>
 A string that contains the package version (for example, `3.5.2`).
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [packageVersionRevision](#API_GetPackageVersionAsset_ResponseSyntax) **   <a name="codeartifact-GetPackageVersionAsset-response-packageVersionRevision"></a>
 The name of the package version revision that contains the downloaded asset.
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `\S+`

The response returns the following as the HTTP body.

 ** [asset](#API_GetPackageVersionAsset_ResponseSyntax) **   <a name="codeartifact-GetPackageVersionAsset-response-asset"></a>
 The binary file, or asset, that is downloaded.

## Errors
<a name="API_GetPackageVersionAsset_Errors"></a>

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
<a name="API_GetPackageVersionAsset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/GetPackageVersionAsset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/GetPackageVersionAsset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/GetPackageVersionAsset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/GetPackageVersionAsset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/GetPackageVersionAsset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/GetPackageVersionAsset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/GetPackageVersionAsset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/GetPackageVersionAsset)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/GetPackageVersionAsset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/GetPackageVersionAsset)
