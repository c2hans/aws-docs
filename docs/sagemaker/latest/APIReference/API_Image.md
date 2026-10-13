---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Image.html
---

# Image
<a name="API_Image"></a>

A SageMaker AI image. A SageMaker AI image represents a set of container images that are derived from a common base container image. Each of these container images is represented by a SageMaker AI `ImageVersion`.

## Contents
<a name="API_Image_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-Image-CreationTime"></a>
When the image was created.
Type: Timestamp
Required: Yes

 ** ImageArn **   <a name="sagemaker-Type-Image-ImageArn"></a>
The ARN of the image.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:sagemaker:.+:[0-9]{12}:image/[a-zA-Z0-9]([-.]?[a-zA-Z0-9])*`
Required: Yes

 ** ImageName **   <a name="sagemaker-Type-Image-ImageName"></a>
The name of the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([-.]?[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ImageStatus **   <a name="sagemaker-Type-Image-ImageStatus"></a>
The status of the image.
Type: String
Valid Values: `CREATING | CREATED | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | DELETE_FAILED`
Required: Yes

 ** LastModifiedTime **   <a name="sagemaker-Type-Image-LastModifiedTime"></a>
When the image was last modified.
Type: Timestamp
Required: Yes

 ** Description **   <a name="sagemaker-Type-Image-Description"></a>
The description of the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*`
Required: No

 ** DisplayName **   <a name="sagemaker-Type-Image-DisplayName"></a>
The name of the image as displayed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\S(.*\S)?`
Required: No

 ** FailureReason **   <a name="sagemaker-Type-Image-FailureReason"></a>
When a create, update, or delete operation fails, the reason for the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_Image_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Image)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Image)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Image)
