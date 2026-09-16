---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListAllowedRepositoriesForGroup.html
---

# ListAllowedRepositoriesForGroup
<a name="API_ListAllowedRepositoriesForGroup"></a>

Lists the repositories in the added repositories list of the specified restriction type for a package group. For more information about restriction types and added repository lists, see [Package group origin controls](https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-origin-controls.html) in the *CodeArtifact User Guide*.

## Request Syntax
<a name="API_ListAllowedRepositoriesForGroup_RequestSyntax"></a>

```
GET /v1/package-group-allowed-repositories?domain={{domain}}&domain-owner={{domainOwner}}&max-results={{maxResults}}&next-token={{nextToken}}&originRestrictionType={{originRestrictionType}}&package-group={{packageGroup}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAllowedRepositoriesForGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_ListAllowedRepositoriesForGroup_RequestSyntax) **   <a name="codeartifact-ListAllowedRepositoriesForGroup-request-uri-domain"></a>
 The name of the domain that contains the package group from which to list allowed repositories.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_ListAllowedRepositoriesForGroup_RequestSyntax) **   <a name="codeartifact-ListAllowedRepositoriesForGroup-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [maxResults](#API_ListAllowedRepositoriesForGroup_RequestSyntax) **   <a name="codeartifact-ListAllowedRepositoriesForGroup-request-uri-maxResults"></a>
 The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListAllowedRepositoriesForGroup_RequestSyntax) **   <a name="codeartifact-ListAllowedRepositoriesForGroup-request-uri-nextToken"></a>
 The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S+`

 ** [originRestrictionType](#API_ListAllowedRepositoriesForGroup_RequestSyntax) **   <a name="codeartifact-ListAllowedRepositoriesForGroup-request-uri-originRestrictionType"></a>
The origin configuration restriction type of which to list allowed repositories.
Valid Values: `EXTERNAL_UPSTREAM | INTERNAL_UPSTREAM | PUBLISH`
Required: Yes

 ** [packageGroup](#API_ListAllowedRepositoriesForGroup_RequestSyntax) **   <a name="codeartifact-ListAllowedRepositoriesForGroup-request-uri-packageGroup"></a>
The pattern of the package group from which to list allowed repositories.
Length Constraints: Minimum length of 2. Maximum length of 520.
Pattern: `[^\p{C}\p{IsWhitespace}]+`
Required: Yes

## Request Body
<a name="API_ListAllowedRepositoriesForGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAllowedRepositoriesForGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "allowedRepositories": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAllowedRepositoriesForGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [allowedRepositories](#API_ListAllowedRepositoriesForGroup_ResponseSyntax) **   <a name="codeartifact-ListAllowedRepositoriesForGroup-response-allowedRepositories"></a>
The list of allowed repositories for the package group and origin configuration restriction type.
Type: Array of strings
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`

 ** [nextToken](#API_ListAllowedRepositoriesForGroup_ResponseSyntax) **   <a name="codeartifact-ListAllowedRepositoriesForGroup-response-nextToken"></a>
 The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S+`

## Errors
<a name="API_ListAllowedRepositoriesForGroup_Errors"></a>

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
<a name="API_ListAllowedRepositoriesForGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/ListAllowedRepositoriesForGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/ListAllowedRepositoriesForGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/ListAllowedRepositoriesForGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/ListAllowedRepositoriesForGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/ListAllowedRepositoriesForGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/ListAllowedRepositoriesForGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/ListAllowedRepositoriesForGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/ListAllowedRepositoriesForGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/ListAllowedRepositoriesForGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/ListAllowedRepositoriesForGroup)
