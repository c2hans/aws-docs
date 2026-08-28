---
source_url: https://docs.aws.amazon.com/appsync/latest/APIReference/API_CachingConfig.html
---

# CachingConfig
<a name="API_CachingConfig"></a>

The caching configuration for a resolver that has caching activated.

## Contents
<a name="API_CachingConfig_Contents"></a>

 ** ttl **   <a name="appsync-Type-CachingConfig-ttl"></a>
The TTL in seconds for a resolver that has caching activated.
Valid values are 1–3,600 seconds.
Type: Long
Required: Yes

 ** cachingKeys **   <a name="appsync-Type-CachingConfig-cachingKeys"></a>
The caching keys for a resolver that has caching activated.
Valid values are entries from the `$context.arguments`, `$context.source`, and `$context.identity` maps.
Type: Array of strings
Required: No

## See Also
<a name="API_CachingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/CachingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/CachingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/CachingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
