---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_OnPremConfig.html
---

# OnPremConfig
<a name="API_OnPremConfig"></a>

The AWS DataSync agents that can connect to your Network File System (NFS) file server.

## Contents
<a name="API_OnPremConfig_Contents"></a>

 ** AgentArns **   <a name="DataSync-Type-OnPremConfig-AgentArns"></a>
The Amazon Resource Names (ARNs) of the DataSync agents that can connect to your NFS file server.
You can specify more than one agent. For more information, see [Using multiple DataSync agents](https://docs.aws.amazon.com/datasync/latest/userguide/do-i-need-datasync-agent.html#multiple-agents).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`
Required: Yes

## See Also
<a name="API_OnPremConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/OnPremConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/OnPremConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/OnPremConfig)
