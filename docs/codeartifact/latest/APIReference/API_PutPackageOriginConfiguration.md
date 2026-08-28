---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PutPackageOriginConfiguration.html
---

# PutPackageOriginConfiguration
<a name="API_PutPackageOriginConfiguration"></a>

Sets the package origin configuration for a package.

The package origin configuration determines how new versions of a package can be added to a repository. You can allow or block direct publishing of new package versions, or ingestion and retaining of new package versions from an external connection or upstream source. For more information about package origin controls and configuration, see [Editing package origin controls](https://docs.aws.amazon.com/codeartifact/latest/ug/package-origin-controls.html) in the * AWS CodeArtifact User Guide*.

 `PutPackageOriginConfiguration` can be called on a package that doesn't yet exist in the repository. When called on a package that does not exist, a package is created in the repository with no versions and the requested restrictions are set on the package. This can be used to preemptively block ingesting or retaining any versions from external connections or upstream repositories, or to block publishing any versions of the package into the repository before connecting any package managers or publishers to the repository.

## Request Syntax
<a name="API_PutPackageOriginConfiguration_RequestSyntax"></a>

```
POST /v1/package?domain={{domain}}&domain-owner={{domainOwner}}&format={{format}}&namespace={{namespace}}&package={{package}}&repository={{repository}} HTTP/1.1
Content-type: application/json

{
   "restrictions": {
      "publish": "{{string}}",
      "upstream": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_PutPackageOriginConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_PutPackageOriginConfiguration_RequestSyntax) **   <a name="codeartifact-PutPackageOriginConfiguration-request-uri-domain"></a>
The name of the domain that contains the repository that contains the package.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_PutPackageOriginConfiguration_RequestSyntax) **   <a name="codeartifact-PutPackageOriginConfiguration-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [format](#API_PutPackageOriginConfiguration_RequestSyntax) **   <a name="codeartifact-PutPackageOriginConfiguration-request-uri-format"></a>
A format that specifies the type of the package to be updated.
Valid Values: `npm | pypi | maven | nuget | generic | ruby | swift | cargo`
Required: Yes

 ** [namespace](#API_PutPackageOriginConfiguration_RequestSyntax) **   <a name="codeartifact-PutPackageOriginConfiguration-request-uri-namespace"></a>
The namespace of the package to be updated. The package component that specifies its namespace depends on its type. For example:
+  The namespace of a Maven package version is its `groupId`.
+  The namespace of an npm or Swift package version is its `scope`.
+ The namespace of a generic package is its `namespace`.
+  Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [package](#API_PutPackageOriginConfiguration_RequestSyntax) **   <a name="codeartifact-PutPackageOriginConfiguration-request-uri-package"></a>
The name of the package to be updated.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

 ** [repository](#API_PutPackageOriginConfiguration_RequestSyntax) **   <a name="codeartifact-PutPackageOriginConfiguration-request-uri-repository"></a>
The name of the repository that contains the package.
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: Yes

## Request Body
<a name="API_PutPackageOriginConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [restrictions](#API_PutPackageOriginConfiguration_RequestSyntax) **   <a name="codeartifact-PutPackageOriginConfiguration-request-restrictions"></a>
A [PackageOriginRestrictions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html) object that contains information about the `upstream` and `publish` package origin restrictions. The `upstream` restriction determines if new package versions can be ingested or retained from external connections or upstream repositories. The `publish` restriction determines if new package versions can be published directly to the repository.
You must include both the desired `upstream` and `publish` restrictions.
Type: [PackageOriginRestrictions](API_PackageOriginRestrictions.md) object
Required: Yes

## Response Syntax
<a name="API_PutPackageOriginConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "originConfiguration": {
      "restrictions": {
         "publish": "string",
         "upstream": "string"
      }
   }
}
```

## Response Elements
<a name="API_PutPackageOriginConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [originConfiguration](#API_PutPackageOriginConfiguration_ResponseSyntax) **   <a name="codeartifact-PutPackageOriginConfiguration-response-originConfiguration"></a>
A [PackageOriginConfiguration](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginConfiguration.html) object that describes the origin configuration set for the package. It contains a [PackageOriginRestrictions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html) object that describes how new versions of the package can be introduced to the repository.
Type: [PackageOriginConfiguration](API_PackageOriginConfiguration.md) object

## Errors
<a name="API_PutPackageOriginConfiguration_Errors"></a>

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
<a name="API_PutPackageOriginConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/PutPackageOriginConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/PutPackageOriginConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/PutPackageOriginConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/PutPackageOriginConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/PutPackageOriginConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/PutPackageOriginConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/PutPackageOriginConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/PutPackageOriginConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/PutPackageOriginConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/PutPackageOriginConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
