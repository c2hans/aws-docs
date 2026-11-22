---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_UpdatedAgentSkillsSourceConfiguration.html
---

# UpdatedAgentSkillsSourceConfiguration

The source configuration patch wrapper. Omit to leave the configuration unchanged; supply an empty object to remove it; supply optionalValue to replace it. When you move an Amazon S3 source to another bucket, the record keeps its configuration. In the same request, specify the new bucket's owner, or specify an empty object so that the registry expects the bucket in the role's account.

## Contents
<a name="API_UpdatedAgentSkillsSourceConfiguration_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedAgentSkillsSourceConfiguration-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.
Type: [AgentSkillsSourceConfiguration](API_AgentSkillsSourceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_UpdatedAgentSkillsSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedAgentSkillsSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedAgentSkillsSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedAgentSkillsSourceConfiguration)
