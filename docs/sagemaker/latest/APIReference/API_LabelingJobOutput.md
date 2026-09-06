---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LabelingJobOutput.html
---

# LabelingJobOutput
<a name="API_LabelingJobOutput"></a>

Specifies the location of the output produced by the labeling job.

## Contents
<a name="API_LabelingJobOutput_Contents"></a>

 ** OutputDatasetS3Uri **   <a name="sagemaker-Type-LabelingJobOutput-OutputDatasetS3Uri"></a>
The Amazon S3 bucket location of the manifest file for labeled data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** FinalActiveLearningModelArn **   <a name="sagemaker-Type-LabelingJobOutput-FinalActiveLearningModelArn"></a>
The Amazon Resource Name (ARN) for the most recent SageMaker model trained as part of automated data labeling.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:model/.*`
Required: No

## See Also
<a name="API_LabelingJobOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/LabelingJobOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/LabelingJobOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/LabelingJobOutput)
