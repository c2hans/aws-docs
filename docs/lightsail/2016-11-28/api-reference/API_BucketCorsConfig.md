---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_BucketCorsConfig.html
---

# BucketCorsConfig
<a name="API_BucketCorsConfig"></a>

Describes the cross-origin resource sharing (CORS) configuration for a Lightsail bucket. CORS defines a way for client web applications that are loaded in one domain to interact with resources in a different domain. For more information, see [Configuring cross-origin resource sharing (CORS)](https://docs.aws.amazon.com/lightsail/latest/userguide/configure-cors.html).

## Contents
<a name="API_BucketCorsConfig_Contents"></a>

 ** rules **   <a name="Lightsail-Type-BucketCorsConfig-rules"></a>
A set of origins and methods (cross-origin access that you want to allow). You can add up to 20 rules to the configuration. The total size is limited to 64 KB.
Type: Array of [BucketCorsRule](API_BucketCorsRule.md) objects
Array Members: Maximum number of 20 items.
Required: No

## See Also
<a name="API_BucketCorsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/BucketCorsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/BucketCorsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/BucketCorsConfig)
