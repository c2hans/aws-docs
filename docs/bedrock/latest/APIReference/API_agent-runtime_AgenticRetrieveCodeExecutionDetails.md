---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveCodeExecutionDetails.html
---

# AgenticRetrieveCodeExecutionDetails
<a name="API_agent-runtime_AgenticRetrieveCodeExecutionDetails"></a>

The details of code that the agent chose to run in an isolated sandbox. The record includes the documents that the code reads. The corresponding CodeExecution step reports the outcome.

## Contents
<a name="API_agent-runtime_AgenticRetrieveCodeExecutionDetails_Contents"></a>

 ** documents **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveCodeExecutionDetails-documents"></a>
The documents that the code reads. This field is present when the code reads documents.
Type: Array of [AgenticRetrieveCodeExecutionDocument](API_agent-runtime_AgenticRetrieveCodeExecutionDocument.md) objects
Required: No

## See Also
<a name="API_agent-runtime_AgenticRetrieveCodeExecutionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveCodeExecutionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveCodeExecutionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveCodeExecutionDetails)
