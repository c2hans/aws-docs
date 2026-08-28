---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-microvmhooks.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage MicrovmHooks
<a name="aws-properties-lambda-microvmimage-microvmhooks"></a>

Configuration for lifecycle hooks invoked during MicroVM events such as run, resume, suspend, and terminate.

## Syntax
<a name="aws-properties-lambda-microvmimage-microvmhooks-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-microvmimage-microvmhooks-syntax.json"></a>

```
{
  "[Resume](#cfn-lambda-microvmimage-microvmhooks-resume)" : {{String}},
  "[ResumeTimeoutInSeconds](#cfn-lambda-microvmimage-microvmhooks-resumetimeoutinseconds)" : {{Integer}},
  "[Run](#cfn-lambda-microvmimage-microvmhooks-run)" : {{String}},
  "[RunTimeoutInSeconds](#cfn-lambda-microvmimage-microvmhooks-runtimeoutinseconds)" : {{Integer}},
  "[Suspend](#cfn-lambda-microvmimage-microvmhooks-suspend)" : {{String}},
  "[SuspendTimeoutInSeconds](#cfn-lambda-microvmimage-microvmhooks-suspendtimeoutinseconds)" : {{Integer}},
  "[Terminate](#cfn-lambda-microvmimage-microvmhooks-terminate)" : {{String}},
  "[TerminateTimeoutInSeconds](#cfn-lambda-microvmimage-microvmhooks-terminatetimeoutinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lambda-microvmimage-microvmhooks-syntax.yaml"></a>

```
  [Resume](#cfn-lambda-microvmimage-microvmhooks-resume): {{String}}
  [ResumeTimeoutInSeconds](#cfn-lambda-microvmimage-microvmhooks-resumetimeoutinseconds): {{Integer}}
  [Run](#cfn-lambda-microvmimage-microvmhooks-run): {{String}}
  [RunTimeoutInSeconds](#cfn-lambda-microvmimage-microvmhooks-runtimeoutinseconds): {{Integer}}
  [Suspend](#cfn-lambda-microvmimage-microvmhooks-suspend): {{String}}
  [SuspendTimeoutInSeconds](#cfn-lambda-microvmimage-microvmhooks-suspendtimeoutinseconds): {{Integer}}
  [Terminate](#cfn-lambda-microvmimage-microvmhooks-terminate): {{String}}
  [TerminateTimeoutInSeconds](#cfn-lambda-microvmimage-microvmhooks-terminatetimeoutinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-lambda-microvmimage-microvmhooks-properties"></a>

`Resume`  <a name="cfn-lambda-microvmimage-microvmhooks-resume"></a>
The path of the hook invoked when the MicroVM resumes from a suspended state.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResumeTimeoutInSeconds`  <a name="cfn-lambda-microvmimage-microvmhooks-resumetimeoutinseconds"></a>
The maximum time in seconds for the resume hook to complete.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Run`  <a name="cfn-lambda-microvmimage-microvmhooks-run"></a>
The path of the hook invoked when the MicroVM starts running.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RunTimeoutInSeconds`  <a name="cfn-lambda-microvmimage-microvmhooks-runtimeoutinseconds"></a>
The maximum time in seconds for the run hook to complete.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Suspend`  <a name="cfn-lambda-microvmimage-microvmhooks-suspend"></a>
The path of the hook invoked when the MicroVM is suspended.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuspendTimeoutInSeconds`  <a name="cfn-lambda-microvmimage-microvmhooks-suspendtimeoutinseconds"></a>
The maximum time in seconds for the suspend hook to complete.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Terminate`  <a name="cfn-lambda-microvmimage-microvmhooks-terminate"></a>
The path of the hook invoked when the MicroVM is terminated.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TerminateTimeoutInSeconds`  <a name="cfn-lambda-microvmimage-microvmhooks-terminatetimeoutinseconds"></a>
The maximum time in seconds for the terminate hook to complete.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
