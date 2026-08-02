---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_UpdateBot.html
---

# UpdateBot
<a name="API_UpdateBot"></a>

Updates the properties of an existing bot in a Wickr network. This operation allows you to modify the bot's display name, security group, password, or suspension status.

## Request Syntax
<a name="API_UpdateBot_RequestSyntax"></a>

```
PATCH /networks/{{networkId}}/bots/{{botId}} HTTP/1.1
Content-type: application/json

{
   "challenge": "{{string}}",
   "displayName": "{{string}}",
   "groupId": "{{string}}",
   "suspend": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateBot_RequestParameters"></a>

The request uses the following URI parameters.

 ** [botId](#API_UpdateBot_RequestSyntax) **   <a name="wickr-UpdateBot-request-uri-botId"></a>
The unique identifier of the bot to update.
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[0-9]+`
Required: Yes

 ** [networkId](#API_UpdateBot_RequestSyntax) **   <a name="wickr-UpdateBot-request-uri-networkId"></a>
The ID of the Wickr network containing the bot to update.
Length Constraints: Fixed length of 8.
Pattern: `[0-9]{8}`
Required: Yes

## Request Body
<a name="API_UpdateBot_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [challenge](#API_UpdateBot_RequestSyntax) **   <a name="wickr-UpdateBot-request-challenge"></a>
The new password for the bot account.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** [displayName](#API_UpdateBot_RequestSyntax) **   <a name="wickr-UpdateBot-request-displayName"></a>
The new display name for the bot.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** [groupId](#API_UpdateBot_RequestSyntax) **   <a name="wickr-UpdateBot-request-groupId"></a>
The ID of the new security group to assign the bot to.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** [suspend](#API_UpdateBot_RequestSyntax) **   <a name="wickr-UpdateBot-request-suspend"></a>
Set to true to suspend the bot or false to unsuspend it. Omit this field for standard updates that don't affect suspension status.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateBot_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "message": "string"
}
```

## Response Elements
<a name="API_UpdateBot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [message](#API_UpdateBot_ResponseSyntax) **   <a name="wickr-UpdateBot-response-message"></a>
A message indicating the result of the bot update operation.
Type: String
Pattern: `[\S\s]*`

## Errors
<a name="API_UpdateBot_Errors"></a>

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
<a name="API_UpdateBot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wickr-2024-02-01/UpdateBot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wickr-2024-02-01/UpdateBot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/UpdateBot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wickr-2024-02-01/UpdateBot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/UpdateBot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wickr-2024-02-01/UpdateBot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wickr-2024-02-01/UpdateBot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wickr-2024-02-01/UpdateBot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wickr-2024-02-01/UpdateBot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/UpdateBot)
