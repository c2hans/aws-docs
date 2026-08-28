---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_NotificationDestinationConfig.html
---

# NotificationDestinationConfig
<a name="API_NotificationDestinationConfig"></a>

The structure that contains the information required to deliver a notification to a customer.

## Contents
<a name="API_NotificationDestinationConfig_Contents"></a>

 ** Uri **   <a name="KinesisVideo-Type-NotificationDestinationConfig-Uri"></a>
The Uniform Resource Identifier (URI) that identifies where the images will be delivered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_0-9]+:(//)?([^/]+)/?([^*]*)$`
Required: Yes

## See Also
<a name="API_NotificationDestinationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/NotificationDestinationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/NotificationDestinationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/NotificationDestinationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
