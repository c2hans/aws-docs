---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CacheUsageLimits.html
---

# CacheUsageLimits
<a name="API_CacheUsageLimits"></a>

The usage limits for storage and ElastiCache Processing Units for the cache.

## Contents
<a name="API_CacheUsageLimits_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataStorage **
 The maximum data storage limit in the cache, expressed in Gigabytes.
Type: [DataStorage](API_DataStorage.md) object
Required: No

 ** ECPUPerSecond **
The configuration for the number of ElastiCache Processing Units (ECPU) the cache can consume per second.
Type: [ECPUPerSecond](API_ECPUPerSecond.md) object
Required: No

## See Also
<a name="API_CacheUsageLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/CacheUsageLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/CacheUsageLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/CacheUsageLimits)
