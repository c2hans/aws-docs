---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DomainStatus.html
---

# DomainStatus
<a name="API_DomainStatus"></a>

The current status of an OpenSearch Service domain.

## Contents
<a name="API_DomainStatus_Contents"></a>

 ** ARN **   <a name="opensearchservice-Type-DomainStatus-ARN"></a>
The Amazon Resource Name (ARN) of the domain. For more information, see [IAM identifiers ](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html) in the * AWS Identity and Access Management User Guide*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: Yes

 ** ClusterConfig **   <a name="opensearchservice-Type-DomainStatus-ClusterConfig"></a>
Container for the cluster configuration of the domain.
Type: [ClusterConfig](API_ClusterConfig.md) object
Required: Yes

 ** DomainId **   <a name="opensearchservice-Type-DomainStatus-DomainId"></a>
Unique identifier for the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** DomainName **   <a name="opensearchservice-Type-DomainStatus-DomainName"></a>
Name of the domain. Domain names are unique across all domains owned by the same account within an AWS Region.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** AccessPolicies **   <a name="opensearchservice-Type-DomainStatus-AccessPolicies"></a>
Identity and Access Management (IAM) policy document specifying the access policies for the domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 102400.
Pattern: `.*`
Required: No

 ** AdvancedOptions **   <a name="opensearchservice-Type-DomainStatus-AdvancedOptions"></a>
Key-value pairs that specify advanced configuration options.
Type: String to string map
Required: No

 ** AdvancedSecurityOptions **   <a name="opensearchservice-Type-DomainStatus-AdvancedSecurityOptions"></a>
Settings for fine-grained access control.
Type: [AdvancedSecurityOptions](API_AdvancedSecurityOptions.md) object
Required: No

 ** AIMLOptions **   <a name="opensearchservice-Type-DomainStatus-AIMLOptions"></a>
Container for parameters required to enable all machine learning features.
Type: [AIMLOptionsOutput](API_AIMLOptionsOutput.md) object
Required: No

 ** AutomatedSnapshotPauseOptions **   <a name="opensearchservice-Type-DomainStatus-AutomatedSnapshotPauseOptions"></a>
The current status of the domain's automated snapshot pause options.
Type: [AutomatedSnapshotPauseOptions](API_AutomatedSnapshotPauseOptions.md) object
Required: No

 ** AutoTuneOptions **   <a name="opensearchservice-Type-DomainStatus-AutoTuneOptions"></a>
Auto-Tune settings for the domain.
Type: [AutoTuneOptionsOutput](API_AutoTuneOptionsOutput.md) object
Required: No

 ** ChangeProgressDetails **   <a name="opensearchservice-Type-DomainStatus-ChangeProgressDetails"></a>
Information about a configuration change happening on the domain.
Type: [ChangeProgressDetails](API_ChangeProgressDetails.md) object
Required: No

 ** CognitoOptions **   <a name="opensearchservice-Type-DomainStatus-CognitoOptions"></a>
Key-value pairs to configure Amazon Cognito authentication for OpenSearch Dashboards.
Type: [CognitoOptions](API_CognitoOptions.md) object
Required: No

 ** Created **   <a name="opensearchservice-Type-DomainStatus-Created"></a>
Creation status of an OpenSearch Service domain. True if domain creation is complete. False if domain creation is still in progress.
Type: Boolean
Required: No

 ** Deleted **   <a name="opensearchservice-Type-DomainStatus-Deleted"></a>
Deletion status of an OpenSearch Service domain. True if domain deletion is complete. False if domain deletion is still in progress. Once deletion is complete, the status of the domain is no longer returned.
Type: Boolean
Required: No

 ** DeploymentStrategyOptions **   <a name="opensearchservice-Type-DomainStatus-DeploymentStrategyOptions"></a>
The current status of the domain's deployment strategy options.
Type: [DeploymentStrategyOptions](API_DeploymentStrategyOptions.md) object
Required: No

 ** DomainEndpointOptions **   <a name="opensearchservice-Type-DomainStatus-DomainEndpointOptions"></a>
Additional options for the domain endpoint, such as whether to require HTTPS for all traffic.
Type: [DomainEndpointOptions](API_DomainEndpointOptions.md) object
Required: No

 ** DomainEndpointV2HostedZoneId **   <a name="opensearchservice-Type-DomainStatus-DomainEndpointV2HostedZoneId"></a>
The dual stack hosted zone ID for the domain.
Type: String
Required: No

 ** DomainProcessingStatus **   <a name="opensearchservice-Type-DomainStatus-DomainProcessingStatus"></a>
The status of any changes that are currently in progress for the domain.
Type: String
Valid Values: `Creating | Active | Modifying | UpgradingEngineVersion | UpdatingServiceSoftware | Isolated | Deleting`
Required: No

 ** EBSOptions **   <a name="opensearchservice-Type-DomainStatus-EBSOptions"></a>
Container for EBS-based storage settings for the domain.
Type: [EBSOptions](API_EBSOptions.md) object
Required: No

 ** EncryptionAtRestOptions **   <a name="opensearchservice-Type-DomainStatus-EncryptionAtRestOptions"></a>
Encryption at rest settings for the domain.
Type: [EncryptionAtRestOptions](API_EncryptionAtRestOptions.md) object
Required: No

 ** Endpoint **   <a name="opensearchservice-Type-DomainStatus-Endpoint"></a>
