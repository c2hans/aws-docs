---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetAssociatedPackageGroup.html
---

# GetAssociatedPackageGroup
<a name="API_GetAssociatedPackageGroup"></a>

Returns the most closely associated package group to the specified package. This API does not require that the package exist in any repository in the domain. As such, `GetAssociatedPackageGroup` can be used to see which package group's origin configuration applies to a package before that package is in a repository. This can be helpful to check if public packages are blocked without ingesting them.

For information package group association and matching, see [Package group definition syntax and matching behavior](https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-definition-syntax-matching-behavior.html) in the *CodeArtifact User Guide*.

## Request Syntax
<a name="API_GetAssociatedPackageGroup_RequestSyntax"></a>

```
GET /v1/get-associated-package-group?domain={{domain}}&domain-owner={{domainOwner}}&format={{format}}&namespace={{namespace}}&package={{package}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAssociatedPackageGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_GetAssociatedPackageGroup_RequestSyntax) **   <a name="codeartifact-GetAssociatedPackageGroup-request-uri-domain"></a>
 The name of the domain that contains the package from which to get the associated package group.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_GetAssociatedPackageGroup_RequestSyntax) **   <a name="codeartifact-GetAssociatedPackageGroup-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [format](#API_GetAssociatedPackageGroup_RequestSyntax) **   <a name="codeartifact-GetAssociatedPackageGroup-request-uri-format"></a>
 The format of the package from which to get the associated package group.
Valid Values: `npm | pypi | maven | nuget | generic | ruby | swift | cargo`
Required: Yes

 ** [namespace](#API_GetAssociatedPackageGroup_RequestSyntax) **   <a name="codeartifact-GetAssociatedPackageGroup-request-uri-namespace"></a>
The namespace of the package from which to get the associated package group. The package component that specifies its namespace depends on its type. For example:
The namespace is required when getting associated package groups from packages of the following formats:
+ Maven
+ Swift
+ generic
+  The namespace of a Maven package version is its `groupId`.
+  The namespace of an npm or Swift package version is its `scope`.
+ The namespace of a generic package is its `namespace`.
+  Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`

 ** [package](#API_GetAssociatedPackageGroup_RequestSyntax) **   <a name="codeartifact-GetAssociatedPackageGroup-request-uri-package"></a>
 The package from which to get the associated package group.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^#/\s]+`
Required: Yes

## Request Body
<a name="API_GetAssociatedPackageGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAssociatedPackageGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "associationType": "string",
   "packageGroup": {
      "arn": "string",
      "contactInfo": "string",
      "createdTime": number,
      "description": "string",
      "domainName": "string",
      "domainOwner": "string",
      "originConfiguration": {
         "restrictions": {
            "string" : {
               "effectiveMode": "string",
               "inheritedFrom": {
                  "arn": "string",
                  "pattern": "string"
               },
               "mode": "string",
               "repositoriesCount": number
            }
         }
      },
      "parent": {
         "arn": "string",
         "pattern": "string"
      },
      "pattern": "string"
   }
}
```

## Response Elements
<a name="API_GetAssociatedPackageGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associationType](#API_GetAssociatedPackageGroup_ResponseSyntax) **   <a name="codeartifact-GetAssociatedPackageGroup-response-associationType"></a>
Describes the strength of the association between the package and package group. A strong match is also known as an exact match, and a weak match is known as a relative match.
Type: String
Valid Values: `STRONG | WEAK`

 ** [packageGroup](#API_GetAssociatedPackageGroup_ResponseSyntax) **   <a name="codeartifact-GetAssociatedPackageGroup-response-packageGroup"></a>
The package group that is associated with the requested package.
Type: [PackageGroupDescription](API_PackageGroupDescription.md) object

## Errors
<a name="API_GetAssociatedPackageGroup_Errors"></a>

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

 ** ValidationException **
 The operation did not succeed because a parameter in the request was sent with an invalid value.
 ** reason **

HTTP Status Code: 400

## See Also
<a name="API_GetAssociatedPackageGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/GetAssociatedPackageGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/GetAssociatedPackageGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/GetAssociatedPackageGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/GetAssociatedPackageGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/GetAssociatedPackageGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/GetAssociatedPackageGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/GetAssociatedPackageGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/GetAssociatedPackageGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/GetAssociatedPackageGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/GetAssociatedPackageGroup)
