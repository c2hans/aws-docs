---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-dataset-inlineexamplessource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Dataset InlineExamplesSource
<a name="aws-properties-bedrockagentcore-dataset-inlineexamplessource"></a>

 Inline examples provided directly in the request body.

## Syntax
<a name="aws-properties-bedrockagentcore-dataset-inlineexamplessource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-dataset-inlineexamplessource-syntax.json"></a>

```
{
  "[Examples](#cfn-bedrockagentcore-dataset-inlineexamplessource-examples)" : {{[ {{{Key}}: {{Value}}, ...}, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-dataset-inlineexamplessource-syntax.yaml"></a>

```
  [Examples](#cfn-bedrockagentcore-dataset-inlineexamplessource-examples): {{
    -
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-bedrockagentcore-dataset-inlineexamplessource-properties"></a>

`Examples`  <a name="cfn-bedrockagentcore-dataset-inlineexamplessource-examples"></a>
 Examples to add. Each example is assigned an auto-generated UUID.
*Required*: Yes
*Type*: Array of Object
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
