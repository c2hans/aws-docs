---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ChatExecution.html
---

# ChatExecution
<a name="API_ChatExecution"></a>

A single chat execution summary

## Contents
<a name="API_ChatExecution_Contents"></a>

 ** createdAt **   <a name="devopsagent-Type-ChatExecution-createdAt"></a>
Timestamp when the chat was created
Type: Timestamp
Required: Yes

 ** executionId **   <a name="devopsagent-Type-ChatExecution-executionId"></a>
The unique identifier for the execution
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** summary **   <a name="devopsagent-Type-ChatExecution-summary"></a>
Summary or title of the chat
Type: String
Required: No

 ** updatedAt **   <a name="devopsagent-Type-ChatExecution-updatedAt"></a>
Timestamp when the chat was last updated
Type: Timestamp
Required: No

## See Also
<a name="API_ChatExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/ChatExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/ChatExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/ChatExecution)
