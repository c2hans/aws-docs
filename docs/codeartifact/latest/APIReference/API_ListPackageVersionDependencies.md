---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersionDependencies.html
---

# ListPackageVersionDependencies
<a name="API_ListPackageVersionDependencies"></a>

 Returns the direct dependencies for a package version. The dependencies are returned as [PackageDependency](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDependency.html) objects. CodeArtifact extracts the dependencies for a package version from the metadata file for the package format (for example, the `package.json` file for npm packages and the `pom.xml` file for Maven). Any package version dependencies that are not listed in the configuration file are not returned.

## Request Syntax
<a name="API_ListPackageVersionDependencies_RequestSyntax"></a>

```
POST /v1/package/version/dependencies?domain={{domain}}&domain-owner={{domainOwner}}&format={{format}}&namespace={{namespace}}&next-token={{nextToken}}&package={{package}}&repository={{repository}}&version={{packageVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPackageVersionDependencies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_ListPackageVersionDependencies_RequestSyntax) **   <a name="codeartifact-ListPackageVersionDependencies-request-uri-domain"></a>
 The name of the domain that contains the repository that contains the requested package version dependencies.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_ListPackageVersionDependencies_RequestSyntax) **   <a name="codeartifact-ListPackageVersionDependencies-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [format](#API_ListPackageVersionDependencies_RequestSyntax) **   <a name="codeartifact-ListPackageVersionDependencies-request-uri-format"></a>
 The format of the package with the requested dependencies.
Valid Values: `npm | pypi | maven | nuget`
Required: Yes

 ** [namespace](#API_ListPackageVersionDependencies_RequestSyntax) **   <a name="codeartifact-ListPackageVersionDependencies-request-uri-namespace"></a>
The namespace of the package version with the requested dependencies. The package component that specifies its namespace depends on its type. For example:
The namespace is required when listing dependencies from package versions of the following formats:
+ Maven
+  The namespace of a Maven package version is its `groupId`.
+  The namespace of an npm package version is its `scope`.
+  Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [nextToken](#API_ListPackageVersionDependencies_RequestSyntax) **   <a name="codeartifact-ListPackageVersionDependencies-request-uri-nextToken"></a>
 The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S+`

 ** [package](#API_ListPackageVersionDependencies_RequestSyntax) **   <a name="codeartifact-ListPackageVersionDependencies-request-uri-package"></a>
 The name of the package versions' package.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

 ** [packageVersion](#API_ListPackageVersionDependencies_RequestSyntax) **   <a name="codeartifact-ListPackageVersionDependencies-request-uri-packageVersion"></a>
 A string that contains the package version (for example, `3.5.2`).
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

 ** [repository](#API_ListPackageVersionDependencies_RequestSyntax) **   <a name="codeartifact-ListPackageVersionDependencies-request-uri-repository"></a>
 The name of the repository that contains the requested package version.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

## Request Body
<a name="API_ListPackageVersionDependencies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPackageVersionDependencies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dependencies": [
      {
         "dependencyType": "string",
         "namespace": "string",
         "package": "string",
         "versionRequirement": "string"
      }
   ],
   "format": "string",
   "namespace": "string",
   "nextToken": "string",
   "package": "string",
   "version": "string",
   "versionRevision": "string"
}
```

## Response Elements
<a name="API_ListPackageVersionDependencies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dependencies](#API_ListPackageVersionDependencies_ResponseSyntax) **   <a name="codeartifact-ListPackageVersionDependencies-response-dependencies"></a>
 The returned list of [PackageDependency](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDependency.html) objects.
Type: Array of [PackageDependency](API_PackageDependency.md) objects

 ** [format](#API_ListPackageVersionDependencies_ResponseSyntax) **   <a name="codeartifact-ListPackageVersionDependencies-response-format"></a>
 A format that specifies the type of the package that contains the returned dependencies.
Type: String
Valid Values: `npm | pypi | maven | nuget`

 ** [namespace](#API_ListPackageVersionDependencies_ResponseSyntax) **   <a name="codeartifact-ListPackageVersionDependencies-response-namespace"></a>
The namespace of the package version that contains the returned dependencies. The package component that specifies its namespace depends on its type. For example:
The namespace is required when listing dependencies from package versions of the following formats:
+ Maven
+  The namespace of a Maven package version is its `groupId`.
+  The namespace of an npm package version is its `scope`.
+  Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [nextToken](#API_ListPackageVersionDependencies_ResponseSyntax) **   <a name="codeartifact-ListPackageVersionDependencies-response-nextToken"></a>
 The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S+`

 ** [package](#API_ListPackageVersionDependencies_ResponseSyntax) **   <a name="codeartifact-ListPackageVersionDependencies-response-package"></a>
 The name of the package that contains the returned package versions dependencies.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [version](#API_ListPackageVersionDependencies_ResponseSyntax) **   <a name="codeartifact-ListPackageVersionDependencies-response-version"></a>
 The version of the package that is specified in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [versionRevision](#API_ListPackageVersionDependencies_ResponseSyntax) **   <a name="codeartifact-ListPackageVersionDependencies-response-versionRevision"></a>
 The current revision associated with the package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `\S+`

## Errors
<a name="API_ListPackageVersionDependencies_Errors"></a>

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
<a name="API_ListPackageVersionDependencies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/ListPackageVersionDependencies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/ListPackageVersionDependencies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/ListPackageVersionDependencies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/ListPackageVersionDependencies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/ListPackageVersionDependencies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/ListPackageVersionDependencies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/ListPackageVersionDependencies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/ListPackageVersionDependencies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/ListPackageVersionDependencies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/ListPackageVersionDependencies)
