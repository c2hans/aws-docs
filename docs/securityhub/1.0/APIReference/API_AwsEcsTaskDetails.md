---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDetails.html
---

# AwsEcsTaskDetails
<a name="API_AwsEcsTaskDetails"></a>

Provides details about a task in a cluster.

## Contents
<a name="API_AwsEcsTaskDetails_Contents"></a>

 ** ClusterArn **   <a name="securityhub-Type-AwsEcsTaskDetails-ClusterArn"></a>
The Amazon Resource Name (ARN) of the cluster that hosts the task.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Containers **   <a name="securityhub-Type-AwsEcsTaskDetails-Containers"></a>
The containers that are associated with the task.
Type: Array of [AwsEcsContainerDetails](API_AwsEcsContainerDetails.md) objects
Required: No

 ** CreatedAt **   <a name="securityhub-Type-AwsEcsTaskDetails-CreatedAt"></a>
The Unix timestamp for the time when the task was created. More specifically, it's for the time when the task entered the `PENDING` state.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Group **   <a name="securityhub-Type-AwsEcsTaskDetails-Group"></a>
The name of the task group that's associated with the task.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StartedAt **   <a name="securityhub-Type-AwsEcsTaskDetails-StartedAt"></a>
The Unix timestamp for the time when the task started. More specifically, it's for the time when the task transitioned from the `PENDING` state to the `RUNNING` state.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StartedBy **   <a name="securityhub-Type-AwsEcsTaskDetails-StartedBy"></a>
The tag specified when a task is started. If an Amazon ECS service started the task, the `startedBy` parameter contains the deployment ID of that service.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TaskDefinitionArn **   <a name="securityhub-Type-AwsEcsTaskDetails-TaskDefinitionArn"></a>
The ARN of the task definition that creates the task.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Version **   <a name="securityhub-Type-AwsEcsTaskDetails-Version"></a>
The version counter for the task.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Volumes **   <a name="securityhub-Type-AwsEcsTaskDetails-Volumes"></a>
Details about the data volume that is used in a task definition.
Type: Array of [AwsEcsTaskVolumeDetails](API_AwsEcsTaskVolumeDetails.md) objects
Required: No

## See Also
<a name="API_AwsEcsTaskDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDetails)
