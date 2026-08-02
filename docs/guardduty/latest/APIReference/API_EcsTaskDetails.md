---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_EcsTaskDetails.html
---

# EcsTaskDetails
<a name="API_EcsTaskDetails"></a>

Contains information about the task in an ECS cluster.

## Contents
<a name="API_EcsTaskDetails_Contents"></a>

 ** arn **   <a name="guardduty-Type-EcsTaskDetails-arn"></a>
The Amazon Resource Name (ARN) of the task.
Type: String
Required: No

 ** containers **   <a name="guardduty-Type-EcsTaskDetails-containers"></a>
The containers that's associated with the task.
Type: Array of [Container](API_Container.md) objects
Required: No

 ** definitionArn **   <a name="guardduty-Type-EcsTaskDetails-definitionArn"></a>
The ARN of the task definition that creates the task.
Type: String
Required: No

 ** group **   <a name="guardduty-Type-EcsTaskDetails-group"></a>
The name of the task group that's associated with the task.
Type: String
Required: No

 ** launchType **   <a name="guardduty-Type-EcsTaskDetails-launchType"></a>
A capacity on which the task is running. For example, `Fargate` and `EC2`.
Type: String
Required: No

 ** startedAt **   <a name="guardduty-Type-EcsTaskDetails-startedAt"></a>
The Unix timestamp for the time when the task started.
Type: Timestamp
Required: No

 ** startedBy **   <a name="guardduty-Type-EcsTaskDetails-startedBy"></a>
Contains the tag specified when a task is started.
Type: String
Required: No

 ** tags **   <a name="guardduty-Type-EcsTaskDetails-tags"></a>
The tags of the ECS Task.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** createdAt **   <a name="guardduty-Type-EcsTaskDetails-createdAt"></a>
The Unix timestamp for the time when the task was created.
Type: Timestamp
Required: No

 ** version **   <a name="guardduty-Type-EcsTaskDetails-version"></a>
The version counter for the task.
Type: String
Required: No

 ** volumes **   <a name="guardduty-Type-EcsTaskDetails-volumes"></a>
The list of data volume definitions for the task.
Type: Array of [Volume](API_Volume.md) objects
Required: No

## See Also
<a name="API_EcsTaskDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/EcsTaskDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/EcsTaskDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/EcsTaskDetails)
