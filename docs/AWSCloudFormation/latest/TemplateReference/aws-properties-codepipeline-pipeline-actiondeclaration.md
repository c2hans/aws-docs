---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-actiondeclaration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline ActionDeclaration
<a name="aws-properties-codepipeline-pipeline-actiondeclaration"></a>

Represents information about an action declaration.

## Syntax
<a name="aws-properties-codepipeline-pipeline-actiondeclaration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-actiondeclaration-syntax.json"></a>

```
{
  "[ActionTypeId](#cfn-codepipeline-pipeline-actiondeclaration-actiontypeid)" : {{ActionTypeId}},
  "[Commands](#cfn-codepipeline-pipeline-actiondeclaration-commands)" : {{[ String, ... ]}},
  "[Configuration](#cfn-codepipeline-pipeline-actiondeclaration-configuration)" : {{Json}},
  "[EnvironmentVariables](#cfn-codepipeline-pipeline-actiondeclaration-environmentvariables)" : {{[ EnvironmentVariable, ... ]}},
  "[InputArtifacts](#cfn-codepipeline-pipeline-actiondeclaration-inputartifacts)" : {{[ InputArtifact, ... ]}},
  "[Name](#cfn-codepipeline-pipeline-actiondeclaration-name)" : {{String}},
  "[Namespace](#cfn-codepipeline-pipeline-actiondeclaration-namespace)" : {{String}},
  "[OutputArtifacts](#cfn-codepipeline-pipeline-actiondeclaration-outputartifacts)" : {{[ OutputArtifact, ... ]}},
  "[OutputVariables](#cfn-codepipeline-pipeline-actiondeclaration-outputvariables)" : {{[ String, ... ]}},
  "[Region](#cfn-codepipeline-pipeline-actiondeclaration-region)" : {{String}},
  "[RoleArn](#cfn-codepipeline-pipeline-actiondeclaration-rolearn)" : {{String}},
  "[RunOrder](#cfn-codepipeline-pipeline-actiondeclaration-runorder)" : {{Integer}},
  "[TimeoutInMinutes](#cfn-codepipeline-pipeline-actiondeclaration-timeoutinminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-actiondeclaration-syntax.yaml"></a>

```
  [ActionTypeId](#cfn-codepipeline-pipeline-actiondeclaration-actiontypeid): {{
    ActionTypeId}}
  [Commands](#cfn-codepipeline-pipeline-actiondeclaration-commands): {{
    - String}}
  [Configuration](#cfn-codepipeline-pipeline-actiondeclaration-configuration): {{Json}}
  [EnvironmentVariables](#cfn-codepipeline-pipeline-actiondeclaration-environmentvariables): {{
    - EnvironmentVariable}}
  [InputArtifacts](#cfn-codepipeline-pipeline-actiondeclaration-inputartifacts): {{
    - InputArtifact}}
  [Name](#cfn-codepipeline-pipeline-actiondeclaration-name): {{String}}
  [Namespace](#cfn-codepipeline-pipeline-actiondeclaration-namespace): {{String}}
  [OutputArtifacts](#cfn-codepipeline-pipeline-actiondeclaration-outputartifacts): {{
    - OutputArtifact}}
  [OutputVariables](#cfn-codepipeline-pipeline-actiondeclaration-outputvariables): {{
    - String}}
  [Region](#cfn-codepipeline-pipeline-actiondeclaration-region): {{String}}
  [RoleArn](#cfn-codepipeline-pipeline-actiondeclaration-rolearn): {{String}}
  [RunOrder](#cfn-codepipeline-pipeline-actiondeclaration-runorder): {{Integer}}
  [TimeoutInMinutes](#cfn-codepipeline-pipeline-actiondeclaration-timeoutinminutes): {{Integer}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-actiondeclaration-properties"></a>

`ActionTypeId`  <a name="cfn-codepipeline-pipeline-actiondeclaration-actiontypeid"></a>
Specifies the action type and the provider of the action.
*Required*: Yes
*Type*: [ActionTypeId](aws-properties-codepipeline-pipeline-actiontypeid.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Commands`  <a name="cfn-codepipeline-pipeline-actiondeclaration-commands"></a>
The shell commands to run with your compute action in CodePipeline. All commands are supported except multi-line formats. While CodeBuild logs and permissions are used, you do not need to create any resources in CodeBuild.
Using compute time for this action will incur separate charges in AWS CodeBuild.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Configuration`  <a name="cfn-codepipeline-pipeline-actiondeclaration-configuration"></a>
The action's configuration. These are key-value pairs that specify input values for an action. For more information, see [Action Structure Requirements in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements). For the list of configuration properties for the AWS CloudFormation action type in CodePipeline, see [Configuration Properties Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html) in the *AWS CloudFormation User Guide*. For template snippets with examples, see [Using Parameter Override Functions with CodePipeline Pipelines](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html) in the *AWS CloudFormation User Guide*.
The values can be represented in either JSON or YAML format. For example, the JSON configuration item format is as follows:
 *JSON:*
 `"Configuration" : { Key : Value },`
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentVariables`  <a name="cfn-codepipeline-pipeline-actiondeclaration-environmentvariables"></a>
The environment variables for the action.
*Required*: No
*Type*: Array of [EnvironmentVariable](aws-properties-codepipeline-pipeline-environmentvariable.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputArtifacts`  <a name="cfn-codepipeline-pipeline-actiondeclaration-inputartifacts"></a>
The name or ID of the artifact consumed by the action, such as a test or build artifact. While the field is not a required parameter, most actions have an action configuration that requires a specified quantity of input artifacts. To refer to the action configuration specification by action provider, see the [Action structure reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference.html) in the *AWS CodePipeline User Guide*.
For a CodeBuild action with multiple input artifacts, one of your input sources must be designated the PrimarySource. For more information, see the [CodeBuild action reference page](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodeBuild.html) in the *AWS CodePipeline User Guide*.
*Required*: No
*Type*: Array of [InputArtifact](aws-properties-codepipeline-pipeline-inputartifact.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-codepipeline-pipeline-actiondeclaration-name"></a>
The action declaration's name.
*Required*: Yes
*Type*: String
*Pattern*: `[A-Za-z0-9.@\-_]+`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-codepipeline-pipeline-actiondeclaration-namespace"></a>
The variable namespace associated with the action. All variables produced as output by this action fall under this namespace.
*Required*: No
*Type*: String
*Pattern*: `[A-Za-z0-9@\-_]+`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputArtifacts`  <a name="cfn-codepipeline-pipeline-actiondeclaration-outputartifacts"></a>
The name or ID of the result of the action declaration, such as a test or build artifact. While the field is not a required parameter, most actions have an action configuration that requires a specified quantity of output artifacts. To refer to the action configuration specification by action provider, see the [Action structure reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference.html) in the *AWS CodePipeline User Guide*.
*Required*: No
*Type*: Array of [OutputArtifact](aws-properties-codepipeline-pipeline-outputartifact.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputVariables`  <a name="cfn-codepipeline-pipeline-actiondeclaration-outputvariables"></a>
The list of variables that are to be exported from the compute action. This is specifically CodeBuild environment variables as used for that action.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-codepipeline-pipeline-actiondeclaration-region"></a>
The action declaration's AWS Region, such as us-east-1.
*Required*: No
*Type*: String
*Minimum*: `4`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-codepipeline-pipeline-actiondeclaration-rolearn"></a>
The ARN of the IAM service role that performs the declared action. This is assumed through the roleArn for the pipeline.
*Required*: No
*Type*: String
*Pattern*: `arn:aws(-[\w]+)*:iam::[0-9]{12}:role/.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RunOrder`  <a name="cfn-codepipeline-pipeline-actiondeclaration-runorder"></a>
The order in which actions are run.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `999`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutInMinutes`  <a name="cfn-codepipeline-pipeline-actiondeclaration-timeoutinminutes"></a>
A timeout duration in minutes that can be applied against the ActionType’s default timeout value specified in [Quotas for AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/limits.html). This attribute is available only to the manual approval ActionType.
*Required*: No
*Type*: Integer
*Minimum*: `5`
*Maximum*: `86400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
