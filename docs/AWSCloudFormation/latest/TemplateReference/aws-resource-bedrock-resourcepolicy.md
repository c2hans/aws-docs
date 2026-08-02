---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-resourcepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::ResourcePolicy
<a name="aws-resource-bedrock-resourcepolicy"></a>

Adds a resource policy for a Bedrock resource.

## Syntax
<a name="aws-resource-bedrock-resourcepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-resourcepolicy-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::ResourcePolicy",
  "Properties" : {
      "[PolicyDocument](#cfn-bedrock-resourcepolicy-policydocument)" : {{Json}},
      "[ResourceArn](#cfn-bedrock-resourcepolicy-resourcearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-resourcepolicy-syntax.yaml"></a>

```
Type: AWS::Bedrock::ResourcePolicy
Properties:
  [PolicyDocument](#cfn-bedrock-resourcepolicy-policydocument): {{Json}}
  [ResourceArn](#cfn-bedrock-resourcepolicy-resourcearn): {{String}}
```

## Properties
<a name="aws-resource-bedrock-resourcepolicy-properties"></a>

`PolicyDocument`  <a name="cfn-bedrock-resourcepolicy-policydocument"></a>
The JSON string representing the Bedrock resource policy.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceArn`  <a name="cfn-bedrock-resourcepolicy-resourcearn"></a>
The ARN of the Bedrock resource to which this resource policy applies.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[a-z]+)*:bedrock:[a-z0-9-]+:[0-9]{12}:(guardrail|guardrail-profile)/[a-z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-bedrock-resourcepolicy-return-values"></a>

### Ref
<a name="aws-resource-bedrock-resourcepolicy-return-values-ref"></a>
