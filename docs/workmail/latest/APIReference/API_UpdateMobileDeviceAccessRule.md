---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_UpdateMobileDeviceAccessRule.html
---

# UpdateMobileDeviceAccessRule
<a name="API_UpdateMobileDeviceAccessRule"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Updates a mobile device access rule for the specified WorkMail organization.

## Request Syntax
<a name="API_UpdateMobileDeviceAccessRule_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "DeviceModels": [ "{{string}}" ],
   "DeviceOperatingSystems": [ "{{string}}" ],
   "DeviceTypes": [ "{{string}}" ],
   "DeviceUserAgents": [ "{{string}}" ],
   "Effect": "{{string}}",
   "MobileDeviceAccessRuleId": "{{string}}",
   "Name": "{{string}}",
   "NotDeviceModels": [ "{{string}}" ],
   "NotDeviceOperatingSystems": [ "{{string}}" ],
   "NotDeviceTypes": [ "{{string}}" ],
   "NotDeviceUserAgents": [ "{{string}}" ],
   "OrganizationId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateMobileDeviceAccessRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-UpdateMobileDeviceAccessRule-request-Description"></a>
The updated rule description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S\s]+`
Required: No

 ** [DeviceModels](#API_UpdateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-UpdateMobileDeviceAccessRule-request-DeviceModels"></a>
Device models that the updated rule will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [DeviceOperatingSystems](#API_UpdateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-UpdateMobileDeviceAccessRule-request-DeviceOperatingSystems"></a>
Device operating systems that the updated rule will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [DeviceTypes](#API_UpdateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-UpdateMobileDeviceAccessRule-request-DeviceTypes"></a>
Device types that the updated rule will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [DeviceUserAgents](#API_UpdateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-UpdateMobileDeviceAccessRule-request-DeviceUserAgents"></a>
User agents that the updated rule will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [Effect](#API_UpdateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-UpdateMobileDeviceAccessRule-request-Effect"></a>
The effect of the rule when it matches. Allowed values are `ALLOW` or `DENY`.
Type: String
Valid Values: `ALLOW | DENY`
Required: Yes

 ** [MobileDeviceAccessRuleId](#API_UpdateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-UpdateMobileDeviceAccessRule-request-MobileDeviceAccessRuleId"></a>
The identifier of the rule to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [Name](#API_UpdateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-UpdateMobileDeviceAccessRule-request-Name"></a>
The updated rule name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\S\s]+`
Required: Yes

 ** [NotDeviceModels](#API_UpdateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-UpdateMobileDeviceAccessRule-request-NotDeviceModels"></a>
Device models that the updated rule **will not** match. All other device models will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [NotDeviceOperatingSystems](#API_UpdateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-UpdateMobileDeviceAccessRule-request-NotDeviceOperatingSystems"></a>
Device operating systems that the updated rule **will not** match. All other device operating systems will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [NotDeviceTypes](#API_UpdateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-UpdateMobileDeviceAccessRule-request-NotDeviceTypes"></a>
Device types that the updated rule **will not** match. All other device types will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [NotDeviceUserAgents](#API_UpdateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-UpdateMobileDeviceAccessRule-request-NotDeviceUserAgents"></a>
User agents that the updated rule **will not** match. All other user agents will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [OrganizationId](#API_UpdateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-UpdateMobileDeviceAccessRule-request-OrganizationId"></a>
The WorkMail organization under which the rule will be updated.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

## Response Elements
<a name="API_UpdateMobileDeviceAccessRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateMobileDeviceAccessRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_UpdateMobileDeviceAccessRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/UpdateMobileDeviceAccessRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/UpdateMobileDeviceAccessRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/UpdateMobileDeviceAccessRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/UpdateMobileDeviceAccessRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/UpdateMobileDeviceAccessRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/UpdateMobileDeviceAccessRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/UpdateMobileDeviceAccessRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/UpdateMobileDeviceAccessRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/UpdateMobileDeviceAccessRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/UpdateMobileDeviceAccessRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
