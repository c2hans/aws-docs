---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TrustedExecutionConfiguration.html
---

# TrustedExecutionConfiguration
<a name="API_TrustedExecutionConfiguration"></a>

The trusted execution configuration for a task. This configuration controls the isolation mode and attestation policy. You set this configuration when you register a task definition.

**Note**
Trusted execution is supported only for Amazon ECS Managed Instances.

## Contents
<a name="API_TrustedExecutionConfiguration_Contents"></a>

 ** isolationMode **   <a name="ECS-Type-TrustedExecutionConfiguration-isolationMode"></a>
The isolation mode for tasks that use this task definition. The isolation mode determines how a task is isolated from other tasks on the same Amazon EC2 instance.
+  `SHARED`: The task shares the underlying Amazon EC2 instance with other tasks. This is the default isolation mode.
+  `ISOLATED_SANDBOX`: The task runs in its own [Nitro Sandbox](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nitro-sandboxes.html), which is a lightweight virtual machine that is isolated by the AWS Nitro System. Each task's sandbox is isolated from every other task's sandbox on the same Amazon EC2 instance, so one task can't access another task's memory or storage. For more information, see [Isolated and confidential tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/isolated-confidential-tasks.html) in *Amazon Elastic Container Service Developer Guide*.
+  `CONFIDENTIAL_SANDBOX`: The task runs in its own [Nitro Sandbox](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nitro-sandboxes.html), which is a lightweight virtual machine that is isolated by the AWS Nitro System, with cryptographic attestation. The host can't access the sandbox's memory or storage, and only the approved workload can decrypt data that you encrypt with your AWS Key Management Service key. For more information, see [Isolated and confidential tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/isolated-confidential-tasks.html) in *Amazon Elastic Container Service Developer Guide*.
Type: String
Valid Values: `SHARED | ISOLATED_SANDBOX | CONFIDENTIAL_SANDBOX`
Required: Yes

 ** attestationPolicy **   <a name="ECS-Type-TrustedExecutionConfiguration-attestationPolicy"></a>
The base64-encoded attestation policy envelope for the task. The policy specifies which containers are allowed to run and the runtime configuration that is cryptographically attested. This parameter is required when `isolationMode` is `CONFIDENTIAL_SANDBOX`.
Type: String
Required: No

## See Also
<a name="API_TrustedExecutionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/TrustedExecutionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/TrustedExecutionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/TrustedExecutionConfiguration)
