---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ManagedEndpointConfiguration.html
---

# ManagedEndpointConfiguration
<a name="API_ManagedEndpointConfiguration"></a>

Describes the configuration of a managed endpoint.

## Contents
<a name="API_ManagedEndpointConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** autoScalingGroups **   <a name="rtbfabric-Type-ManagedEndpointConfiguration-autoScalingGroups"></a>
Describes the configuration of an auto scaling group.
Type: [AutoScalingGroupsConfiguration](API_AutoScalingGroupsConfiguration.md) object
Required: No

 ** eksEndpoints **   <a name="rtbfabric-Type-ManagedEndpointConfiguration-eksEndpoints"></a>
Describes the configuration of an Amazon Elastic Kubernetes Service endpoint.
Type: [EksEndpointsConfiguration](API_EksEndpointsConfiguration.md) object
Required: No

## See Also
<a name="API_ManagedEndpointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/ManagedEndpointConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/ManagedEndpointConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/ManagedEndpointConfiguration)
