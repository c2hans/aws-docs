---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_StreamSummary.html
---

# StreamSummary
<a name="API_StreamSummary"></a>

A summary of a stream.

## Contents
<a name="API_StreamSummary_Contents"></a>

 ** description **   <a name="iot-Type-StreamSummary-description"></a>
A description of the stream.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`
Required: No

 ** streamArn **   <a name="iot-Type-StreamSummary-streamArn"></a>
The stream ARN.
Type: String
Required: No

 ** streamId **   <a name="iot-Type-StreamSummary-streamId"></a>
The stream ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** streamVersion **   <a name="iot-Type-StreamSummary-streamVersion"></a>
The stream version.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

## See Also
<a name="API_StreamSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/StreamSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/StreamSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/StreamSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
