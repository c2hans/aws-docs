---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetPackageVersionReadme.html
---

# GetPackageVersionReadme
<a name="API_GetPackageVersionReadme"></a>

 Gets the readme file or descriptive text for a package version.

 The returned text might contain formatting. For example, it might contain formatting for Markdown or reStructuredText.

## Request Syntax
<a name="API_GetPackageVersionReadme_RequestSyntax"></a>

```
GET /v1/package/version/readme?domain={{domain}}&domain-owner={{domainOwner}}&format={{format}}&namespace={{namespace}}&package={{package}}&repository={{repository}}&version={{packageVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPackageVersionReadme_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_GetPackageVersionReadme_RequestSyntax) **   <a name="codeartifact-GetPackageVersionReadme-request-uri-domain"></a>
 The name of the domain that contains the repository that contains the package version with the requested readme file.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_GetPackageVersionReadme_RequestSyntax) **   <a name="codeartifact-GetPackageVersionReadme-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [format](#API_GetPackageVersionReadme_RequestSyntax) **   <a name="codeartifact-GetPackageVersionReadme-request-uri-format"></a>
 A format that specifies the type of the package version with the requested readme file.
Valid Values: `npm | pypi | nuget`
Required: Yes

 ** [namespace](#API_GetPackageVersionReadme_RequestSyntax) **   <a name="codeartifact-GetPackageVersionReadme-request-uri-namespace"></a>
The namespace of the package version with the requested readme file. The package component that specifies its namespace depends on its type. For example:
The namespace is required when requesting the readme from package versions of the following formats:
+ Maven
+ Swift
+ generic
+  The namespace of a Maven package version is its `groupId`.
+  The namespace of an npm or Swift package version is its `scope`.
+ The namespace of a generic package is its `namespace`.
+  Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [package](#API_GetPackageVersionReadme_RequestSyntax) **   <a name="codeartifact-GetPackageVersionReadme-request-uri-package"></a>
 The name of the package version that contains the requested readme file.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

 ** [packageVersion](#API_GetPackageVersionReadme_RequestSyntax) **   <a name="codeartifact-GetPackageVersionReadme-request-uri-packageVersion"></a>
 A string that contains the package version (for example, `3.5.2`).
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

 ** [repository](#API_GetPackageVersionReadme_RequestSyntax) **   <a name="codeartifact-GetPackageVersionReadme-request-uri-repository"></a>
 The repository that contains the package with the requested readme file.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

## Request Body
<a name="API_GetPackageVersionReadme_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPackageVersionReadme_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "format": "string",
   "namespace": "string",
   "package": "string",
   "readme": "string",
   "version": "string",
   "versionRevision": "string"
}
```

## Response Elements
<a name="API_GetPackageVersionReadme_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [format](#API_GetPackageVersionReadme_ResponseSyntax) **   <a name="codeartifact-GetPackageVersionReadme-response-format"></a>
 The format of the package with the requested readme file.
Type: String
Valid Values: `npm | pypi | maven | nuget | generic | ruby | swift | cargo`

 ** [namespace](#API_GetPackageVersionReadme_ResponseSyntax) **   <a name="codeartifact-GetPackageVersionReadme-response-namespace"></a>
The namespace of the package version with the requested readme file. The package component that specifies its namespace depends on its type. For example:
+  The namespace of a Maven package version is its `groupId`.
+  The namespace of an npm or Swift package version is its `scope`.
+ The namespace of a generic package is its `namespace`.
+  Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [package](#API_GetPackageVersionReadme_ResponseSyntax) **   <a name="codeartifact-GetPackageVersionReadme-response-package"></a>
 The name of the package that contains the returned readme file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [readme](#API_GetPackageVersionReadme_ResponseSyntax) **   <a name="codeartifact-GetPackageVersionReadme-response-readme"></a>
 The text of the returned readme file.
Type: String

 ** [version](#API_GetPackageVersionReadme_ResponseSyntax) **   <a name="codeartifact-GetPackageVersionReadme-response-version"></a>
 The version of the package with the requested readme file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [versionRevision](#API_GetPackageVersionReadme_ResponseSyntax) **   <a name="codeartifact-GetPackageVersionReadme-response-versionRevision"></a>
 The current revision associated with the package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `\S+`

## Errors
<a name="API_GetPackageVersionReadme_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The operation did not succeed because of an unauthorized access attempt.
HTTP Status Code: 403

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
<a name="API_GetPackageVersionReadme_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/GetPackageVersionReadme)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/GetPackageVersionReadme)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/GetPackageVersionReadme)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/GetPackageVersionReadme)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/GetPackageVersionReadme)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/GetPackageVersionReadme)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/GetPackageVersionReadme)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/GetPackageVersionReadme)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/GetPackageVersionReadme)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/GetPackageVersionReadme)
