---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_VirtualCluster.html
---

# VirtualCluster
<a name="API_VirtualCluster"></a>

This entity describes a virtual cluster. A virtual cluster is a Kubernetes namespace that Amazon EMR is registered with. Amazon EMR uses virtual clusters to run jobs and host endpoints. Multiple virtual clusters can be backed by the same physical cluster. However, each virtual cluster maps to one namespace on an Amazon EKS cluster. Virtual clusters do not create any active resources that contribute to your bill or that require lifecycle management outside the service.

## Contents
<a name="API_VirtualCluster_Contents"></a>

 ** arn **   <a name="emroneks-Type-VirtualCluster-arn"></a>
The ARN of the virtual cluster.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):emr-containers:.+:(\d{12}):\/virtualclusters\/[0-9a-zA-Z]+$`
Required: No

 ** containerProvider **   <a name="emroneks-Type-VirtualCluster-containerProvider"></a>
The container provider of the virtual cluster.
Type: [ContainerProvider](API_ContainerProvider.md) object
Required: No

 ** createdAt **   <a name="emroneks-Type-VirtualCluster-createdAt"></a>
The date and time when the virtual cluster is created.
Type: Timestamp
Required: No

 ** id **   <a name="emroneks-Type-VirtualCluster-id"></a>
The ID of the virtual cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: No

 ** name **   <a name="emroneks-Type-VirtualCluster-name"></a>
The name of the virtual cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** schedulerConfiguration **   <a name="emroneks-Type-VirtualCluster-schedulerConfiguration"></a>
The scheduler configuration (concurrency and queue limits) applied to the virtual cluster. The service does not return this field when no scheduler limits are configured.
Type: [SchedulerConfiguration](API_SchedulerConfiguration.md) object
Required: No

 ** schedulerStatus **   <a name="emroneks-Type-VirtualCluster-schedulerStatus"></a>
The current in-queue and concurrent job-run counts for the virtual cluster.
Type: [SchedulerStatus](API_SchedulerStatus.md) object
Required: No

 ** securityConfigurationId **   <a name="emroneks-Type-VirtualCluster-securityConfigurationId"></a>
The ID of the security configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: No

 ** sessionEnabled **   <a name="emroneks-Type-VirtualCluster-sessionEnabled"></a>
Specifies whether the virtual cluster has session support enabled.
Type: Boolean
Required: No

 ** state **   <a name="emroneks-Type-VirtualCluster-state"></a>
The state of the virtual cluster.
Type: String
Valid Values: `RUNNING | TERMINATING | TERMINATED | ARRESTED`
Required: No

 ** tags **   <a name="emroneks-Type-VirtualCluster-tags"></a>
The assigned tags of the virtual cluster.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.*\S.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_VirtualCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/VirtualCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/VirtualCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/VirtualCluster)
