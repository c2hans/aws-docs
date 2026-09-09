---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ImageVersion.html
---

# ImageVersion
<a name="API_ImageVersion"></a>

A version of a SageMaker AI `Image`. A version represents an existing container image.

## Contents
<a name="API_ImageVersion_Contents"></a>

 ** ImageArn **   <a name="sagemaker-Type-ImageVersion-ImageArn"></a>
The ARN of the image the version is based on.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:sagemaker:.+:[0-9]{12}:image/[a-zA-Z0-9]([-.]?[a-zA-Z0-9])*`
Required: Yes

 ** ImageVersionArn **   <a name="sagemaker-Type-ImageVersion-ImageVersionArn"></a>
The ARN of the version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws(-[\w]+)*:sagemaker:.+:[0-9]{12}:image-version/[a-z0-9]([-.]?[a-z0-9])*/[0-9]+|None)`
Required: Yes

 ** ImageVersionStatus **   <a name="sagemaker-Type-ImageVersion-ImageVersionStatus"></a>
The status of the version.
Type: String
Valid Values: `CREATING | CREATED | CREATE_FAILED | DELETING | DELETE_FAILED`
Required: Yes

 ** Version **   <a name="sagemaker-Type-ImageVersion-Version"></a>
The version number.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** FailureReason **   <a name="sagemaker-Type-ImageVersion-FailureReason"></a>
When a create or delete operation fails, the reason for the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_ImageVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ImageVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ImageVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ImageVersion)
