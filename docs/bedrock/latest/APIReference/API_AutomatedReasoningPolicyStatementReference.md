---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_AutomatedReasoningPolicyStatementReference.html
---

# AutomatedReasoningPolicyStatementReference
<a name="API_AutomatedReasoningPolicyStatementReference"></a>

References a specific atomic statement within a source document, used to link policy elements back to their source material.

## Contents
<a name="API_AutomatedReasoningPolicyStatementReference_Contents"></a>

 ** documentId **   <a name="bedrock-Type-AutomatedReasoningPolicyStatementReference-documentId"></a>
The unique identifier of the document containing the referenced statement.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8.
Pattern: `[a-zA-Z0-9]*`
Required: Yes

 ** statementId **   <a name="bedrock-Type-AutomatedReasoningPolicyStatementReference-statementId"></a>
The unique identifier of the specific atomic statement being referenced.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8.
Pattern: `[a-zA-Z0-9]*`
Required: Yes

## See Also
<a name="API_AutomatedReasoningPolicyStatementReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyStatementReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyStatementReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyStatementReference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
