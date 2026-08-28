---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CacheBehavior.html
---

# CacheBehavior
<a name="API_CacheBehavior"></a>

Describes the default cache behavior of an Amazon Lightsail content delivery network (CDN) distribution.

## Contents
<a name="API_CacheBehavior_Contents"></a>

 ** behavior **   <a name="Lightsail-Type-CacheBehavior-behavior"></a>
The cache behavior of the distribution.
The following cache behaviors can be specified:
+  ** `cache` ** - This option is best for static sites. When specified, your distribution caches and serves your entire website as static content. This behavior is ideal for websites with static content that doesn't change depending on who views it, or for websites that don't use cookies, headers, or query strings to personalize content.
+  ** `dont-cache` ** - This option is best for sites that serve a mix of static and dynamic content. When specified, your distribution caches and serve only the content that is specified in the distribution's `CacheBehaviorPerPath` parameter. This behavior is ideal for websites or web applications that use cookies, headers, and query strings to personalize content for individual users.
Type: String
Valid Values: `dont-cache | cache`
Required: No

## See Also
<a name="API_CacheBehavior_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CacheBehavior)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CacheBehavior)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CacheBehavior)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
