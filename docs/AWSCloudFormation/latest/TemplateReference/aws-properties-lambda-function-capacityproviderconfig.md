---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-capacityproviderconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Function CapacityProviderConfig
<a name="aws-properties-lambda-function-capacityproviderconfig"></a>

Configuration for the capacity provider that manages compute resources for Lambda functions.

## Syntax
<a name="aws-properties-lambda-function-capacityproviderconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-function-capacityproviderconfig-syntax.json"></a>

```
{
  "[LambdaManagedInstancesCapacityProviderConfig](#cfn-lambda-function-capacityproviderconfig-lambdamanagedinstancescapacityproviderconfig)" : {{LambdaManagedInstancesCapacityProviderConfig}}
}
```

### YAML
<a name="aws-properties-lambda-function-capacityproviderconfig-syntax.yaml"></a>

```
  [LambdaManagedInstancesCapacityProviderConfig](#cfn-lambda-function-capacityproviderconfig-lambdamanagedinstancescapacityproviderconfig): {{
    LambdaManagedInstancesCapacityProviderConfig}}
```

## Properties
<a name="aws-properties-lambda-function-capacityproviderconfig-properties"></a>

`LambdaManagedInstancesCapacityProviderConfig`  <a name="cfn-lambda-function-capacityproviderconfig-lambdamanagedinstancescapacityproviderconfig"></a>
Configuration for Lambda-managed instances used by the capacity provider.
*Required*: Yes
*Type*: [LambdaManagedInstancesCapacityProviderConfig](aws-properties-lambda-function-lambdamanagedinstancescapacityproviderconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
