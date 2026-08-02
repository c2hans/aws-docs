---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_PutAccessControlRule.html
---

# PutAccessControlRule
<a name="API_PutAccessControlRule"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Adds a new access control rule for the specified organization. The rule allows or denies access to the organization for the specified IPv4 addresses, access protocol actions, user IDs and impersonation IDs. Adding a new rule with the same name as an existing rule replaces the older rule.

## Request Syntax
<a name="API_PutAccessControlRule_RequestSyntax"></a>

```
{
   "Actions": [ "{{string}}" ],
   "Description": "{{string}}",
   "Effect": "{{string}}",
   "ImpersonationRoleIds": [ "{{string}}" ],
   "IpRanges": [ "{{string}}" ],
   "Name": "{{string}}",
   "NotActions": [ "{{string}}" ],
   "NotImpersonationRoleIds": [ "{{string}}" ],
   "NotIpRanges": [ "{{string}}" ],
   "NotUserIds": [ "{{string}}" ],
   "OrganizationId": "{{string}}",
   "UserIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_PutAccessControlRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Actions](#API_PutAccessControlRule_RequestSyntax) **   <a name="workmail-PutAccessControlRule-request-Actions"></a>
Access protocol actions to include in the rule. Valid values include `ActiveSync`, `AutoDiscover`, `EWS`, `IMAP`, `SMTP`, `WindowsOutlook`, and `WebMail`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z]+`
Required: No

 ** [Description](#API_PutAccessControlRule_RequestSyntax) **   <a name="workmail-PutAccessControlRule-request-Description"></a>
The rule description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\u00FF]+`
Required: Yes

 ** [Effect](#API_PutAccessControlRule_RequestSyntax) **   <a name="workmail-PutAccessControlRule-request-Effect"></a>
The rule effect.
Type: String
Valid Values: `ALLOW | DENY`
Required: Yes

 ** [ImpersonationRoleIds](#API_PutAccessControlRule_RequestSyntax) **   <a name="workmail-PutAccessControlRule-request-ImpersonationRoleIds"></a>
Impersonation role IDs to include in the rule.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** [IpRanges](#API_PutAccessControlRule_RequestSyntax) **   <a name="workmail-PutAccessControlRule-request-IpRanges"></a>
IPv4 CIDR ranges to include in the rule.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1024 items.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])/([0-9]|[12][0-9]|3[0-2])$`
Required: No

 ** [Name](#API_PutAccessControlRule_RequestSyntax) **   <a name="workmail-PutAccessControlRule-request-Name"></a>
The rule name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [NotActions](#API_PutAccessControlRule_RequestSyntax) **   <a name="workmail-PutAccessControlRule-request-NotActions"></a>
Access protocol actions to exclude from the rule. Valid values include `ActiveSync`, `AutoDiscover`, `EWS`, `IMAP`, `SMTP`, `WindowsOutlook`, and `WebMail`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z]+`
Required: No

 ** [NotImpersonationRoleIds](#API_PutAccessControlRule_RequestSyntax) **   <a name="workmail-PutAccessControlRule-request-NotImpersonationRoleIds"></a>
Impersonation role IDs to exclude from the rule.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** [NotIpRanges](#API_PutAccessControlRule_RequestSyntax) **   <a name="workmail-PutAccessControlRule-request-NotIpRanges"></a>
IPv4 CIDR ranges to exclude from the rule.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1024 items.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])/([0-9]|[12][0-9]|3[0-2])$`
Required: No

 ** [NotUserIds](#API_PutAccessControlRule_RequestSyntax) **   <a name="workmail-PutAccessControlRule-request-NotUserIds"></a>
User IDs to exclude from the rule.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 12. Maximum length of 256.
Required: No

 ** [OrganizationId](#API_PutAccessControlRule_RequestSyntax) **   <a name="workmail-PutAccessControlRule-request-OrganizationId"></a>
The identifier of the organization.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

 ** [UserIds](#API_PutAccessControlRule_RequestSyntax) **   <a name="workmail-PutAccessControlRule-request-UserIds"></a>
User IDs to include in the rule.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 12. Maximum length of 256.
Required: No

## Response Elements
<a name="API_PutAccessControlRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutAccessControlRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The identifier supplied for the user, group, or resource does not exist in your organization.
HTTP Status Code: 400

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** LimitExceededException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The request exceeds the limit of the resource.
HTTP Status Code: 400

 ** OrganizationNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
An operation received a valid organization identifier that either doesn't belong or exist in the system.
HTTP Status Code: 400

 ** OrganizationStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The organization must have a valid state to perform certain operations on the organization or its members.
HTTP Status Code: 400

 ** ResourceNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_PutAccessControlRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/PutAccessControlRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/PutAccessControlRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/PutAccessControlRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/PutAccessControlRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/PutAccessControlRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/PutAccessControlRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/PutAccessControlRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/PutAccessControlRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/PutAccessControlRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/PutAccessControlRule)
