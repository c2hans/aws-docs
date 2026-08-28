---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeUser.html
---

# DescribeUser
<a name="API_DescribeUser"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Provides information regarding the user.

## Request Syntax
<a name="API_DescribeUser_RequestSyntax"></a>

```
{
   "OrganizationId": "{{string}}",
   "UserId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeUser_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OrganizationId](#API_DescribeUser_RequestSyntax) **   <a name="workmail-DescribeUser-request-OrganizationId"></a>
The identifier for the organization under which the user exists.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

 ** [UserId](#API_DescribeUser_RequestSyntax) **   <a name="workmail-DescribeUser-request-UserId"></a>
The identifier for the user to be described.
The identifier can be the *UserId*, *Username*, or *email*. The following identity formats are available:
+ User ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234
+ Email address: user@domain.tld
+ User name: user

Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9._%+@-]+`
Required: Yes

## Response Syntax
<a name="API_DescribeUser_ResponseSyntax"></a>

```
{
   "City": "string",
   "Company": "string",
   "Country": "string",
   "Department": "string",
   "DisabledDate": number,
   "DisplayName": "string",
   "Email": "string",
   "EnabledDate": number,
   "FirstName": "string",
   "HiddenFromGlobalAddressList": boolean,
   "IdentityProviderIdentityStoreId": "string",
   "IdentityProviderUserId": "string",
   "Initials": "string",
   "JobTitle": "string",
   "LastName": "string",
   "MailboxDeprovisionedDate": number,
   "MailboxProvisionedDate": number,
   "Name": "string",
   "Office": "string",
   "State": "string",
   "Street": "string",
   "Telephone": "string",
   "UserId": "string",
   "UserRole": "string",
   "ZipCode": "string"
}
```

## Response Elements
<a name="API_DescribeUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [City](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-City"></a>
City where the user is located.
Type: String
Length Constraints: Maximum length of 256.

 ** [Company](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-Company"></a>
Company of the user.
Type: String
Length Constraints: Maximum length of 256.

 ** [Country](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-Country"></a>
Country where the user is located.
Type: String
Length Constraints: Maximum length of 256.

 ** [Department](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-Department"></a>
Department of the user.
Type: String
Length Constraints: Maximum length of 256.

 ** [DisabledDate](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-DisabledDate"></a>
The date and time at which the user was disabled for WorkMail usage, in UNIX epoch time format.
Type: Timestamp

 ** [DisplayName](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-DisplayName"></a>
The display name of the user.
Type: String
Length Constraints: Maximum length of 256.

 ** [Email](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-Email"></a>
The email of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Pattern: `[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]+\.[a-zA-Z-]{2,}`

 ** [EnabledDate](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-EnabledDate"></a>
The date and time at which the user was enabled for WorkMailusage, in UNIX epoch time format.
Type: Timestamp

 ** [FirstName](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-FirstName"></a>
First name of the user.
Type: String
Length Constraints: Maximum length of 256.

 ** [HiddenFromGlobalAddressList](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-HiddenFromGlobalAddressList"></a>
If enabled, the user is hidden from the global address list.
Type: Boolean

 ** [IdentityProviderIdentityStoreId](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-IdentityProviderIdentityStoreId"></a>
 Identity Store ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^d-[0-9a-f]{10}$|^[0-9a-f]{8}\\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\\b[0-9a-f]{12}$`

 ** [IdentityProviderUserId](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-IdentityProviderUserId"></a>
User ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$`

 ** [Initials](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-Initials"></a>
Initials of the user.
Type: String
Length Constraints: Maximum length of 256.

 ** [JobTitle](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-JobTitle"></a>
Job title of the user.
Type: String
Length Constraints: Maximum length of 256.

 ** [LastName](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-LastName"></a>
Last name of the user.
Type: String
Length Constraints: Maximum length of 256.

 ** [MailboxDeprovisionedDate](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-MailboxDeprovisionedDate"></a>
The date when the mailbox was removed for the user.
Type: Timestamp

 ** [MailboxProvisionedDate](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-MailboxProvisionedDate"></a>
The date when the mailbox was created for the user.
Type: Timestamp

 ** [Name](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-Name"></a>
The name for the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w\-.]+(@[a-zA-Z0-9.\-]+\.[a-zA-Z0-9-]{2,})?`

 ** [Office](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-Office"></a>
Office where the user is located.
Type: String
Length Constraints: Maximum length of 256.

 ** [State](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-State"></a>
The state of a user: enabled (registered to WorkMail) or disabled (deregistered or never registered to WorkMail).
Type: String
Valid Values: `ENABLED | DISABLED | DELETED`

 ** [Street](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-Street"></a>
Street where the user is located.
Type: String
Length Constraints: Maximum length of 256.

 ** [Telephone](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-Telephone"></a>
User's contact number.
Type: String
Length Constraints: Maximum length of 256.

 ** [UserId](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-UserId"></a>
The identifier for the described user.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 256.

 ** [UserRole](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-UserRole"></a>
In certain cases, other entities are modeled as users. If interoperability is enabled, resources are imported into WorkMail as users. Because different WorkMail organizations rely on different directory types, administrators can distinguish between an unregistered user (account is disabled and has a user role) and the directory administrators. The values are USER, RESOURCE, SYSTEM\_USER, and REMOTE\_USER.
Type: String
Valid Values: `USER | RESOURCE | SYSTEM_USER | REMOTE_USER`

 ** [ZipCode](#API_DescribeUser_ResponseSyntax) **   <a name="workmail-DescribeUser-response-ZipCode"></a>
Zip code of the user.
Type: String
Length Constraints: Maximum length of 256.

## Errors
<a name="API_DescribeUser_Errors"></a>

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

## See Also
<a name="API_DescribeUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/DescribeUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/DescribeUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/DescribeUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/DescribeUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/DescribeUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/DescribeUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/DescribeUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/DescribeUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/DescribeUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/DescribeUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
