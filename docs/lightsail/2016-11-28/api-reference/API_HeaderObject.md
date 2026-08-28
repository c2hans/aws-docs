---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_HeaderObject.html
---

# HeaderObject
<a name="API_HeaderObject"></a>

Describes the request headers that a Lightsail distribution bases caching on.

For the headers that you specify, your distribution caches separate versions of the specified content based on the header values in viewer requests. For example, suppose viewer requests for `logo.jpg` contain a custom `product` header that has a value of either `acme` or `apex`, and you configure your distribution to cache your content based on values in the `product` header. Your distribution forwards the `product` header to the origin and caches the response from the origin once for each header value.

## Contents
<a name="API_HeaderObject_Contents"></a>

 ** headersAllowList **   <a name="Lightsail-Type-HeaderObject-headersAllowList"></a>
The specific headers to forward to your distribution's origin.
Type: Array of strings
Valid Values: `Accept | Accept-Charset | Accept-Datetime | Accept-Encoding | Accept-Language | Authorization | CloudFront-Forwarded-Proto | CloudFront-Is-Desktop-Viewer | CloudFront-Is-Mobile-Viewer | CloudFront-Is-SmartTV-Viewer | CloudFront-Is-Tablet-Viewer | CloudFront-Viewer-Country | Host | Origin | Referer`
Required: No

 ** option **   <a name="Lightsail-Type-HeaderObject-option"></a>
The headers that you want your distribution to forward to your origin and base caching on.
You can configure your distribution to do one of the following:
+  ** `all` ** - Forward all headers to your origin.
+  ** `none` ** - Forward only the default headers.
+  ** `allow-list` ** - Forward only the headers you specify using the `headersAllowList` parameter.
Type: String
Valid Values: `none | allow-list | all`
Required: No

## See Also
<a name="API_HeaderObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/HeaderObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/HeaderObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/HeaderObject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
