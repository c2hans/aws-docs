---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_AgentSkillsAdditionalData.html
---

# AgentSkillsAdditionalData

Additional data associated with an agent skills definition descriptor: the skill's SKILL.md and the source that the registry synchronizes the skill from. A record synchronizes from one source at most, either `skillMd.source` for SKILL.md only or `skillPackage.source` for the full skill package. When the record has a skill package or a synchronized source, the registry sets `skillMd.data` from the SKILL.md in that package or source.

## Contents
<a name="API_AgentSkillsAdditionalData_Contents"></a>

 ** repositoryProvider **   <a name="agentregistrycontrol-Type-AgentSkillsAdditionalData-repositoryProvider"></a>
The repository provider of the record's skill source. Set it to `GITHUB` when `skillMd.source` or `skillPackage.source` is a GitHub folder URL. The registry treats an `https://` source as a GitHub source only when this member is set. Don't set it for an Amazon S3 source.
Type: String
Valid Values: `GITHUB`
Required: No

 ** skillMd **   <a name="agentregistrycontrol-Type-AgentSkillsAdditionalData-skillMd"></a>
The markdown skill content associated with an agent skills definition.
Type: [AgentSkillsMdDescriptor](API_AgentSkillsMdDescriptor.md) object
Required: No

 ** skillPackage **   <a name="agentregistrycontrol-Type-AgentSkillsAdditionalData-skillPackage"></a>
The source that the registry synchronizes the full skill package from. The registry validates and stores the package, sets `skillMd.data` from its SKILL.md, and returns the package in the `artifact` member of `GetRegistryRecord`. You can't set both this source and `skillMd.source`.
Type: [AgentSkillsPackageDescriptor](API_AgentSkillsPackageDescriptor.md) object
Required: No

 ** sourceConfiguration **   <a name="agentregistrycontrol-Type-AgentSkillsAdditionalData-sourceConfiguration"></a>
The provider-specific settings of the record's skill source. For an Amazon S3 source, `s3.bucketOwnerAccountId` specifies the account that owns the source bucket.
Type: [AgentSkillsSourceConfiguration](API_AgentSkillsSourceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_AgentSkillsAdditionalData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AgentSkillsAdditionalData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AgentSkillsAdditionalData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AgentSkillsAdditionalData)
