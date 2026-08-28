---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UnsatisfiedConnectionConditionsFlowValidationDetails.html
---

# UnsatisfiedConnectionConditionsFlowValidationDetails
<a name="API_agent_UnsatisfiedConnectionConditionsFlowValidationDetails"></a>

Details about unsatisfied conditions for a connection. A condition is unsatisfied if it can never be true, for example two branches of condition node cannot be simultaneously true.

## Contents
<a name="API_agent_UnsatisfiedConnectionConditionsFlowValidationDetails_Contents"></a>

 ** connection **   <a name="bedrock-Type-agent_UnsatisfiedConnectionConditionsFlowValidationDetails-connection"></a>
The name of the connection with unsatisfied conditions.
Type: String
Pattern: `[a-zA-Z]([_]?[0-9a-zA-Z]){1,100}`
Required: Yes

## See Also
<a name="API_agent_UnsatisfiedConnectionConditionsFlowValidationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/UnsatisfiedConnectionConditionsFlowValidationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/UnsatisfiedConnectionConditionsFlowValidationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/UnsatisfiedConnectionConditionsFlowValidationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
