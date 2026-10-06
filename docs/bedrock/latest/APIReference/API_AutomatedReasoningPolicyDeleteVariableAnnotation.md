---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_AutomatedReasoningPolicyDeleteVariableAnnotation.html
---

# AutomatedReasoningPolicyDeleteVariableAnnotation
<a name="API_AutomatedReasoningPolicyDeleteVariableAnnotation"></a>

An annotation for removing a variable from an Automated Reasoning policy.

## Contents
<a name="API_AutomatedReasoningPolicyDeleteVariableAnnotation_Contents"></a>

 ** name **   <a name="bedrock-Type-AutomatedReasoningPolicyDeleteVariableAnnotation-name"></a>
The name of the variable to delete from the policy. The variable must not be referenced by any rules.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `\p{L}[\p{L}\p{M}0-9_]*( [\p{L}\p{M}0-9_]+)*`
Required: Yes

## See Also
<a name="API_AutomatedReasoningPolicyDeleteVariableAnnotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyDeleteVariableAnnotation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyDeleteVariableAnnotation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyDeleteVariableAnnotation)
