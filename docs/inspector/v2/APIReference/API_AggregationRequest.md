---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AggregationRequest.html
---

# AggregationRequest
<a name="API_AggregationRequest"></a>

Contains details about an aggregation request.

## Contents
<a name="API_AggregationRequest_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** accountAggregation **   <a name="inspector2-Type-AggregationRequest-accountAggregation"></a>
An object that contains details about an aggregation request based on AWS account IDs.
Type: [AccountAggregation](API_AccountAggregation.md) object
Required: No

 ** amiAggregation **   <a name="inspector2-Type-AggregationRequest-amiAggregation"></a>
An object that contains details about an aggregation request based on Amazon Machine Images (AMIs).
Type: [AmiAggregation](API_AmiAggregation.md) object
Required: No

 ** awsEcrContainerAggregation **   <a name="inspector2-Type-AggregationRequest-awsEcrContainerAggregation"></a>
An object that contains details about an aggregation request based on Amazon ECR container images.
Type: [AwsEcrContainerAggregation](API_AwsEcrContainerAggregation.md) object
Required: No

 ** codeRepositoryAggregation **   <a name="inspector2-Type-AggregationRequest-codeRepositoryAggregation"></a>
An object that contains details about an aggregation request based on code repositories.
Type: [CodeRepositoryAggregation](API_CodeRepositoryAggregation.md) object
Required: No

 ** containerImageAggregation **   <a name="inspector2-Type-AggregationRequest-containerImageAggregation"></a>
An object that contains details about an aggregation request based on container images.
Type: [ContainerImageAggregation](API_ContainerImageAggregation.md) object
Required: No

 ** ec2InstanceAggregation **   <a name="inspector2-Type-AggregationRequest-ec2InstanceAggregation"></a>
An object that contains details about an aggregation request based on Amazon EC2 instances.
Type: [Ec2InstanceAggregation](API_Ec2InstanceAggregation.md) object
Required: No

 ** findingTypeAggregation **   <a name="inspector2-Type-AggregationRequest-findingTypeAggregation"></a>
An object that contains details about an aggregation request based on finding types.
Type: [FindingTypeAggregation](API_FindingTypeAggregation.md) object
Required: No

 ** imageLayerAggregation **   <a name="inspector2-Type-AggregationRequest-imageLayerAggregation"></a>
An object that contains details about an aggregation request based on container image layers.
Type: [ImageLayerAggregation](API_ImageLayerAggregation.md) object
Required: No

 ** lambdaFunctionAggregation **   <a name="inspector2-Type-AggregationRequest-lambdaFunctionAggregation"></a>
Returns an object with findings aggregated by AWS Lambda function.
Type: [LambdaFunctionAggregation](API_LambdaFunctionAggregation.md) object
Required: No

 ** lambdaLayerAggregation **   <a name="inspector2-Type-AggregationRequest-lambdaLayerAggregation"></a>
Returns an object with findings aggregated by AWS Lambda layer.
Type: [LambdaLayerAggregation](API_LambdaLayerAggregation.md) object
Required: No

 ** packageAggregation **   <a name="inspector2-Type-AggregationRequest-packageAggregation"></a>
An object that contains details about an aggregation request based on operating system package type.
Type: [PackageAggregation](API_PackageAggregation.md) object
Required: No

 ** repositoryAggregation **   <a name="inspector2-Type-AggregationRequest-repositoryAggregation"></a>
An object that contains details about an aggregation request based on Amazon ECR repositories.
Type: [RepositoryAggregation](API_RepositoryAggregation.md) object
Required: No

 ** serverlessFunctionAggregation **   <a name="inspector2-Type-AggregationRequest-serverlessFunctionAggregation"></a>
An object that contains details about an aggregation request based on serverless functions.
Type: [ServerlessFunctionAggregation](API_ServerlessFunctionAggregation.md) object
Required: No

 ** titleAggregation **   <a name="inspector2-Type-AggregationRequest-titleAggregation"></a>
An object that contains details about an aggregation request based on finding title.
Type: [TitleAggregation](API_TitleAggregation.md) object
Required: No

 ** vmInstanceAggregation **   <a name="inspector2-Type-AggregationRequest-vmInstanceAggregation"></a>
An object that contains details about an aggregation request based on virtual machine (VM) instances.
Type: [VmInstanceAggregation](API_VmInstanceAggregation.md) object
Required: No

## See Also
<a name="API_AggregationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AggregationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AggregationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AggregationRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
