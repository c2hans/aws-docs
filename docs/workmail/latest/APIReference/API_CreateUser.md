---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_CreateUser.html
---

# CreateUser
<a name="API_CreateUser"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Creates a user who can be used in WorkMail by calling the [RegisterToWorkMail](API_RegisterToWorkMail.md) operation.

## Request Syntax
<a name="API_CreateUser_RequestSyntax"></a>

```
{
   "DisplayName": "{{string}}",
   "FirstName": "{{string}}",
   "HiddenFromGlobalAddressList": {{boolean}},
   "IdentityProviderUserId": "{{string}}",
   "LastName": "{{string}}",
   "Name": "{{string}}",
   "OrganizationId": "{{string}}",
   "Password": "{{string}}",
   "Role": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateUser_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DisplayName](#API_CreateUser_RequestSyntax) **   <a name="workmail-CreateUser-request-DisplayName"></a>
The display name for the new user.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** [FirstName](#API_CreateUser_RequestSyntax) **   <a name="workmail-CreateUser-request-FirstName"></a>
The first name of the new user.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [HiddenFromGlobalAddressList](#API_CreateUser_RequestSyntax) **   <a name="workmail-CreateUser-request-HiddenFromGlobalAddressList"></a>
If this parameter is enabled, the user will be hidden from the address book.
Type: Boolean
Required: No

 ** [IdentityProviderUserId](#API_CreateUser_RequestSyntax) **   <a name="workmail-CreateUser-request-IdentityProviderUserId"></a>
User ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$`
Required: No

 ** [LastName](#API_CreateUser_RequestSyntax) **   <a name="workmail-CreateUser-request-LastName"></a>
The last name of the new user.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [Name](#API_CreateUser_RequestSyntax) **   <a name="workmail-CreateUser-request-Name"></a>
The name for the new user. WorkMail directory user names have a maximum length of 64. All others have a maximum length of 20.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w\-.]+(@[a-zA-Z0-9.\-]+\.[a-zA-Z0-9-]{2,})?`
Required: Yes

 ** [OrganizationId](#API_CreateUser_RequestSyntax) **   <a name="workmail-CreateUser-request-OrganizationId"></a>
The identifier of the organization for which the user is created.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

 ** [Password](#API_CreateUser_RequestSyntax) **   <a name="workmail-CreateUser-request-Password"></a>
The password for the new user.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [Role](#API_CreateUser_RequestSyntax) **   <a name="workmail-CreateUser-request-Role"></a>
The role of the new user.
You cannot pass *SYSTEM\_USER* or *RESOURCE* role in a single request. When a user role is not selected, the default role of *USER* is selected.
Type: String
Valid Values: `USER | RESOURCE | SYSTEM_USER | REMOTE_USER`
Required: No

## Response Syntax
<a name="API_CreateUser_ResponseSyntax"></a>

```
{
   "UserId": "string"
}
```

## Response Elements
<a name="API_CreateUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UserId](#API_CreateUser_ResponseSyntax) **   <a name="workmail-CreateUser-response-UserId"></a>
The identifier for the new user.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 256.

## Errors
<a name="API_CreateUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectoryServiceAuthenticationFailedException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The directory service doesn't recognize the credentials supplied by WorkMail.
HTTP Status Code: 400

 ** DirectoryUnavailableException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The directory is unavailable. It might be located in another Region or deleted.
HTTP Status Code: 400

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** InvalidPasswordException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The supplied password doesn't match the minimum security constraints, such as length or use of special characters.
HTTP Status Code: 400

 ** NameAvailabilityException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The user, group, or resource name isn't unique in WorkMail.
HTTP Status Code: 400

 ** OrganizationNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
An operation received a valid organization identifier that either doesn't belong or exist in the system.
HTTP Status Code: 400

 ** OrganizationStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The organization must have a valid state to perform certain operations on the organization or its members.
HTTP Status Code: 400

 ** ReservedNameException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
This user, group, or resource name is not allowed in WorkMail.
HTTP Status Code: 400

 ** UnsupportedOperationException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
You can't perform a write operation against a read-only directory.
HTTP Status Code: 400

## See Also
<a name="API_CreateUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/CreateUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/CreateUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/CreateUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/CreateUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/CreateUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/CreateUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/CreateUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/CreateUser)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/CreateUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/CreateUser)
