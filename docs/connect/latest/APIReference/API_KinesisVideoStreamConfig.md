---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_KinesisVideoStreamConfig.html
---

# KinesisVideoStreamConfig
<a name="API_KinesisVideoStreamConfig"></a>

Configuration information of a Kinesis video stream.

## Contents
<a name="API_KinesisVideoStreamConfig_Contents"></a>

 ** EncryptionConfig **   <a name="connect-Type-KinesisVideoStreamConfig-EncryptionConfig"></a>
The encryption configuration.
Type: [EncryptionConfig](API_EncryptionConfig.md) object
Required: Yes

 ** Prefix **   <a name="connect-Type-KinesisVideoStreamConfig-Prefix"></a>
The prefix of the video stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** RetentionPeriodHours **   <a name="connect-Type-KinesisVideoStreamConfig-RetentionPeriodHours"></a>
The number of hours data is retained in the stream. Kinesis Video Streams retains the data in a data store that is associated with the stream.
The default value is 0, indicating that the stream does not persist data.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 87600.
Required: Yes

## See Also
<a name="API_KinesisVideoStreamConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/KinesisVideoStreamConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/KinesisVideoStreamConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/KinesisVideoStreamConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
