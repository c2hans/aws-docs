---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_DashTtmlConfiguration.html
---

# DashTtmlConfiguration
<a name="API_DashTtmlConfiguration"></a>

The settings for TTML subtitles.

## Contents
<a name="API_DashTtmlConfiguration_Contents"></a>

 ** TtmlProfile **   <a name="mediapackage-Type-DashTtmlConfiguration-TtmlProfile"></a>
The profile that MediaPackage uses when signaling subtitles in the manifest. `IMSC` is the default profile. `EBU-TT-D` produces subtitles that are compliant with the EBU-TT-D TTML profile. MediaPackage passes through subtitle styles to the manifest. For more information about EBU-TT-D subtitles, see [EBU-TT-D Subtitling Distribution Format](https://tech.ebu.ch/publications/tech3380).
Type: String
Valid Values: `IMSC_1 | EBU_TT_D_101`
Required: Yes

## See Also
<a name="API_DashTtmlConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/DashTtmlConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/DashTtmlConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/DashTtmlConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
