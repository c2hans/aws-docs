---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AggregationResponse.html
---

# AggregationResponse
<a name="API_AggregationResponse"></a>

A structure that contains details about the results of an aggregation type.

## Contents
<a name="API_AggregationResponse_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** accountAggregation **   <a name="inspector2-Type-AggregationResponse-accountAggregation"></a>
An object that contains details about an aggregation response based on AWS account IDs.
Type: [AccountAggregationResponse](API_AccountAggregationResponse.md) object
Required: No

 ** amiAggregation **   <a name="inspector2-Type-AggregationResponse-amiAggregation"></a>
An object that contains details about an aggregation response based on Amazon Machine Images (AMIs).
Type: [AmiAggregationResponse](API_AmiAggregationResponse.md) object
Required: No

 ** awsEcrContainerAggregation **   <a name="inspector2-Type-AggregationResponse-awsEcrContainerAggregation"></a>
An object that contains details about an aggregation response based on Amazon ECR container images.
Type: [AwsEcrContainerAggregationResponse](API_AwsEcrContainerAggregationResponse.md) object
Required: No

 ** codeRepositoryAggregation **   <a name="inspector2-Type-AggregationResponse-codeRepositoryAggregation"></a>
An object that contains details about an aggregation response based on code repositories.
Type: [CodeRepositoryAggregationResponse](API_CodeRepositoryAggregationResponse.md) object
Required: No

 ** containerImageAggregation **   <a name="inspector2-Type-AggregationResponse-containerImageAggregation"></a>
An object that contains details about an aggregation response based on container images.
Type: [ContainerImageAggregationResponse](API_ContainerImageAggregationResponse.md) object
Required: No

 ** ec2InstanceAggregation **   <a name="inspector2-Type-AggregationResponse-ec2InstanceAggregation"></a>
An object that contains details about an aggregation response based on Amazon EC2 instances.
Type: [Ec2InstanceAggregationResponse](API_Ec2InstanceAggregationResponse.md) object
Required: No

 ** findingTypeAggregation **   <a name="inspector2-Type-AggregationResponse-findingTypeAggregation"></a>
An object that contains details about an aggregation response based on finding types.
Type: [FindingTypeAggregationResponse](API_FindingTypeAggregationResponse.md) object
Required: No

 ** imageLayerAggregation **   <a name="inspector2-Type-AggregationResponse-imageLayerAggregation"></a>
An object that contains details about an aggregation response based on container image layers.
Type: [ImageLayerAggregationResponse](API_ImageLayerAggregationResponse.md) object
Required: No

 ** lambdaFunctionAggregation **   <a name="inspector2-Type-AggregationResponse-lambdaFunctionAggregation"></a>
An aggregation of findings by AWS Lambda function.
Type: [LambdaFunctionAggregationResponse](API_LambdaFunctionAggregationResponse.md) object
Required: No

 ** lambdaLayerAggregation **   <a name="inspector2-Type-AggregationResponse-lambdaLayerAggregation"></a>
An aggregation of findings by AWS Lambda layer.
Type: [LambdaLayerAggregationResponse](API_LambdaLayerAggregationResponse.md) object
Required: No

 ** packageAggregation **   <a name="inspector2-Type-AggregationResponse-packageAggregation"></a>
An object that contains details about an aggregation response based on operating system package type.
Type: [PackageAggregationResponse](API_PackageAggregationResponse.md) object
Required: No

 ** repositoryAggregation **   <a name="inspector2-Type-AggregationResponse-repositoryAggregation"></a>
An object that contains details about an aggregation response based on Amazon ECR repositories.
Type: [RepositoryAggregationResponse](API_RepositoryAggregationResponse.md) object
Required: No

 ** serverlessFunctionAggregation **   <a name="inspector2-Type-AggregationResponse-serverlessFunctionAggregation"></a>
An object that contains details about an aggregation response based on serverless functions.
Type: [ServerlessFunctionAggregationResponse](API_ServerlessFunctionAggregationResponse.md) object
Required: No

 ** titleAggregation **   <a name="inspector2-Type-AggregationResponse-titleAggregation"></a>
An object that contains details about an aggregation response based on finding title.
Type: [TitleAggregationResponse](API_TitleAggregationResponse.md) object
Required: No

 ** vmInstanceAggregation **   <a name="inspector2-Type-AggregationResponse-vmInstanceAggregation"></a>
An object that contains details about an aggregation response based on VM instances.
Type: [VmInstanceAggregationResponse](API_VmInstanceAggregationResponse.md) object
Required: No

## See Also
<a name="API_AggregationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AggregationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AggregationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AggregationResponse)
