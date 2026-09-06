---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_EvaluationResultQualifier.html
---

# EvaluationResultQualifier
<a name="API_EvaluationResultQualifier"></a>

Identifies an AWS Config rule that evaluated an AWS resource, and provides the type and ID of the resource that the rule evaluated.

## Contents
<a name="API_EvaluationResultQualifier_Contents"></a>

 ** ConfigRuleName **   <a name="config-Type-EvaluationResultQualifier-ConfigRuleName"></a>
The name of the AWS Config rule that was used in the evaluation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** EvaluationMode **   <a name="config-Type-EvaluationResultQualifier-EvaluationMode"></a>
The mode of an evaluation. The valid values are Detective or Proactive.
Type: String
Valid Values: `DETECTIVE | PROACTIVE`
Required: No

 ** ResourceId **   <a name="config-Type-EvaluationResultQualifier-ResourceId"></a>
The ID of the evaluated AWS resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 768.
Required: No

 ** ResourceType **   <a name="config-Type-EvaluationResultQualifier-ResourceType"></a>
The type of AWS resource that was evaluated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_EvaluationResultQualifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/EvaluationResultQualifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/EvaluationResultQualifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/EvaluationResultQualifier)
