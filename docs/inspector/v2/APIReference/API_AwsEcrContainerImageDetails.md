---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AwsEcrContainerImageDetails.html
---

# AwsEcrContainerImageDetails
<a name="API_AwsEcrContainerImageDetails"></a>

The image details of the Amazon ECR container image.

## Contents
<a name="API_AwsEcrContainerImageDetails_Contents"></a>

 ** imageHash **   <a name="inspector2-Type-AwsEcrContainerImageDetails-imageHash"></a>
The image hash of the Amazon ECR container image.
Type: String
Length Constraints: Fixed length of 71.
Pattern: `sha256:[a-z0-9]{64}`
Required: Yes

 ** registry **   <a name="inspector2-Type-AwsEcrContainerImageDetails-registry"></a>
The registry for the Amazon ECR container image.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** repositoryName **   <a name="inspector2-Type-AwsEcrContainerImageDetails-repositoryName"></a>
The name of the repository the Amazon ECR container image resides in.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** architecture **   <a name="inspector2-Type-AwsEcrContainerImageDetails-architecture"></a>
The architecture of the Amazon ECR container image.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** author **   <a name="inspector2-Type-AwsEcrContainerImageDetails-author"></a>
The image author of the Amazon ECR container image.
Type: String
Required: No

 ** imageTags **   <a name="inspector2-Type-AwsEcrContainerImageDetails-imageTags"></a>
The image tags attached to the Amazon ECR container image.
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

 ** inUseCount **   <a name="inspector2-Type-AwsEcrContainerImageDetails-inUseCount"></a>
The number of Amazon ECS tasks or Amazon EKS pods where the Amazon ECR container image is in use.
Type: Long
Required: No

 ** lastInUseAt **   <a name="inspector2-Type-AwsEcrContainerImageDetails-lastInUseAt"></a>
The last time an Amazon ECR image was used in an Amazon ECS task or Amazon EKS pod.
Type: Timestamp
Required: No

 ** platform **   <a name="inspector2-Type-AwsEcrContainerImageDetails-platform"></a>
The platform of the Amazon ECR container image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** pushedAt **   <a name="inspector2-Type-AwsEcrContainerImageDetails-pushedAt"></a>
The date and time the Amazon ECR container image was pushed.
Type: Timestamp
Required: No

## See Also
<a name="API_AwsEcrContainerImageDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AwsEcrContainerImageDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AwsEcrContainerImageDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AwsEcrContainerImageDetails)
