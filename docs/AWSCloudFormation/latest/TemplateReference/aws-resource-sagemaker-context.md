---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-context.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Context
<a name="aws-resource-sagemaker-context"></a>

Creates a *context*. A context is a lineage tracking entity that represents a logical grouping of other tracking or experiment entities. Some examples are an endpoint and a model package. For more information, see [Amazon SageMaker ML Lineage Tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking.html).

## Syntax
<a name="aws-resource-sagemaker-context-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-context-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::Context",
  "Properties" : {
      "[ContextName](#cfn-sagemaker-context-contextname)" : {{String}},
      "[ContextType](#cfn-sagemaker-context-contexttype)" : {{String}},
      "[Description](#cfn-sagemaker-context-description)" : {{String}},
      "[Properties](#cfn-sagemaker-context-properties)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Source](#cfn-sagemaker-context-source)" : {{Source}},
      "[Tags](#cfn-sagemaker-context-tags)" : {{[ TagsItems, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-context-syntax.yaml"></a>

```
Type: AWS::SageMaker::Context
Properties:
  [ContextName](#cfn-sagemaker-context-contextname): {{String}}
  [ContextType](#cfn-sagemaker-context-contexttype): {{String}}
  [Description](#cfn-sagemaker-context-description): {{String}}
  [Properties](#cfn-sagemaker-context-properties): {{
    {{Key}}: {{Value}}}}
  [Source](#cfn-sagemaker-context-source): {{
    Source}}
  [Tags](#cfn-sagemaker-context-tags): {{
    - TagsItems}}
```

## Properties
<a name="aws-resource-sagemaker-context-properties"></a>

`ContextName`  <a name="cfn-sagemaker-context-contextname"></a>
The name of the context.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,119}$`
*Minimum*: `1`
*Maximum*: `120`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContextType`  <a name="cfn-sagemaker-context-contexttype"></a>
The type of the context.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-sagemaker-context-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `3072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Properties`  <a name="cfn-sagemaker-context-properties"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^.{0,2500}$`
*Maximum*: `2500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-sagemaker-context-source"></a>
The source of the context.
*Required*: Yes
*Type*: [Source](aws-properties-sagemaker-context-source.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-context-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-sagemaker-context-tagsitems.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-context-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-context-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-context-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-context-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
When the context was created.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
When the context was last modified.
