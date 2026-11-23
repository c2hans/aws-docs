---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DomainItem.html
---

# DomainItem

The domain for the specified distribution tenant.

## Contents
<a name="API_DomainItem_Contents"></a>

 ** Domain **   <a name="cloudfront-Type-DomainItem-Domain"></a>
The domain name.
Type: String
Required: Yes

 ** ServeOn **   <a name="cloudfront-Type-DomainItem-ServeOn"></a>
Specifies which requests for this domain CloudFront routes to the distribution tenant. Valid values are:
+  `any` – CloudFront routes requests for this domain to the distribution tenant regardless of the IP address that they arrive on. This is the default if you don't specify a value.
+  `anycast-ip-list-only` – CloudFront routes requests for this domain to the distribution tenant only when they arrive on the Anycast static IPs of the distribution tenant's connection group. CloudFront treats requests that arrive on other IP addresses as requests for an unknown domain.
Type: String
Valid Values: `any | anycast-ip-list-only`
Required: No

## See Also
<a name="API_DomainItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DomainItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DomainItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DomainItem)
