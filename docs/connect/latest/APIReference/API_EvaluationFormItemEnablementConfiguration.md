---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormItemEnablementConfiguration.html
---

# EvaluationFormItemEnablementConfiguration
<a name="API_EvaluationFormItemEnablementConfiguration"></a>

An item enablement configuration.

## Contents
<a name="API_EvaluationFormItemEnablementConfiguration_Contents"></a>

 ** Action **   <a name="connect-Type-EvaluationFormItemEnablementConfiguration-Action"></a>
An enablement action that if condition is satisfied.
Type: String
Valid Values: `DISABLE | ENABLE`
Required: Yes

 ** Condition **   <a name="connect-Type-EvaluationFormItemEnablementConfiguration-Condition"></a>
A condition for item enablement configuration.
Type: [EvaluationFormItemEnablementCondition](API_EvaluationFormItemEnablementCondition.md) object
Required: Yes

 ** DefaultAction **   <a name="connect-Type-EvaluationFormItemEnablementConfiguration-DefaultAction"></a>
An enablement action that if condition is not satisfied.
Type: String
Valid Values: `DISABLE | ENABLE`
Required: No

## See Also
<a name="API_EvaluationFormItemEnablementConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormItemEnablementConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormItemEnablementConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormItemEnablementConfiguration)
