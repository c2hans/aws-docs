---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_DocumentChunkLocation.html
---

# DocumentChunkLocation
<a name="API_runtime_DocumentChunkLocation"></a>

Specifies a chunk-level location within a document, providing positioning information for cited content using logical document segments or chunks.

## Contents
<a name="API_runtime_DocumentChunkLocation_Contents"></a>

 ** documentIndex **   <a name="bedrock-Type-runtime_DocumentChunkLocation-documentIndex"></a>
The index of the document within the array of documents provided in the request.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** end **   <a name="bedrock-Type-runtime_DocumentChunkLocation-end"></a>
The ending chunk identifier or index of the cited content within the document.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** start **   <a name="bedrock-Type-runtime_DocumentChunkLocation-start"></a>
The starting chunk identifier or index of the cited content within the document.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_runtime_DocumentChunkLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/DocumentChunkLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/DocumentChunkLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/DocumentChunkLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
