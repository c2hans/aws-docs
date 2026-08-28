---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_UpdateUser.html
---

# UpdateUser
<a name="API_UpdateUser"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Updates data for the user. To have the latest information, it must be preceded by a [DescribeUser](API_DescribeUser.md) call. The dataset in the request should be the one expected when performing another `DescribeUser` call.

## Request Syntax
<a name="API_UpdateUser_RequestSyntax"></a>

```
{
   "City": "{{string}}",
   "Company": "{{string}}",
   "Country": "{{string}}",
   "Department": "{{string}}",
   "DisplayName": "{{string}}",
   "FirstName": "{{string}}",
   "HiddenFromGlobalAddressList": {{boolean}},
   "IdentityProviderUserId": "{{string}}",
   "Initials": "{{string}}",
   "JobTitle": "{{string}}",
   "LastName": "{{string}}",
   "Office": "{{string}}",
   "OrganizationId": "{{string}}",
   "Role": "{{string}}",
   "Street": "{{string}}",
   "Telephone": "{{string}}",
   "UserId": "{{string}}",
   "ZipCode": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateUser_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [City](#API_UpdateUser_RequestSyntax) **   <a name="workmail-UpdateUser-request-City"></a>
Updates the user's city.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [Company](#API_UpdateUser_RequestSyntax) **   <a name="workmail-UpdateUser-request-Company"></a>
Updates the user's company.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [Country](#API_UpdateUser_RequestSyntax) **   <a name="workmail-UpdateUser-request-Country"></a>
Updates the user's country.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [Department](#API_UpdateUser_RequestSyntax) **   <a name="workmail-UpdateUser-request-Department"></a>
Updates the user's department.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [DisplayName](#API_UpdateUser_RequestSyntax) **   <a name="workmail-UpdateUser-request-DisplayName"></a>
Updates the display name of the user.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [FirstName](#API_UpdateUser_RequestSyntax) **   <a name="workmail-UpdateUser-request-FirstName"></a>
Updates the user's first name.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [HiddenFromGlobalAddressList](#API_UpdateUser_RequestSyntax) **   <a name="workmail-UpdateUser-request-HiddenFromGlobalAddressList"></a>
If enabled, the user is hidden from the global address list.
Type: Boolean
Required: No

 ** [IdentityProviderUserId](#API_UpdateUser_RequestSyntax) **   <a name="workmail-UpdateUser-request-IdentityProviderUserId"></a>
User ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 47.
Pattern: `^$|^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$`
Required: No

 ** [Initials](#API_UpdateUser_RequestSyntax) **   <a name="workmail-UpdateUser-request-Initials"></a>
Updates the user's initials.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [JobTitle](#API_UpdateUser_RequestSyntax) **   <a name="workmail-UpdateUser-request-JobTitle"></a>
Updates the user's job title.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [LastName](#API_UpdateUser_RequestSyntax) **   <a name="workmail-UpdateUser-request-LastName"></a>
Updates the user's last name.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [Office](#API_UpdateUser_RequestSyntax) **   <a name="workmail-UpdateUser-request-Office"></a>
Updates the user's office.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [OrganizationId](#API_UpdateUser_RequestSyntax) **   <a name="workmail-UpdateUser-request-OrganizationId"></a>
The identifier for the organization under which the user exists.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

 ** [Role](#API_UpdateUser_RequestSyntax) **   <a name="workmail-UpdateUser-request-Role"></a>
Updates the user role.
You cannot pass *SYSTEM\_USER* or *RESOURCE*.
Type: String
Valid Values: `USER | RESOURCE | SYSTEM_USER | REMOTE_USER`
Required: No

 ** [Street](#API_UpdateUser_RequestSyntax) **   <a name="workmail-UpdateUser-request-Street"></a>
Updates the user's street address.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [Telephone](#API_UpdateUser_RequestSyntax) **   <a name="workmail-UpdateUser-request-Telephone"></a>
Updates the user's contact details.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [UserId](#API_UpdateUser_RequestSyntax) **   <a name="workmail-UpdateUser-request-UserId"></a>
The identifier for the user to be updated.
The identifier can be the *UserId*, *Username*, or *email*. The following identity formats are available:
+ User ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234
+ Email address: user@domain.tld
+ User name: user
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9._%+@-]+`
Required: Yes

 ** [ZipCode](#API_UpdateUser_RequestSyntax) **   <a name="workmail-UpdateUser-request-ZipCode"></a>
Updates the user's zip code.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## Response Elements
<a name="API_UpdateUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectoryServiceAuthenticationFailedException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The directory service doesn't recognize the credentials supplied by WorkMail.
HTTP Status Code: 400

 ** DirectoryUnavailableException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The directory is unavailable. It might be located in another Region or deleted.
HTTP Status Code: 400

 ** EntityNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The identifier supplied for the user, group, or resource does not exist in your organization.
HTTP Status Code: 400

 ** EntityStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
You are performing an operation on a user, group, or resource that isn't in the expected state, such as trying to delete an active user.
HTTP Status Code: 400

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** OrganizationNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
An operation received a valid organization identifier that either doesn't belong or exist in the system.
HTTP Status Code: 400

 ** OrganizationStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The organization must have a valid state to perform certain operations on the organization or its members.
HTTP Status Code: 400

 ** UnsupportedOperationException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
You can't perform a write operation against a read-only directory.
HTTP Status Code: 400

## See Also
<a name="API_UpdateUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/UpdateUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/UpdateUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/UpdateUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/UpdateUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/UpdateUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/UpdateUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/UpdateUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/UpdateUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/UpdateUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/UpdateUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
