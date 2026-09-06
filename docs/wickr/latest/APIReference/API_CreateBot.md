---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_CreateBot.html
---

# CreateBot
<a name="API_CreateBot"></a>

Creates a new bot in a specified Wickr network. Bots are automated accounts that can send and receive messages, enabling integration with external systems and automation of tasks.

## Request Syntax
<a name="API_CreateBot_RequestSyntax"></a>

```
POST /networks/{{networkId}}/bots HTTP/1.1
Content-type: application/json

{
   "challenge": "{{string}}",
   "displayName": "{{string}}",
   "groupId": "{{string}}",
   "username": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateBot_RequestParameters"></a>

The request uses the following URI parameters.

 ** [networkId](#API_CreateBot_RequestSyntax) **   <a name="wickr-CreateBot-request-uri-networkId"></a>
The ID of the Wickr network where the bot will be created.
Length Constraints: Fixed length of 8.
Pattern: `[0-9]{8}`
Required: Yes

## Request Body
<a name="API_CreateBot_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [challenge](#API_CreateBot_RequestSyntax) **   <a name="wickr-CreateBot-request-challenge"></a>
The password for the bot account.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** [groupId](#API_CreateBot_RequestSyntax) **   <a name="wickr-CreateBot-request-groupId"></a>
The ID of the security group to which the bot will be assigned.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** [username](#API_CreateBot_RequestSyntax) **   <a name="wickr-CreateBot-request-username"></a>
The username for the bot. This must be unique within the network and follow the network's naming conventions.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** [displayName](#API_CreateBot_RequestSyntax) **   <a name="wickr-CreateBot-request-displayName"></a>
The display name for the bot that will be visible to users in the network.
Type: String
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_CreateBot_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "botId": "string",
   "displayName": "string",
   "groupId": "string",
   "message": "string",
   "networkId": "string",
   "username": "string"
}
```

## Response Elements
<a name="API_CreateBot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [botId](#API_CreateBot_ResponseSyntax) **   <a name="wickr-CreateBot-response-botId"></a>
The unique identifier assigned to the newly created bot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[0-9]+`

 ** [displayName](#API_CreateBot_ResponseSyntax) **   <a name="wickr-CreateBot-response-displayName"></a>
The display name of the newly created bot.
Type: String
Pattern: `[\S\s]*`

 ** [groupId](#API_CreateBot_ResponseSyntax) **   <a name="wickr-CreateBot-response-groupId"></a>
The ID of the security group to which the bot was assigned.
Type: String
Pattern: `[\S\s]*`

 ** [message](#API_CreateBot_ResponseSyntax) **   <a name="wickr-CreateBot-response-message"></a>
A message indicating the result of the bot creation operation.
Type: String
Pattern: `[\S\s]*`

 ** [networkId](#API_CreateBot_ResponseSyntax) **   <a name="wickr-CreateBot-response-networkId"></a>
The ID of the network where the bot was created.
Type: String
Length Constraints: Fixed length of 8.
Pattern: `[0-9]{8}`

 ** [username](#API_CreateBot_ResponseSyntax) **   <a name="wickr-CreateBot-response-username"></a>
The username of the newly created bot.
Type: String
Pattern: `[\S\s]*`

## Errors
<a name="API_CreateBot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [BadRequestError](API_BadRequestError.md)
The request was invalid or malformed. This error occurs when the request parameters do not meet the API requirements, such as invalid field values, missing required parameters, or improperly formatted data.
 ** message **
A detailed message explaining what was wrong with the request and how to correct it.
HTTP Status Code: 400

 [ForbiddenError](API_ForbiddenError.md)
Access to the requested resource is forbidden. This error occurs when the authenticated user does not have the necessary permissions to perform the requested operation, even though they are authenticated.
 ** message **
A message explaining why access was denied and what permissions are required.
HTTP Status Code: 403

 [InternalServerError](API_InternalServerError.md)
An unexpected error occurred on the server while processing the request. This indicates a problem with the Wickr service itself rather than with the request. If this error persists, contact AWS Support.
 ** message **
A message describing the internal server error that occurred.
HTTP Status Code: 500

 [RateLimitError](API_RateLimitError.md)
The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.
 ** message **
A message indicating that the rate limit was exceeded and suggesting when to retry.
HTTP Status Code: 429

 [ResourceNotFoundError](API_ResourceNotFoundError.md)
The requested resource could not be found. This error occurs when you try to access or modify a network, user, bot, security group, or other resource that doesn't exist or has been deleted.
 ** message **
A message identifying which resource was not found.
HTTP Status Code: 404

 [UnauthorizedError](API_UnauthorizedError.md)
The request was not authenticated or the authentication credentials were invalid. This error occurs when the request lacks valid authentication credentials or the credentials have expired.
 ** message **
A message explaining why the authentication failed.
HTTP Status Code: 401

 [ValidationError](API_ValidationError.md)
One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.
 ** message **
A message describing the validation error error that occurred.
 ** reasons **
A list of validation error details, where each item identifies a specific field that failed validation and explains the reason for the failure.
HTTP Status Code: 422

## See Also
<a name="API_CreateBot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wickr-2024-02-01/CreateBot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wickr-2024-02-01/CreateBot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/CreateBot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wickr-2024-02-01/CreateBot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/CreateBot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wickr-2024-02-01/CreateBot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wickr-2024-02-01/CreateBot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wickr-2024-02-01/CreateBot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wickr-2024-02-01/CreateBot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/CreateBot)
