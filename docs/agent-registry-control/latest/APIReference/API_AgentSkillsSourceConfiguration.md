---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_AgentSkillsSourceConfiguration.html
---

# AgentSkillsSourceConfiguration

The provider-specific settings of a skill source. Specify the member that matches the source's provider, such as `s3` for an Amazon S3 source.

## Contents
<a name="API_AgentSkillsSourceConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** s3 **   <a name="agentregistrycontrol-Type-AgentSkillsSourceConfiguration-s3"></a>
The settings of an Amazon S3 source.
Type: [S3SourceConfiguration](API_S3SourceConfiguration.md) object
Required: No

## See Also
<a name="API_AgentSkillsSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AgentSkillsSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AgentSkillsSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AgentSkillsSourceConfiguration)
