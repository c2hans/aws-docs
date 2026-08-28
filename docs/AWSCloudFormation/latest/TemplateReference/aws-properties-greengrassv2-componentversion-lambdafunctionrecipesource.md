---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GreengrassV2::ComponentVersion LambdaFunctionRecipeSource
<a name="aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource"></a>

Contains information about an AWS Lambda function to import to create a component.

## Syntax
<a name="aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource-syntax.json"></a>

```
{
  "[ComponentDependencies](#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentdependencies)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ComponentLambdaParameters](#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentlambdaparameters)" : {{LambdaExecutionParameters}},
  "[ComponentName](#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentname)" : {{String}},
  "[ComponentPlatforms](#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentplatforms)" : {{[ ComponentPlatform, ... ]}},
  "[ComponentVersion](#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentversion)" : {{String}},
  "[LambdaArn](#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-lambdaarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource-syntax.yaml"></a>

```
  [ComponentDependencies](#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentdependencies): {{
    {{Key}}: {{Value}}}}
  [ComponentLambdaParameters](#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentlambdaparameters): {{
    LambdaExecutionParameters}}
  [ComponentName](#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentname): {{String}}
  [ComponentPlatforms](#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentplatforms): {{
    - ComponentPlatform}}
  [ComponentVersion](#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentversion): {{String}}
  [LambdaArn](#cfn-greengrassv2-componentversion-lambdafunctionrecipesource-lambdaarn): {{String}}
```

## Properties
<a name="aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource-properties"></a>

`ComponentDependencies`  <a name="cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentdependencies"></a>
The component versions on which this Lambda function component depends.
*Required*: No
*Type*: Object of [ComponentDependencyRequirement](aws-properties-greengrassv2-componentversion-componentdependencyrequirement.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ComponentLambdaParameters`  <a name="cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentlambdaparameters"></a>
The system and runtime parameters for the Lambda function as it runs on the AWS IoT Greengrass core device.
*Required*: No
*Type*: [LambdaExecutionParameters](aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ComponentName`  <a name="cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentname"></a>
The name of the component.
Defaults to the name of the Lambda function.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ComponentPlatforms`  <a name="cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentplatforms"></a>
The platforms that the component version supports.
*Required*: No
*Type*: Array of [ComponentPlatform](aws-properties-greengrassv2-componentversion-componentplatform.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ComponentVersion`  <a name="cfn-greengrassv2-componentversion-lambdafunctionrecipesource-componentversion"></a>
The version of the component.
Defaults to the version of the Lambda function as a semantic version. For example, if your function version is `3`, the component version becomes `3.0.0`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LambdaArn`  <a name="cfn-greengrassv2-componentversion-lambdafunctionrecipesource-lambdaarn"></a>
The ARN of the Lambda function. The ARN must include the version of the function to import. You can't use version aliases like `$LATEST`.
*Required*: No
*Type*: String
*Pattern*: `^arn:[^:]*:lambda:(([a-z]+-)+[0-9])?:([0-9]{12})?:[^.]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
