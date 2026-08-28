---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessingStopSelector.html
---

# StreamProcessingStopSelector
<a name="API_StreamProcessingStopSelector"></a>

 Specifies when to stop processing the stream. You can specify a maximum amount of time to process the video.

## Contents
<a name="API_StreamProcessingStopSelector_Contents"></a>

 ** MaxDurationInSeconds **   <a name="rekognition-Type-StreamProcessingStopSelector-MaxDurationInSeconds"></a>
 Specifies the maximum amount of time in seconds that you want the stream to be processed. The largest amount of time is 2 minutes. The default is 10 seconds.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 120.
Required: No

## See Also
<a name="API_StreamProcessingStopSelector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StreamProcessingStopSelector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/StreamProcessingStopSelector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/StreamProcessingStopSelector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
