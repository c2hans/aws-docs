---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-trustedexecutionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition TrustedExecutionConfiguration

The trusted execution configuration for a task. This configuration controls the isolation mode and attestation policy. You set this configuration when you register a task definition.

**Note**
Trusted execution is supported only for Amazon ECS Managed Instances.

## Syntax
<a name="aws-properties-ecs-taskdefinition-trustedexecutionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskdefinition-trustedexecutionconfiguration-syntax.json"></a>

```json
{
  "[AttestationPolicy](#cfn-ecs-taskdefinition-trustedexecutionconfiguration-attestationpolicy)" : {{String}},
  "[IsolationMode](#cfn-ecs-taskdefinition-trustedexecutionconfiguration-isolationmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-taskdefinition-trustedexecutionconfiguration-syntax.yaml"></a>

```yaml
  [AttestationPolicy](#cfn-ecs-taskdefinition-trustedexecutionconfiguration-attestationpolicy): {{String}}
  [IsolationMode](#cfn-ecs-taskdefinition-trustedexecutionconfiguration-isolationmode): {{String}}
```

## Properties
<a name="aws-properties-ecs-taskdefinition-trustedexecutionconfiguration-properties"></a>

`AttestationPolicy`  <a name="cfn-ecs-taskdefinition-trustedexecutionconfiguration-attestationpolicy"></a>
The base64-encoded attestation policy envelope for the task. The policy specifies which containers are allowed to run and the runtime configuration that is cryptographically attested. This parameter is required when `isolationMode` is `CONFIDENTIAL_SANDBOX`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsolationMode`  <a name="cfn-ecs-taskdefinition-trustedexecutionconfiguration-isolationmode"></a>
The isolation mode for tasks that use this task definition. The isolation mode determines how a task is isolated from other tasks on the same Amazon EC2 instance.
+ `SHARED`: The task shares the underlying Amazon EC2 instance with other tasks. This is the default isolation mode.
+ `ISOLATED_SANDBOX`: The task runs in its own [Nitro Sandbox](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nitro-sandboxes.html), which is a lightweight virtual machine that is isolated by the AWS Nitro System. Each task's sandbox is isolated from every other task's sandbox on the same Amazon EC2 instance, so one task can't access another task's memory or storage. For more information, see [Isolated and confidential tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/isolated-confidential-tasks.html) in *Amazon Elastic Container Service Developer Guide*.
+ `CONFIDENTIAL_SANDBOX`: The task runs in its own [Nitro Sandbox](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nitro-sandboxes.html), which is a lightweight virtual machine that is isolated by the AWS Nitro System, with cryptographic attestation. The host can't access the sandbox's memory or storage, and only the approved workload can decrypt data that you encrypt with your AWS Key Management Service key. For more information, see [Isolated and confidential tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/isolated-confidential-tasks.html) in *Amazon Elastic Container Service Developer Guide*.
*Required*: Yes
*Type*: String
*Allowed values*: `SHARED | ISOLATED_SANDBOX | CONFIDENTIAL_SANDBOX`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
