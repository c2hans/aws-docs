---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_InlineCustomInstruction.html
---

# InlineCustomInstruction
<a name="API_InlineCustomInstruction"></a>

An inline custom instruction with text content and optional file upload metadata.

## Contents
<a name="API_InlineCustomInstruction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** InstructionText **   <a name="QS-Type-InlineCustomInstruction-InstructionText"></a>
The instruction text content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50000.
Required: Yes

 ** UploadedDocumentMetadata **   <a name="QS-Type-InlineCustomInstruction-UploadedDocumentMetadata"></a>
Metadata about an uploaded document associated with this instruction.
Type: [UploadedDocumentMetadata](API_UploadedDocumentMetadata.md) object
Required: No

## See Also
<a name="API_InlineCustomInstruction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/InlineCustomInstruction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/InlineCustomInstruction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/InlineCustomInstruction)
