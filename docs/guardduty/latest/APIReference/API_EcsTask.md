---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_EcsTask.html
---

# EcsTask
<a name="API_EcsTask"></a>

Contains information about Amazon ECS task involved in a GuardDuty finding, including task definition and container identifiers.

## Contents
<a name="API_EcsTask_Contents"></a>

 ** containerUids **   <a name="guardduty-Type-EcsTask-containerUids"></a>
A list of unique identifiers for the containers associated with the Amazon ECS task.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** createdAt **   <a name="guardduty-Type-EcsTask-createdAt"></a>
The timestamp indicating when the Amazon ECS task was created, in UTC format.
Type: Timestamp
Required: No

 ** launchType **   <a name="guardduty-Type-EcsTask-launchType"></a>
The infrastructure type on which the Amazon ECS task runs.
Type: String
Valid Values: `FARGATE | EC2`
Required: No

 ** taskDefinitionArn **   <a name="guardduty-Type-EcsTask-taskDefinitionArn"></a>
The ARN of task definition which describes the container and volume definitions of the Amazon ECS task.
Type: String
Required: No

## See Also
<a name="API_EcsTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/EcsTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/EcsTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/EcsTask)
