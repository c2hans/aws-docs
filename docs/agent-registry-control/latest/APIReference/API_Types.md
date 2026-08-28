---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_Types.html
---

# Data Types
<a name="API_Types"></a>

The Agent Registry Control API contains several data types that various actions use. This section describes each data type in detail.

**Note**
The order of each element in a data type structure is not guaranteed. Applications should not assume a particular order.

The following data types are supported:
+  [A2aAgentCardDescriptor](API_A2aAgentCardDescriptor.md)
+  [AgentSkillsAdditionalData](API_AgentSkillsAdditionalData.md)
+  [AgentSkillsDefinitionDescriptor](API_AgentSkillsDefinitionDescriptor.md)
+  [AgentSkillsMdDescriptor](API_AgentSkillsMdDescriptor.md)
+  [ApprovalConfiguration](API_ApprovalConfiguration.md)
+  [AuthorizerConfiguration](API_AuthorizerConfiguration.md)
+  [AuthorizingClaimMatchValueType](API_AuthorizingClaimMatchValueType.md)
+  [ClaimMatchValueType](API_ClaimMatchValueType.md)
+  [CustomClaimValidationType](API_CustomClaimValidationType.md)
+  [CustomDescriptor](API_CustomDescriptor.md)
+  [CustomJWTAuthorizerConfiguration](API_CustomJWTAuthorizerConfiguration.md)
+  [Descriptors](API_Descriptors.md)
+  [DescriptorSource](API_DescriptorSource.md)
+  [DescriptorSourceFromUrl](API_DescriptorSourceFromUrl.md)
+  [DiscoveryConfiguration](API_DiscoveryConfiguration.md)
+  [ManagedVpcResource](API_ManagedVpcResource.md)
+  [McpServerAdditionalData](API_McpServerAdditionalData.md)
+  [McpServerDescriptor](API_McpServerDescriptor.md)
+  [McpToolsDescriptor](API_McpToolsDescriptor.md)
+  [PrivateEndpoint](API_PrivateEndpoint.md)
+  [PrivateEndpointOverride](API_PrivateEndpointOverride.md)
+  [RegistryFilter](API_RegistryFilter.md)
+  [RegistryRecordCredentialProviderConfiguration](API_RegistryRecordCredentialProviderConfiguration.md)
+  [RegistryRecordCredentialProviderUnion](API_RegistryRecordCredentialProviderUnion.md)
+  [RegistryRecordFilter](API_RegistryRecordFilter.md)
+  [RegistryRecordIamCredentialProvider](API_RegistryRecordIamCredentialProvider.md)
+  [RegistryRecordOAuthCredentialProvider](API_RegistryRecordOAuthCredentialProvider.md)
+  [RegistryRecordSummary](API_RegistryRecordSummary.md)
+  [RegistrySummary](API_RegistrySummary.md)
+  [SelfManagedLatticeResource](API_SelfManagedLatticeResource.md)
+  [UpdatedA2aAgentCardDescriptor](API_UpdatedA2aAgentCardDescriptor.md)
+  [UpdatedA2aAgentCardDescriptorFields](API_UpdatedA2aAgentCardDescriptorFields.md)
+  [UpdatedAgentSkillsAdditionalData](API_UpdatedAgentSkillsAdditionalData.md)
+  [UpdatedAgentSkillsAdditionalDataFields](API_UpdatedAgentSkillsAdditionalDataFields.md)
+  [UpdatedAgentSkillsDefinitionDescriptor](API_UpdatedAgentSkillsDefinitionDescriptor.md)
+  [UpdatedAgentSkillsDefinitionDescriptorFields](API_UpdatedAgentSkillsDefinitionDescriptorFields.md)
+  [UpdatedAgentSkillsMdDescriptor](API_UpdatedAgentSkillsMdDescriptor.md)
+  [UpdatedAgentSkillsMdDescriptorFields](API_UpdatedAgentSkillsMdDescriptorFields.md)
+  [UpdatedApprovalConfiguration](API_UpdatedApprovalConfiguration.md)
+  [UpdatedAuthorizerConfiguration](API_UpdatedAuthorizerConfiguration.md)
+  [UpdatedCustomDescriptor](API_UpdatedCustomDescriptor.md)
+  [UpdatedCustomDescriptorFields](API_UpdatedCustomDescriptorFields.md)
+  [UpdatedDataSchemaVersion](API_UpdatedDataSchemaVersion.md)
+  [UpdatedDescription](API_UpdatedDescription.md)
+  [UpdatedDescriptorData](API_UpdatedDescriptorData.md)
+  [UpdatedDescriptors](API_UpdatedDescriptors.md)
+  [UpdatedDescriptorsFields](API_UpdatedDescriptorsFields.md)
+  [UpdatedDescriptorSource](API_UpdatedDescriptorSource.md)
+  [UpdatedDiscoveryConfiguration](API_UpdatedDiscoveryConfiguration.md)
+  [UpdatedDisplayName](API_UpdatedDisplayName.md)
+  [UpdatedMcpServerAdditionalData](API_UpdatedMcpServerAdditionalData.md)
+  [UpdatedMcpServerAdditionalDataFields](API_UpdatedMcpServerAdditionalDataFields.md)
+  [UpdatedMcpServerDescriptor](API_UpdatedMcpServerDescriptor.md)
+  [UpdatedMcpServerDescriptorFields](API_UpdatedMcpServerDescriptorFields.md)
+  [UpdatedMcpToolsDescriptor](API_UpdatedMcpToolsDescriptor.md)
+  [UpdatedMcpToolsDescriptorFields](API_UpdatedMcpToolsDescriptorFields.md)
+  [ValidationExceptionField](API_ValidationExceptionField.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AgentRegistry Control Plane API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agent-registry-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
