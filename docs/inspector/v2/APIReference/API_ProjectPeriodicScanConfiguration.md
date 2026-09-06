---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ProjectPeriodicScanConfiguration.html
---

# ProjectPeriodicScanConfiguration
<a name="API_ProjectPeriodicScanConfiguration"></a>

Contains the periodic scan configuration settings applied to a specific project.

## Contents
<a name="API_ProjectPeriodicScanConfiguration_Contents"></a>

 ** frequencyExpression **   <a name="inspector2-Type-ProjectPeriodicScanConfiguration-frequencyExpression"></a>
The schedule expression for periodic scans, in cron format, applied to the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ruleSetCategories **   <a name="inspector2-Type-ProjectPeriodicScanConfiguration-ruleSetCategories"></a>
The categories of security rules applied during periodic scans for the project.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `SAST | IAC | SCA`
Required: No

## See Also
<a name="API_ProjectPeriodicScanConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ProjectPeriodicScanConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ProjectPeriodicScanConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ProjectPeriodicScanConfiguration)
