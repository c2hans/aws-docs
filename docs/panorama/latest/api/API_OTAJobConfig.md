---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_OTAJobConfig.html
---

# OTAJobConfig
<a name="API_OTAJobConfig"></a>

An over-the-air update (OTA) job configuration.

## Contents
<a name="API_OTAJobConfig_Contents"></a>

 ** ImageVersion **   <a name="panorama-Type-OTAJobConfig-ImageVersion"></a>
The target version of the device software.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: Yes

 ** AllowMajorVersionUpdate **   <a name="panorama-Type-OTAJobConfig-AllowMajorVersionUpdate"></a>
Whether to apply the update if it is a major version change.
Type: Boolean
Required: No

## See Also
<a name="API_OTAJobConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/OTAJobConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/OTAJobConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/OTAJobConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
