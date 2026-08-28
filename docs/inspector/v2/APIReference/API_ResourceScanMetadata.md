---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ResourceScanMetadata.html
---

# ResourceScanMetadata
<a name="API_ResourceScanMetadata"></a>

An object that contains details about the metadata for an Amazon ECR resource.

## Contents
<a name="API_ResourceScanMetadata_Contents"></a>

 ** codeRepository **   <a name="inspector2-Type-ResourceScanMetadata-codeRepository"></a>
Contains metadata about scan coverage for a code repository resource.
Type: [CodeRepositoryMetadata](API_CodeRepositoryMetadata.md) object
Required: No

 ** containerImage **   <a name="inspector2-Type-ResourceScanMetadata-containerImage"></a>
The container image metadata associated with a covered resource.
Type: [ContainerImageMetadata](API_ContainerImageMetadata.md) object
Required: No

 ** containerRegistry **   <a name="inspector2-Type-ResourceScanMetadata-containerRegistry"></a>
The container registry metadata associated with a covered resource.
Type: [ContainerRegistryMetadata](API_ContainerRegistryMetadata.md) object
Required: No

 ** containerRepository **   <a name="inspector2-Type-ResourceScanMetadata-containerRepository"></a>
The container repository metadata associated with a covered resource.
Type: [ContainerRepositoryMetadata](API_ContainerRepositoryMetadata.md) object
Required: No

 ** ec2 **   <a name="inspector2-Type-ResourceScanMetadata-ec2"></a>
An object that contains metadata details for an Amazon EC2 instance.
Type: [Ec2Metadata](API_Ec2Metadata.md) object
Required: No

 ** ecrImage **   <a name="inspector2-Type-ResourceScanMetadata-ecrImage"></a>
An object that contains details about the container metadata for an Amazon ECR image.
Type: [EcrContainerImageMetadata](API_EcrContainerImageMetadata.md) object
Required: No

 ** ecrRepository **   <a name="inspector2-Type-ResourceScanMetadata-ecrRepository"></a>
An object that contains details about the repository an Amazon ECR image resides in.
Type: [EcrRepositoryMetadata](API_EcrRepositoryMetadata.md) object
Required: No

 ** lambdaFunction **   <a name="inspector2-Type-ResourceScanMetadata-lambdaFunction"></a>
An object that contains metadata details for an AWS Lambda function.
Type: [LambdaFunctionMetadata](API_LambdaFunctionMetadata.md) object
Required: No

 ** serverlessFunction **   <a name="inspector2-Type-ResourceScanMetadata-serverlessFunction"></a>
The serverless function metadata associated with a covered resource.
Type: [ServerlessFunctionMetadata](API_ServerlessFunctionMetadata.md) object
Required: No

 ** vmInstance **   <a name="inspector2-Type-ResourceScanMetadata-vmInstance"></a>
The VM instance metadata associated with a covered resource.
Type: [VmInstanceMetadata](API_VmInstanceMetadata.md) object
Required: No

## See Also
<a name="API_ResourceScanMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ResourceScanMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ResourceScanMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ResourceScanMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
