---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-stagedeclaration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline StageDeclaration
<a name="aws-properties-codepipeline-pipeline-stagedeclaration"></a>

Represents information about a stage and its definition.

## Syntax
<a name="aws-properties-codepipeline-pipeline-stagedeclaration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-stagedeclaration-syntax.json"></a>

```
{
  "[Actions](#cfn-codepipeline-pipeline-stagedeclaration-actions)" : {{[ ActionDeclaration, ... ]}},
  "[BeforeEntry](#cfn-codepipeline-pipeline-stagedeclaration-beforeentry)" : {{BeforeEntryConditions}},
  "[Blockers](#cfn-codepipeline-pipeline-stagedeclaration-blockers)" : {{[ BlockerDeclaration, ... ]}},
  "[Name](#cfn-codepipeline-pipeline-stagedeclaration-name)" : {{String}},
  "[OnFailure](#cfn-codepipeline-pipeline-stagedeclaration-onfailure)" : {{FailureConditions}},
  "[OnSuccess](#cfn-codepipeline-pipeline-stagedeclaration-onsuccess)" : {{SuccessConditions}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-stagedeclaration-syntax.yaml"></a>

```
  [Actions](#cfn-codepipeline-pipeline-stagedeclaration-actions): {{
    - ActionDeclaration}}
  [BeforeEntry](#cfn-codepipeline-pipeline-stagedeclaration-beforeentry): {{
    BeforeEntryConditions}}
  [Blockers](#cfn-codepipeline-pipeline-stagedeclaration-blockers): {{
    - BlockerDeclaration}}
  [Name](#cfn-codepipeline-pipeline-stagedeclaration-name): {{String}}
  [OnFailure](#cfn-codepipeline-pipeline-stagedeclaration-onfailure): {{
    FailureConditions}}
  [OnSuccess](#cfn-codepipeline-pipeline-stagedeclaration-onsuccess): {{
    SuccessConditions}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-stagedeclaration-properties"></a>

`Actions`  <a name="cfn-codepipeline-pipeline-stagedeclaration-actions"></a>
The actions included in a stage.
*Required*: Yes
*Type*: Array of [ActionDeclaration](aws-properties-codepipeline-pipeline-actiondeclaration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BeforeEntry`  <a name="cfn-codepipeline-pipeline-stagedeclaration-beforeentry"></a>
The method to use when a stage allows entry. For example, configuring this field for conditions will allow entry to the stage when the conditions are met.
*Required*: No
*Type*: [BeforeEntryConditions](aws-properties-codepipeline-pipeline-beforeentryconditions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Blockers`  <a name="cfn-codepipeline-pipeline-stagedeclaration-blockers"></a>
Reserved for future use.
*Required*: No
*Type*: Array of [BlockerDeclaration](aws-properties-codepipeline-pipeline-blockerdeclaration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-codepipeline-pipeline-stagedeclaration-name"></a>
The name of the stage.
*Required*: Yes
*Type*: String
*Pattern*: `[A-Za-z0-9.@\-_]+`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnFailure`  <a name="cfn-codepipeline-pipeline-stagedeclaration-onfailure"></a>
The method to use when a stage has not completed successfully. For example, configuring this field for rollback will roll back a failed stage automatically to the last successful pipeline execution in the stage.
*Required*: No
*Type*: [FailureConditions](aws-properties-codepipeline-pipeline-failureconditions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnSuccess`  <a name="cfn-codepipeline-pipeline-stagedeclaration-onsuccess"></a>
The method to use when a stage has succeeded. For example, configuring this field for conditions will allow the stage to succeed when the conditions are met.
*Required*: No
*Type*: [SuccessConditions](aws-properties-codepipeline-pipeline-successconditions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
