---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LabelingJobResourceConfig.html
---

# LabelingJobResourceConfig
<a name="API_LabelingJobResourceConfig"></a>

Configure encryption on the storage volume attached to the ML compute instance used to run automated data labeling model training and inference.

## Contents
<a name="API_LabelingJobResourceConfig_Contents"></a>

 ** VolumeKmsKeyId **   <a name="sagemaker-Type-LabelingJobResourceConfig-VolumeKmsKeyId"></a>
The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training and inference jobs used for automated data labeling.
You can only specify a `VolumeKmsKeyId` when you create a labeling job with automated data labeling enabled using the API operation `CreateLabelingJob`. You cannot specify an AWS KMS key to encrypt the storage volume used for automated data labeling model training and inference when you create a labeling job using the console. To learn more, see [Output Data and Storage Volume Encryption](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security.html).
The `VolumeKmsKeyId` can be any of the following formats:
+ KMS Key ID

   `"1234abcd-12ab-34cd-56ef-1234567890ab"`
+ Amazon Resource Name (ARN) of a KMS Key

   `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** VpcConfig **   <a name="sagemaker-Type-LabelingJobResourceConfig-VpcConfig"></a>
Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html).
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## See Also
<a name="API_LabelingJobResourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/LabelingJobResourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/LabelingJobResourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/LabelingJobResourceConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
