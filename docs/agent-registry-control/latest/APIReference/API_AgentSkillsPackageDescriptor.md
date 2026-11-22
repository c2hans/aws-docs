---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_AgentSkillsPackageDescriptor.html
---

# AgentSkillsPackageDescriptor

Descriptor that names the source that the registry synchronizes a full skill package from. It holds only the source. The record's `artifact` member returns the package that the registry reads from this source.

## Contents
<a name="API_AgentSkillsPackageDescriptor_Contents"></a>

 ** source **   <a name="agentregistrycontrol-Type-AgentSkillsPackageDescriptor-source"></a>
The source of the skill package. Specify an `s3://` URL of a ZIP object, or a GitHub folder URL together with `repositoryProvider` set to `GITHUB`. For a GitHub folder, the registry builds the package from every file in the folder.
Type: [DescriptorSource](API_DescriptorSource.md) object
Required: No

## See Also
<a name="API_AgentSkillsPackageDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AgentSkillsPackageDescriptor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AgentSkillsPackageDescriptor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AgentSkillsPackageDescriptor)
