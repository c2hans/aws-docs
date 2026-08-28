---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionDetails.html
---

# AwsEcsTaskDefinitionDetails
<a name="API_AwsEcsTaskDefinitionDetails"></a>

Details about a task definition. A task definition describes the container and volume definitions of an Amazon Elastic Container Service task.

## Contents
<a name="API_AwsEcsTaskDefinitionDetails_Contents"></a>

 ** ContainerDefinitions **   <a name="securityhub-Type-AwsEcsTaskDefinitionDetails-ContainerDefinitions"></a>
The container definitions that describe the containers that make up the task.
Type: Array of [AwsEcsTaskDefinitionContainerDefinitionsDetails](API_AwsEcsTaskDefinitionContainerDefinitionsDetails.md) objects
Required: No

 ** Cpu **   <a name="securityhub-Type-AwsEcsTaskDefinitionDetails-Cpu"></a>
The number of CPU units used by the task.Valid values are as follows:
+  `256 (.25 vCPU)`
+  `512 (.5 vCPU)`
+  `1024 (1 vCPU)`
+  `2048 (2 vCPU)`
+  `4096 (4 vCPU)`
Type: String
Pattern: `.*\S.*`
Required: No

 ** ExecutionRoleArn **   <a name="securityhub-Type-AwsEcsTaskDefinitionDetails-ExecutionRoleArn"></a>
The ARN of the task execution role that grants the container agent permission to make API calls on behalf of the container user.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Family **   <a name="securityhub-Type-AwsEcsTaskDefinitionDetails-Family"></a>
The name of a family that this task definition is registered to.
Type: String
Pattern: `.*\S.*`
Required: No

 ** InferenceAccelerators **   <a name="securityhub-Type-AwsEcsTaskDefinitionDetails-InferenceAccelerators"></a>
The Elastic Inference accelerators to use for the containers in the task.
Type: Array of [AwsEcsTaskDefinitionInferenceAcceleratorsDetails](API_AwsEcsTaskDefinitionInferenceAcceleratorsDetails.md) objects
Required: No

 ** IpcMode **   <a name="securityhub-Type-AwsEcsTaskDefinitionDetails-IpcMode"></a>
The inter-process communication (IPC) resource namespace to use for the containers in the task. Valid values are as follows:
+  `host`
+  `none`
+  `task`
Type: String
Pattern: `.*\S.*`
Required: No

 ** Memory **   <a name="securityhub-Type-AwsEcsTaskDefinitionDetails-Memory"></a>
The amount (in MiB) of memory used by the task.
For tasks that are hosted on Amazon EC2, you can provide a task-level memory value or a container-level memory value. For tasks that are hosted on AWS Fargate, you must use one of the [specified values](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#task_size) in the * *Amazon Elastic Container Service Developer Guide* *, which determines your range of supported values for the `Cpu` and `Memory` parameters.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NetworkMode **   <a name="securityhub-Type-AwsEcsTaskDefinitionDetails-NetworkMode"></a>
The Docker networking mode to use for the containers in the task. Valid values are as follows:
+  `awsvpc`
+  `bridge`
+  `host`
+  `none`
Type: String
Pattern: `.*\S.*`
Required: No

 ** PidMode **   <a name="securityhub-Type-AwsEcsTaskDefinitionDetails-PidMode"></a>
The process namespace to use for the containers in the task. Valid values are `host` or `task`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PlacementConstraints **   <a name="securityhub-Type-AwsEcsTaskDefinitionDetails-PlacementConstraints"></a>
The placement constraint objects to use for tasks.
Type: Array of [AwsEcsTaskDefinitionPlacementConstraintsDetails](API_AwsEcsTaskDefinitionPlacementConstraintsDetails.md) objects
Required: No

 ** ProxyConfiguration **   <a name="securityhub-Type-AwsEcsTaskDefinitionDetails-ProxyConfiguration"></a>
The configuration details for the App Mesh proxy.
Type: [AwsEcsTaskDefinitionProxyConfigurationDetails](API_AwsEcsTaskDefinitionProxyConfigurationDetails.md) object
Required: No

 ** RequiresCompatibilities **   <a name="securityhub-Type-AwsEcsTaskDefinitionDetails-RequiresCompatibilities"></a>
The task launch types that the task definition was validated against.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsEcsTaskDefinitionDetails-Status"></a>
 The status of the task definition.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TaskRoleArn **   <a name="securityhub-Type-AwsEcsTaskDefinitionDetails-TaskRoleArn"></a>
The short name or ARN of the IAM role that grants containers in the task permission to call AWS API operations on your behalf.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Volumes **   <a name="securityhub-Type-AwsEcsTaskDefinitionDetails-Volumes"></a>
The data volume definitions for the task.
Type: Array of [AwsEcsTaskDefinitionVolumesDetails](API_AwsEcsTaskDefinitionVolumesDetails.md) objects
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
