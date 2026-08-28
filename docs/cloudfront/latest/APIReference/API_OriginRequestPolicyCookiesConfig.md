---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_OriginRequestPolicyCookiesConfig.html
---

# OriginRequestPolicyCookiesConfig
<a name="API_OriginRequestPolicyCookiesConfig"></a>

An object that determines whether any cookies in viewer requests (and if so, which cookies) are included in requests that CloudFront sends to the origin.

## Contents
<a name="API_OriginRequestPolicyCookiesConfig_Contents"></a>

 ** CookieBehavior **   <a name="cloudfront-Type-OriginRequestPolicyCookiesConfig-CookieBehavior"></a>
Determines whether cookies in viewer requests are included in requests that CloudFront sends to the origin. Valid values are:
+  `none` – No cookies in viewer requests are included in requests that CloudFront sends to the origin. Even when this field is set to `none`, any cookies that are listed in a `CachePolicy` *are* included in origin requests.
+  `whitelist` – Only the cookies in viewer requests that are listed in the `CookieNames` type are included in requests that CloudFront sends to the origin.
+  `all` – All cookies in viewer requests are included in requests that CloudFront sends to the origin.
+  `allExcept` – All cookies in viewer requests are included in requests that CloudFront sends to the origin, * **except** * for those listed in the `CookieNames` type, which are not included.
Type: String
Valid Values: `none | whitelist | all | allExcept`
Required: Yes

 ** Cookies **   <a name="cloudfront-Type-OriginRequestPolicyCookiesConfig-Cookies"></a>
Contains a list of cookie names.
Type: [CookieNames](API_CookieNames.md) object
Required: No

## See Also
<a name="API_OriginRequestPolicyCookiesConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginRequestPolicyCookiesConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginRequestPolicyCookiesConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginRequestPolicyCookiesConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
