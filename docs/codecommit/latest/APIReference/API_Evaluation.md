---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_Evaluation.html
---

# Evaluation
<a name="API_Evaluation"></a>

Returns information about the approval rules applied to a pull request and whether conditions have been met.

## Contents
<a name="API_Evaluation_Contents"></a>

 ** approvalRulesNotSatisfied **   <a name="CodeCommit-Type-Evaluation-approvalRulesNotSatisfied"></a>
The names of the approval rules that have not had their conditions met.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** approvalRulesSatisfied **   <a name="CodeCommit-Type-Evaluation-approvalRulesSatisfied"></a>
The names of the approval rules that have had their conditions met.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** approved **   <a name="CodeCommit-Type-Evaluation-approved"></a>
Whether the state of the pull request is approved.
Type: Boolean
Required: No

 ** overridden **   <a name="CodeCommit-Type-Evaluation-overridden"></a>
Whether the approval rule requirements for the pull request have been overridden and no longer need to be met.
Type: Boolean
Required: No

## See Also
<a name="API_Evaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/Evaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/Evaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/Evaluation)