Domain-specific endpoint used to submit index, search, and data upload requests to the domain.
Type: String
Required: No

 ** Endpoints **   <a name="opensearchservice-Type-DomainStatus-Endpoints"></a>
The key-value pair that exists if the OpenSearch Service domain uses VPC endpoints. For example:
+  **IPv4 IP addresses** - `'vpc','vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'`
+  **Dual stack IP addresses** - `'vpcv2':'vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.aos.us-east-1.on.aws'`
Type: String to string map
Required: No

 ** EndpointV2 **   <a name="opensearchservice-Type-DomainStatus-EndpointV2"></a>
If `IPAddressType` to set to `dualstack`, a version 2 domain endpoint is provisioned. This endpoint functions like a normal endpoint, except that it works with both IPv4 and IPv6 IP addresses. Normal endpoints work only with IPv4 IP addresses.
Type: String
Required: No

 ** EngineMode **   <a name="opensearchservice-Type-DomainStatus-EngineMode"></a>
The engine mode for the domain.
Type: String
Valid Values: `GENERAL | OPTIMIZED`
Required: No

 ** EngineVersion **   <a name="opensearchservice-Type-DomainStatus-EngineVersion"></a>
Version of OpenSearch or Elasticsearch that the domain is running, in the format `Elasticsearch_X.Y` or `OpenSearch_X.Y`.
Type: String
Length Constraints: Minimum length of 14. Maximum length of 18.
Pattern: `^Elasticsearch_[0-9]{1}\.[0-9]{1,2}$|^OpenSearch_[0-9]{1,2}\.[0-9]{1,2}$`
Required: No

 ** IdentityCenterOptions **   <a name="opensearchservice-Type-DomainStatus-IdentityCenterOptions"></a>
Configuration options for controlling IAM Identity Center integration within a domain.
Type: [IdentityCenterOptions](API_IdentityCenterOptions.md) object
Required: No

 ** IPAddressType **   <a name="opensearchservice-Type-DomainStatus-IPAddressType"></a>
The type of IP addresses supported by the endpoint for the domain.
Type: String
Valid Values: `ipv4 | dualstack`
Required: No

 ** LogPublishingOptions **   <a name="opensearchservice-Type-DomainStatus-LogPublishingOptions"></a>
Log publishing options for the domain.
Type: String to [LogPublishingOption](API_LogPublishingOption.md) object map
Valid Keys: `INDEX_SLOW_LOGS | SEARCH_SLOW_LOGS | ES_APPLICATION_LOGS | AUDIT_LOGS`
Required: No

 ** ModifyingProperties **   <a name="opensearchservice-Type-DomainStatus-ModifyingProperties"></a>
Information about the domain properties that are currently being modified.
Type: Array of [ModifyingProperties](API_ModifyingProperties.md) objects
Required: No

 ** NodeToNodeEncryptionOptions **   <a name="opensearchservice-Type-DomainStatus-NodeToNodeEncryptionOptions"></a>
Whether node-to-node encryption is enabled or disabled.
Type: [NodeToNodeEncryptionOptions](API_NodeToNodeEncryptionOptions.md) object
Required: No

 ** OffPeakWindowOptions **   <a name="opensearchservice-Type-DomainStatus-OffPeakWindowOptions"></a>
Options that specify a custom 10-hour window during which OpenSearch Service can perform configuration changes on the domain.
Type: [OffPeakWindowOptions](API_OffPeakWindowOptions.md) object
Required: No

 ** Processing **   <a name="opensearchservice-Type-DomainStatus-Processing"></a>
The status of the domain configuration. True if OpenSearch Service is processing configuration changes. False if the configuration is active.
Type: Boolean
Required: No

 ** ServiceSoftwareOptions **   <a name="opensearchservice-Type-DomainStatus-ServiceSoftwareOptions"></a>
The current status of the domain's service software.
Type: [ServiceSoftwareOptions](API_ServiceSoftwareOptions.md) object
Required: No

 ** SnapshotOptions **   <a name="opensearchservice-Type-DomainStatus-SnapshotOptions"></a>
DEPRECATED. Container for parameters required to configure automated snapshots of domain indexes.
Type: [SnapshotOptions](API_SnapshotOptions.md) object
Required: No

 ** SoftwareUpdateOptions **   <a name="opensearchservice-Type-DomainStatus-SoftwareUpdateOptions"></a>
Service software update options for the domain.
Type: [SoftwareUpdateOptions](API_SoftwareUpdateOptions.md) object
Required: No

 ** UpgradeProcessing **   <a name="opensearchservice-Type-DomainStatus-UpgradeProcessing"></a>
The status of a domain version upgrade to a new version of OpenSearch or Elasticsearch. True if OpenSearch Service is in the process of a version upgrade. False if the configuration is active.
Type: Boolean
Required: No

 ** UseCase **   <a name="opensearchservice-Type-DomainStatus-UseCase"></a>
The primary use case for the domain.
Type: String
Valid Values: `SEARCH | VECTOR | OBSERVABILITY | MIXED`
Required: No

 ** VPCOptions **   <a name="opensearchservice-Type-DomainStatus-VPCOptions"></a>
The VPC configuration for the domain.
Type: [VPCDerivedInfo](API_VPCDerivedInfo.md) object
Required: No

## See Also
<a name="API_DomainStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DomainStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DomainStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DomainStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
