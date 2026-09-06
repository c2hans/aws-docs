---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceRevision.html
---

# ServiceRevision
<a name="API_ServiceRevision"></a>

Information about the service revision.

A service revision contains a record of the workload configuration Amazon ECS is attempting to deploy. Whenever you create or deploy a service, Amazon ECS automatically creates and captures the configuration that you're trying to deploy in the service revision. For information about service revisions, see [Amazon ECS service revisions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision.html) in the * *Amazon Elastic Container Service Developer Guide* *.

## Contents
<a name="API_ServiceRevision_Contents"></a>

 ** capacityProviderStrategy **   <a name="ECS-Type-ServiceRevision-capacityProviderStrategy"></a>
The capacity provider strategy the service revision uses.
Type: Array of [CapacityProviderStrategyItem](API_CapacityProviderStrategyItem.md) objects
Required: No

 ** clusterArn **   <a name="ECS-Type-ServiceRevision-clusterArn"></a>
The ARN of the cluster that hosts the service.
Type: String
Required: No

 ** containerImages **   <a name="ECS-Type-ServiceRevision-containerImages"></a>
The container images the service revision uses.
Type: Array of [ContainerImage](API_ContainerImage.md) objects
Required: No

 ** createdAt **   <a name="ECS-Type-ServiceRevision-createdAt"></a>
The time that the service revision was created. The format is yyyy-mm-dd HH:mm:ss.SSSSS.
Type: Timestamp
Required: No

 ** ecsManagedResources **   <a name="ECS-Type-ServiceRevision-ecsManagedResources"></a>
The resources created and managed by Amazon ECS when you create an Express service for Amazon ECS.
Type: [ECSManagedResources](API_ECSManagedResources.md) object
Required: No

 ** fargateEphemeralStorage **   <a name="ECS-Type-ServiceRevision-fargateEphemeralStorage"></a>
The amount of ephemeral storage to allocate for the deployment.
Type: [DeploymentEphemeralStorage](API_DeploymentEphemeralStorage.md) object
Required: No

 ** guardDutyEnabled **   <a name="ECS-Type-ServiceRevision-guardDutyEnabled"></a>
Indicates whether Runtime Monitoring is turned on.
Type: Boolean
Required: No

 ** launchType **   <a name="ECS-Type-ServiceRevision-launchType"></a>
The launch type the service revision uses.
Type: String
Valid Values: `EC2 | FARGATE | EXTERNAL | MANAGED_INSTANCES`
Required: No

 ** loadBalancers **   <a name="ECS-Type-ServiceRevision-loadBalancers"></a>
The load balancers the service revision uses.
Type: Array of [LoadBalancer](API_LoadBalancer.md) objects
Required: No

 ** monitoring **   <a name="ECS-Type-ServiceRevision-monitoring"></a>
The optional monitoring configuration for the service, which defines the resolution for the service-level `CPUUtilization` and `MemoryUtilization` Amazon CloudWatch metrics. When not specified, Amazon ECS uses the default resolution of `60` seconds.
Type: [MonitoringConfiguration](API_MonitoringConfiguration.md) object
Required: No

 ** networkConfiguration **   <a name="ECS-Type-ServiceRevision-networkConfiguration"></a>
The network configuration for a task or service.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** overrides **   <a name="ECS-Type-ServiceRevision-overrides"></a>
The effective runtime overrides that Amazon ECS applies to this service revision. This value is present only when Amazon ECS detects a difference between the task definition and the actual runtime configuration.
Type: [ServiceRevisionOverrides](API_ServiceRevisionOverrides.md) object
Required: No

 ** platformFamily **   <a name="ECS-Type-ServiceRevision-platformFamily"></a>
The platform family the service revision uses.
Type: String
Required: No

 ** platformVersion **   <a name="ECS-Type-ServiceRevision-platformVersion"></a>
For the Fargate launch type, the platform version the service revision uses.
Type: String
Required: No

 ** resolvedConfiguration **   <a name="ECS-Type-ServiceRevision-resolvedConfiguration"></a>
The resolved configuration for the service revision which contains the actual resources your service revision uses, such as which target groups serve traffic.
Type: [ResolvedConfiguration](API_ResolvedConfiguration.md) object
Required: No

 ** serviceArn **   <a name="ECS-Type-ServiceRevision-serviceArn"></a>
The ARN of the service for the service revision.
Type: String
Required: No

 ** serviceConnectConfiguration **   <a name="ECS-Type-ServiceRevision-serviceConnectConfiguration"></a>
The Service Connect configuration of your Amazon ECS service. The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.
Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: [ServiceConnectConfiguration](API_ServiceConnectConfiguration.md) object
Required: No

 ** serviceRegistries **   <a name="ECS-Type-ServiceRevision-serviceRegistries"></a>
The service registries (for Service Discovery) the service revision uses.
Type: Array of [ServiceRegistry](API_ServiceRegistry.md) objects
Required: No

 ** serviceRevisionArn **   <a name="ECS-Type-ServiceRevision-serviceRevisionArn"></a>
The ARN of the service revision.
Type: String
Required: No

 ** taskDefinition **   <a name="ECS-Type-ServiceRevision-taskDefinition"></a>
The task definition the service revision uses.
Type: String
Required: No

 ** volumeConfigurations **   <a name="ECS-Type-ServiceRevision-volumeConfigurations"></a>
The volumes that are configured at deployment that the service revision uses.
Type: Array of [ServiceVolumeConfiguration](API_ServiceVolumeConfiguration.md) objects
Required: No

 ** vpcLatticeConfigurations **   <a name="ECS-Type-ServiceRevision-vpcLatticeConfigurations"></a>
The VPC Lattice configuration for the service revision.
Type: Array of [VpcLatticeConfiguration](API_VpcLatticeConfiguration.md) objects
Required: No

## See Also
<a name="API_ServiceRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ServiceRevision)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ServiceRevision)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ServiceRevision)
