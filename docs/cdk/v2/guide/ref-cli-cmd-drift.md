---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/ref-cli-cmd-drift.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# `cdk drift`
<a name="ref-cli-cmd-drift"></a>

Detect configuration drift for resources that you define, manage, and deploy using the AWS Cloud Development Kit (AWS CDK). Drift occurs when a stack’s actual configuration differs from its expected configuration, which happens when resources are modified outside of AWS CloudFormation.

This command identifies resources that have been modified (for example, through the AWS Console or AWS CLI) by comparing their current state against their expected configuration. These modifications can cause unexpected behavior in your infrastructure.

During drift detection, the CDK CLI will output progress indicators and results, showing:
+ Resources that have drifted from their expected configuration.
+ The total number of resources with drift.
+ A summary indicating whether drift was detected in the stack.

**Important**
The `cdk drift` and `cdk diff` commands work differently:
 `cdk drift` calls CloudFormation’s drift detection operation to compare the actual state of resources in AWS ("reality") against their expected configuration in CloudFormation. Not all AWS resources support drift detection. For a list of supported resources, see [Resource type support](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html) in the * AWS CloudFormation User Guide*.
 `cdk diff` compares the CloudFormation template synthesized from your local CDK code against the template of the deployed CloudFormation stack.
Use `cdk drift` when you need to verify if resources have been modified outside of CloudFormation (for example, through the AWS Console or AWS CLI). Use `cdk diff` when you want to preview how your local code changes would affect your infrastructure before deployment.

## Usage
<a name="ref-cli-cmd-drift-usage"></a>

```
$ cdk drift <arguments> <options>
```

## Arguments
<a name="ref-cli-cmd-drift-args"></a><a name="ref-cli-cmd-drift-args-stack-name"></a>

 **Stack name**
The name of the stack that you want to check for drift. The stack must be previously deployed to CloudFormation to perform drift detection.
 *Type*: String
 *Required*: No
If no stack is specified, drift detection will be performed on all stacks defined in your CDK app.

## Options
<a name="ref-cli-cmd-drift-options"></a>

For a list of global options that work with all CDK CLI commands, see [Global options](ref-cli-cmd.md#ref-cli-cmd-options).<a name="ref-cli-cmd-drift-options-fail"></a>

 `--fail <BOOLEAN>`
Return with exit code 1 if drift is detected.
 *Default value*: `false` <a name="ref-cli-cmd-drift-options-help"></a>

 `--help, -h <BOOLEAN>`
Show command reference information for the `cdk drift` command.

## Examples
<a name="ref-cli-cmd-drift-examples"></a>

### Check drift for a specific stack
<a name="ref-cli-cmd-drift-examples-stack"></a>

```
$ cdk drift MyStackName
```

The command will output results similar to:

```
Stack MyStackName
Modified Resources
[~] AWS::Lambda::Function MyFunction MyLambdaFunc1234ABCD
 └─ [~] /Description
     ├─ [-] My original hello world Lambda function
     └─ [+] My drifted hello world Lambda function

1 resource has drifted from their expected configuration

✨  Number of resources with drift: 1
```

### Check drift when resources have been deleted
<a name="ref-cli-cmd-drift-examples-deleted"></a>

The following example shows what the output looks like when resources have been both modified and deleted:

```
Stack MyStackName
Modified Resources
[~] AWS::Lambda::Function MyFunction MyLambdaFunc1234ABCD
 └─ [~] /Description
     ├─ [-] My original hello world Lambda function
     └─ [+] My drifted hello world Lambda function
Deleted Resources
[-] AWS::CloudWatch::Alarm MyAlarm MyCWAlarmABCD1234

2 resources have drifted from their expected configuration

✨  Number of resources with drift: 2
```

### Check drift with exit code
<a name="ref-cli-cmd-drift-examples-fail"></a>

To have the command return a non-zero exit code if drift is detected:

```
$ cdk drift MyStackName --fail
```

This is useful in CI/CD pipelines to automatically detect and respond to infrastructure drift.
