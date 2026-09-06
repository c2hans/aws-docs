---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_CdnConfiguration.html
---

# CdnConfiguration
<a name="API_CdnConfiguration"></a>

The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.

## Contents
<a name="API_CdnConfiguration_Contents"></a>

 ** AdSegmentUrlPrefix **   <a name="mediatailor-Type-CdnConfiguration-AdSegmentUrlPrefix"></a>
A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the origin ads.mediatailor.*<region>*.amazonaws.com. Then specify the rule's name in this `AdSegmentUrlPrefix`. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.
Type: String
Required: No

 ** ContentSegmentUrlPrefix **   <a name="mediatailor-Type-CdnConfiguration-ContentSegmentUrlPrefix"></a>
A content delivery network (CDN) to cache content segments, so that content requests don’t always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the rule's name in this `ContentSegmentUrlPrefix`. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.
Type: String
Required: No

## See Also
<a name="API_CdnConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/CdnConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/CdnConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/CdnConfiguration)
