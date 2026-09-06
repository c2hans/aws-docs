---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveMemorySessionBinding.html
---

# AgenticRetrieveMemorySessionBinding
<a name="API_agent-runtime_AgenticRetrieveMemorySessionBinding"></a>

The short-term memory session that this retrieval reads from and writes to.

## Contents
<a name="API_agent-runtime_AgenticRetrieveMemorySessionBinding_Contents"></a>

 ** actorId **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemorySessionBinding-actorId"></a>
The identifier of the end user or agent that the session belongs to. This identifier scopes session history so that one actor's history is never returned for another. You are responsible for sending the correct actor value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-_/]*(?::[a-zA-Z0-9\-_/]+)*[a-zA-Z0-9\-_/]*`
Required: Yes

 ** sessionId **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemorySessionBinding-sessionId"></a>
The identifier of the session to restore and continue. You are responsible for sending the correct session value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-_]*`
Required: Yes

## See Also
<a name="API_agent-runtime_AgenticRetrieveMemorySessionBinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemorySessionBinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemorySessionBinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemorySessionBinding)
