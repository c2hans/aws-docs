---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LabelingJobDataSource.html
---

# LabelingJobDataSource
<a name="API_LabelingJobDataSource"></a>

Provides information about the location of input data.

You must specify at least one of the following: `S3DataSource` or `SnsDataSource`.

Use `SnsDataSource` to specify an SNS input topic for a streaming labeling job. If you do not specify and SNS input topic ARN, Ground Truth will create a one-time labeling job.

Use `S3DataSource` to specify an input manifest file for both streaming and one-time labeling jobs. Adding an `S3DataSource` is optional if you use `SnsDataSource` to create a streaming labeling job.

## Contents
<a name="API_LabelingJobDataSource_Contents"></a>

 ** S3DataSource **   <a name="sagemaker-Type-LabelingJobDataSource-S3DataSource"></a>
The Amazon S3 location of the input data objects.
Type: [LabelingJobS3DataSource](API_LabelingJobS3DataSource.md) object
Required: No

 ** SnsDataSource **   <a name="sagemaker-Type-LabelingJobDataSource-SnsDataSource"></a>
An Amazon SNS data source used for streaming labeling jobs. To learn more, see [Send Data to a Streaming Labeling Job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-labeling-job.html#sms-streaming-how-it-works-send-data).
Type: [LabelingJobSnsDataSource](API_LabelingJobSnsDataSource.md) object
Required: No

## See Also
<a name="API_LabelingJobDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/LabelingJobDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/LabelingJobDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/LabelingJobDataSource)
