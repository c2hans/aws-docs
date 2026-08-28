---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-action.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Action
<a name="aws-resource-sagemaker-action"></a>

Creates an *action*. An action is a lineage tracking entity that represents an action or activity. For example, a model deployment or an HPO job. Generally, an action involves at least one input or output artifact. For more information, see [Amazon SageMaker ML Lineage Tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking.html).

## Syntax
<a name="aws-resource-sagemaker-action-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-action-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::Action",
  "Properties" : {
      "[ActionName](#cfn-sagemaker-action-actionname)" : {{String}},
      "[ActionType](#cfn-sagemaker-action-actiontype)" : {{String}},
      "[Description](#cfn-sagemaker-action-description)" : {{String}},
      "[MetadataProperties](#cfn-sagemaker-action-metadataproperties)" : {{MetadataProperties}},
      "[Properties](#cfn-sagemaker-action-properties)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Source](#cfn-sagemaker-action-source)" : {{ActionSource}},
      "[Status](#cfn-sagemaker-action-status)" : {{String}},
      "[Tags](#cfn-sagemaker-action-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-action-syntax.yaml"></a>

```
Type: AWS::SageMaker::Action
Properties:
  [ActionName](#cfn-sagemaker-action-actionname): {{String}}
  [ActionType](#cfn-sagemaker-action-actiontype): {{String}}
  [Description](#cfn-sagemaker-action-description): {{String}}
  [MetadataProperties](#cfn-sagemaker-action-metadataproperties): {{
    MetadataProperties}}
  [Properties](#cfn-sagemaker-action-properties): {{
    {{Key}}: {{Value}}}}
  [Source](#cfn-sagemaker-action-source): {{
    ActionSource}}
  [Status](#cfn-sagemaker-action-status): {{String}}
  [Tags](#cfn-sagemaker-action-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sagemaker-action-properties"></a>

`ActionName`  <a name="cfn-sagemaker-action-actionname"></a>
The name of the action.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}$`
*Minimum*: `1`
*Maximum*: `120`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ActionType`  <a name="cfn-sagemaker-action-actiontype"></a>
The type of the action.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-sagemaker-action-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `3072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetadataProperties`  <a name="cfn-sagemaker-action-metadataproperties"></a>
Metadata properties of the tracking entity, trial, or trial component.
*Required*: No
*Type*: [MetadataProperties](aws-properties-sagemaker-action-metadataproperties.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Properties`  <a name="cfn-sagemaker-action-properties"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Maximum*: `2500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-sagemaker-action-source"></a>
The source of the action.
*Required*: Yes
*Type*: [ActionSource](aws-properties-sagemaker-action-actionsource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Status`  <a name="cfn-sagemaker-action-status"></a>
The status of the action.
*Required*: No
*Type*: String
*Allowed values*: `Unknown | InProgress | Completed | Failed | Stopping | Stopped`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sagemaker-action-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-action-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-action-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-action-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-action-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-action-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
When the action was created.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
When the action was last modified.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
