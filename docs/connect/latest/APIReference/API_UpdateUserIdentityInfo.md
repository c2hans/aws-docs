---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateUserIdentityInfo.html
---

# UpdateUserIdentityInfo
<a name="API_UpdateUserIdentityInfo"></a>

Updates the identity information for the specified user.

**Important**
We strongly recommend limiting who has the ability to invoke `UpdateUserIdentityInfo`. Someone with that ability can change the login credentials of other users by changing their email address. This poses a security risk to your organization. They can change the email address of a user to the attacker's email address, and then reset the password through email. For more information, see [Best Practices for Security Profiles](https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-best-practices.html) in the *Connect Customer Administrator Guide*.

## Request Syntax
<a name="API_UpdateUserIdentityInfo_RequestSyntax"></a>

```
POST /users/{{InstanceId}}/{{UserId}}/identity-info HTTP/1.1
Content-type: application/json

{
   "IdentityInfo": {
      "Email": "{{string}}",
      "FirstName": "{{string}}",
      "LastName": "{{string}}",
      "Mobile": "{{string}}",
      "SecondaryEmail": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateUserIdentityInfo_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_UpdateUserIdentityInfo_RequestSyntax) **   <a name="connect-UpdateUserIdentityInfo-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [UserId](#API_UpdateUserIdentityInfo_RequestSyntax) **   <a name="connect-UpdateUserIdentityInfo-request-uri-UserId"></a>
The identifier of the user account.
Required: Yes

## Request Body
<a name="API_UpdateUserIdentityInfo_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [IdentityInfo](#API_UpdateUserIdentityInfo_RequestSyntax) **   <a name="connect-UpdateUserIdentityInfo-request-IdentityInfo"></a>
The identity information for the user.
Type: [UserIdentityInfo](API_UserIdentityInfo.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateUserIdentityInfo_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateUserIdentityInfo_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateUserIdentityInfo_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateUserIdentityInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateUserIdentityInfo)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateUserIdentityInfo)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateUserIdentityInfo)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateUserIdentityInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateUserIdentityInfo)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateUserIdentityInfo)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateUserIdentityInfo)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateUserIdentityInfo)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateUserIdentityInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateUserIdentityInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
