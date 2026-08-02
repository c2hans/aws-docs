---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ResourceDetails.html
---

# ResourceDetails
<a name="API_ResourceDetails"></a>

Contains details about the resource involved in the finding.

## Contents
<a name="API_ResourceDetails_Contents"></a>

 ** awsEc2Instance **   <a name="inspector2-Type-ResourceDetails-awsEc2Instance"></a>
An object that contains details about the Amazon EC2 instance involved in the finding.
Type: [AwsEc2InstanceDetails](API_AwsEc2InstanceDetails.md) object
Required: No

 ** awsEcrContainerImage **   <a name="inspector2-Type-ResourceDetails-awsEcrContainerImage"></a>
An object that contains details about the Amazon ECR container image involved in the finding.
Type: [AwsEcrContainerImageDetails](API_AwsEcrContainerImageDetails.md) object
Required: No

 ** awsLambdaFunction **   <a name="inspector2-Type-ResourceDetails-awsLambdaFunction"></a>
A summary of the information about an AWS Lambda function affected by a finding.
Type: [AwsLambdaFunctionDetails](API_AwsLambdaFunctionDetails.md) object
Required: No

 ** codeRepository **   <a name="inspector2-Type-ResourceDetails-codeRepository"></a>
Contains details about a code repository resource associated with a finding.
Type: [CodeRepositoryDetails](API_CodeRepositoryDetails.md) object
Required: No

 ** image **   <a name="inspector2-Type-ResourceDetails-image"></a>
An object that contains details about a container image involved in the finding.
Type: [Image](API_Image.md) object
Required: No

 ** serverlessFunction **   <a name="inspector2-Type-ResourceDetails-serverlessFunction"></a>
An object that contains details about a serverless function involved in the finding.
Type: [ServerlessFunction](API_ServerlessFunction.md) object
Required: No

 ** vm **   <a name="inspector2-Type-ResourceDetails-vm"></a>
An object that contains details about a VM instance involved in the finding.
Type: [Vm](API_Vm.md) object
Required: No

## See Also
<a name="API_ResourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ResourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ResourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ResourceDetails)
