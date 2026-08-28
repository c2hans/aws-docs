---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterContentQualityAnalysisConfiguration.html
---

# RouterContentQualityAnalysisConfiguration
<a name="API_RouterContentQualityAnalysisConfiguration"></a>

The content quality analysis configuration for the router input.

**Important**
The content quality analysis feature only monitors the first video stream and the first audio stream it encounters within the router input source.

## Contents
<a name="API_RouterContentQualityAnalysisConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** contentLevel **   <a name="mediaconnect-Type-RouterContentQualityAnalysisConfiguration-contentLevel"></a>
The content quality analysis configuration.
Type: [ContentQualityAnalysisFeatureConfiguration](API_ContentQualityAnalysisFeatureConfiguration.md) object
Required: No

## See Also
<a name="API_RouterContentQualityAnalysisConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterContentQualityAnalysisConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterContentQualityAnalysisConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterContentQualityAnalysisConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
