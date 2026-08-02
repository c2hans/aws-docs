---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CacheBehaviorPerPath.html
---

# CacheBehaviorPerPath
<a name="API_CacheBehaviorPerPath"></a>

Describes the per-path cache behavior of an Amazon Lightsail content delivery network (CDN) distribution.

A per-path cache behavior is used to override, or add an exception to, the default cache behavior of a distribution. For example, if the `cacheBehavior` is set to `cache`, then a per-path cache behavior can be used to specify a directory, file, or file type that your distribution will cache. Alternately, if the distribution's `cacheBehavior` is `dont-cache`, then a per-path cache behavior can be used to specify a directory, file, or file type that your distribution will not cache.

## Contents
<a name="API_CacheBehaviorPerPath_Contents"></a>

 ** behavior **   <a name="Lightsail-Type-CacheBehaviorPerPath-behavior"></a>
The cache behavior for the specified path.
You can specify one of the following per-path cache behaviors:
+  ** `cache` ** - This behavior caches the specified path.
+  ** `dont-cache` ** - This behavior doesn't cache the specified path.
Type: String
Valid Values: `dont-cache | cache`
Required: No

 ** path **   <a name="Lightsail-Type-CacheBehaviorPerPath-path"></a>
The path to a directory or file to cached, or not cache. Use an asterisk symbol to specify wildcard directories (`path/to/assets/*`), and file types (`*.html, *jpg, *js`). Directories and file paths are case-sensitive.
Examples:
+ Specify the following to cache all files in the document root of an Apache web server running on a Lightsail instance.

   `var/www/html/`
+ Specify the following file to cache only the index page in the document root of an Apache web server.

   `var/www/html/index.html`
+ Specify the following to cache only the .html files in the document root of an Apache web server.

   `var/www/html/*.html`
+ Specify the following to cache only the .jpg, .png, and .gif files in the images sub-directory of the document root of an Apache web server.

   `var/www/html/images/*.jpg`

   `var/www/html/images/*.png`

   `var/www/html/images/*.gif`

  Specify the following to cache all files in the images sub-directory of the document root of an Apache web server.

   `var/www/html/images/`
Type: String
Required: No

## See Also
<a name="API_CacheBehaviorPerPath_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CacheBehaviorPerPath)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CacheBehaviorPerPath)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CacheBehaviorPerPath)
