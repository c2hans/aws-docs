---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html
---

# ListPackageVersions
<a name="API_ListPackageVersions"></a>

 Returns a list of [PackageVersionSummary](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionSummary.html) objects for package versions in a repository that match the request parameters. Package versions of all statuses will be returned by default when calling `list-package-versions` with no `--status` parameter.

## Request Syntax
<a name="API_ListPackageVersions_RequestSyntax"></a>

```
POST /v1/package/versions?domain={{domain}}&domain-owner={{domainOwner}}&format={{format}}&max-results={{maxResults}}&namespace={{namespace}}&next-token={{nextToken}}&originType={{originType}}&package={{package}}&repository={{repository}}&sortBy={{sortBy}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPackageVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_ListPackageVersions_RequestSyntax) **   <a name="codeartifact-ListPackageVersions-request-uri-domain"></a>
 The name of the domain that contains the repository that contains the requested package versions.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_ListPackageVersions_RequestSyntax) **   <a name="codeartifact-ListPackageVersions-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [format](#API_ListPackageVersions_RequestSyntax) **   <a name="codeartifact-ListPackageVersions-request-uri-format"></a>
 The format of the package versions you want to list.
Valid Values: `npm | pypi | maven | nuget | generic | ruby | swift | cargo`
Required: Yes

 ** [maxResults](#API_ListPackageVersions_RequestSyntax) **   <a name="codeartifact-ListPackageVersions-request-uri-maxResults"></a>
 The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [namespace](#API_ListPackageVersions_RequestSyntax) **   <a name="codeartifact-ListPackageVersions-request-uri-namespace"></a>
The namespace of the package that contains the requested package versions. The package component that specifies its namespace depends on its type. For example:
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

 ** [nextToken](#API_ListPackageVersions_RequestSyntax) **   <a name="codeartifact-ListPackageVersions-request-uri-nextToken"></a>
 The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S+`

 ** [originType](#API_ListPackageVersions_RequestSyntax) **   <a name="codeartifact-ListPackageVersions-request-uri-originType"></a>
The `originType` used to filter package versions. Only package versions with the provided `originType` will be returned.
Valid Values: `INTERNAL | EXTERNAL | UNKNOWN`

 ** [package](#API_ListPackageVersions_RequestSyntax) **   <a name="codeartifact-ListPackageVersions-request-uri-package"></a>
 The name of the package for which you want to request package versions.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

 ** [repository](#API_ListPackageVersions_RequestSyntax) **   <a name="codeartifact-ListPackageVersions-request-uri-repository"></a>
 The name of the repository that contains the requested package versions.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

 ** [sortBy](#API_ListPackageVersions_RequestSyntax) **   <a name="codeartifact-ListPackageVersions-request-uri-sortBy"></a>
 How to sort the requested list of package versions.
Valid Values: `PUBLISHED_TIME`

 ** [status](#API_ListPackageVersions_RequestSyntax) **   <a name="codeartifact-ListPackageVersions-request-uri-status"></a>
 A string that filters the requested package versions by status.
Valid Values: `Archived | Disposed | Published | Unfinished | Unlisted`

## Request Body
<a name="API_ListPackageVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPackageVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "defaultDisplayVersion": "string",
   "format": "string",
   "namespace": "string",
   "nextToken": "string",
   "package": "string",
   "versions": [
      {
         "origin": {
            "domainEntryPoint": {
               "externalConnectionName": "string",
               "repositoryName": "string"
            },
            "originType": "string"
         },
         "revision": "string",
         "status": "string",
         "version": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPackageVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [defaultDisplayVersion](#API_ListPackageVersions_ResponseSyntax) **   <a name="codeartifact-ListPackageVersions-response-defaultDisplayVersion"></a>
 The default package version to display. This depends on the package format:
+  For Maven and PyPI packages, it's the most recently published package version.
+  For npm packages, it's the version referenced by the `latest` tag. If the `latest` tag is not set, it's the most recently published package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [format](#API_ListPackageVersions_ResponseSyntax) **   <a name="codeartifact-ListPackageVersions-response-format"></a>
 A format of the package.
Type: String
Valid Values: `npm | pypi | maven | nuget | generic | ruby | swift | cargo`

 ** [namespace](#API_ListPackageVersions_ResponseSyntax) **   <a name="codeartifact-ListPackageVersions-response-namespace"></a>
The namespace of the package that contains the requested package versions. The package component that specifies its namespace depends on its type. For example:
+  The namespace of a Maven package version is its `groupId`.
+  The namespace of an npm or Swift package version is its `scope`.
+ The namespace of a generic package is its `namespace`.
+  Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [nextToken](#API_ListPackageVersions_ResponseSyntax) **   <a name="codeartifact-ListPackageVersions-response-nextToken"></a>
 If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S+`

 ** [package](#API_ListPackageVersions_ResponseSyntax) **   <a name="codeartifact-ListPackageVersions-response-package"></a>
 The name of the package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [versions](#API_ListPackageVersions_ResponseSyntax) **   <a name="codeartifact-ListPackageVersions-response-versions"></a>
 The returned list of [PackageVersionSummary](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionSummary.html) objects.
Type: Array of [PackageVersionSummary](API_PackageVersionSummary.md) objects

## Errors
<a name="API_ListPackageVersions_Errors"></a>

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
<a name="API_ListPackageVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/ListPackageVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/ListPackageVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/ListPackageVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/ListPackageVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/ListPackageVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/ListPackageVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/ListPackageVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/ListPackageVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/ListPackageVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/ListPackageVersions)
