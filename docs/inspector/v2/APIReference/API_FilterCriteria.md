---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_FilterCriteria.html
---

# FilterCriteria
<a name="API_FilterCriteria"></a>

Details on the criteria used to define the filter.

## Contents
<a name="API_FilterCriteria_Contents"></a>

 ** awsAccountId **   <a name="inspector2-Type-FilterCriteria-awsAccountId"></a>
Details of the AWS account IDs used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudImageArchitecture **   <a name="inspector2-Type-FilterCriteria-cloudImageArchitecture"></a>
Filter criteria for the architecture of a container image.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudImageDigest **   <a name="inspector2-Type-FilterCriteria-cloudImageDigest"></a>
Filter criteria for the digest of a container image.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudImageInUseCount **   <a name="inspector2-Type-FilterCriteria-cloudImageInUseCount"></a>
Filter criteria for the in-use count of a container image.
Type: Array of [NumberFilter](API_NumberFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudImageLastInUseAt **   <a name="inspector2-Type-FilterCriteria-cloudImageLastInUseAt"></a>
Filter criteria for the last time a container image was in use.
Type: Array of [DateFilter](API_DateFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudImagePushedAt **   <a name="inspector2-Type-FilterCriteria-cloudImagePushedAt"></a>
Filter criteria for when a container image was pushed.
Type: Array of [DateFilter](API_DateFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudImageRegistry **   <a name="inspector2-Type-FilterCriteria-cloudImageRegistry"></a>
Filter criteria for the registry of a container image.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudImageRepositoryName **   <a name="inspector2-Type-FilterCriteria-cloudImageRepositoryName"></a>
Filter criteria for the repository name of a container image.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudImageTags **   <a name="inspector2-Type-FilterCriteria-cloudImageTags"></a>
Filter criteria for the tags of a container image.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudProvider **   <a name="inspector2-Type-FilterCriteria-cloudProvider"></a>
Filter criteria for the cloud provider.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudProviderAccountId **   <a name="inspector2-Type-FilterCriteria-cloudProviderAccountId"></a>
Filter criteria for the cloud provider account ID.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudProviderOrgId **   <a name="inspector2-Type-FilterCriteria-cloudProviderOrgId"></a>
Filter criteria for the cloud provider organization ID.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudProviderRegion **   <a name="inspector2-Type-FilterCriteria-cloudProviderRegion"></a>
Filter criteria for the cloud provider region.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudServerlessFunctionExecutionRole **   <a name="inspector2-Type-FilterCriteria-cloudServerlessFunctionExecutionRole"></a>
Filter criteria for the execution role of a serverless function.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudServerlessFunctionLastModifiedAt **   <a name="inspector2-Type-FilterCriteria-cloudServerlessFunctionLastModifiedAt"></a>
Filter criteria for when a serverless function was last modified.
Type: Array of [DateFilter](API_DateFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudServerlessFunctionName **   <a name="inspector2-Type-FilterCriteria-cloudServerlessFunctionName"></a>
Filter criteria for the name of a serverless function.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudServerlessFunctionRuntime **   <a name="inspector2-Type-FilterCriteria-cloudServerlessFunctionRuntime"></a>
Filter criteria for the runtime of a serverless function.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudVmImageReference **   <a name="inspector2-Type-FilterCriteria-cloudVmImageReference"></a>
Filter criteria for the image reference of a VM instance.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudVmNetworkId **   <a name="inspector2-Type-FilterCriteria-cloudVmNetworkId"></a>
Filter criteria for the network ID of a VM instance.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudVmSubnetIds **   <a name="inspector2-Type-FilterCriteria-cloudVmSubnetIds"></a>
Filter criteria for the subnet IDs of a VM instance.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** codeRepositoryProjectName **   <a name="inspector2-Type-FilterCriteria-codeRepositoryProjectName"></a>
Filter criteria for findings based on the project name in a code repository.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** codeRepositoryProviderType **   <a name="inspector2-Type-FilterCriteria-codeRepositoryProviderType"></a>
Filter criteria for findings based on the repository provider type (such as GitHub, GitLab, etc.).
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** codeVulnerabilityDetectorName **   <a name="inspector2-Type-FilterCriteria-codeVulnerabilityDetectorName"></a>
The name of the detector used to identify a code vulnerability in a Lambda function used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** codeVulnerabilityDetectorTags **   <a name="inspector2-Type-FilterCriteria-codeVulnerabilityDetectorTags"></a>
The detector type tag associated with the vulnerability used to filter findings. Detector tags group related vulnerabilities by common themes or tactics. For a list of available tags by programming language, see [Java tags](https://docs.aws.amazon.com/codeguru/detector-library/java/tags/), or [Python tags](https://docs.aws.amazon.com/codeguru/detector-library/python/tags/).
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** codeVulnerabilityFilePath **   <a name="inspector2-Type-FilterCriteria-codeVulnerabilityFilePath"></a>
The file path to the file in a Lambda function that contains a code vulnerability used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** componentId **   <a name="inspector2-Type-FilterCriteria-componentId"></a>
Details of the component IDs used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** componentType **   <a name="inspector2-Type-FilterCriteria-componentType"></a>
Details of the component types used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ec2InstanceImageId **   <a name="inspector2-Type-FilterCriteria-ec2InstanceImageId"></a>
Details of the Amazon EC2 instance image IDs used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ec2InstanceSubnetId **   <a name="inspector2-Type-FilterCriteria-ec2InstanceSubnetId"></a>
Details of the Amazon EC2 instance subnet IDs used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ec2InstanceVpcId **   <a name="inspector2-Type-FilterCriteria-ec2InstanceVpcId"></a>
Details of the Amazon EC2 instance VPC IDs used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ecrImageArchitecture **   <a name="inspector2-Type-FilterCriteria-ecrImageArchitecture"></a>
Details of the Amazon ECR image architecture types used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ecrImageHash **   <a name="inspector2-Type-FilterCriteria-ecrImageHash"></a>
Details of the Amazon ECR image hashes used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ecrImageInUseCount **   <a name="inspector2-Type-FilterCriteria-ecrImageInUseCount"></a>
Filter criteria indicating when details for an Amazon ECR image include when an Amazon ECR image is in use.
Type: Array of [NumberFilter](API_NumberFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ecrImageLastInUseAt **   <a name="inspector2-Type-FilterCriteria-ecrImageLastInUseAt"></a>
Filter criteria indicating when an Amazon ECR image was last used in an Amazon ECS cluster task or Amazon EKS cluster pod.
Type: Array of [DateFilter](API_DateFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ecrImagePushedAt **   <a name="inspector2-Type-FilterCriteria-ecrImagePushedAt"></a>
Details on the Amazon ECR image push date and time used to filter findings.
Type: Array of [DateFilter](API_DateFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ecrImageRegistry **   <a name="inspector2-Type-FilterCriteria-ecrImageRegistry"></a>
Details on the Amazon ECR registry used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ecrImageRepositoryName **   <a name="inspector2-Type-FilterCriteria-ecrImageRepositoryName"></a>
Details on the name of the Amazon ECR repository used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ecrImageTags **   <a name="inspector2-Type-FilterCriteria-ecrImageTags"></a>
The tags attached to the Amazon ECR container image.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** epssScore **   <a name="inspector2-Type-FilterCriteria-epssScore"></a>
The EPSS score used to filter findings.
Type: Array of [NumberFilter](API_NumberFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** exploitAvailable **   <a name="inspector2-Type-FilterCriteria-exploitAvailable"></a>
Filters the list of AWS Lambda findings by the availability of exploits.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** findingArn **   <a name="inspector2-Type-FilterCriteria-findingArn"></a>
Details on the finding ARNs used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** findingStatus **   <a name="inspector2-Type-FilterCriteria-findingStatus"></a>
Details on the finding status types used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** findingType **   <a name="inspector2-Type-FilterCriteria-findingType"></a>
Details on the finding types used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** firstObservedAt **   <a name="inspector2-Type-FilterCriteria-firstObservedAt"></a>
Details on the date and time a finding was first seen used to filter findings.
Type: Array of [DateFilter](API_DateFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** fixAvailable **   <a name="inspector2-Type-FilterCriteria-fixAvailable"></a>
Details on whether a fix is available through a version update. This value can be `YES`, `NO`, or `PARTIAL`. A `PARTIAL` fix means that some, but not all, of the packages identified in the finding have fixes available through updated versions.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** inspectorScore **   <a name="inspector2-Type-FilterCriteria-inspectorScore"></a>
The Amazon Inspector score to filter on.
Type: Array of [NumberFilter](API_NumberFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** lambdaFunctionExecutionRoleArn **   <a name="inspector2-Type-FilterCriteria-lambdaFunctionExecutionRoleArn"></a>
Filters the list of AWS Lambda functions by execution role.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** lambdaFunctionLastModifiedAt **   <a name="inspector2-Type-FilterCriteria-lambdaFunctionLastModifiedAt"></a>
Filters the list of AWS Lambda functions by the date and time that a user last updated the configuration, in [ISO 8601 format](https://www.iso.org/iso-8601-date-and-time-format.html)
Type: Array of [DateFilter](API_DateFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** lambdaFunctionLayers **   <a name="inspector2-Type-FilterCriteria-lambdaFunctionLayers"></a>
Filters the list of AWS Lambda functions by the function's [ layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html). A Lambda function can have up to five layers.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** lambdaFunctionName **   <a name="inspector2-Type-FilterCriteria-lambdaFunctionName"></a>
Filters the list of AWS Lambda functions by the name of the function.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** lambdaFunctionRuntime **   <a name="inspector2-Type-FilterCriteria-lambdaFunctionRuntime"></a>
Filters the list of AWS Lambda functions by the runtime environment for the Lambda function.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** lastObservedAt **   <a name="inspector2-Type-FilterCriteria-lastObservedAt"></a>
Details on the date and time a finding was last seen used to filter findings.
Type: Array of [DateFilter](API_DateFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** networkProtocol **   <a name="inspector2-Type-FilterCriteria-networkProtocol"></a>
Details on network protocol used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** portRange **   <a name="inspector2-Type-FilterCriteria-portRange"></a>
Details on the port ranges used to filter findings.
Type: Array of [PortRangeFilter](API_PortRangeFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** relatedVulnerabilities **   <a name="inspector2-Type-FilterCriteria-relatedVulnerabilities"></a>
Details on the related vulnerabilities used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** resourceId **   <a name="inspector2-Type-FilterCriteria-resourceId"></a>
Details on the resource IDs used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** resourceTags **   <a name="inspector2-Type-FilterCriteria-resourceTags"></a>
Details on the resource tags used to filter findings.
Type: Array of [MapFilter](API_MapFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** resourceType **   <a name="inspector2-Type-FilterCriteria-resourceType"></a>
Details on the resource types used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** severity **   <a name="inspector2-Type-FilterCriteria-severity"></a>
Details on the severity used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** title **   <a name="inspector2-Type-FilterCriteria-title"></a>
Details on the finding title used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** updatedAt **   <a name="inspector2-Type-FilterCriteria-updatedAt"></a>
Details on the date and time a finding was last updated at used to filter findings.
Type: Array of [DateFilter](API_DateFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** vendorSeverity **   <a name="inspector2-Type-FilterCriteria-vendorSeverity"></a>
Details on the vendor severity used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** vulnerabilityId **   <a name="inspector2-Type-FilterCriteria-vulnerabilityId"></a>
Details on the vulnerability ID used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** vulnerabilitySource **   <a name="inspector2-Type-FilterCriteria-vulnerabilitySource"></a>
Details on the vulnerability type used to filter findings.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** vulnerablePackages **   <a name="inspector2-Type-FilterCriteria-vulnerablePackages"></a>
Details on the vulnerable packages used to filter findings.
Type: Array of [PackageFilter](API_PackageFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_FilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/FilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/FilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/FilterCriteria)
