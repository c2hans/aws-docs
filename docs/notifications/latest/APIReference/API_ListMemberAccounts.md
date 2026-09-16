---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListMemberAccounts.html
---

# ListMemberAccounts
<a name="API_ListMemberAccounts"></a>

Returns a list of member accounts associated with a notification configuration.

## Request Syntax
<a name="API_ListMemberAccounts_RequestSyntax"></a>

```
GET /list-member-accounts?maxResults={{maxResults}}&memberAccount={{memberAccount}}&nextToken={{nextToken}}&notificationConfigurationArn={{notificationConfigurationArn}}&organizationalUnitId={{organizationalUnitId}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMemberAccounts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListMemberAccounts_RequestSyntax) **   <a name="Notifications-ListMemberAccounts-request-uri-maxResults"></a>
The maximum number of results to return in a single call. Valid values are 1-100.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [memberAccount](#API_ListMemberAccounts_RequestSyntax) **   <a name="Notifications-ListMemberAccounts-request-uri-memberAccount"></a>
The member account identifier used to filter the results.
Pattern: `\d{12}`

 ** [nextToken](#API_ListMemberAccounts_RequestSyntax) **   <a name="Notifications-ListMemberAccounts-request-uri-nextToken"></a>
The token for the next page of results. Use the value returned in the previous response.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\w+-/=]+`

 ** [notificationConfigurationArn](#API_ListMemberAccounts_RequestSyntax) **   <a name="Notifications-ListMemberAccounts-request-uri-notificationConfigurationArn"></a>
The Amazon Resource Name (ARN) of the notification configuration used to filter the member accounts.
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`
Required: Yes

 ** [organizationalUnitId](#API_ListMemberAccounts_RequestSyntax) **   <a name="Notifications-ListMemberAccounts-request-uri-organizationalUnitId"></a>
The organizational unit ID used to filter the member accounts.
Pattern: `(Root|r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`

 ** [status](#API_ListMemberAccounts_RequestSyntax) **   <a name="Notifications-ListMemberAccounts-request-uri-status"></a>
The status used to filter the member accounts.
Valid Values: `ACTIVE | PENDING | INACTIVE | CREATING | DELETING`

## Request Body
<a name="API_ListMemberAccounts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMemberAccounts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "memberAccounts": [
      {
         "accountId": "string",
         "notificationConfigurationArn": "string",
         "organizationalUnitId": "string",
         "status": "string",
         "statusReason": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMemberAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [memberAccounts](#API_ListMemberAccounts_ResponseSyntax) **   <a name="Notifications-ListMemberAccounts-response-memberAccounts"></a>
The list of member accounts that match the specified criteria.
Type: Array of [MemberAccount](API_MemberAccount.md) objects

 ** [nextToken](#API_ListMemberAccounts_ResponseSyntax) **   <a name="Notifications-ListMemberAccounts-response-nextToken"></a>
The token to use for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\w+-/=]+`

## Errors
<a name="API_ListMemberAccounts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The ID of the resource that wasn't found.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service being throttled.
HTTP Status Code: 429

 ** ValidationException **
This exception is thrown when the notification event fails validation.
 ** fieldList **
The list of input fields that are invalid.
 ** reason **
The reason why your input is considered invalid.
HTTP Status Code: 400

## See Also
<a name="API_ListMemberAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/ListMemberAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/ListMemberAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/ListMemberAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/ListMemberAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/ListMemberAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/ListMemberAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/ListMemberAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/ListMemberAccounts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/ListMemberAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/ListMemberAccounts)
