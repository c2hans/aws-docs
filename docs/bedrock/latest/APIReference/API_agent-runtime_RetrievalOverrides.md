---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrievalOverrides.html
---

# RetrievalOverrides
<a name="API_agent-runtime_RetrievalOverrides"></a>

Overrides for retrieval behavior.

## Contents
<a name="API_agent-runtime_RetrievalOverrides_Contents"></a>

 ** filter **   <a name="bedrock-Type-agent-runtime_RetrievalOverrides-filter"></a>
A filter to apply to the retrieval results.
Type: [RetrievalFilter](API_agent-runtime_RetrievalFilter.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** maxNumberOfResults **   <a name="bedrock-Type-agent-runtime_RetrievalOverrides-maxNumberOfResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_agent-runtime_RetrievalOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/RetrievalOverrides)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/RetrievalOverrides)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/RetrievalOverrides)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
