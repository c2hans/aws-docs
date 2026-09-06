---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AgentTurnResult.html
---

# AgentTurnResult
<a name="API_AgentTurnResult"></a>

The information about the agent turn in a test set execution.

## Contents
<a name="API_AgentTurnResult_Contents"></a>

 ** expectedAgentPrompt **   <a name="lexv2-Type-AgentTurnResult-expectedAgentPrompt"></a>
The expected agent prompt for the agent turn in a test set execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** actualAgentPrompt **   <a name="lexv2-Type-AgentTurnResult-actualAgentPrompt"></a>
The actual agent prompt for the agent turn in a test set execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** actualElicitedSlot **   <a name="lexv2-Type-AgentTurnResult-actualElicitedSlot"></a>
The actual elicited slot for the agent turn in a test set execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_.-]?)+$`
Required: No

 ** actualIntent **   <a name="lexv2-Type-AgentTurnResult-actualIntent"></a>
The actual intent for the agent turn in a test set execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

 ** errorDetails **   <a name="lexv2-Type-AgentTurnResult-errorDetails"></a>
Details about an error in an execution of a test set.
Type: [ExecutionErrorDetails](API_ExecutionErrorDetails.md) object
Required: No

## See Also
<a name="API_AgentTurnResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AgentTurnResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AgentTurnResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AgentTurnResult)
