---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_LocalSizeConfig.html
---

# LocalSizeConfig
<a name="API_LocalSizeConfig"></a>

The configuration details that include the maximum size of the media (`MaxLocalMediaSizeInMB`) that you want to store for a stream on the Edge Agent, as well as the strategy that should be used (`StrategyOnFullSize`) when a stream's maximum size has been reached.

## Contents
<a name="API_LocalSizeConfig_Contents"></a>

 ** MaxLocalMediaSizeInMB **   <a name="KinesisVideo-Type-LocalSizeConfig-MaxLocalMediaSizeInMB"></a>
The overall maximum size of the media that you want to store for a stream on the Edge Agent.
Type: Integer
Valid Range: Minimum value of 64. Maximum value of 2000000.
Required: No

 ** StrategyOnFullSize **   <a name="KinesisVideo-Type-LocalSizeConfig-StrategyOnFullSize"></a>
The strategy to perform when a stream’s `MaxLocalMediaSizeInMB` limit is reached.
Type: String
Valid Values: `DELETE_OLDEST_MEDIA | DENY_NEW_MEDIA`
Required: No

## See Also
<a name="API_LocalSizeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/LocalSizeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/LocalSizeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/LocalSizeConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
