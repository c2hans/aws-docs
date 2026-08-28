---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateUser.html
---

# CreateUser
<a name="API_CreateUser"></a>

Creates a new user in the user pool.

## Request Syntax
<a name="API_CreateUser_RequestSyntax"></a>

```
{
   "AuthenticationType": "{{string}}",
   "FirstName": "{{string}}",
   "LastName": "{{string}}",
   "MessageAction": "{{string}}",
   "UserName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateUser_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AuthenticationType](#API_CreateUser_RequestSyntax) **   <a name="WorkSpacesApplications-CreateUser-request-AuthenticationType"></a>
The authentication type for the user. You must specify USERPOOL.
Type: String
Valid Values: `API | SAML | USERPOOL | AWS_AD`
Required: Yes

 ** [FirstName](#API_CreateUser_RequestSyntax) **   <a name="WorkSpacesApplications-CreateUser-request-FirstName"></a>
The first name, or given name, of the user.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[A-Za-z0-9_\-\s]+$`
Required: No

 ** [LastName](#API_CreateUser_RequestSyntax) **   <a name="WorkSpacesApplications-CreateUser-request-LastName"></a>
The last name, or surname, of the user.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[A-Za-z0-9_\-\s]+$`
Required: No

 ** [MessageAction](#API_CreateUser_RequestSyntax) **   <a name="WorkSpacesApplications-CreateUser-request-MessageAction"></a>
The action to take for the welcome email that is sent to a user after the user is created in the user pool. If you specify SUPPRESS, no email is sent. If you specify RESEND, do not specify the first name or last name of the user. If the value is null, the email is sent.
The temporary password in the welcome email is valid for only 7 days. If users don’t set their passwords within 7 days, you must send them a new welcome email.
Type: String
Valid Values: `SUPPRESS | RESEND`
Required: No

 ** [UserName](#API_CreateUser_RequestSyntax) **   <a name="WorkSpacesApplications-CreateUser-request-UserName"></a>
The email address of the user.
Users' email addresses are case-sensitive. During login, if they specify an email address that doesn't use the same capitalization as the email address specified when their user pool account was created, a "user does not exist" error message displays.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

## Response Elements
<a name="API_CreateUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidAccountStatusException **
The resource cannot be created because your AWS account is suspended. For assistance, contact AWS Support.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidParameterCombinationException **
Indicates an incorrect combination of parameters, or a missing parameter.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** LimitExceededException **
The requested limit exceeds the permitted limit for an account.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The specified resource already exists.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/CreateUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/CreateUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/CreateUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/CreateUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/CreateUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/CreateUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/CreateUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/CreateUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/CreateUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/CreateUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
