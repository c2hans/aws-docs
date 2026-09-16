---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListPrivacyBudgetTemplates.html
---

# ListPrivacyBudgetTemplates
<a name="API_ListPrivacyBudgetTemplates"></a>

Returns detailed information about the privacy budget templates in a specified membership.

## Request Syntax
<a name="API_ListPrivacyBudgetTemplates_RequestSyntax"></a>

```
GET /memberships/{{membershipIdentifier}}/privacybudgettemplates?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPrivacyBudgetTemplates_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListPrivacyBudgetTemplates_RequestSyntax) **   <a name="API-ListPrivacyBudgetTemplates-request-uri-maxResults"></a>
The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [membershipIdentifier](#API_ListPrivacyBudgetTemplates_RequestSyntax) **   <a name="API-ListPrivacyBudgetTemplates-request-uri-membershipIdentifier"></a>
A unique identifier for one of your memberships for a collaboration. The privacy budget templates are retrieved from the collaboration that this membership belongs to. Accepts a membership ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [nextToken](#API_ListPrivacyBudgetTemplates_RequestSyntax) **   <a name="API-ListPrivacyBudgetTemplates-request-uri-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 0. Maximum length of 10240.

## Request Body
<a name="API_ListPrivacyBudgetTemplates_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPrivacyBudgetTemplates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "privacyBudgetTemplateSummaries": [
      {
         "arn": "string",
         "collaborationArn": "string",
         "collaborationId": "string",
         "createTime": number,
         "id": "string",
         "membershipArn": "string",
         "membershipId": "string",
         "privacyBudgetType": "string",
         "updateTime": number
      }
   ]
}
```

## Response Elements
<a name="API_ListPrivacyBudgetTemplates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPrivacyBudgetTemplates_ResponseSyntax) **   <a name="API-ListPrivacyBudgetTemplates-response-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.

 ** [privacyBudgetTemplateSummaries](#API_ListPrivacyBudgetTemplates_ResponseSyntax) **   <a name="API-ListPrivacyBudgetTemplates-response-privacyBudgetTemplateSummaries"></a>
An array that summarizes the privacy budget templates. The summary includes collaboration information, creation information, and privacy budget type.
Type: Array of [PrivacyBudgetTemplateSummary](API_PrivacyBudgetTemplateSummary.md) objects

## Errors
<a name="API_ListPrivacyBudgetTemplates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The Id of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
 ** fieldList **
Validation errors for specific input parameters.
 ** reason **
A reason code for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListPrivacyBudgetTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/ListPrivacyBudgetTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/ListPrivacyBudgetTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ListPrivacyBudgetTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/ListPrivacyBudgetTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ListPrivacyBudgetTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/ListPrivacyBudgetTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/ListPrivacyBudgetTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/ListPrivacyBudgetTemplates)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/ListPrivacyBudgetTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ListPrivacyBudgetTemplates)
