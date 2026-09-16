---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackages.html
---

# ListPackages
<a name="API_ListPackages"></a>

 Returns a list of [PackageSummary](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageSummary.html) objects for packages in a repository that match the request parameters.

## Request Syntax
<a name="API_ListPackages_RequestSyntax"></a>

```
POST /v1/packages?domain={{domain}}&domain-owner={{domainOwner}}&format={{format}}&max-results={{maxResults}}&namespace={{namespace}}&next-token={{nextToken}}&package-prefix={{packagePrefix}}&publish={{publish}}&repository={{repository}}&upstream={{upstream}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPackages_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_ListPackages_RequestSyntax) **   <a name="codeartifact-ListPackages-request-uri-domain"></a>
 The name of the domain that contains the repository that contains the requested packages.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_ListPackages_RequestSyntax) **   <a name="codeartifact-ListPackages-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [format](#API_ListPackages_RequestSyntax) **   <a name="codeartifact-ListPackages-request-uri-format"></a>
The format used to filter requested packages. Only packages from the provided format will be returned.
Valid Values: `npm | pypi | maven | nuget | generic | ruby | swift | cargo`

 ** [maxResults](#API_ListPackages_RequestSyntax) **   <a name="codeartifact-ListPackages-request-uri-maxResults"></a>
 The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [namespace](#API_ListPackages_RequestSyntax) **   <a name="codeartifact-ListPackages-request-uri-namespace"></a>
The namespace prefix used to filter requested packages. Only packages with a namespace that starts with the provided string value are returned. Note that although this option is called `--namespace` and not `--namespace-prefix`, it has prefix-matching behavior.
Each package format uses namespace as follows:
+  The namespace of a Maven package version is its `groupId`.
+  The namespace of an npm or Swift package version is its `scope`.
+ The namespace of a generic package is its `namespace`.
+  Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [nextToken](#API_ListPackages_RequestSyntax) **   <a name="codeartifact-ListPackages-request-uri-nextToken"></a>
 The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S+`

 ** [packagePrefix](#API_ListPackages_RequestSyntax) **   <a name="codeartifact-ListPackages-request-uri-packagePrefix"></a>
 A prefix used to filter requested packages. Only packages with names that start with `packagePrefix` are returned.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [publish](#API_ListPackages_RequestSyntax) **   <a name="codeartifact-ListPackages-request-uri-publish"></a>
The value of the `Publish` package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see [PackageOriginRestrictions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html).
Valid Values: `ALLOW | BLOCK`

 ** [repository](#API_ListPackages_RequestSyntax) **   <a name="codeartifact-ListPackages-request-uri-repository"></a>
 The name of the repository that contains the requested packages.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

 ** [upstream](#API_ListPackages_RequestSyntax) **   <a name="codeartifact-ListPackages-request-uri-upstream"></a>
The value of the `Upstream` package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see [PackageOriginRestrictions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html).
Valid Values: `ALLOW | BLOCK`

## Request Body
<a name="API_ListPackages_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPackages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "packages": [
      {
         "format": "string",
         "namespace": "string",
         "originConfiguration": {
            "restrictions": {
               "publish": "string",
               "upstream": "string"
            }
         },
         "package": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPackages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPackages_ResponseSyntax) **   <a name="codeartifact-ListPackages-response-nextToken"></a>
 If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S+`

 ** [packages](#API_ListPackages_ResponseSyntax) **   <a name="codeartifact-ListPackages-response-packages"></a>
 The list of returned [PackageSummary](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageSummary.html) objects.
Type: Array of [PackageSummary](API_PackageSummary.md) objects

## Errors
<a name="API_ListPackages_Errors"></a>

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
<a name="API_ListPackages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/ListPackages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/ListPackages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/ListPackages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/ListPackages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/ListPackages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/ListPackages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/ListPackages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/ListPackages)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/ListPackages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/ListPackages)
