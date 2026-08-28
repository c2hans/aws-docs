---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_CreateMobileDeviceAccessRule.html
---

# CreateMobileDeviceAccessRule
<a name="API_CreateMobileDeviceAccessRule"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Creates a new mobile device access rule for the specified WorkMail organization.

## Request Syntax
<a name="API_CreateMobileDeviceAccessRule_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "DeviceModels": [ "{{string}}" ],
   "DeviceOperatingSystems": [ "{{string}}" ],
   "DeviceTypes": [ "{{string}}" ],
   "DeviceUserAgents": [ "{{string}}" ],
   "Effect": "{{string}}",
   "Name": "{{string}}",
   "NotDeviceModels": [ "{{string}}" ],
   "NotDeviceOperatingSystems": [ "{{string}}" ],
   "NotDeviceTypes": [ "{{string}}" ],
   "NotDeviceUserAgents": [ "{{string}}" ],
   "OrganizationId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateMobileDeviceAccessRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-CreateMobileDeviceAccessRule-request-ClientToken"></a>
The idempotency token for the client request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7e]+`
Required: No

 ** [Description](#API_CreateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-CreateMobileDeviceAccessRule-request-Description"></a>
The rule description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S\s]+`
Required: No

 ** [DeviceModels](#API_CreateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-CreateMobileDeviceAccessRule-request-DeviceModels"></a>
Device models that the rule will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [DeviceOperatingSystems](#API_CreateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-CreateMobileDeviceAccessRule-request-DeviceOperatingSystems"></a>
Device operating systems that the rule will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [DeviceTypes](#API_CreateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-CreateMobileDeviceAccessRule-request-DeviceTypes"></a>
Device types that the rule will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [DeviceUserAgents](#API_CreateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-CreateMobileDeviceAccessRule-request-DeviceUserAgents"></a>
Device user agents that the rule will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [Effect](#API_CreateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-CreateMobileDeviceAccessRule-request-Effect"></a>
The effect of the rule when it matches. Allowed values are `ALLOW` or `DENY`.
Type: String
Valid Values: `ALLOW | DENY`
Required: Yes

 ** [Name](#API_CreateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-CreateMobileDeviceAccessRule-request-Name"></a>
The rule name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\S\s]+`
Required: Yes

 ** [NotDeviceModels](#API_CreateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-CreateMobileDeviceAccessRule-request-NotDeviceModels"></a>
Device models that the rule **will not** match. All other device models will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [NotDeviceOperatingSystems](#API_CreateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-CreateMobileDeviceAccessRule-request-NotDeviceOperatingSystems"></a>
Device operating systems that the rule **will not** match. All other device operating systems will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [NotDeviceTypes](#API_CreateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-CreateMobileDeviceAccessRule-request-NotDeviceTypes"></a>
Device types that the rule **will not** match. All other device types will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [NotDeviceUserAgents](#API_CreateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-CreateMobileDeviceAccessRule-request-NotDeviceUserAgents"></a>
Device user agents that the rule **will not** match. All other device user agents will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** [OrganizationId](#API_CreateMobileDeviceAccessRule_RequestSyntax) **   <a name="workmail-CreateMobileDeviceAccessRule-request-OrganizationId"></a>
The WorkMail organization under which the rule will be created.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

## Response Syntax
<a name="API_CreateMobileDeviceAccessRule_ResponseSyntax"></a>

```
{
   "MobileDeviceAccessRuleId": "string"
}
```

## Response Elements
<a name="API_CreateMobileDeviceAccessRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MobileDeviceAccessRuleId](#API_CreateMobileDeviceAccessRule_ResponseSyntax) **   <a name="workmail-CreateMobileDeviceAccessRule-response-MobileDeviceAccessRuleId"></a>
The identifier for the newly created mobile device access rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

## Errors
<a name="API_CreateMobileDeviceAccessRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## See Also
<a name="API_CreateMobileDeviceAccessRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/CreateMobileDeviceAccessRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/CreateMobileDeviceAccessRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/CreateMobileDeviceAccessRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/CreateMobileDeviceAccessRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/CreateMobileDeviceAccessRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/CreateMobileDeviceAccessRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/CreateMobileDeviceAccessRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/CreateMobileDeviceAccessRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/CreateMobileDeviceAccessRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/CreateMobileDeviceAccessRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
