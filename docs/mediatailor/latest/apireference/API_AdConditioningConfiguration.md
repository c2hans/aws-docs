---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AdConditioningConfiguration.html
---

# AdConditioningConfiguration
<a name="API_AdConditioningConfiguration"></a>

The setting that indicates what conditioning MediaTailor will perform on ads that the ad decision server (ADS) returns.

## Contents
<a name="API_AdConditioningConfiguration_Contents"></a>

 ** StreamingMediaFileConditioning **   <a name="mediatailor-Type-AdConditioningConfiguration-StreamingMediaFileConditioning"></a>
For ads that have media files with streaming delivery and supported file extensions, indicates what transcoding action MediaTailor takes when it first receives these ads from the ADS. `TRANSCODE` indicates that MediaTailor must transcode the ads. `NONE` indicates that you have already transcoded the ads outside of MediaTailor and don't need them transcoded as part of the ad insertion workflow. For more information about ad conditioning see [Using preconditioned ads](https://docs.aws.amazon.com/mediatailor/latest/ug/precondition-ads.html) in the AWS Elemental MediaTailor user guide.
Type: String
Valid Values: `TRANSCODE | NONE`
Required: Yes

## See Also
<a name="API_AdConditioningConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/AdConditioningConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/AdConditioningConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/AdConditioningConfiguration)
