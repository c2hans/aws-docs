---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_MobileDeviceAccessOverride.html
---

# MobileDeviceAccessOverride
<a name="API_MobileDeviceAccessOverride"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

The override object.

## Contents
<a name="API_MobileDeviceAccessOverride_Contents"></a>

 ** DateCreated **   <a name="workmail-Type-MobileDeviceAccessOverride-DateCreated"></a>
The date the override was first created.
Type: Timestamp
Required: No

 ** DateModified **   <a name="workmail-Type-MobileDeviceAccessOverride-DateModified"></a>
The date the override was last modified.
Type: Timestamp
Required: No

 ** Description **   <a name="workmail-Type-MobileDeviceAccessOverride-Description"></a>
A description of the override.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S\s]+`
Required: No

 ** DeviceId **   <a name="workmail-Type-MobileDeviceAccessOverride-DeviceId"></a>
The device to which the override applies.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[A-Za-z0-9]+`
Required: No

 ** Effect **   <a name="workmail-Type-MobileDeviceAccessOverride-Effect"></a>
The effect of the override, `ALLOW` or `DENY`.
Type: String
Valid Values: `ALLOW | DENY`
Required: No

 ** UserId **   <a name="workmail-Type-MobileDeviceAccessOverride-UserId"></a>
The WorkMail user to which the access override applies.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 256.
Required: No

## See Also
<a name="API_MobileDeviceAccessOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/MobileDeviceAccessOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/MobileDeviceAccessOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/MobileDeviceAccessOverride)
