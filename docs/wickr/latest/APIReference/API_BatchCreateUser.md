---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchCreateUser.html
---

# BatchCreateUser
<a name="API_BatchCreateUser"></a>

Creates multiple users in a specified Wickr network. This operation allows you to provision multiple user accounts simultaneously, optionally specifying security groups, and validation requirements for each user.

**Note**
 `codeValidation`, `inviteCode`, and `inviteCodeTtl` are restricted to networks under preview only.

## Request Syntax
<a name="API_BatchCreateUser_RequestSyntax"></a>

```
POST /networks/{{networkId}}/users HTTP/1.1
X-Client-Token: {{clientToken}}
Content-type: application/json

{
   "users": [
      {
         "codeValidation": {{boolean}},
         "firstName": "{{string}}",
         "inviteCode": "{{string}}",
         "inviteCodeTtl": {{number}},
         "lastName": "{{string}}",
         "securityGroupIds": [ "{{string}}" ],
         "username": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchCreateUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_BatchCreateUser_RequestSyntax) **   <a name="wickr-BatchCreateUser-request-clientToken"></a>
A unique identifier for this request to ensure idempotency. If you retry a request with the same client token, the service will return the same response without creating duplicate users.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_:]+`

 ** [networkId](#API_BatchCreateUser_RequestSyntax) **   <a name="wickr-BatchCreateUser-request-uri-networkId"></a>
The ID of the Wickr network where users will be created.
Length Constraints: Fixed length of 8.
Pattern: `[0-9]{8}`
Required: Yes

## Request Body
<a name="API_BatchCreateUser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [users](#API_BatchCreateUser_RequestSyntax) **   <a name="wickr-BatchCreateUser-request-users"></a>
A list of user objects containing the details for each user to be created, including username, name, security groups, and optional invite codes. Maximum 50 users per batch request.
Type: Array of [BatchCreateUserRequestItem](API_BatchCreateUserRequestItem.md) objects
Required: Yes

## Response Syntax
<a name="API_BatchCreateUser_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failed": [
      {
         "field": "string",
         "reason": "string",
         "userId": "string"
      }
   ],
   "message": "string",
   "successful": [
      {
         "cell": "string",
         "challengeFailures": number,
         "codeValidation": boolean,
         "countryCode": "string",
         "firstName": "string",
         "inviteCode": "string",
         "isAdmin": boolean,
         "isInviteExpired": boolean,
         "isUser": boolean,
         "lastName": "string",
         "otpEnabled": boolean,
         "scimId": "string",
         "securityGroups": [ "string" ],
         "status": number,
         "suspended": boolean,
         "type": "string",
         "uname": "string",
         "userId": "string",
         "username": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchCreateUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failed](#API_BatchCreateUser_ResponseSyntax) **   <a name="wickr-BatchCreateUser-response-failed"></a>
A list of user creation attempts that failed, including error details explaining why each user could not be created.
Type: Array of [BatchUserErrorResponseItem](API_BatchUserErrorResponseItem.md) objects

 ** [message](#API_BatchCreateUser_ResponseSyntax) **   <a name="wickr-BatchCreateUser-response-message"></a>
A message indicating the overall result of the batch operation.
Type: String
Pattern: `[\S\s]*`

 ** [successful](#API_BatchCreateUser_ResponseSyntax) **   <a name="wickr-BatchCreateUser-response-successful"></a>
A list of user objects that were successfully created, including their assigned user IDs and invite codes.
Type: Array of [User](API_User.md) objects

## Errors
<a name="API_BatchCreateUser_Errors"></a>

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
<a name="API_BatchCreateUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wickr-2024-02-01/BatchCreateUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wickr-2024-02-01/BatchCreateUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/BatchCreateUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wickr-2024-02-01/BatchCreateUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/BatchCreateUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wickr-2024-02-01/BatchCreateUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wickr-2024-02-01/BatchCreateUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wickr-2024-02-01/BatchCreateUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wickr-2024-02-01/BatchCreateUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/BatchCreateUser)
