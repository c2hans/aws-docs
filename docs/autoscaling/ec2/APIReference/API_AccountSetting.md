---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AccountSetting.html
---

# AccountSetting
<a name="API_AccountSetting"></a>

 Describes an account setting for Amazon EC2 Auto Scaling. Account settings control how certain features behave for your account. Some settings can be enforced after a specified date, meaning that after the enforcement date, you can no longer modify the setting.

## Contents
<a name="API_AccountSetting_Contents"></a>

 ** DefaultValue **
 The default value of the account setting before the enforcement date. Valid values are enabled and disabled. This parameter is only returned for settings with hard or flexible enforcement types.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9\-_\/]+`
Required: No

 ** EnforcedValue **
 The value that will be enforced after the enforcement date. Valid values are enabled and disabled. This parameter is only returned for settings with hard or flexible enforcement types.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9\-_\/]+`
Required: No

 ** EnforcementDate **
 The date when the account setting will be enforced. After this date, for settings with hard enforcement type, you can no longer modify the setting value. This parameter is only returned for settings with hard or flexible enforcement types.
Type: Timestamp
Required: No

 ** EnforcementType **
 The type of enforcement for the account setting. Valid values include: `hard` (the setting has a hard enforcement date after which the setting will be enforced and cannot be modified), `flexible` (the setting has a flexible enforcement where you can always modify the setting value), and `none` (the setting has no enforcement and can always be modified).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9\-_\/]+`
Required: No

 ** Name **
 The name of the account setting. Each account setting has a unique name that identifies the specific feature it controls.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9\-_\/]+`
Required: No

 ** Value **
 The current value of the account setting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9\-_\/]+`
Required: No

## See Also
<a name="API_AccountSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/AccountSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/AccountSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/AccountSetting)
