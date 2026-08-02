---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ProcessedUpdateAction.html
---

# ProcessedUpdateAction
<a name="API_ProcessedUpdateAction"></a>

Update action that has been processed for the corresponding apply/stop request

## Contents
<a name="API_ProcessedUpdateAction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CacheClusterId **
The ID of the cache cluster
Type: String
Required: No

 ** ReplicationGroupId **
The ID of the replication group
Type: String
Required: No

 ** ServiceUpdateName **
The unique ID of the service update
Type: String
Required: No

 ** UpdateActionStatus **
The status of the update action on the Valkey or Redis OSS cluster
Type: String
Valid Values: `not-applied | waiting-to-start | in-progress | stopping | stopped | complete | scheduling | scheduled | not-applicable`
Required: No

## See Also
<a name="API_ProcessedUpdateAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/ProcessedUpdateAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/ProcessedUpdateAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/ProcessedUpdateAction)
