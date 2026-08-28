---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hook-configuration-schema.html
---

# Hook configuration schema syntax reference
<a name="hook-configuration-schema"></a>

This section outlines the schema syntax used to configure Hooks. CloudFormation uses this configuration schema at runtime when invoking a Hook in an AWS account.

To enable your Hook to proactively inspect the configuration of your stack, set the `HookInvocationStatus` to `ENABLED` after the Hook has been registered and activated in your account.

**Topics**
+ [Hook configuration schema properties](#hook-configuration-schema-properties)
+ [Hook configuration examples](#hook-configuration-examples)
+ [CloudFormation Hooks stack level filters](hooks-stack-level-filtering.md)
+ [CloudFormation Hooks target filters](hooks-target-filtering.md)
+ [Using wildcards with Hook target names](wildcard-hook-targets.md)

**Note**
The maximum amount of data that a Hook’s configuration can store is 300 KB. This is in addition to all the constraints imposed on `Configuration` request parameter of [SetTypeConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html) operation.

## Hook configuration schema properties
<a name="hook-configuration-schema-properties"></a>

The following schema is the structure for a Hook configuration schema.

```
{
    "CloudFormationConfiguration": {
        "HookConfiguration": {
            "HookInvocationStatus": "ENABLED",
            "TargetOperations": ["STACK"],
            "FailureMode": "FAIL",
            "EncryptionConfiguration": {
                "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/abc-123"
            },
            "Properties": {
                ...
            }
        }
    }
}
```

`HookConfiguration`  <a name="hooks-hook-configuration"></a>
Hook configuration supports activating or deactivating Hooks at stack level, failure modes, and Hook properties values.
The Hook configuration supports the following properties.
`HookInvocationStatus`  <a name="hooks-hookinvocationstatus"></a>
Specifies if the Hook is `ENABLED` or `DISABLED`.
*Valid values*: `ENABLED` \| `DISABLED`
`TargetOperations`  <a name="hooks-targetoperations"></a>
Specifies the list of operations the Hook is run against. For more information, see [Hook targets](hooks-concepts.md#hook-terms-hook-target).
*Valid values*: `STACK` \| `RESOURCE` \| `CHANGE_SET` \| `CLOUD_CONTROL`
`TargetStacks`  <a name="hooks-targetstacks"></a>
*Available for backward compatibility. Use `HookInvocationStatus` instead.*
If the mode is set to `ALL`, the Hook applies to all stacks in your account during a `CREATE`, `UPDATE`, or `DELETE` resource operation.
If the mode is set to `NONE`, the Hook won't apply to stacks in your account.
*Valid values*: `ALL` \| `NONE`
`FailureMode`  <a name="hooks-failuremode"></a>
This field tells the service how to treat Hook failures.
+ If the mode is set to `FAIL`, and the Hook fails, then the fail configuration stops provisioning resources and rolls back the stack.
+ If the mode is set to `WARN` and the Hook fails, then the warn configuration allows provisioning to continue with a warning message.
*Valid values*: `FAIL` \| `WARN`
`EncryptionConfiguration`  <a name="hooks-encryptionconfiguration"></a>
Specifies encryption settings for Hook annotations data.
`KmsKeyId`
The alias, alias ARN, key ID, or key ARN of the symmetric encryption AWS KMS key used to encrypt Hook annotations data. For more information, see [KeyId](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters) in the AWS KMS docs.
Before you can create Hooks with customer managed AWS KMS keys, your user or role must have AWS KMS permissions to `DescribeKey` and `GenerateDataKey`. For more information, see [AWS KMS key policy and permissions for encrypting CloudFormation Hooks results at rest](hooks-kms-key-policy.md).
`Properties`  <a name="hooks-properties"></a>
Specifies Hook runtime properties. These should match the shape of the properties supported by Hooks schema.

## Hook configuration examples
<a name="hook-configuration-examples"></a>

For examples of configuring Hooks from the AWS CLI, see the following sections:
+ [Activate a proactive control-based Hook (AWS CLI)](proactive-controls-hooks-activate-hooks.md#proactive-controls-hooks-activate-hooks-cli)
+ [Activate a Guard Hook (AWS CLI)](guard-hooks-activate-hooks.md#guard-hooks-activate-hooks-cli)
+ [Activate a Lambda Hook (AWS CLI)](lambda-hooks-activate-hooks.md#lambda-hooks-activate-hooks-cli)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
