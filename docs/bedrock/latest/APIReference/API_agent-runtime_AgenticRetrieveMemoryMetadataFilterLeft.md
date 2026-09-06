---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveMemoryMetadataFilterLeft.html
---

# AgenticRetrieveMemoryMetadataFilterLeft
<a name="API_agent-runtime_AgenticRetrieveMemoryMetadataFilterLeft"></a>

The left operand of a metadata filter expression. Set exactly one member.

## Contents
<a name="API_agent-runtime_AgenticRetrieveMemoryMetadataFilterLeft_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** metadataKey **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryMetadataFilterLeft-metadataKey"></a>
The metadata key to filter on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\s._:/=+@-]*`
Required: No

## See Also
<a name="API_agent-runtime_AgenticRetrieveMemoryMetadataFilterLeft_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemoryMetadataFilterLeft)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemoryMetadataFilterLeft)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemoryMetadataFilterLeft)
