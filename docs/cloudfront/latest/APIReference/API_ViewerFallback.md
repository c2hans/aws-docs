---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ViewerFallback.html
---

# ViewerFallback

The distribution whose certificate CloudFront uses for viewer requests that arrive on the connection group's Anycast static IPs without Server Name Indication (SNI). You can specify one distribution per Anycast static IP list.

## Contents
<a name="API_ViewerFallback_Contents"></a>

 ** DistributionId **   <a name="cloudfront-Type-ViewerFallback-DistributionId"></a>
The ID of the distribution whose certificate CloudFront uses to establish TLS connections for viewer requests that don't include SNI.
Type: String
Required: No

## See Also
<a name="API_ViewerFallback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ViewerFallback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ViewerFallback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ViewerFallback)
