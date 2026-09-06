---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topic-semanticentitytype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Topic SemanticEntityType
<a name="aws-properties-quicksight-topic-semanticentitytype"></a>

A structure that represents a semantic entity type.

## Syntax
<a name="aws-properties-quicksight-topic-semanticentitytype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topic-semanticentitytype-syntax.json"></a>

```
{
  "[SubTypeName](#cfn-quicksight-topic-semanticentitytype-subtypename)" : {{String}},
  "[TypeName](#cfn-quicksight-topic-semanticentitytype-typename)" : {{String}},
  "[TypeParameters](#cfn-quicksight-topic-semanticentitytype-typeparameters)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-quicksight-topic-semanticentitytype-syntax.yaml"></a>

```
  [SubTypeName](#cfn-quicksight-topic-semanticentitytype-subtypename): {{String}}
  [TypeName](#cfn-quicksight-topic-semanticentitytype-typename): {{String}}
  [TypeParameters](#cfn-quicksight-topic-semanticentitytype-typeparameters): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-quicksight-topic-semanticentitytype-properties"></a>

`SubTypeName`  <a name="cfn-quicksight-topic-semanticentitytype-subtypename"></a>
The semantic entity sub type name.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TypeName`  <a name="cfn-quicksight-topic-semanticentitytype-typename"></a>
The semantic entity type name.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TypeParameters`  <a name="cfn-quicksight-topic-semanticentitytype-typeparameters"></a>
The semantic entity type parameters.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
