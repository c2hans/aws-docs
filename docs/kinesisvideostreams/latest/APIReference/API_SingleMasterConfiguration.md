---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_SingleMasterConfiguration.html
---

# SingleMasterConfiguration
<a name="API_SingleMasterConfiguration"></a>

A structure that contains the configuration for the `SINGLE_MASTER` channel type.

## Contents
<a name="API_SingleMasterConfiguration_Contents"></a>

 ** MessageTtlSeconds **   <a name="KinesisVideo-Type-SingleMasterConfiguration-MessageTtlSeconds"></a>
The period of time (in seconds) a signaling channel retains undelivered messages before they are discarded. Use [UpdateSignalingChannel](API_UpdateSignalingChannel.md) to update this value.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 120.
Required: No

## See Also
<a name="API_SingleMasterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/SingleMasterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/SingleMasterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/SingleMasterConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
