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
