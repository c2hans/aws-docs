---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_TrackingOptions.html
---

# TrackingOptions
<a name="API_TrackingOptions"></a>

An object that defines the tracking options for a configuration set. When you use the Amazon SES API v2 to send an email, it contains an invisible image that's used to track when recipients open your email. If your email contains links, those links are changed slightly in order to track when recipients click them.

These images and links include references to a domain operated by AWS. You can optionally configure the Amazon SES to use a domain that you operate for these images and links.

## Contents
<a name="API_TrackingOptions_Contents"></a>

 ** CustomRedirectDomain **   <a name="SES-Type-TrackingOptions-CustomRedirectDomain"></a>
The domain to use for tracking open and click events.
Type: String
Required: Yes

 ** HttpsPolicy **   <a name="SES-Type-TrackingOptions-HttpsPolicy"></a>
The https policy to use for tracking open and click events.
Type: String
Valid Values: `REQUIRE | REQUIRE_OPEN_ONLY | OPTIONAL`
Required: No

## See Also
<a name="API_TrackingOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/TrackingOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/TrackingOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/TrackingOptions)
