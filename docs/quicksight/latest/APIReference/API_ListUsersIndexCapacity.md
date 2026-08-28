---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListUsersIndexCapacity.html
---

# ListUsersIndexCapacity
<a name="API_ListUsersIndexCapacity"></a>

Lists per-user index capacity consumption for an account.

## Request Syntax
<a name="API_ListUsersIndexCapacity_RequestSyntax"></a>

```
POST /accounts/{{awsAccountId}}/quick-index/user-capacity HTTP/1.1
Content-type: application/json

{
   "filters": [
      { ... }
   ],
   "maxResults": {{number}},
   "namespace": "{{string}}",
   "nextToken": "{{string}}",
   "sortBy": "{{string}}",
   "sortOrder": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListUsersIndexCapacity_RequestParameters"></a>

The request uses the following URI parameters.

 ** [awsAccountId](#API_ListUsersIndexCapacity_RequestSyntax) **   <a name="QS-ListUsersIndexCapacity-request-uri-awsAccountId"></a>
The ID of the AWS account that contains the index capacity data.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_ListUsersIndexCapacity_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListUsersIndexCapacity_RequestSyntax) **   <a name="QS-ListUsersIndexCapacity-request-filters"></a>
Filters to apply. Only one filter is supported per request. The userNameOrEmail and totalCapacityBytes filters are mutually exclusive.
Type: Array of [UserIndexCapacityFilter](API_UserIndexCapacityFilter.md) objects
Required: No

 ** [maxResults](#API_ListUsersIndexCapacity_RequestSyntax) **   <a name="QS-ListUsersIndexCapacity-request-maxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [namespace](#API_ListUsersIndexCapacity_RequestSyntax) **   <a name="QS-ListUsersIndexCapacity-request-namespace"></a>
The namespace to scope the user search to. Required when the userNameOrEmail filter is present.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`
Required: No

 ** [nextToken](#API_ListUsersIndexCapacity_RequestSyntax) **   <a name="QS-ListUsersIndexCapacity-request-nextToken"></a>
The token for the next set of results, received from a previous call.
Type: String
Required: No

 ** [sortBy](#API_ListUsersIndexCapacity_RequestSyntax) **   <a name="QS-ListUsersIndexCapacity-request-sortBy"></a>
The field to sort results by.
Type: String
Valid Values: `TOTAL_CAPACITY_BYTES`
Required: No

 ** [sortOrder](#API_ListUsersIndexCapacity_RequestSyntax) **   <a name="QS-ListUsersIndexCapacity-request-sortOrder"></a>
The sort order for results. Defaults to DESC if not specified.
Type: String
Valid Values: `ASC | DESC`
Required: No

## Response Syntax
<a name="API_ListUsersIndexCapacity_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "requestId": "string",
   "users": [
      {
         "email": "string",
         "kbCount": number,
         "role": "string",
         "spaceCount": number,
         "totalCapacityBytes": number,
         "totalKBCapacityBytes": number,
         "totalSpaceCapacityBytes": number,
         "userArn": "string",
         "userName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListUsersIndexCapacity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListUsersIndexCapacity_ResponseSyntax) **   <a name="QS-ListUsersIndexCapacity-response-nextToken"></a>
The token for the next set of results, or null if there are no more results.
Type: String

 ** [requestId](#API_ListUsersIndexCapacity_ResponseSyntax) **   <a name="QS-ListUsersIndexCapacity-response-requestId"></a>
The AWS request ID for this operation.
Type: String

 ** [users](#API_ListUsersIndexCapacity_ResponseSyntax) **   <a name="QS-ListUsersIndexCapacity-response-users"></a>
The list of users with their index capacity metrics.
Type: Array of [UserIndexCapacity](API_UserIndexCapacity.md) objects

## Errors
<a name="API_ListUsersIndexCapacity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidRequestException **
You don't have this feature activated for your account. To fix this issue, contact AWS support.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** PreconditionNotMetException **
One or more preconditions aren't met.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_ListUsersIndexCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListUsersIndexCapacity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListUsersIndexCapacity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListUsersIndexCapacity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListUsersIndexCapacity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListUsersIndexCapacity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListUsersIndexCapacity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListUsersIndexCapacity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListUsersIndexCapacity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListUsersIndexCapacity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListUsersIndexCapacity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
