---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ServiceUpdate.html
---

# ServiceUpdate
<a name="API_ServiceUpdate"></a>

An update that you can apply to your Valkey or Redis OSS clusters.

## Contents
<a name="API_ServiceUpdate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AutoUpdateAfterRecommendedApplyByDate **
Indicates whether the service update will be automatically applied once the recommended apply-by date has expired.
Type: Boolean
Required: No

 ** Engine **
The Elasticache engine to which the update applies. Either Valkey, Redis OSS or Memcached.
Type: String
Required: No

 ** EngineVersion **
The Elasticache engine version to which the update applies. Either Valkey, Redis OSS or Memcached engine version.
Type: String
Required: No

 ** EstimatedUpdateTime **
The estimated length of time the service update will take
Type: String
Required: No

 ** ServiceUpdateDescription **
Provides details of the service update
Type: String
Required: No

 ** ServiceUpdateEndDate **
The date after which the service update is no longer available
Type: Timestamp
Required: No

 ** ServiceUpdateName **
The unique ID of the service update
Type: String
Required: No

 ** ServiceUpdateRecommendedApplyByDate **
The recommendend date to apply the service update in order to ensure compliance. For information on compliance, see [Self-Service Security Updates for Compliance](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/elasticache-compliance.html#elasticache-compliance-self-service).
Type: Timestamp
Required: No

 ** ServiceUpdateReleaseDate **
The date when the service update is initially available
Type: Timestamp
Required: No

 ** ServiceUpdateSeverity **
The severity of the service update
Type: String
Valid Values: `critical | important | medium | low`
Required: No

 ** ServiceUpdateStatus **
The status of the service update
Type: String
Valid Values: `available | cancelled | expired`
Required: No

 ** ServiceUpdateType **
Reflects the nature of the service update
Type: String
Valid Values: `security-update`
Required: No

## See Also
<a name="API_ServiceUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/ServiceUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/ServiceUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/ServiceUpdate)
