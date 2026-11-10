---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TrustedExecutionSummary.html
---

# TrustedExecutionSummary
<a name="API_TrustedExecutionSummary"></a>

A summary of the trusted execution configuration for a task. This is a read-only view of the isolation configuration that was set on the task definition. Use it to see a task's isolation configuration in the response to `DescribeTasks`, `RunTask`, or `StopTask` without calling `DescribeTaskDefinition`. This summary never includes the attestation policy itself.

**Note**
Trusted execution is supported only for Amazon ECS Managed Instances.

## Contents
<a name="API_TrustedExecutionSummary_Contents"></a>

 ** isolationMode **   <a name="ECS-Type-TrustedExecutionSummary-isolationMode"></a>
The isolation mode that the task runs in. This value mirrors the `isolationMode` that was set in the task definition's `TrustedExecutionConfiguration`.
+  `SHARED`: The task shares the underlying Amazon EC2 instance with other tasks. This is the default isolation mode.
+  `ISOLATED_SANDBOX`: The task runs in its own [Nitro Sandbox](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nitro-sandboxes.html), which is a lightweight virtual machine that is isolated by the AWS Nitro System. Each task's sandbox is isolated from every other task's sandbox on the same Amazon EC2 instance, so one task can't access another task's memory or storage. For more information, see [Isolated and confidential tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/isolated-confidential-tasks.html) in *Amazon Elastic Container Service Developer Guide*.
+  `CONFIDENTIAL_SANDBOX`: The task runs in its own [Nitro Sandbox](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nitro-sandboxes.html), which is a lightweight virtual machine that is isolated by the AWS Nitro System, with cryptographic attestation. The host can't access the sandbox's memory or storage, and only the approved workload can decrypt data that you encrypt with your AWS Key Management Service key. For more information, see [Isolated and confidential tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/isolated-confidential-tasks.html) in *Amazon Elastic Container Service Developer Guide*.
Type: String
Valid Values: `SHARED | ISOLATED_SANDBOX | CONFIDENTIAL_SANDBOX`
Required: Yes

 ** attestationPolicyStatus **   <a name="ECS-Type-TrustedExecutionSummary-attestationPolicyStatus"></a>
The status of the attestation policy for the task. This value is present only for tasks that use the `CONFIDENTIAL_SANDBOX` isolation mode.
Type: String
Valid Values: `CONFIGURED`
Required: No

## See Also
<a name="API_TrustedExecutionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/TrustedExecutionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/TrustedExecutionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/TrustedExecutionSummary)
