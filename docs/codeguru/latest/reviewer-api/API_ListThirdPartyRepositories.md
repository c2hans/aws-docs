---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListThirdPartyRepositories.html
---

# ListThirdPartyRepositories
<a name="API_ListThirdPartyRepositories"></a>

**Note**
As of November 7, 2025, you cannot create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

Lists third-party repositories that are connected to CodeGuru Reviewer for code analysis.

## Request Syntax
<a name="API_ListThirdPartyRepositories_RequestSyntax"></a>

```
GET /thirdPartyRepositories?ConnectionToken={{ConnectionToken}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListThirdPartyRepositories_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectionToken](#API_ListThirdPartyRepositories_RequestSyntax) **   <a name="reviewer-ListThirdPartyRepositories-request-uri-ConnectionToken"></a>
The connection token used to authenticate with the third-party repository provider.
Length Constraints: Minimum length of 8. Maximum length of 2048.
Pattern: `\S+`
Required: Yes

 ** [NextToken](#API_ListThirdPartyRepositories_RequestSyntax) **   <a name="reviewer-ListThirdPartyRepositories-request-uri-NextToken"></a>
The pagination token for retrieving the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S+`

## Request Body
<a name="API_ListThirdPartyRepositories_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListThirdPartyRepositories_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ThirdPartyRepositories": [
      {
         "ConnectionToken": "string",
         "IsEnabled": boolean,
         "Name": "string",
         "Owner": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListThirdPartyRepositories_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListThirdPartyRepositories_ResponseSyntax) **   <a name="reviewer-ListThirdPartyRepositories-response-NextToken"></a>
The pagination token for retrieving additional results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S+`

 ** [ThirdPartyRepositories](#API_ListThirdPartyRepositories_ResponseSyntax) **   <a name="reviewer-ListThirdPartyRepositories-response-ThirdPartyRepositories"></a>
A list of third-party repositories available for code review.
Type: Array of [ThirdPartyRepository](API_ThirdPartyRepository.md) objects

## Errors
<a name="API_ListThirdPartyRepositories_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_ListThirdPartyRepositories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguru-reviewer-2019-09-19/ListThirdPartyRepositories)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguru-reviewer-2019-09-19/ListThirdPartyRepositories)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/ListThirdPartyRepositories)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguru-reviewer-2019-09-19/ListThirdPartyRepositories)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/ListThirdPartyRepositories)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguru-reviewer-2019-09-19/ListThirdPartyRepositories)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguru-reviewer-2019-09-19/ListThirdPartyRepositories)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguru-reviewer-2019-09-19/ListThirdPartyRepositories)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguru-reviewer-2019-09-19/ListThirdPartyRepositories)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/ListThirdPartyRepositories)
