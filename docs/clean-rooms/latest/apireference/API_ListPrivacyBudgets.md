---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListPrivacyBudgets.html
---

# ListPrivacyBudgets
<a name="API_ListPrivacyBudgets"></a>

Returns detailed information about the privacy budgets in a specified membership.

## Request Syntax
<a name="API_ListPrivacyBudgets_RequestSyntax"></a>

```
GET /memberships/{{membershipIdentifier}}/privacybudgets?accessBudgetResourceArn={{accessBudgetResourceArn}}&maxResults={{maxResults}}&nextToken={{nextToken}}&privacyBudgetType={{privacyBudgetType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPrivacyBudgets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accessBudgetResourceArn](#API_ListPrivacyBudgets_RequestSyntax) **   <a name="API-ListPrivacyBudgets-request-uri-accessBudgetResourceArn"></a>
The Amazon Resource Name (ARN) of the access budget resource to filter privacy budgets by.
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/(configuredtableassociation|intermediatetable)/[\d\w-]+`

 ** [maxResults](#API_ListPrivacyBudgets_RequestSyntax) **   <a name="API-ListPrivacyBudgets-request-uri-maxResults"></a>
The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [membershipIdentifier](#API_ListPrivacyBudgets_RequestSyntax) **   <a name="API-ListPrivacyBudgets-request-uri-membershipIdentifier"></a>
A unique identifier for one of your memberships for a collaboration. The privacy budget is retrieved from the collaboration that this membership belongs to. Accepts a membership ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [nextToken](#API_ListPrivacyBudgets_RequestSyntax) **   <a name="API-ListPrivacyBudgets-request-uri-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 0. Maximum length of 10240.

 ** [privacyBudgetType](#API_ListPrivacyBudgets_RequestSyntax) **   <a name="API-ListPrivacyBudgets-request-uri-privacyBudgetType"></a>
The privacy budget type.
Valid Values: `DIFFERENTIAL_PRIVACY | ACCESS_BUDGET`
Required: Yes

## Request Body
<a name="API_ListPrivacyBudgets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPrivacyBudgets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "privacyBudgetSummaries": [
      {
         "budget": { ... },
         "collaborationArn": "string",
         "collaborationId": "string",
         "createTime": number,
         "id": "string",
         "membershipArn": "string",
         "membershipId": "string",
         "privacyBudgetTemplateArn": "string",
         "privacyBudgetTemplateId": "string",
         "type": "string",
         "updateTime": number
      }
   ]
}
```

## Response Elements
<a name="API_ListPrivacyBudgets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPrivacyBudgets_ResponseSyntax) **   <a name="API-ListPrivacyBudgets-response-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.

 ** [privacyBudgetSummaries](#API_ListPrivacyBudgets_ResponseSyntax) **   <a name="API-ListPrivacyBudgets-response-privacyBudgetSummaries"></a>
An array that summarizes the privacy budgets. The summary includes collaboration information, membership information, privacy budget template information, and privacy budget details.
Type: Array of [PrivacyBudgetSummary](API_PrivacyBudgetSummary.md) objects

## Errors
<a name="API_ListPrivacyBudgets_Errors"></a>

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
<a name="API_ListPrivacyBudgets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/ListPrivacyBudgets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/ListPrivacyBudgets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ListPrivacyBudgets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/ListPrivacyBudgets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ListPrivacyBudgets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/ListPrivacyBudgets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/ListPrivacyBudgets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/ListPrivacyBudgets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/ListPrivacyBudgets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ListPrivacyBudgets)
