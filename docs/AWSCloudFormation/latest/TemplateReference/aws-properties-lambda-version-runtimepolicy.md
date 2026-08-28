---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-version-runtimepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Version RuntimePolicy
<a name="aws-properties-lambda-version-runtimepolicy"></a>

Sets the runtime management configuration for a function's version. For more information, see [Runtime updates](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html).

## Syntax
<a name="aws-properties-lambda-version-runtimepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-version-runtimepolicy-syntax.json"></a>

```
{
  "[RuntimeVersionArn](#cfn-lambda-version-runtimepolicy-runtimeversionarn)" : {{String}},
  "[UpdateRuntimeOn](#cfn-lambda-version-runtimepolicy-updateruntimeon)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-version-runtimepolicy-syntax.yaml"></a>

```
  [RuntimeVersionArn](#cfn-lambda-version-runtimepolicy-runtimeversionarn): {{String}}
  [UpdateRuntimeOn](#cfn-lambda-version-runtimepolicy-updateruntimeon): {{String}}
```

## Properties
<a name="aws-properties-lambda-version-runtimepolicy-properties"></a>

`RuntimeVersionArn`  <a name="cfn-lambda-version-runtimepolicy-runtimeversionarn"></a>
The ARN of the runtime version you want the function to use.
This is only required if you're using the **Manual** runtime update mode.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}::runtime:.+$`
*Minimum*: `26`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UpdateRuntimeOn`  <a name="cfn-lambda-version-runtimepolicy-updateruntimeon"></a>
Specify the runtime update mode.
+ **Auto (default)** - Automatically update to the most recent and secure runtime version using a [Two-phase runtime version rollout](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html#runtime-management-two-phase). This is the best choice for most customers to ensure they always benefit from runtime updates.
+ **FunctionUpdate** - Lambda updates the runtime of you function to the most recent and secure runtime version when you update your function. This approach synchronizes runtime updates with function deployments, giving you control over when runtime updates are applied and allowing you to detect and mitigate rare runtime update incompatibilities early. When using this setting, you need to regularly update your functions to keep their runtime up-to-date.
+ **Manual** - You specify a runtime version in your function configuration. The function will use this runtime version indefinitely. In the rare case where a new runtime version is incompatible with an existing function, this allows you to roll back your function to an earlier runtime version. For more information, see [Roll back a runtime version](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html#runtime-management-rollback).
*Valid Values*: `Auto` \| `FunctionUpdate` \| `Manual`
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
