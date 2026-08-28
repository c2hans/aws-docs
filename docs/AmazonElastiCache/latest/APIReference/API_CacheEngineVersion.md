---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CacheEngineVersion.html
---

# CacheEngineVersion
<a name="API_CacheEngineVersion"></a>

Provides all of the details about a particular cache engine version.

## Contents
<a name="API_CacheEngineVersion_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CacheEngineDescription **
The description of the cache engine.
Type: String
Required: No

 ** CacheEngineVersionDescription **
The description of the cache engine version.
Type: String
Required: No

 ** CacheParameterGroupFamily **
The name of the cache parameter group family associated with this cache engine.
Valid values are: `memcached1.4` \| `memcached1.5` \| `memcached1.6` \| `redis2.6` \| `redis2.8` \| `redis3.2` \| `redis4.0` \| `redis5.0` \| `redis6.x` \| `redis7`
Type: String
Required: No

 ** Engine **
The name of the cache engine.
Type: String
Required: No

 ** EngineVersion **
The version number of the cache engine.
Type: String
Required: No

## See Also
<a name="API_CacheEngineVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/CacheEngineVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/CacheEngineVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/CacheEngineVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
