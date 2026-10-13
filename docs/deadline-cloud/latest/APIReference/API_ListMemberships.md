---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListMemberships.html
---

# ListMemberships
<a name="API_ListMemberships"></a>

Lists the Deadline Cloud resource memberships associated with a specified IAM Identity Center principal, optionally filtered by the requested resource types.

## Request Syntax
<a name="API_ListMemberships_RequestSyntax"></a>

```
GET /2023-10-12/memberships?identityCenterRegion={{identityCenterRegion}}&identityStoreId={{identityStoreId}}&maxResults={{maxResults}}&nextToken={{nextToken}}&principalId={{principalId}}&resourceTypes={{resourceTypes}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMemberships_RequestParameters"></a>

The request uses the following URI parameters.

 ** [identityCenterRegion](#API_ListMemberships_RequestSyntax) **   <a name="deadlinecloud-ListMemberships-request-uri-identityCenterRegion"></a>
The Region of the IAM Identity Center instance. If not provided, the service defaults to the AWS Region in which you make the request.
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `[a-z0-9-]+`

 ** [identityStoreId](#API_ListMemberships_RequestSyntax) **   <a name="deadlinecloud-ListMemberships-request-uri-identityStoreId"></a>
The identity store ID that contains the principal. This parameter is required for callers that do not use a monitor session.
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [maxResults](#API_ListMemberships_RequestSyntax) **   <a name="deadlinecloud-ListMemberships-request-uri-maxResults"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListMemberships_RequestSyntax) **   <a name="deadlinecloud-ListMemberships-request-uri-nextToken"></a>
The token for the next set of results, or `null` to start from the beginning.
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [principalId](#API_ListMemberships_RequestSyntax) **   <a name="deadlinecloud-ListMemberships-request-uri-principalId"></a>
The ID of the IAM Identity Center principal whose Deadline Cloud resource memberships you want to list.
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: Yes

 ** [resourceTypes](#API_ListMemberships_RequestSyntax) **   <a name="deadlinecloud-ListMemberships-request-uri-resourceTypes"></a>
The resource types to include when listing the principal's memberships. If not specified, memberships for all supported resource types are returned.
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `FARM | QUEUE | FLEET | JOB`

## Request Body
<a name="API_ListMemberships_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMemberships_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "memberships": [
      { ... }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMemberships_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [memberships](#API_ListMemberships_ResponseSyntax) **   <a name="deadlinecloud-ListMemberships-response-memberships"></a>
The memberships associated with the specified principal.
Type: Array of [MembershipSummary](API_MembershipSummary.md) objects

 ** [nextToken](#API_ListMemberships_ResponseSyntax) **   <a name="deadlinecloud-ListMemberships-response-nextToken"></a>
If Deadline Cloud returns `nextToken`, then there are more results available. The value of `nextToken` is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then `nextToken` is set to `null`. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 `ValidationException` error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

## Errors
<a name="API_ListMemberships_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
 ** context **
Information about the resources in use when the exception was thrown.
HTTP Status Code: 403

 ** InternalServerErrorException **
Deadline Cloud can't process your request right now. Try again later.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** context **
Information about the resources in use when the exception was thrown.
 ** resourceId **
The identifier of the resource that couldn't be found.
 ** resourceType **
The type of the resource that couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a request rate quota.
 ** context **
Information about the resources in use when the exception was thrown.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service that is being throttled.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** context **
Information about the resources in use when the exception was thrown.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListMemberships_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/ListMemberships)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/ListMemberships)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ListMemberships)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/ListMemberships)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ListMemberships)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/ListMemberships)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/ListMemberships)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/ListMemberships)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/ListMemberships)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ListMemberships)
