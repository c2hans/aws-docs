---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsClusterDetails.html
---

# AwsEcsClusterDetails
<a name="API_AwsEcsClusterDetails"></a>

Provides details about an Amazon ECS cluster.

## Contents
<a name="API_AwsEcsClusterDetails_Contents"></a>

 ** ActiveServicesCount **   <a name="securityhub-Type-AwsEcsClusterDetails-ActiveServicesCount"></a>
The number of services that are running on the cluster in an `ACTIVE` state. You can view these services with the Amazon ECS [`ListServices`](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html) API operation.
Type: Integer
Required: No

 ** CapacityProviders **   <a name="securityhub-Type-AwsEcsClusterDetails-CapacityProviders"></a>
The short name of one or more capacity providers to associate with the cluster.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** ClusterArn **   <a name="securityhub-Type-AwsEcsClusterDetails-ClusterArn"></a>
The Amazon Resource Name (ARN) that identifies the cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ClusterName **   <a name="securityhub-Type-AwsEcsClusterDetails-ClusterName"></a>
A name that you use to identify your cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ClusterSettings **   <a name="securityhub-Type-AwsEcsClusterDetails-ClusterSettings"></a>
The setting to use to create the cluster. Specifically used to configure whether to enable CloudWatch Container Insights for the cluster.
Type: Array of [AwsEcsClusterClusterSettingsDetails](API_AwsEcsClusterClusterSettingsDetails.md) objects
Required: No

 ** Configuration **   <a name="securityhub-Type-AwsEcsClusterDetails-Configuration"></a>
The run command configuration for the cluster.
Type: [AwsEcsClusterConfigurationDetails](API_AwsEcsClusterConfigurationDetails.md) object
Required: No

 ** DefaultCapacityProviderStrategy **   <a name="securityhub-Type-AwsEcsClusterDetails-DefaultCapacityProviderStrategy"></a>
The default capacity provider strategy for the cluster. The default capacity provider strategy is used when services or tasks are run without a specified launch type or capacity provider strategy.
Type: Array of [AwsEcsClusterDefaultCapacityProviderStrategyDetails](API_AwsEcsClusterDefaultCapacityProviderStrategyDetails.md) objects
Required: No

 ** RegisteredContainerInstancesCount **   <a name="securityhub-Type-AwsEcsClusterDetails-RegisteredContainerInstancesCount"></a>
The number of container instances registered into the cluster. This includes container instances in both `ACTIVE` and `DRAINING` status.
Type: Integer
Required: No

 ** RunningTasksCount **   <a name="securityhub-Type-AwsEcsClusterDetails-RunningTasksCount"></a>
The number of tasks in the cluster that are in the `RUNNING` state.
Type: Integer
Required: No

 ** Status **   <a name="securityhub-Type-AwsEcsClusterDetails-Status"></a>
The status of the cluster.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsClusterDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsClusterDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsClusterDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsClusterDetails)
