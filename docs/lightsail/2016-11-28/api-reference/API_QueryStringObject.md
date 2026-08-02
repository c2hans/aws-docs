---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_QueryStringObject.html
---

# QueryStringObject
<a name="API_QueryStringObject"></a>

Describes the query string parameters that an Amazon Lightsail content delivery network (CDN) distribution to bases caching on.

For the query strings that you specify, your distribution caches separate versions of the specified content based on the query string values in viewer requests.

## Contents
<a name="API_QueryStringObject_Contents"></a>

 ** option **   <a name="Lightsail-Type-QueryStringObject-option"></a>
Indicates whether the distribution forwards and caches based on query strings.
Type: Boolean
Required: No

 ** queryStringsAllowList **   <a name="Lightsail-Type-QueryStringObject-queryStringsAllowList"></a>
The specific query strings that the distribution forwards to the origin.
Your distribution will cache content based on the specified query strings.
If the `option` parameter is true, then your distribution forwards all query strings, regardless of what you specify using the `queryStringsAllowList` parameter.
Type: Array of strings
Required: No

## See Also
<a name="API_QueryStringObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/QueryStringObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/QueryStringObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/QueryStringObject)
