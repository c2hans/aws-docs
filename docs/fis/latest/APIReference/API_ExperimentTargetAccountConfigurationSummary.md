---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTargetAccountConfigurationSummary.html
---

# ExperimentTargetAccountConfigurationSummary
<a name="API_ExperimentTargetAccountConfigurationSummary"></a>

Provides a summary of a target account configuration.

## Contents
<a name="API_ExperimentTargetAccountConfigurationSummary_Contents"></a>

 ** accountId **   <a name="fis-Type-ExperimentTargetAccountConfigurationSummary-accountId"></a>
The AWS account ID of the target account.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 48.
Pattern: `[\S]+`
Required: No

 ** description **   <a name="fis-Type-ExperimentTargetAccountConfigurationSummary-description"></a>
The description of the target account.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\S]*`
Required: No

 ** roleArn **   <a name="fis-Type-ExperimentTargetAccountConfigurationSummary-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role for the target account.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\S]+`
Required: No

## See Also
<a name="API_ExperimentTargetAccountConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentTargetAccountConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentTargetAccountConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentTargetAccountConfigurationSummary)
