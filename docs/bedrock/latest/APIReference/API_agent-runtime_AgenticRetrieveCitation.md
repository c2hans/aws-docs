---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveCitation.html
---

# AgenticRetrieveCitation
<a name="API_agent-runtime_AgenticRetrieveCitation"></a>

A citation mapping a span of the generated answer to supporting results.

## Contents
<a name="API_agent-runtime_AgenticRetrieveCitation_Contents"></a>

 ** endIndex **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveCitation-endIndex"></a>
Character offset end (exclusive) in the answer text.
Type: Integer
Required: Yes

 ** references **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveCitation-references"></a>
References to results that support this span.
Type: Array of [AgenticRetrieveCitationReference](API_agent-runtime_AgenticRetrieveCitationReference.md) objects
Required: Yes

 ** startIndex **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveCitation-startIndex"></a>
Character offset start in the answer text.
Type: Integer
Required: Yes

## See Also
<a name="API_agent-runtime_AgenticRetrieveCitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveCitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveCitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveCitation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
