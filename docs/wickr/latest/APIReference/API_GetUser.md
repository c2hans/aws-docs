---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_GetUser.html
---

# GetUser
<a name="API_GetUser"></a>

Retrieves detailed information about a specific user in a Wickr network, including their profile, status, and activity history.

## Request Syntax
<a name="API_GetUser_RequestSyntax"></a>

```
GET /networks/{{networkId}}/users/{{userId}}?endTime={{endTime}}&startTime={{startTime}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endTime](#API_GetUser_RequestSyntax) **   <a name="wickr-GetUser-request-uri-endTime"></a>
The end time for filtering the user's last activity. Only activity before this timestamp will be considered. Time is specified in epoch seconds.

 ** [networkId](#API_GetUser_RequestSyntax) **   <a name="wickr-GetUser-request-uri-networkId"></a>
The ID of the Wickr network containing the user.
Length Constraints: Fixed length of 8.
Pattern: `[0-9]{8}`
Required: Yes

 ** [startTime](#API_GetUser_RequestSyntax) **   <a name="wickr-GetUser-request-uri-startTime"></a>
The start time for filtering the user's last activity. Only activity after this timestamp will be considered. Time is specified in epoch seconds.

 ** [userId](#API_GetUser_RequestSyntax) **   <a name="wickr-GetUser-request-uri-userId"></a>
The unique identifier of the user to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_GetUser_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetUser_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "firstName": "string",
   "isAdmin": boolean,
   "lastActivity": number,
   "lastLogin": number,
   "lastName": "string",
   "securityGroupIds": [ "string" ],
   "status": number,
   "suspended": boolean,
   "userId": "string",
   "username": "string"
}
```

## Response Elements
<a name="API_GetUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [userId](#API_GetUser_ResponseSyntax) **   <a name="wickr-GetUser-response-userId"></a>
The unique identifier of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[0-9]+`

 ** [firstName](#API_GetUser_ResponseSyntax) **   <a name="wickr-GetUser-response-firstName"></a>
The first name of the user.
Type: String
Pattern: `[\S\s]*`

 ** [isAdmin](#API_GetUser_ResponseSyntax) **   <a name="wickr-GetUser-response-isAdmin"></a>
Indicates whether the user has administrator privileges in the network.
Type: Boolean

 ** [lastActivity](#API_GetUser_ResponseSyntax) **   <a name="wickr-GetUser-response-lastActivity"></a>
The timestamp of the user's last activity in the network, specified in epoch seconds.
Type: Integer

 ** [lastLogin](#API_GetUser_ResponseSyntax) **   <a name="wickr-GetUser-response-lastLogin"></a>
The timestamp of the user's last login to the network, specified in epoch seconds.
Type: Integer

 ** [lastName](#API_GetUser_ResponseSyntax) **   <a name="wickr-GetUser-response-lastName"></a>
The last name of the user.
Type: String
Pattern: `[\S\s]*`

 ** [securityGroupIds](#API_GetUser_ResponseSyntax) **   <a name="wickr-GetUser-response-securityGroupIds"></a>
A list of security group IDs to which the user belongs.
Type: Array of strings
Pattern: `[\S]+`

 ** [status](#API_GetUser_ResponseSyntax) **   <a name="wickr-GetUser-response-status"></a>
The current status of the user (1 for pending, 2 for active).
Type: Integer

 ** [suspended](#API_GetUser_ResponseSyntax) **   <a name="wickr-GetUser-response-suspended"></a>
Indicates whether the user is currently suspended.
Type: Boolean

 ** [username](#API_GetUser_ResponseSyntax) **   <a name="wickr-GetUser-response-username"></a>
The email address or username of the user.
Type: String
Pattern: `[\S\s]*`

## Errors
<a name="API_GetUser_Errors"></a>

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
<a name="API_GetUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wickr-2024-02-01/GetUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wickr-2024-02-01/GetUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/GetUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wickr-2024-02-01/GetUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/GetUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wickr-2024-02-01/GetUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wickr-2024-02-01/GetUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wickr-2024-02-01/GetUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wickr-2024-02-01/GetUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/GetUser)
