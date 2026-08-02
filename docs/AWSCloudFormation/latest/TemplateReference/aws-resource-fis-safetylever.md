---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-fis-safetylever.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FIS::SafetyLever
<a name="aws-resource-fis-safetylever"></a>

 Describes a safety lever.

## Syntax
<a name="aws-resource-fis-safetylever-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-fis-safetylever-syntax.json"></a>

```
{
  "Type" : "AWS::FIS::SafetyLever",
  "Properties" : {
      "[Id](#cfn-fis-safetylever-id)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-fis-safetylever-syntax.yaml"></a>

```
Type: AWS::FIS::SafetyLever
Properties:
  [Id](#cfn-fis-safetylever-id): {{String}}
```

## Properties
<a name="aws-resource-fis-safetylever-properties"></a>

`Id`  <a name="cfn-fis-safetylever-id"></a>
 The ID of the safety lever.
*Required*: No
*Type*: String
*Pattern*: `^[\S]+$`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-fis-safetylever-return-values"></a>

### Ref
<a name="aws-resource-fis-safetylever-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-fis-safetylever-return-values-fn--getatt"></a>

####
<a name="aws-resource-fis-safetylever-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
 The Amazon Resource Name (ARN) of the safety lever.

`Reason`  <a name="Reason-fn::getatt"></a>
 The reason for the state of the safety lever.

`Status`  <a name="Status-fn::getatt"></a>
 The state of the safety lever.
