---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutAccountSetting.html
---

# PutAccountSetting
<a name="API_PutAccountSetting"></a>

 Modifies an account setting for your account. You can use this operation to opt in or opt out of features provided through account settings when permitted. Account settings give you control over features that might have backwards-incompatible changes. When Amazon EC2 Auto Scaling introduces such changes, account settings allow you to test and adopt new features. Some account settings are enforced after a specified date. This means that after the enforcement date, you can no longer modify the setting.

## Request Parameters
<a name="API_PutAccountSetting_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Name **
 The name of the account setting to modify. Each account setting has a unique name that identifies the specific feature it controls.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9\-_\/]+`
Required: Yes

 ** Value **
 The value for the account setting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9\-_\/]+`
Required: Yes

## Errors
<a name="API_PutAccountSetting_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_PutAccountSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/PutAccountSetting)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/PutAccountSetting)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/PutAccountSetting)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/PutAccountSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/PutAccountSetting)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/PutAccountSetting)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/PutAccountSetting)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/PutAccountSetting)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/PutAccountSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/PutAccountSetting)
