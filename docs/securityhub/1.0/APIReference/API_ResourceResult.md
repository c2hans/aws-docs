---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ResourceResult.html
---

# ResourceResult
<a name="API_ResourceResult"></a>

Provides comprehensive details about an AWS resource and its associated security findings.

## Contents
<a name="API_ResourceResult_Contents"></a>

 ** AccountId **   <a name="securityhub-Type-ResourceResult-AccountId"></a>
The AWS account that recorded the resource data in Security Hub.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Region **   <a name="securityhub-Type-ResourceResult-Region"></a>
The AWS Region that recorded the resource data in Security Hub.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ResourceConfig **   <a name="securityhub-Type-ResourceResult-ResourceConfig"></a>
The configuration details of a resource.
Type: JSON value
Required: Yes

 ** ResourceDetailCaptureTimeDt **   <a name="securityhub-Type-ResourceResult-ResourceDetailCaptureTimeDt"></a>
The timestamp when information about the resource was captured.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ResourceId **   <a name="securityhub-Type-ResourceResult-ResourceId"></a>
The unique identifier for a resource.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ResourceType **   <a name="securityhub-Type-ResourceResult-ResourceType"></a>
The type of resource.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** AccountName **   <a name="securityhub-Type-ResourceResult-AccountName"></a>
The name of the AWS account that's associated with the resource.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DiscoveryType **   <a name="securityhub-Type-ResourceResult-DiscoveryType"></a>
Specifies how the resource was discovered. If the value is `Managed`, the resource is natively provided by a cloud service provider. If the value is `SelfHosted`, the resource is hosted on customer-managed infrastructure, such as a compute instance or container image.
Type: String
Valid Values: `Managed | SelfHosted`
Required: No

 ** FindingsSummary **   <a name="securityhub-Type-ResourceResult-FindingsSummary"></a>
An aggregated view of security findings associated with a resource.
Type: Array of [ResourceFindingsSummary](API_ResourceFindingsSummary.md) objects
Required: No

 ** ResourceCategory **   <a name="securityhub-Type-ResourceResult-ResourceCategory"></a>
The grouping where the resource belongs.
Type: String
Valid Values: `Compute | Database | Storage | Code | AI/ML | Identity | Network | Messaging | Other`
Required: No

 ** ResourceCloudPartition **   <a name="securityhub-Type-ResourceResult-ResourceCloudPartition"></a>
The cloud partition where the resource exists. For AWS, valid values include `aws`, `aws-cn`, and `aws-us-gov`. This field isn't returned for cloud providers that don't use partitions.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceCreationTimeDt **   <a name="securityhub-Type-ResourceResult-ResourceCreationTimeDt"></a>
The time when the resource was created.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceGuid **   <a name="securityhub-Type-ResourceResult-ResourceGuid"></a>
The global identifier used to identify a resource.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceInfo **   <a name="securityhub-Type-ResourceResult-ResourceInfo"></a>
Additional resource-type-specific details. For self-hosted AI resources and their host resources, contains an `AIDetails` structure.
Type: [ResourceInfo](API_ResourceInfo.md) object
Required: No

 ** ResourceName **   <a name="securityhub-Type-ResourceResult-ResourceName"></a>
The name of the resource.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceOwnerAccountId **   <a name="securityhub-Type-ResourceResult-ResourceOwnerAccountId"></a>
The identifier of the cloud account that owns the resource. For AWS resources, this is the AWS account ID. For Azure resources, this is the Azure subscription ID.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceOwnerOrgId **   <a name="securityhub-Type-ResourceResult-ResourceOwnerOrgId"></a>
The identifier of the cloud organization that owns the resource. For AWS resources, this is the AWS Organizations ID. For Azure resources, this is the Azure tenant ID.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceProvider **   <a name="securityhub-Type-ResourceResult-ResourceProvider"></a>
The cloud provider where the resource exists. Valid values are `AWS` and `Azure`. This field is always included.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceRegion **   <a name="securityhub-Type-ResourceResult-ResourceRegion"></a>
The native cloud region where the resource is located. For AWS, this is an AWS Region (for example, `us-east-1`). For Azure resources, this is the Azure region (for example, `westus2`). This field is always included.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceSubCategory **   <a name="securityhub-Type-ResourceResult-ResourceSubCategory"></a>
The AI/ML sub-grouping of the resource. Present only when `ResourceCategory` is `AI/ML`.
Type: String
Valid Values: `Model | ModelServing | Agent | AgentFramework | AgentToolsAndIdentity | SafetyAndGuardrail | KnowledgeAndData | OrchestrationAndPipeline | ExternalEndpoint | Development | Other`
Required: No

 ** ResourceTags **   <a name="securityhub-Type-ResourceResult-ResourceTags"></a>
The key-value pairs associated with a resource.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Required: No

## See Also
<a name="API_ResourceResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ResourceResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ResourceResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ResourceResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
