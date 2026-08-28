---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessingStartSelector.html
---

# StreamProcessingStartSelector
<a name="API_StreamProcessingStartSelector"></a>

This is a required parameter for label detection stream processors and should not be used to start a face search stream processor.

## Contents
<a name="API_StreamProcessingStartSelector_Contents"></a>

 ** KVSStreamStartSelector **   <a name="rekognition-Type-StreamProcessingStartSelector-KVSStreamStartSelector"></a>
 Specifies the starting point in the stream to start processing. This can be done with a producer timestamp or a fragment number in a Kinesis stream.
Type: [KinesisVideoStreamStartSelector](API_KinesisVideoStreamStartSelector.md) object
Required: No

## See Also
<a name="API_StreamProcessingStartSelector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StreamProcessingStartSelector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/StreamProcessingStartSelector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/StreamProcessingStartSelector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
