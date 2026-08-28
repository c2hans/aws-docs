---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_EncodingConfig.html
---

# EncodingConfig
<a name="API_EncodingConfig"></a>

 The encoding configuration to apply to the NDI® source when transcoding it to a transport stream for downstream distribution. You can choose between several predefined encoding profiles based on common use cases.

## Contents
<a name="API_EncodingConfig_Contents"></a>

 ** encodingProfile **   <a name="mediaconnect-Type-EncodingConfig-encodingProfile"></a>
 The encoding profile to use when transcoding the NDI source content to a transport stream. You can change this value while the flow is running.
Type: String
Valid Values: `DISTRIBUTION_H264_DEFAULT | CONTRIBUTION_H264_DEFAULT`
Required: No

 ** videoMaxBitrate **   <a name="mediaconnect-Type-EncodingConfig-videoMaxBitrate"></a>
 The maximum video bitrate to use when transcoding the NDI source to a transport stream. This parameter enables you to override the default video bitrate within the encoding profile's supported range.
 The supported range is 10,000,000 - 50,000,000 bits per second (bps). If you don't specify a value, MediaConnect uses the default value of 20,000,000 bps.
Type: Integer
Required: No

## See Also
<a name="API_EncodingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/EncodingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/EncodingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/EncodingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
