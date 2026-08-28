---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_PersistentConnectionConfig.html
---

# PersistentConnectionConfig
<a name="API_PersistentConnectionConfig"></a>

Configuration settings for persistent connection for a specific channel.

## Contents
<a name="API_PersistentConnectionConfig_Contents"></a>

 ** Channel **   <a name="connect-Type-PersistentConnectionConfig-Channel"></a>
Configuration settings for persistent connection. **Only `VOICE` is supported for this data type.**
Type: String
Valid Values: `VOICE | CHAT | TASK | EMAIL`
Required: Yes

 ** PersistentConnection **   <a name="connect-Type-PersistentConnectionConfig-PersistentConnection"></a>
Indicates whether persistent connection is enabled. When enabled, the agent's connection is maintained after a call ends, enabling subsequent calls to connect faster.
Type: Boolean
Required: Yes

## See Also
<a name="API_PersistentConnectionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/PersistentConnectionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/PersistentConnectionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/PersistentConnectionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
