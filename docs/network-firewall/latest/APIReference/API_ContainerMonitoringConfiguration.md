---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ContainerMonitoringConfiguration.html
---

# ContainerMonitoringConfiguration
<a name="API_ContainerMonitoringConfiguration"></a>

Contains the monitoring configuration for a single cluster in a container association. Specifies the cluster ARN and optional attribute filters to narrow which containers are tracked.

## Contents
<a name="API_ContainerMonitoringConfiguration_Contents"></a>

 ** ClusterArn **   <a name="networkfirewall-Type-ContainerMonitoringConfiguration-ClusterArn"></a>
The ARN of the Amazon ECS or Amazon EKS cluster to monitor. The cluster must be in the same Region and account as the container association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: Yes

 ** AttributeFilters **   <a name="networkfirewall-Type-ContainerMonitoringConfiguration-AttributeFilters"></a>
Key-value pairs that filter which containers are tracked. For Amazon EKS, you can filter by namespace and Kubernetes labels. For Amazon ECS, you can filter by container instance attributes (EC2 launch type only).
Attribute values can contain wildcard patterns, for example `payments-*`. Attribute keys must match exactly.
Type: Array of [ContainerAttribute](API_ContainerAttribute.md) objects
Required: No

## See Also
<a name="API_ContainerMonitoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ContainerMonitoringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ContainerMonitoringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ContainerMonitoringConfiguration)
