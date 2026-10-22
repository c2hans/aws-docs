---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-retrievalinstruction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::RetrievalInstruction
<a name="aws-resource-bedrock-retrievalinstruction"></a>

Creates a new retrieval instruction. The retrieval instruction is usable once its status becomes ACTIVE. Use GetRetrievalInstruction to check whether it is ready.

## Syntax
<a name="aws-resource-bedrock-retrievalinstruction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-retrievalinstruction-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::RetrievalInstruction",
  "Properties" : {
      "[CustomerEncryptionKeyArn](#cfn-bedrock-retrievalinstruction-customerencryptionkeyarn)" : {{String}},
      "[Description](#cfn-bedrock-retrievalinstruction-description)" : {{String}},
      "[Instruction](#cfn-bedrock-retrievalinstruction-instruction)" : {{Instruction}},
      "[Name](#cfn-bedrock-retrievalinstruction-name)" : {{String}},
      "[Tags](#cfn-bedrock-retrievalinstruction-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-retrievalinstruction-syntax.yaml"></a>

```
Type: AWS::Bedrock::RetrievalInstruction
Properties:
  [CustomerEncryptionKeyArn](#cfn-bedrock-retrievalinstruction-customerencryptionkeyarn): {{String}}
  [Description](#cfn-bedrock-retrievalinstruction-description): {{String}}
  [Instruction](#cfn-bedrock-retrievalinstruction-instruction): {{
    Instruction}}
  [Name](#cfn-bedrock-retrievalinstruction-name): {{String}}
  [Tags](#cfn-bedrock-retrievalinstruction-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrock-retrievalinstruction-properties"></a>

`CustomerEncryptionKeyArn`  <a name="cfn-bedrock-retrievalinstruction-customerencryptionkeyarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-cn|-us-gov|-eusc|-iso(-[b-f])?)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-bedrock-retrievalinstruction-description"></a>
A description of the retrieval instruction.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Instruction`  <a name="cfn-bedrock-retrievalinstruction-instruction"></a>
Property description not available.
*Required*: Yes
*Type*: [Instruction](aws-properties-bedrock-retrievalinstruction-instruction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrock-retrievalinstruction-name"></a>
The name of the retrieval instruction.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?){1,100}$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrock-retrievalinstruction-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrock-retrievalinstruction-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrock-retrievalinstruction-return-values"></a>

### Ref
<a name="aws-resource-bedrock-retrievalinstruction-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrock-retrievalinstruction-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrock-retrievalinstruction-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
When you created the retrieval instruction.

`LastTransitionStatus`  <a name="LastTransitionStatus-fn::getatt"></a>
The outcome or in-progress state of the most recent create or update of the retrieval instruction.

`RetrievalInstructionId`  <a name="RetrievalInstructionId-fn::getatt"></a>
The identifier of the retrieval instruction.

`Status`  <a name="Status-fn::getatt"></a>
Whether the instruction can be used. Only ACTIVE is resolvable at retrieval time.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
When the retrieval instruction was last updated.
