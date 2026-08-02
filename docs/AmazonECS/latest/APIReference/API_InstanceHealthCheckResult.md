---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_InstanceHealthCheckResult.html
---

# InstanceHealthCheckResult
<a name="API_InstanceHealthCheckResult"></a>

An object representing the result of a container instance health status check.

## Contents
<a name="API_InstanceHealthCheckResult_Contents"></a>

 ** lastStatusChange **   <a name="ECS-Type-InstanceHealthCheckResult-lastStatusChange"></a>
The Unix timestamp for when the container instance health status last changed.
Type: Timestamp
Required: No

 ** lastUpdated **   <a name="ECS-Type-InstanceHealthCheckResult-lastUpdated"></a>
The Unix timestamp for when the container instance health status was last updated.
Type: Timestamp
Required: No

 ** status **   <a name="ECS-Type-InstanceHealthCheckResult-status"></a>
The container instance health status.
Type: String
Valid Values: `OK | IMPAIRED | INSUFFICIENT_DATA | INITIALIZING`
Required: No

 ** statusReason **   <a name="ECS-Type-InstanceHealthCheckResult-statusReason"></a>
The reason for the container instance health status.
Type: String
Required: No

 ** type **   <a name="ECS-Type-InstanceHealthCheckResult-type"></a>
The type of container instance health status that was verified.
Type: String
Valid Values: `CONTAINER_RUNTIME | ACCELERATED_COMPUTE | DAEMON`
Required: No

## See Also
<a name="API_InstanceHealthCheckResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/InstanceHealthCheckResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/InstanceHealthCheckResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/InstanceHealthCheckResult)
