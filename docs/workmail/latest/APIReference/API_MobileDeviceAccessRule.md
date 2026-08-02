---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_MobileDeviceAccessRule.html
---

# MobileDeviceAccessRule
<a name="API_MobileDeviceAccessRule"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

A rule that controls access to mobile devices for an WorkMail group.

## Contents
<a name="API_MobileDeviceAccessRule_Contents"></a>

 ** DateCreated **   <a name="workmail-Type-MobileDeviceAccessRule-DateCreated"></a>
The date and time at which an access rule was created.
Type: Timestamp
Required: No

 ** DateModified **   <a name="workmail-Type-MobileDeviceAccessRule-DateModified"></a>
The date and time at which an access rule was modified.
Type: Timestamp
Required: No

 ** Description **   <a name="workmail-Type-MobileDeviceAccessRule-Description"></a>
The description of a mobile access rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S\s]+`
Required: No

 ** DeviceModels **   <a name="workmail-Type-MobileDeviceAccessRule-DeviceModels"></a>
Device models that a rule will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** DeviceOperatingSystems **   <a name="workmail-Type-MobileDeviceAccessRule-DeviceOperatingSystems"></a>
Device operating systems that a rule will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** DeviceTypes **   <a name="workmail-Type-MobileDeviceAccessRule-DeviceTypes"></a>
Device types that a rule will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** DeviceUserAgents **   <a name="workmail-Type-MobileDeviceAccessRule-DeviceUserAgents"></a>
Device user agents that a rule will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** Effect **   <a name="workmail-Type-MobileDeviceAccessRule-Effect"></a>
The effect of the rule when it matches. Allowed values are `ALLOW` or `DENY`.
Type: String
Valid Values: `ALLOW | DENY`
Required: No

 ** MobileDeviceAccessRuleId **   <a name="workmail-Type-MobileDeviceAccessRule-MobileDeviceAccessRuleId"></a>
The ID assigned to a mobile access rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** Name **   <a name="workmail-Type-MobileDeviceAccessRule-Name"></a>
The name of a mobile access rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\S\s]+`
Required: No

 ** NotDeviceModels **   <a name="workmail-Type-MobileDeviceAccessRule-NotDeviceModels"></a>
Device models that a rule **will not** match. All other device models will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** NotDeviceOperatingSystems **   <a name="workmail-Type-MobileDeviceAccessRule-NotDeviceOperatingSystems"></a>
Device operating systems that a rule **will not** match. All other device types will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** NotDeviceTypes **   <a name="workmail-Type-MobileDeviceAccessRule-NotDeviceTypes"></a>
Device types that a rule **will not** match. All other device types will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** NotDeviceUserAgents **   <a name="workmail-Type-MobileDeviceAccessRule-NotDeviceUserAgents"></a>
Device user agents that a rule **will not** match. All other device user agents will match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: No

## See Also
<a name="API_MobileDeviceAccessRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/MobileDeviceAccessRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/MobileDeviceAccessRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/MobileDeviceAccessRule)
