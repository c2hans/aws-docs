---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListAssociatedPackages.html
---

# ListAssociatedPackages
<a name="API_ListAssociatedPackages"></a>

Returns a list of packages associated with the requested package group. For information package group association and matching, see [Package group definition syntax and matching behavior](https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-definition-syntax-matching-behavior.html) in the *CodeArtifact User Guide*.

## Request Syntax
<a name="API_ListAssociatedPackages_RequestSyntax"></a>

```
GET /v1/list-associated-packages?domain={{domain}}&domain-owner={{domainOwner}}&max-results={{maxResults}}&next-token={{nextToken}}&package-group={{packageGroup}}&preview={{preview}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAssociatedPackages_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_ListAssociatedPackages_RequestSyntax) **   <a name="codeartifact-ListAssociatedPackages-request-uri-domain"></a>
 The name of the domain that contains the package group from which to list associated packages.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_ListAssociatedPackages_RequestSyntax) **   <a name="codeartifact-ListAssociatedPackages-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [maxResults](#API_ListAssociatedPackages_RequestSyntax) **   <a name="codeartifact-ListAssociatedPackages-request-uri-maxResults"></a>
 The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListAssociatedPackages_RequestSyntax) **   <a name="codeartifact-ListAssociatedPackages-request-uri-nextToken"></a>
 The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S+`

 ** [packageGroup](#API_ListAssociatedPackages_RequestSyntax) **   <a name="codeartifact-ListAssociatedPackages-request-uri-packageGroup"></a>
 The pattern of the package group from which to list associated packages.
Length Constraints: Minimum length of 2. Maximum length of 520.
Pattern: `[^\p{C}\p{IsWhitespace}]+`
Required: Yes

 ** [preview](#API_ListAssociatedPackages_RequestSyntax) **   <a name="codeartifact-ListAssociatedPackages-request-uri-preview"></a>
 When this flag is included, `ListAssociatedPackages` will return a list of packages that would be associated with a package group, even if it does not exist.

## Request Body
<a name="API_ListAssociatedPackages_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAssociatedPackages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "packages": [
      {
         "associationType": "string",
         "format": "string",
         "namespace": "string",
         "package": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListAssociatedPackages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListAssociatedPackages_ResponseSyntax) **   <a name="codeartifact-ListAssociatedPackages-response-nextToken"></a>
 The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S+`

 ** [packages](#API_ListAssociatedPackages_ResponseSyntax) **   <a name="codeartifact-ListAssociatedPackages-response-packages"></a>
 The list of packages associated with the requested package group.
Type: Array of [AssociatedPackage](API_AssociatedPackage.md) objects

## Errors
<a name="API_ListAssociatedPackages_Errors"></a>

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
<a name="API_ListAssociatedPackages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/ListAssociatedPackages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/ListAssociatedPackages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/ListAssociatedPackages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/ListAssociatedPackages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/ListAssociatedPackages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/ListAssociatedPackages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/ListAssociatedPackages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/ListAssociatedPackages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/ListAssociatedPackages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/ListAssociatedPackages)
