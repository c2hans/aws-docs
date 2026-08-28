---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_KinesisVideoStreamStartSelector.html
---

# KinesisVideoStreamStartSelector
<a name="API_KinesisVideoStreamStartSelector"></a>

Specifies the starting point in a Kinesis stream to start processing. You can use the producer timestamp or the fragment number. One of either producer timestamp or fragment number is required. If you use the producer timestamp, you must put the time in milliseconds. For more information about fragment numbers, see [Fragment](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_Fragment.html).

## Contents
<a name="API_KinesisVideoStreamStartSelector_Contents"></a>

 ** FragmentNumber **   <a name="rekognition-Type-KinesisVideoStreamStartSelector-FragmentNumber"></a>
 The unique identifier of the fragment. This value monotonically increases based on the ingestion order.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9]+$`
Required: No

 ** ProducerTimestamp **   <a name="rekognition-Type-KinesisVideoStreamStartSelector-ProducerTimestamp"></a>
 The timestamp from the producer corresponding to the fragment, in milliseconds, expressed in unix time format.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_KinesisVideoStreamStartSelector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/KinesisVideoStreamStartSelector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/KinesisVideoStreamStartSelector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/KinesisVideoStreamStartSelector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
