---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ProtectedTask.html
---

# ProtectedTask
<a name="API_ProtectedTask"></a>

An object representing the protection status details for a task. You can set the protection status with the [UpdateTaskProtection](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateTaskProtection.html) API and get the status of tasks with the [GetTaskProtection](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GetTaskProtection.html) API.

## Contents
<a name="API_ProtectedTask_Contents"></a>

 ** expirationDate **   <a name="ECS-Type-ProtectedTask-expirationDate"></a>
The epoch time when protection for the task will expire.
Type: Timestamp
Required: No

 ** protectionEnabled **   <a name="ECS-Type-ProtectedTask-protectionEnabled"></a>
The protection status of the task. If scale-in protection is on for a task, the value is `true`. Otherwise, it is `false`.
Type: Boolean
Required: No

 ** taskArn **   <a name="ECS-Type-ProtectedTask-taskArn"></a>
The task ARN.
Type: String
Required: No

## See Also
<a name="API_ProtectedTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ProtectedTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ProtectedTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ProtectedTask)
