---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_UpdateUser.html
---

# UpdateUser
<a name="API_UpdateUser"></a>

Updates the properties of an existing user in a Wickr network. This operation allows you to modify the user's name, password, security group membership, and invite code settings.

**Note**
 `codeValidation`, `inviteCode`, and `inviteCodeTtl` are restricted to networks under preview only.

## Request Syntax
<a name="API_UpdateUser_RequestSyntax"></a>

```
PATCH /networks/{{networkId}}/users HTTP/1.1
Content-type: application/json

{
   "userDetails": {
      "codeValidation": {{boolean}},
      "firstName": "{{string}}",
      "inviteCode": "{{string}}",
      "inviteCodeTtl": {{number}},
      "lastName": "{{string}}",
      "securityGroupIds": [ "{{string}}" ],
      "username": "{{string}}"
   },
   "userId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [networkId](#API_UpdateUser_RequestSyntax) **   <a name="wickr-UpdateUser-request-uri-networkId"></a>
The ID of the Wickr network containing the user to update.
Length Constraints: Fixed length of 8.
Pattern: `[0-9]{8}`
Required: Yes

## Request Body
<a name="API_UpdateUser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [userId](#API_UpdateUser_RequestSyntax) **   <a name="wickr-UpdateUser-request-userId"></a>
The unique identifier of the user to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[0-9]+`
Required: Yes

 ** [userDetails](#API_UpdateUser_RequestSyntax) **   <a name="wickr-UpdateUser-request-userDetails"></a>
An object containing the user details to be updated, such as name, password, security groups, and invite code settings.
Type: [UpdateUserDetails](API_UpdateUserDetails.md) object
Required: No

## Response Syntax
<a name="API_UpdateUser_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "codeValidation": boolean,
   "firstName": "string",
   "inviteCode": "string",
   "inviteExpiration": number,
   "lastName": "string",
   "middleName": "string",
   "modified": number,
   "networkId": "string",
   "securityGroupIds": [ "string" ],
   "status": number,
   "suspended": boolean,
   "userId": "string"
}
```

## Response Elements
<a name="API_UpdateUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [networkId](#API_UpdateUser_ResponseSyntax) **   <a name="wickr-UpdateUser-response-networkId"></a>
The ID of the network where the user was updated.
Type: String
Length Constraints: Fixed length of 8.
Pattern: `[0-9]{8}`

 ** [suspended](#API_UpdateUser_ResponseSyntax) **   <a name="wickr-UpdateUser-response-suspended"></a>
Indicates whether the user is suspended after the update.
Type: Boolean

 ** [userId](#API_UpdateUser_ResponseSyntax) **   <a name="wickr-UpdateUser-response-userId"></a>
The unique identifier of the updated user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[0-9]+`

 ** [codeValidation](#API_UpdateUser_ResponseSyntax) **   <a name="wickr-UpdateUser-response-codeValidation"></a>
Indicates whether the user can be verified through a custom invite code.
Type: Boolean

 ** [firstName](#API_UpdateUser_ResponseSyntax) **   <a name="wickr-UpdateUser-response-firstName"></a>
The updated first name of the user.
Type: String
Pattern: `[\S\s]*`

 ** [inviteCode](#API_UpdateUser_ResponseSyntax) **   <a name="wickr-UpdateUser-response-inviteCode"></a>
The updated invite code for the user, if applicable.
Type: String
Pattern: `[\S\s]*`

 ** [inviteExpiration](#API_UpdateUser_ResponseSyntax) **   <a name="wickr-UpdateUser-response-inviteExpiration"></a>
The expiration time of the user's invite code, specified in epoch seconds.
Type: Integer

 ** [lastName](#API_UpdateUser_ResponseSyntax) **   <a name="wickr-UpdateUser-response-lastName"></a>
The updated last name of the user.
Type: String
Pattern: `[\S\s]*`

 ** [middleName](#API_UpdateUser_ResponseSyntax) **   <a name="wickr-UpdateUser-response-middleName"></a>
The middle name of the user (currently not used).
Type: String
Pattern: `[\S\s]*`

 ** [modified](#API_UpdateUser_ResponseSyntax) **   <a name="wickr-UpdateUser-response-modified"></a>
The timestamp when the user was last modified, specified in epoch seconds.
Type: Integer

 ** [securityGroupIds](#API_UpdateUser_ResponseSyntax) **   <a name="wickr-UpdateUser-response-securityGroupIds"></a>
The list of security group IDs to which the user now belongs after the update.
Type: Array of strings
Pattern: `[\S]+`

 ** [status](#API_UpdateUser_ResponseSyntax) **   <a name="wickr-UpdateUser-response-status"></a>
The user's status after the update.
Type: Integer

## Errors
<a name="API_UpdateUser_Errors"></a>

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
<a name="API_UpdateUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wickr-2024-02-01/UpdateUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wickr-2024-02-01/UpdateUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/UpdateUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wickr-2024-02-01/UpdateUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/UpdateUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wickr-2024-02-01/UpdateUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wickr-2024-02-01/UpdateUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wickr-2024-02-01/UpdateUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wickr-2024-02-01/UpdateUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/UpdateUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
