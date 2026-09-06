---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AIDetails.html
---

# AIDetails
<a name="API_AIDetails"></a>

Contains information about self-hosted AI resources and their host resources. The fields that are present depend on the role of the resource.

On a self-hosted AI resource (a resource with a `SelfHosted::AI::` resource type, such as `SelfHosted::AI::Model` or `SelfHosted::AI::Agent`), the `HostResourceGuid` and `HostResourceType` fields link the resource to its host. The `CanonicalId` field identifies what the resource is, enabling aggregation of identical resources across multiple hosts.

On a host resource (such as an Amazon EC2 instance), the `SelfHostedAI*ResourceCount` fields contain the count for each `ResourceSubCategory` and the total count of self-hosted AI resources detected on the host.

## Contents
<a name="API_AIDetails_Contents"></a>

 ** CanonicalId **   <a name="securityhub-Type-AIDetails-CanonicalId"></a>
The canonical identifier for the AI resource, independent of where it is deployed. Multiple occurrences of the same resource on different hosts share the same `CanonicalId`. For model resources, the value follows the format `model/<purl>`, such as `model/pkg:huggingface/meta-llama/llama-3-8b`. Present only on self-hosted AI resources.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HostResourceGuid **   <a name="securityhub-Type-AIDetails-HostResourceGuid"></a>
The identifier of the host resource that hosts the self-hosted AI resource. Present only on self-hosted AI resources.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HostResourceType **   <a name="securityhub-Type-AIDetails-HostResourceType"></a>
The `ResourceType` of the host resource that hosts the self-hosted AI resource, such as `AWS::EC2::Instance`. Present only on self-hosted AI resources.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SelfHostedAIAgentFrameworkResourceCount **   <a name="securityhub-Type-AIDetails-SelfHostedAIAgentFrameworkResourceCount"></a>
The number of self-hosted AI resources of `ResourceSubCategory` `AgentFramework` detected on the host resource. Present only on host resources.
Type: Integer
Required: No

 ** SelfHostedAIAgentResourceCount **   <a name="securityhub-Type-AIDetails-SelfHostedAIAgentResourceCount"></a>
The number of self-hosted AI resources of `ResourceSubCategory` `Agent` detected on the host resource. Present only on host resources.
Type: Integer
Required: No

 ** SelfHostedAIAgentToolsAndIdentityResourceCount **   <a name="securityhub-Type-AIDetails-SelfHostedAIAgentToolsAndIdentityResourceCount"></a>
The number of self-hosted AI resources of `ResourceSubCategory` `AgentToolsAndIdentity` detected on the host resource. Present only on host resources.
Type: Integer
Required: No

 ** SelfHostedAIDevelopmentResourceCount **   <a name="securityhub-Type-AIDetails-SelfHostedAIDevelopmentResourceCount"></a>
The number of self-hosted AI resources of `ResourceSubCategory` `Development` detected on the host resource. Present only on host resources.
Type: Integer
Required: No

 ** SelfHostedAIExternalEndpointResourceCount **   <a name="securityhub-Type-AIDetails-SelfHostedAIExternalEndpointResourceCount"></a>
The number of self-hosted AI resources of `ResourceSubCategory` `ExternalEndpoint` detected on the host resource. Present only on host resources.
Type: Integer
Required: No

 ** SelfHostedAIModelResourceCount **   <a name="securityhub-Type-AIDetails-SelfHostedAIModelResourceCount"></a>
The number of self-hosted AI resources of `ResourceSubCategory` `Model` detected on the host resource. Present only on host resources.
Type: Integer
Required: No

 ** SelfHostedAIModelServingResourceCount **   <a name="securityhub-Type-AIDetails-SelfHostedAIModelServingResourceCount"></a>
The number of self-hosted AI resources of `ResourceSubCategory` `ModelServing` detected on the host resource. Present only on host resources.
Type: Integer
Required: No

 ** SelfHostedTotalAIResourceCount **   <a name="securityhub-Type-AIDetails-SelfHostedTotalAIResourceCount"></a>
The total number of all self-hosted AI resources detected on the host resource. Present only on host resources.
Type: Integer
Required: No

## See Also
<a name="API_AIDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AIDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AIDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AIDetails)
