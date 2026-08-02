---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AvailableUpgrade.html
---

# AvailableUpgrade
<a name="API_AvailableUpgrade"></a>

Contains information about an available upgrade for a SageMaker Partner AI App, including the version number and release notes.

## Contents
<a name="API_AvailableUpgrade_Contents"></a>

 ** ReleaseNotes **   <a name="sagemaker-Type-AvailableUpgrade-ReleaseNotes"></a>
A list of release notes describing the changes and improvements included in the available upgrade version.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** Version **   <a name="sagemaker-Type-AvailableUpgrade-Version"></a>
The semantic version number of the available upgrade for the SageMaker Partner AI App.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `\d+\.\d+`
Required: No

## See Also
<a name="API_AvailableUpgrade_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AvailableUpgrade)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AvailableUpgrade)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AvailableUpgrade)
