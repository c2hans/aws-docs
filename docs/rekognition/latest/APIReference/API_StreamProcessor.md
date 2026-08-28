---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessor.html
---

# StreamProcessor
<a name="API_StreamProcessor"></a>

An object that recognizes faces or labels in a streaming video. An Amazon Rekognition stream processor is created by a call to [CreateStreamProcessor](API_CreateStreamProcessor.md). The request parameters for `CreateStreamProcessor` describe the Kinesis video stream source for the streaming video, face recognition parameters, and where to stream the analysis resullts.

## Contents
<a name="API_StreamProcessor_Contents"></a>

 ** Name **   <a name="rekognition-Type-StreamProcessor-Name"></a>
Name of the Amazon Rekognition stream processor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: No

 ** Status **   <a name="rekognition-Type-StreamProcessor-Status"></a>
Current status of the Amazon Rekognition stream processor.
Type: String
Valid Values: `STOPPED | STARTING | RUNNING | FAILED | STOPPING | UPDATING`
Required: No

## See Also
<a name="API_StreamProcessor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StreamProcessor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/StreamProcessor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/StreamProcessor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
