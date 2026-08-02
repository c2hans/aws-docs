---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Cluster.html
---

# Cluster
<a name="API_Cluster"></a>

A regional grouping of one or more container instances where you can run task requests. Each account receives a default cluster the first time you use the Amazon ECS service, but you may also create other clusters. Clusters may contain more than one instance type simultaneously.

## Contents
<a name="API_Cluster_Contents"></a>

 ** activeServicesCount **   <a name="ECS-Type-Cluster-activeServicesCount"></a>
The number of services that are running on the cluster in an `ACTIVE` state. You can view these services with [ListServices](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html).
Type: Integer
Required: No

 ** attachments **   <a name="ECS-Type-Cluster-attachments"></a>
The resources attached to a cluster. When using a capacity provider with a cluster, the capacity provider and associated resources are returned as cluster attachments.
Type: Array of [Attachment](API_Attachment.md) objects
Required: No

 ** attachmentsStatus **   <a name="ECS-Type-Cluster-attachmentsStatus"></a>
The status of the capacity providers associated with the cluster. The following are the states that are returned.
UPDATE\_IN\_PROGRESS
The available capacity providers for the cluster are updating.
UPDATE\_COMPLETE
The capacity providers have successfully updated.
UPDATE\_FAILED
The capacity provider updates failed.
Type: String
Required: No

 ** capacityProviders **   <a name="ECS-Type-Cluster-capacityProviders"></a>
The capacity providers associated with the cluster.
Type: Array of strings
Required: No

 ** clusterArn **   <a name="ECS-Type-Cluster-clusterArn"></a>
The Amazon Resource Name (ARN) that identifies the cluster. For more information about the ARN format, see [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids) in the *Amazon ECS Developer Guide*.
Type: String
Required: No

 ** clusterName **   <a name="ECS-Type-Cluster-clusterName"></a>
A user-generated string that you use to identify your cluster.
Type: String
Required: No

 ** configuration **   <a name="ECS-Type-Cluster-configuration"></a>
The execute command and managed storage configuration for the cluster.
Type: [ClusterConfiguration](API_ClusterConfiguration.md) object
Required: No

 ** defaultCapacityProviderStrategy **   <a name="ECS-Type-Cluster-defaultCapacityProviderStrategy"></a>
The default capacity provider strategy for the cluster. When services or tasks are run in the cluster with no launch type or capacity provider strategy specified, the default capacity provider strategy is used.
Type: Array of [CapacityProviderStrategyItem](API_CapacityProviderStrategyItem.md) objects
Required: No

 ** pendingTasksCount **   <a name="ECS-Type-Cluster-pendingTasksCount"></a>
The number of tasks in the cluster that are in the `PENDING` state.
Type: Integer
Required: No

 ** registeredContainerInstancesCount **   <a name="ECS-Type-Cluster-registeredContainerInstancesCount"></a>
The number of container instances registered into the cluster. This includes container instances in both `ACTIVE` and `DRAINING` status.
Type: Integer
Required: No

 ** runningTasksCount **   <a name="ECS-Type-Cluster-runningTasksCount"></a>
The number of tasks in the cluster that are in the `RUNNING` state.
Type: Integer
Required: No

 ** serviceConnectDefaults **   <a name="ECS-Type-Cluster-serviceConnectDefaults"></a>
Use this parameter to set a default Service Connect namespace. After you set a default Service Connect namespace, any new services with Service Connect turned on that are created in the cluster are added as client services in the namespace. This setting only applies to new services that set the `enabled` parameter to `true` in the `ServiceConnectConfiguration`. You can set the namespace of each service individually in the `ServiceConnectConfiguration` to override this default parameter.
Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: [ClusterServiceConnectDefaults](API_ClusterServiceConnectDefaults.md) object
Required: No

 ** settings **   <a name="ECS-Type-Cluster-settings"></a>
The settings for the cluster. This parameter indicates whether CloudWatch Container Insights is on or off for a cluster.
Type: Array of [ClusterSetting](API_ClusterSetting.md) objects
Required: No

 ** statistics **   <a name="ECS-Type-Cluster-statistics"></a>
Additional information about your clusters that are separated by launch type. They include the following:
+ runningEC2TasksCount
+ RunningFargateTasksCount
+ pendingEC2TasksCount
+ pendingFargateTasksCount
+ activeEC2ServiceCount
+ activeFargateServiceCount
+ drainingEC2ServiceCount
+ drainingFargateServiceCount
Type: Array of [KeyValuePair](API_KeyValuePair.md) objects
Required: No

 ** status **   <a name="ECS-Type-Cluster-status"></a>
The status of the cluster. The following are the possible states that are returned.
ACTIVE
The cluster is ready to accept tasks and if applicable you can register container instances with the cluster.
PROVISIONING
The cluster has capacity providers that are associated with it and the resources needed for the capacity provider are being created.
DEPROVISIONING
The cluster has capacity providers that are associated with it and the resources needed for the capacity provider are being deleted.
FAILED
The cluster has capacity providers that are associated with it and the resources needed for the capacity provider have failed to create.
INACTIVE
The cluster has been deleted. Clusters with an `INACTIVE` status may remain discoverable in your account for a period of time. However, this behavior is subject to change in the future. We don't recommend that you rely on `INACTIVE` clusters persisting.
Type: String
Required: No

 ** tags **   <a name="ECS-Type-Cluster-tags"></a>
The metadata that you apply to the cluster to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.
The following basic restrictions apply to tags:
+ Maximum number of tags per resource - 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length - 128 Unicode characters in UTF-8
+ Maximum value length - 256 Unicode characters in UTF-8
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case-sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_Cluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/Cluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/Cluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/Cluster)
