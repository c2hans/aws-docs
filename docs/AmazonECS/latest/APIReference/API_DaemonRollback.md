---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonRollback.html
---

# DaemonRollback
<a name="API_DaemonRollback"></a>

Information about a daemon deployment rollback.

## Contents
<a name="API_DaemonRollback_Contents"></a>

 ** reason **   <a name="ECS-Type-DaemonRollback-reason"></a>
The reason the rollback happened. For example, the circuit breaker initiated the rollback operation.
Type: String
Required: No

 ** rollbackCapacityProviders **   <a name="ECS-Type-DaemonRollback-rollbackCapacityProviders"></a>
The capacity providers involved in the rollback.
Type: Array of strings
Required: No

 ** rollbackTargetDaemonRevisionArn **   <a name="ECS-Type-DaemonRollback-rollbackTargetDaemonRevisionArn"></a>
The ARN of the daemon revision deployed as part of the rollback.
Type: String
Required: No

 ** startedAt **   <a name="ECS-Type-DaemonRollback-startedAt"></a>
The time that the rollback started. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.
Type: Timestamp
Required: No

## See Also
<a name="API_DaemonRollback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonRollback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonRollback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonRollback)
