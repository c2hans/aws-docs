---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-ruletypeid.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline RuleTypeId
<a name="aws-properties-codepipeline-pipeline-ruletypeid"></a>

The ID for the rule type, which is made up of the combined values for category, owner, provider, and version. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html). For more information about rules, see the [AWS CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html).

## Syntax
<a name="aws-properties-codepipeline-pipeline-ruletypeid-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-ruletypeid-syntax.json"></a>

```
{
  "[Category](#cfn-codepipeline-pipeline-ruletypeid-category)" : {{String}},
  "[Owner](#cfn-codepipeline-pipeline-ruletypeid-owner)" : {{String}},
  "[Provider](#cfn-codepipeline-pipeline-ruletypeid-provider)" : {{String}},
  "[Version](#cfn-codepipeline-pipeline-ruletypeid-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-ruletypeid-syntax.yaml"></a>

```
  [Category](#cfn-codepipeline-pipeline-ruletypeid-category): {{String}}
  [Owner](#cfn-codepipeline-pipeline-ruletypeid-owner): {{String}}
  [Provider](#cfn-codepipeline-pipeline-ruletypeid-provider): {{String}}
  [Version](#cfn-codepipeline-pipeline-ruletypeid-version): {{String}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-ruletypeid-properties"></a>

`Category`  <a name="cfn-codepipeline-pipeline-ruletypeid-category"></a>
A category defines what kind of rule can be run in the stage, and constrains the provider type for the rule. The valid category is `Rule`.
*Required*: No
*Type*: String
*Allowed values*: `Rule`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Owner`  <a name="cfn-codepipeline-pipeline-ruletypeid-owner"></a>
The creator of the rule being called. The valid value for the `Owner` field in the rule category is `AWS`.
*Required*: No
*Type*: String
*Allowed values*: `AWS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Provider`  <a name="cfn-codepipeline-pipeline-ruletypeid-provider"></a>
The rule provider, such as the `DeploymentWindow` rule. For a list of rule provider names, see the rules listed in the [AWS CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html).
*Required*: No
*Type*: String
*Pattern*: `[0-9A-Za-z_-]+`
*Minimum*: `1`
*Maximum*: `35`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-codepipeline-pipeline-ruletypeid-version"></a>
A string that describes the rule version.
*Required*: No
*Type*: String
*Pattern*: `[0-9A-Za-z_-]+`
*Minimum*: `1`
*Maximum*: `9`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
