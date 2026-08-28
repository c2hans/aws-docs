---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_SemanticChunkingConfiguration.html
---

# SemanticChunkingConfiguration
<a name="API_amazon-q-connect_SemanticChunkingConfiguration"></a>

Settings for semantic document chunking for a data source. Semantic chunking splits a document into smaller documents based on groups of similar content derived from the text with natural language processing.

## Contents
<a name="API_amazon-q-connect_SemanticChunkingConfiguration_Contents"></a>

 ** breakpointPercentileThreshold **   <a name="connect-Type-amazon-q-connect_SemanticChunkingConfiguration-breakpointPercentileThreshold"></a>
The dissimilarity threshold for splitting chunks.
Type: Integer
Valid Range: Minimum value of 50. Maximum value of 99.
Required: Yes

 ** bufferSize **   <a name="connect-Type-amazon-q-connect_SemanticChunkingConfiguration-bufferSize"></a>
The buffer size.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1.
Required: Yes

 ** maxTokens **   <a name="connect-Type-amazon-q-connect_SemanticChunkingConfiguration-maxTokens"></a>
The maximum number of tokens that a chunk can contain.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

## See Also
<a name="API_amazon-q-connect_SemanticChunkingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/SemanticChunkingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/SemanticChunkingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/SemanticChunkingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
