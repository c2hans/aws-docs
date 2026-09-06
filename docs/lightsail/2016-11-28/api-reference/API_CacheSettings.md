---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CacheSettings.html
---

# CacheSettings
<a name="API_CacheSettings"></a>

Describes the cache settings of an Amazon Lightsail content delivery network (CDN) distribution.

These settings apply only to your distribution's `cacheBehaviors` (including the `defaultCacheBehavior`) that have a `behavior` of `cache`.

## Contents
<a name="API_CacheSettings_Contents"></a>

 ** allowedHTTPMethods **   <a name="Lightsail-Type-CacheSettings-allowedHTTPMethods"></a>
The HTTP methods that are processed and forwarded to the distribution's origin.
You can specify the following options:
+  `GET,HEAD` - The distribution forwards the `GET` and `HEAD` methods.
+  `GET,HEAD,OPTIONS` - The distribution forwards the `GET`, `HEAD`, and `OPTIONS` methods.
+  `GET,HEAD,OPTIONS,PUT,PATCH,POST,DELETE` - The distribution forwards the `GET`, `HEAD`, `OPTIONS`, `PUT`, `PATCH`, `POST`, and `DELETE` methods.
If you specify the third option, you might need to restrict access to your distribution's origin so users can't perform operations that you don't want them to. For example, you might not want users to have permission to delete objects from your origin.
Type: String
Pattern: `.*\S.*`
Required: No

 ** cachedHTTPMethods **   <a name="Lightsail-Type-CacheSettings-cachedHTTPMethods"></a>
The HTTP method responses that are cached by your distribution.
You can specify the following options:
+  `GET,HEAD` - The distribution caches responses to the `GET` and `HEAD` methods.
+  `GET,HEAD,OPTIONS` - The distribution caches responses to the `GET`, `HEAD`, and `OPTIONS` methods.
Type: String
Pattern: `.*\S.*`
Required: No

 ** defaultTTL **   <a name="Lightsail-Type-CacheSettings-defaultTTL"></a>
The default amount of time that objects stay in the distribution's cache before the distribution forwards another request to the origin to determine whether the content has been updated.
The value specified applies only when the origin does not add HTTP headers such as `Cache-Control max-age`, `Cache-Control s-maxage`, and `Expires` to objects.
Type: Long
Required: No

 ** forwardedCookies **   <a name="Lightsail-Type-CacheSettings-forwardedCookies"></a>
An object that describes the cookies that are forwarded to the origin. Your content is cached based on the cookies that are forwarded.
Type: [CookieObject](API_CookieObject.md) object
Required: No

 ** forwardedHeaders **   <a name="Lightsail-Type-CacheSettings-forwardedHeaders"></a>
An object that describes the headers that are forwarded to the origin. Your content is cached based on the headers that are forwarded.
Type: [HeaderObject](API_HeaderObject.md) object
Required: No

 ** forwardedQueryStrings **   <a name="Lightsail-Type-CacheSettings-forwardedQueryStrings"></a>
An object that describes the query strings that are forwarded to the origin. Your content is cached based on the query strings that are forwarded.
Type: [QueryStringObject](API_QueryStringObject.md) object
Required: No

 ** maximumTTL **   <a name="Lightsail-Type-CacheSettings-maximumTTL"></a>
The maximum amount of time that objects stay in the distribution's cache before the distribution forwards another request to the origin to determine whether the object has been updated.
The value specified applies only when the origin adds HTTP headers such as `Cache-Control max-age`, `Cache-Control s-maxage`, and `Expires` to objects.
Type: Long
Required: No

 ** minimumTTL **   <a name="Lightsail-Type-CacheSettings-minimumTTL"></a>
The minimum amount of time that objects stay in the distribution's cache before the distribution forwards another request to the origin to determine whether the object has been updated.
A value of `0` must be specified for `minimumTTL` if the distribution is configured to forward all headers to the origin.
Type: Long
Required: No

## See Also
<a name="API_CacheSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CacheSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CacheSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CacheSettings)
