---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_RenditionConfiguration.html
---

# RenditionConfiguration
<a name="API_RenditionConfiguration"></a>

Object that describes which renditions should be recorded for a stream.

## Contents
<a name="API_RenditionConfiguration_Contents"></a>

 ** renditions **   <a name="ivs-Type-RenditionConfiguration-renditions"></a>
Indicates which renditions are recorded for a stream, if `renditionSelection` is `CUSTOM`; otherwise, this field is irrelevant. The selected renditions are recorded if they are available during the stream. If a selected rendition is unavailable, the best available rendition is recorded. For details on the resolution dimensions of each rendition, see [Auto-Record to Amazon S3](https://docs.aws.amazon.com/ivs/latest/userguide/record-to-s3.html).
Type: Array of strings
Valid Values: `SD | HD | FULL_HD | LOWEST_RESOLUTION`
Required: No

 ** renditionSelection **   <a name="ivs-Type-RenditionConfiguration-renditionSelection"></a>
Indicates which set of renditions are recorded for a stream. For `BASIC` channels, the `CUSTOM` value has no effect. If `CUSTOM` is specified, a set of renditions must be specified in the `renditions` field. Default: `ALL`.
Type: String
Valid Values: `ALL | NONE | CUSTOM`
Required: No

## See Also
<a name="API_RenditionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/RenditionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/RenditionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/RenditionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
