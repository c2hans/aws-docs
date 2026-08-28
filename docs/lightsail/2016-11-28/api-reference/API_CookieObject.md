---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CookieObject.html
---

# CookieObject
<a name="API_CookieObject"></a>

Describes whether an Amazon Lightsail content delivery network (CDN) distribution forwards cookies to the origin and, if so, which ones.

For the cookies that you specify, your distribution caches separate versions of the specified content based on the cookie values in viewer requests.

## Contents
<a name="API_CookieObject_Contents"></a>

 ** cookiesAllowList **   <a name="Lightsail-Type-CookieObject-cookiesAllowList"></a>
The specific cookies to forward to your distribution's origin.
Type: Array of strings
Required: No

 ** option **   <a name="Lightsail-Type-CookieObject-option"></a>
Specifies which cookies to forward to the distribution's origin for a cache behavior: `all`, `none`, or `allow-list` to forward only the cookies specified in the `cookiesAllowList` parameter.
Type: String
Valid Values: `none | allow-list | all`
Required: No

## See Also
<a name="API_CookieObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CookieObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CookieObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CookieObject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
