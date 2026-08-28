---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codepipeline-pipeline-actiontypeid.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodePipeline::Pipeline ActionTypeId
<a name="aws-properties-codepipeline-pipeline-actiontypeid"></a>

Represents information about an action type.

## Syntax
<a name="aws-properties-codepipeline-pipeline-actiontypeid-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codepipeline-pipeline-actiontypeid-syntax.json"></a>

```
{
  "[Category](#cfn-codepipeline-pipeline-actiontypeid-category)" : {{String}},
  "[Owner](#cfn-codepipeline-pipeline-actiontypeid-owner)" : {{String}},
  "[Provider](#cfn-codepipeline-pipeline-actiontypeid-provider)" : {{String}},
  "[Version](#cfn-codepipeline-pipeline-actiontypeid-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-codepipeline-pipeline-actiontypeid-syntax.yaml"></a>

```
  [Category](#cfn-codepipeline-pipeline-actiontypeid-category): {{String}}
  [Owner](#cfn-codepipeline-pipeline-actiontypeid-owner): {{String}}
  [Provider](#cfn-codepipeline-pipeline-actiontypeid-provider): {{String}}
  [Version](#cfn-codepipeline-pipeline-actiontypeid-version): {{String}}
```

## Properties
<a name="aws-properties-codepipeline-pipeline-actiontypeid-properties"></a>

`Category`  <a name="cfn-codepipeline-pipeline-actiontypeid-category"></a>
A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the values below.
+  `Source`
+  `Build`
+  `Test`
+  `Deploy`
+  `Invoke`
+  `Approval`
+  `Compute`
*Required*: Yes
*Type*: String
*Allowed values*: `Source | Build | Test | Deploy | Invoke | Approval | Compute`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Owner`  <a name="cfn-codepipeline-pipeline-actiontypeid-owner"></a>
The creator of the action being called. There are three valid values for the `Owner` field in the action category section within your pipeline structure: `AWS`, `ThirdParty`, and `Custom`. For more information, see [Valid Action Types and Providers in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Provider`  <a name="cfn-codepipeline-pipeline-actiontypeid-provider"></a>
The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of CodeDeploy, which would be specified as `CodeDeploy`. For more information, see [Valid Action Types and Providers in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-codepipeline-pipeline-actiontypeid-version"></a>
A string that describes the action version.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
