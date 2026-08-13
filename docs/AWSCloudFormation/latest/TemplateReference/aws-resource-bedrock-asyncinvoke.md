---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-asyncinvoke.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::AsyncInvoke
<a name="aws-resource-bedrock-asyncinvoke"></a>

<a name="aws-resource-bedrock-asyncinvoke-description"></a>The `AWS::Bedrock::AsyncInvoke` resource Property description not available. for Bedrock.

## Syntax
<a name="aws-resource-bedrock-asyncinvoke-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-asyncinvoke-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::AsyncInvoke",
  "Properties" : {
      "[Tags](#cfn-bedrock-asyncinvoke-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-asyncinvoke-syntax.yaml"></a>

```
Type: AWS::Bedrock::AsyncInvoke
Properties:
  [Tags](#cfn-bedrock-asyncinvoke-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrock-asyncinvoke-properties"></a>

`Tags`  <a name="cfn-bedrock-asyncinvoke-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrock-asyncinvoke-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-bedrock-asyncinvoke-return-values"></a>

### Ref
<a name="aws-resource-bedrock-asyncinvoke-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrock-asyncinvoke-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrock-asyncinvoke-return-values-fn--getatt-fn--getatt"></a>

`EndTime`  <a name="EndTime-fn::getatt"></a>
When the invocation ended.

`InvocationArn`  <a name="InvocationArn-fn::getatt"></a>
The invocation's ARN.

`InvocationId`  <a name="InvocationId-fn::getatt"></a>
Property description not available.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
When the invocation was last modified.

`ModelArn`  <a name="ModelArn-fn::getatt"></a>
The invoked model's ARN.

`Status`  <a name="Status-fn::getatt"></a>
The invocation's status.

`SubmitTime`  <a name="SubmitTime-fn::getatt"></a>
When the invocation was submitted.
