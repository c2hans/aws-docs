---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/transform-aws-codedeploybluegreen.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# `AWS::CodeDeployBlueGreen` transform
<a name="transform-aws-codedeploybluegreen"></a>

This topic describes how to use the `AWS::CodeDeployBlueGreen` transform to enable ECS blue/green deployments through CodeDeploy on your stack.

For more information, see [Perform ECS blue/green deployments through CodeDeploy using CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/blue-green.html) in the *AWS CloudFormation User Guide*.

## Usage
<a name="aws-codedeploybluegreen-usage"></a>

To use the `AWS::CodeDeployBlueGreen` transform, you must declare it at the top level of your CloudFormation template. You can't use `AWS::CodeDeployBlueGreen` as a transform embedded in any other template section.

The value for the transform declaration must be a literal string. You can't use a parameter or function to specify a transform value.

### Syntax
<a name="aws-codedeploybluegreen-syntax"></a>

To declare this transform in your CloudFormation template, use the following syntax:

#### JSON
<a name="aws-codedeploybluegreen-syntax.json"></a>

```
{
  "Transform":[
    "AWS::CodeDeployBlueGreen"
  ],
  "Resources":{
    {{...}}
  }
}
```

#### YAML
<a name="aws-codedeploybluegreen-syntax.yaml"></a>

```
Transform:
  - 'AWS::CodeDeployBlueGreen'
Resources:
  {{...}}
```

The `AWS::CodeDeployBlueGreen` transform is a standalone declaration with no additional parameters.

## Related resources
<a name="aws-codedeploybluegreen-related-resources"></a>

For complete CloudFormation template examples that you can use to enable ECS blue/green deployments on your stack, see [Blue/green deployment template example](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/blue-green-template-example.html) in the *AWS CloudFormation User Guide*.

For general information about using macros, see [Perform custom processing on CloudFormation templates with template macros](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html) in the *AWS CloudFormation User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
