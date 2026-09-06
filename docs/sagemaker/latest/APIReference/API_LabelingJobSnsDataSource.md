---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LabelingJobSnsDataSource.html
---

# LabelingJobSnsDataSource
<a name="API_LabelingJobSnsDataSource"></a>

An Amazon SNS data source used for streaming labeling jobs.

## Contents
<a name="API_LabelingJobSnsDataSource_Contents"></a>

 ** SnsTopicArn **   <a name="sagemaker-Type-LabelingJobSnsDataSource-SnsTopicArn"></a>
The Amazon SNS input topic Amazon Resource Name (ARN). Specify the ARN of the input topic you will use to send new data objects to a streaming labeling job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sns:[a-z0-9\-]*:[0-9]{12}:[a-zA-Z0-9_.-]+`
Required: Yes

## See Also
<a name="API_LabelingJobSnsDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/LabelingJobSnsDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/LabelingJobSnsDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/LabelingJobSnsDataSource)
