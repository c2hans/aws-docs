---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CoverageFilterCriteria.html
---

# CoverageFilterCriteria
<a name="API_CoverageFilterCriteria"></a>

A structure that identifies filter criteria for `GetCoverageStatistics`.

## Contents
<a name="API_CoverageFilterCriteria_Contents"></a>

 ** accountId **   <a name="inspector2-Type-CoverageFilterCriteria-accountId"></a>
An array of AWS account IDs to return coverage statistics for.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudContainerImageTags **   <a name="inspector2-Type-CoverageFilterCriteria-cloudContainerImageTags"></a>
The cloud container image tags to filter coverage results by.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudContainerRegistryName **   <a name="inspector2-Type-CoverageFilterCriteria-cloudContainerRegistryName"></a>
The cloud container registry name to filter coverage results by.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudContainerRepositoryName **   <a name="inspector2-Type-CoverageFilterCriteria-cloudContainerRepositoryName"></a>
The cloud container repository name to filter coverage results by.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudProvider **   <a name="inspector2-Type-CoverageFilterCriteria-cloudProvider"></a>
The cloud provider to filter coverage results by.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudProviderAccountId **   <a name="inspector2-Type-CoverageFilterCriteria-cloudProviderAccountId"></a>
The cloud provider account ID to filter coverage results by.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudProviderOrgId **   <a name="inspector2-Type-CoverageFilterCriteria-cloudProviderOrgId"></a>
The cloud provider organization ID to filter coverage results by.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudProviderRegion **   <a name="inspector2-Type-CoverageFilterCriteria-cloudProviderRegion"></a>
The cloud provider region to filter coverage results by.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudServerlessFunctionName **   <a name="inspector2-Type-CoverageFilterCriteria-cloudServerlessFunctionName"></a>
The cloud serverless function name to filter coverage results by.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudServerlessFunctionRuntime **   <a name="inspector2-Type-CoverageFilterCriteria-cloudServerlessFunctionRuntime"></a>
The cloud serverless function runtime to filter coverage results by.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudServerlessFunctionTags **   <a name="inspector2-Type-CoverageFilterCriteria-cloudServerlessFunctionTags"></a>
The cloud serverless function tags to filter coverage results by.
Type: Array of [CoverageMapFilter](API_CoverageMapFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** cloudVmInstanceTags **   <a name="inspector2-Type-CoverageFilterCriteria-cloudVmInstanceTags"></a>
The cloud VM instance tags to filter coverage results by.
Type: Array of [CoverageMapFilter](API_CoverageMapFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** codeRepositoryProjectName **   <a name="inspector2-Type-CoverageFilterCriteria-codeRepositoryProjectName"></a>
Filter criteria for code repositories based on project name.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** codeRepositoryProviderType **   <a name="inspector2-Type-CoverageFilterCriteria-codeRepositoryProviderType"></a>
Filter criteria for code repositories based on provider type (such as GitHub, GitLab, etc.).
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** codeRepositoryProviderTypeVisibility **   <a name="inspector2-Type-CoverageFilterCriteria-codeRepositoryProviderTypeVisibility"></a>
Filter criteria for code repositories based on visibility setting (public or private).
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ec2InstanceTags **   <a name="inspector2-Type-CoverageFilterCriteria-ec2InstanceTags"></a>
The Amazon EC2 instance tags to filter on.
Type: Array of [CoverageMapFilter](API_CoverageMapFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ecrImageInUseCount **   <a name="inspector2-Type-CoverageFilterCriteria-ecrImageInUseCount"></a>
The number of Amazon ECR images in use.
Type: Array of [CoverageNumberFilter](API_CoverageNumberFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ecrImageLastInUseAt **   <a name="inspector2-Type-CoverageFilterCriteria-ecrImageLastInUseAt"></a>
The Amazon ECR image that was last in use.
Type: Array of [CoverageDateFilter](API_CoverageDateFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ecrImageTags **   <a name="inspector2-Type-CoverageFilterCriteria-ecrImageTags"></a>
The Amazon ECR image tags to filter on.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ecrRepositoryName **   <a name="inspector2-Type-CoverageFilterCriteria-ecrRepositoryName"></a>
The Amazon ECR repository name to filter on.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** imagePulledAt **   <a name="inspector2-Type-CoverageFilterCriteria-imagePulledAt"></a>
The date an image was last pulled at.
Type: Array of [CoverageDateFilter](API_CoverageDateFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** lambdaFunctionName **   <a name="inspector2-Type-CoverageFilterCriteria-lambdaFunctionName"></a>
Returns coverage statistics for AWS Lambda functions filtered by function names.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** lambdaFunctionRuntime **   <a name="inspector2-Type-CoverageFilterCriteria-lambdaFunctionRuntime"></a>
Returns coverage statistics for AWS Lambda functions filtered by runtime.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** lambdaFunctionTags **   <a name="inspector2-Type-CoverageFilterCriteria-lambdaFunctionTags"></a>
Returns coverage statistics for AWS Lambda functions filtered by tag.
Type: Array of [CoverageMapFilter](API_CoverageMapFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** lastScannedAt **   <a name="inspector2-Type-CoverageFilterCriteria-lastScannedAt"></a>
Filters AWS resources based on whether Amazon Inspector has checked them for vulnerabilities within the specified time range.
Type: Array of [CoverageDateFilter](API_CoverageDateFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** lastScannedCommitId **   <a name="inspector2-Type-CoverageFilterCriteria-lastScannedCommitId"></a>
Filter criteria for code repositories based on the ID of the last scanned commit.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** resourceId **   <a name="inspector2-Type-CoverageFilterCriteria-resourceId"></a>
An array of AWS resource IDs to return coverage statistics for.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** resourceType **   <a name="inspector2-Type-CoverageFilterCriteria-resourceType"></a>
An array of AWS resource types to return coverage statistics for. The values can be `AWS_EC2_INSTANCE`, `AWS_LAMBDA_FUNCTION`, `AWS_ECR_CONTAINER_IMAGE`, `AWS_ECR_REPOSITORY` or `AWS_ACCOUNT`.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** scanMode **   <a name="inspector2-Type-CoverageFilterCriteria-scanMode"></a>
The filter to search for Amazon EC2 instance coverage by scan mode. Valid values are `EC2_SSM_AGENT_BASED`, `EC2_AGENTLESS`, and `EC2_INSPECTOR_AGENT_BASED`.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** scanStatusCode **   <a name="inspector2-Type-CoverageFilterCriteria-scanStatusCode"></a>
The scan status code to filter on. Valid values are: `ValidationException`, `InternalServerException`, `ResourceNotFoundException`, `BadRequestException`, and `ThrottlingException`.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** scanStatusReason **   <a name="inspector2-Type-CoverageFilterCriteria-scanStatusReason"></a>
The scan status reason to filter on.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** scanType **   <a name="inspector2-Type-CoverageFilterCriteria-scanType"></a>
An array of Amazon Inspector scan types to return coverage statistics for.
Type: Array of [CoverageStringFilter](API_CoverageStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_CoverageFilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CoverageFilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CoverageFilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CoverageFilterCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
