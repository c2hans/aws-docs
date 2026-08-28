---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DestinationConfiguration.html
---

# DestinationConfiguration
<a name="API_DestinationConfiguration"></a>

Complex data type that defines destination-configuration objects.

## Contents
<a name="API_DestinationConfiguration_Contents"></a>

 ** channel **   <a name="ivsrealtimeeapireference-Type-DestinationConfiguration-channel"></a>
An IVS channel to be used for broadcasting, for server-side composition. Either a `channel` or an `s3` must be specified.
Type: [ChannelDestinationConfiguration](API_ChannelDestinationConfiguration.md) object
Required: No

 ** name **   <a name="ivsrealtimeeapireference-Type-DestinationConfiguration-name"></a>
Name that can be specified to help identify the destination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** s3 **   <a name="ivsrealtimeeapireference-Type-DestinationConfiguration-s3"></a>
An S3 storage configuration to be used for recording video data. Either a `channel` or an `s3` must be specified.
Type: [S3DestinationConfiguration](API_S3DestinationConfiguration.md) object
Required: No

## See Also
<a name="API_DestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/DestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/DestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/DestinationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
