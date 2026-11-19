---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ResourceFilterCriteria.html
---

# ResourceFilterCriteria

The resource filter criteria for a Software bill of materials (SBOM) report.

## Contents
<a name="API_ResourceFilterCriteria_Contents"></a>

 ** accountId **   <a name="inspector2-Type-ResourceFilterCriteria-accountId"></a>
The account IDs used as resource filter criteria.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudContainerImageTags **   <a name="inspector2-Type-ResourceFilterCriteria-cloudContainerImageTags"></a>
The cloud container image tags used as resource filter criteria.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudContainerRegistryName **   <a name="inspector2-Type-ResourceFilterCriteria-cloudContainerRegistryName"></a>
The cloud container registry names used as resource filter criteria.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudContainerRepositoryName **   <a name="inspector2-Type-ResourceFilterCriteria-cloudContainerRepositoryName"></a>
The cloud container repository names used as resource filter criteria.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudProvider **   <a name="inspector2-Type-ResourceFilterCriteria-cloudProvider"></a>
The cloud providers used as resource filter criteria. Valid values:
+  `AWS` – AWS resources.
+  `AZURE` – Microsoft Azure resources.
+  `GCP` – Google Cloud Platform (GCP) resources.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudProviderAccountId **   <a name="inspector2-Type-ResourceFilterCriteria-cloudProviderAccountId"></a>
The cloud provider account IDs used as resource filter criteria. The value format depends on the cloud provider:
+ An AWS account ID.
+ An Azure subscription ID.
+ A Google Cloud Platform (GCP) project ID.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudProviderOrgId **   <a name="inspector2-Type-ResourceFilterCriteria-cloudProviderOrgId"></a>
The cloud provider organization IDs used as resource filter criteria. The value format depends on the cloud provider:
+ An AWS Organizations organization ID.
+ An Azure tenant ID.
+ A Google Cloud Platform (GCP) organization ID.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudProviderRegion **   <a name="inspector2-Type-ResourceFilterCriteria-cloudProviderRegion"></a>
The cloud provider regions used as resource filter criteria. The value format depends on the cloud provider:
+ An AWS Region, such as `us-east-1`.
+ An Azure region, such as `eastus`.
+ A Google Cloud Platform (GCP) location, such as the region `us-central1` or the zone `us-central1-a`.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudServerlessFunctionName **   <a name="inspector2-Type-ResourceFilterCriteria-cloudServerlessFunctionName"></a>
The cloud serverless function names used as resource filter criteria.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudServerlessFunctionRuntime **   <a name="inspector2-Type-ResourceFilterCriteria-cloudServerlessFunctionRuntime"></a>
The cloud serverless function runtimes used as resource filter criteria.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudServerlessFunctionTags **   <a name="inspector2-Type-ResourceFilterCriteria-cloudServerlessFunctionTags"></a>
The cloud serverless function tags used as resource filter criteria.
Type: Array of [ResourceMapFilter](API_ResourceMapFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudVmInstanceTags **   <a name="inspector2-Type-ResourceFilterCriteria-cloudVmInstanceTags"></a>
The cloud VM instance tags used as resource filter criteria.
Type: Array of [ResourceMapFilter](API_ResourceMapFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ec2InstanceTags **   <a name="inspector2-Type-ResourceFilterCriteria-ec2InstanceTags"></a>
The EC2 instance tags used as resource filter criteria.
Type: Array of [ResourceMapFilter](API_ResourceMapFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ecrImageTags **   <a name="inspector2-Type-ResourceFilterCriteria-ecrImageTags"></a>
The ECR image tags used as resource filter criteria.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ecrRepositoryName **   <a name="inspector2-Type-ResourceFilterCriteria-ecrRepositoryName"></a>
The ECR repository names used as resource filter criteria.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** lambdaFunctionName **   <a name="inspector2-Type-ResourceFilterCriteria-lambdaFunctionName"></a>
The AWS Lambda function name used as resource filter criteria.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** lambdaFunctionTags **   <a name="inspector2-Type-ResourceFilterCriteria-lambdaFunctionTags"></a>
The AWS Lambda function tags used as resource filter criteria.
Type: Array of [ResourceMapFilter](API_ResourceMapFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** resourceId **   <a name="inspector2-Type-ResourceFilterCriteria-resourceId"></a>
The resource IDs used as resource filter criteria.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** resourceType **   <a name="inspector2-Type-ResourceFilterCriteria-resourceType"></a>
The resource types used as resource filter criteria. Valid values:
+  AWS – `AWS_EC2_INSTANCE`, `AWS_ECR_CONTAINER_IMAGE`, `AWS_LAMBDA_FUNCTION`, or `MACHINE_IMAGE`.
+ Microsoft Azure – `Microsoft.Compute/virtualMachines`, `Microsoft.ContainerRegistry/registry/containerImage`, or `Microsoft.Web/sites`.
+ Google Cloud Platform (GCP) – `compute.googleapis.com/Instance`, `cloudfunctions.googleapis.com/Function`, or `artifactregistry.googleapis.com/DockerImage`.
Type: Array of [ResourceStringFilter](API_ResourceStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_ResourceFilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ResourceFilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ResourceFilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ResourceFilterCriteria)
