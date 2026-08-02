---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DomainConfig.html
---

# DomainConfig
<a name="API_DomainConfig"></a>

Container for the configuration of an OpenSearch Service domain.

## Contents
<a name="API_DomainConfig_Contents"></a>

 ** AccessPolicies **   <a name="opensearchservice-Type-DomainConfig-AccessPolicies"></a>
Specifies the access policies for the domain.
Type: [AccessPoliciesStatus](API_AccessPoliciesStatus.md) object
Required: No

 ** AdvancedOptions **   <a name="opensearchservice-Type-DomainConfig-AdvancedOptions"></a>
Key-value pairs to specify advanced configuration options. For more information, see [Advanced options](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options).
Type: [AdvancedOptionsStatus](API_AdvancedOptionsStatus.md) object
Required: No

 ** AdvancedSecurityOptions **   <a name="opensearchservice-Type-DomainConfig-AdvancedSecurityOptions"></a>
Container for fine-grained access control settings for the domain.
Type: [AdvancedSecurityOptionsStatus](API_AdvancedSecurityOptionsStatus.md) object
Required: No

 ** AIMLOptions **   <a name="opensearchservice-Type-DomainConfig-AIMLOptions"></a>
Container for parameters required to enable all machine learning features.
Type: [AIMLOptionsStatus](API_AIMLOptionsStatus.md) object
Required: No

 ** AutomatedSnapshotPauseOptions **   <a name="opensearchservice-Type-DomainConfig-AutomatedSnapshotPauseOptions"></a>
Specifies `AutomatedSnapshotPauseOptions` for the domain.
Type: [AutomatedSnapshotPauseOptionsStatus](API_AutomatedSnapshotPauseOptionsStatus.md) object
Required: No

 ** AutoTuneOptions **   <a name="opensearchservice-Type-DomainConfig-AutoTuneOptions"></a>
Container for Auto-Tune settings for the domain.
Type: [AutoTuneOptionsStatus](API_AutoTuneOptionsStatus.md) object
Required: No

 ** ChangeProgressDetails **   <a name="opensearchservice-Type-DomainConfig-ChangeProgressDetails"></a>
Container for information about the progress of an existing configuration change.
Type: [ChangeProgressDetails](API_ChangeProgressDetails.md) object
Required: No

 ** ClusterConfig **   <a name="opensearchservice-Type-DomainConfig-ClusterConfig"></a>
Container for the cluster configuration of a the domain.
Type: [ClusterConfigStatus](API_ClusterConfigStatus.md) object
Required: No

 ** CognitoOptions **   <a name="opensearchservice-Type-DomainConfig-CognitoOptions"></a>
Container for Amazon Cognito options for the domain.
Type: [CognitoOptionsStatus](API_CognitoOptionsStatus.md) object
Required: No

 ** DeploymentStrategyOptions **   <a name="opensearchservice-Type-DomainConfig-DeploymentStrategyOptions"></a>
Specifies `DeploymentStrategyOptions` for the domain.
Type: [DeploymentStrategyOptionsStatus](API_DeploymentStrategyOptionsStatus.md) object
Required: No

 ** DomainEndpointOptions **   <a name="opensearchservice-Type-DomainConfig-DomainEndpointOptions"></a>
Additional options for the domain endpoint, such as whether to require HTTPS for all traffic.
Type: [DomainEndpointOptionsStatus](API_DomainEndpointOptionsStatus.md) object
Required: No

 ** EBSOptions **   <a name="opensearchservice-Type-DomainConfig-EBSOptions"></a>
Container for EBS options configured for the domain.
Type: [EBSOptionsStatus](API_EBSOptionsStatus.md) object
Required: No

 ** EncryptionAtRestOptions **   <a name="opensearchservice-Type-DomainConfig-EncryptionAtRestOptions"></a>
Key-value pairs to enable encryption at rest.
Type: [EncryptionAtRestOptionsStatus](API_EncryptionAtRestOptionsStatus.md) object
Required: No

 ** EngineMode **   <a name="opensearchservice-Type-DomainConfig-EngineMode"></a>
The engine mode configured for the domain.
Type: [EngineModeStatus](API_EngineModeStatus.md) object
Required: No

 ** EngineVersion **   <a name="opensearchservice-Type-DomainConfig-EngineVersion"></a>
The OpenSearch or Elasticsearch version that the domain is running.
Type: [VersionStatus](API_VersionStatus.md) object
Required: No

 ** IdentityCenterOptions **   <a name="opensearchservice-Type-DomainConfig-IdentityCenterOptions"></a>
Configuration options for enabling and managing IAM Identity Center integration within a domain.
Type: [IdentityCenterOptionsStatus](API_IdentityCenterOptionsStatus.md) object
Required: No

 ** IPAddressType **   <a name="opensearchservice-Type-DomainConfig-IPAddressType"></a>
Choose either dual stack or IPv4 as your IP address type. Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option. If you set your IP address type to dual stack, you can't change your address type later.
Type: [IPAddressTypeStatus](API_IPAddressTypeStatus.md) object
Required: No

 ** LogPublishingOptions **   <a name="opensearchservice-Type-DomainConfig-LogPublishingOptions"></a>
Key-value pairs to configure log publishing.
Type: [LogPublishingOptionsStatus](API_LogPublishingOptionsStatus.md) object
Required: No

 ** ModifyingProperties **   <a name="opensearchservice-Type-DomainConfig-ModifyingProperties"></a>
Information about the domain properties that are currently being modified.
Type: Array of [ModifyingProperties](API_ModifyingProperties.md) objects
Required: No

 ** NodeToNodeEncryptionOptions **   <a name="opensearchservice-Type-DomainConfig-NodeToNodeEncryptionOptions"></a>
Whether node-to-node encryption is enabled or disabled.
Type: [NodeToNodeEncryptionOptionsStatus](API_NodeToNodeEncryptionOptionsStatus.md) object
Required: No

 ** OffPeakWindowOptions **   <a name="opensearchservice-Type-DomainConfig-OffPeakWindowOptions"></a>
Container for off-peak window options for the domain.
Type: [OffPeakWindowOptionsStatus](API_OffPeakWindowOptionsStatus.md) object
Required: No

 ** SnapshotOptions **   <a name="opensearchservice-Type-DomainConfig-SnapshotOptions"></a>
DEPRECATED. Container for parameters required to configure automated snapshots of domain indexes.
Type: [SnapshotOptionsStatus](API_SnapshotOptionsStatus.md) object
Required: No

 ** SoftwareUpdateOptions **   <a name="opensearchservice-Type-DomainConfig-SoftwareUpdateOptions"></a>
Software update options for the domain.
Type: [SoftwareUpdateOptionsStatus](API_SoftwareUpdateOptionsStatus.md) object
Required: No

 ** UseCase **   <a name="opensearchservice-Type-DomainConfig-UseCase"></a>
The use case configured for the domain.
Type: [UseCaseStatus](API_UseCaseStatus.md) object
Required: No

 ** VPCOptions **   <a name="opensearchservice-Type-DomainConfig-VPCOptions"></a>
The current VPC options for the domain and the status of any updates to their configuration.
Type: [VPCDerivedInfoStatus](API_VPCDerivedInfoStatus.md) object
Required: No

## See Also
<a name="API_DomainConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DomainConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DomainConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DomainConfig)
