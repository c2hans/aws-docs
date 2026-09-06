---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackageVersion.html
---

# DescribePackageVersion
<a name="API_DescribePackageVersion"></a>

 Returns a [PackageVersionDescription](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html) object that contains information about the requested package version.

## Request Syntax
<a name="API_DescribePackageVersion_RequestSyntax"></a>

```
GET /v1/package/version?domain={{domain}}&domain-owner={{domainOwner}}&format={{format}}&namespace={{namespace}}&package={{package}}&repository={{repository}}&version={{packageVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribePackageVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_DescribePackageVersion_RequestSyntax) **   <a name="codeartifact-DescribePackageVersion-request-uri-domain"></a>
 The name of the domain that contains the repository that contains the package version.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_DescribePackageVersion_RequestSyntax) **   <a name="codeartifact-DescribePackageVersion-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [format](#API_DescribePackageVersion_RequestSyntax) **   <a name="codeartifact-DescribePackageVersion-request-uri-format"></a>
 A format that specifies the type of the requested package version.
Valid Values: `npm | pypi | maven | nuget | generic | ruby | swift | cargo`
Required: Yes

 ** [namespace](#API_DescribePackageVersion_RequestSyntax) **   <a name="codeartifact-DescribePackageVersion-request-uri-namespace"></a>
The namespace of the requested package version. The package component that specifies its namespace depends on its type. For example:
The namespace is required when requesting package versions of the following formats:
+ Maven
+ Swift
+ generic
+  The namespace of a Maven package version is its `groupId`.
+  The namespace of an npm or Swift package version is its `scope`.
+ The namespace of a generic package is its `namespace`.
+  Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [package](#API_DescribePackageVersion_RequestSyntax) **   <a name="codeartifact-DescribePackageVersion-request-uri-package"></a>
 The name of the requested package version.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

 ** [packageVersion](#API_DescribePackageVersion_RequestSyntax) **   <a name="codeartifact-DescribePackageVersion-request-uri-packageVersion"></a>
 A string that contains the package version (for example, `3.5.2`).
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

 ** [repository](#API_DescribePackageVersion_RequestSyntax) **   <a name="codeartifact-DescribePackageVersion-request-uri-repository"></a>
 The name of the repository that contains the package version.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

## Request Body
<a name="API_DescribePackageVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribePackageVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "packageVersion": {
      "displayName": "string",
      "format": "string",
      "homePage": "string",
      "licenses": [
         {
            "name": "string",
            "url": "string"
         }
      ],
      "namespace": "string",
      "origin": {
         "domainEntryPoint": {
            "externalConnectionName": "string",
            "repositoryName": "string"
         },
         "originType": "string"
      },
      "packageName": "string",
      "publishedTime": number,
      "revision": "string",
      "sourceCodeRepository": "string",
      "status": "string",
      "summary": "string",
      "version": "string"
   }
}
```

## Response Elements
<a name="API_DescribePackageVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [packageVersion](#API_DescribePackageVersion_ResponseSyntax) **   <a name="codeartifact-DescribePackageVersion-response-packageVersion"></a>
 A [PackageVersionDescription](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html) object that contains information about the requested package version.
Type: [PackageVersionDescription](API_PackageVersionDescription.md) object

## Errors
<a name="API_DescribePackageVersion_Errors"></a>

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
<a name="API_DescribePackageVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/DescribePackageVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/DescribePackageVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/DescribePackageVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/DescribePackageVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/DescribePackageVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/DescribePackageVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/DescribePackageVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/DescribePackageVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/DescribePackageVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/DescribePackageVersion)
