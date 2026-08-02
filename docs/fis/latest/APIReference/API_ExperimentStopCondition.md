---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentStopCondition.html
---

# ExperimentStopCondition
<a name="API_ExperimentStopCondition"></a>

Describes the stop condition for an experiment.

## Contents
<a name="API_ExperimentStopCondition_Contents"></a>

 ** source **   <a name="fis-Type-ExperimentStopCondition-source"></a>
The source for the stop condition.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: No

 ** value **   <a name="fis-Type-ExperimentStopCondition-value"></a>
The Amazon Resource Name (ARN) of the CloudWatch alarm, if applicable.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\s\S]+`
Required: No

## See Also
<a name="API_ExperimentStopCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentStopCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentStopCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentStopCondition)
