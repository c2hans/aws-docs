---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_StreamInfo.html
---

# StreamInfo
<a name="API_StreamInfo"></a>

Information about a stream.

## Contents
<a name="API_StreamInfo_Contents"></a>

 ** createdAt **   <a name="iot-Type-StreamInfo-createdAt"></a>
The date when the stream was created.
Type: Timestamp
Required: No

 ** description **   <a name="iot-Type-StreamInfo-description"></a>
The description of the stream.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`
Required: No

 ** files **   <a name="iot-Type-StreamInfo-files"></a>
The files to stream.
Type: Array of [StreamFile](API_StreamFile.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** lastUpdatedAt **   <a name="iot-Type-StreamInfo-lastUpdatedAt"></a>
The date when the stream was last updated.
Type: Timestamp
Required: No

 ** roleArn **   <a name="iot-Type-StreamInfo-roleArn"></a>
An IAM role AWS IoT assumes to access your S3 files.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** streamArn **   <a name="iot-Type-StreamInfo-streamArn"></a>
The stream ARN.
Type: String
Required: No

 ** streamId **   <a name="iot-Type-StreamInfo-streamId"></a>
The stream ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** streamVersion **   <a name="iot-Type-StreamInfo-streamVersion"></a>
The stream version.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

## See Also
<a name="API_StreamInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/StreamInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/StreamInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/StreamInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
