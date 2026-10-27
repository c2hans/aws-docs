---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-space.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Space
<a name="aws-resource-cloudwatch-space"></a>

<a name="aws-resource-cloudwatch-space-description"></a>The `AWS::CloudWatch::Space` resource Property description not available. for CloudWatch.

## Syntax
<a name="aws-resource-cloudwatch-space-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-space-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::Space",
  "Properties" : {
      "[AgentCoreEvaluationRoleArn](#cfn-cloudwatch-space-agentcoreevaluationrolearn)" : {{String}},
      "[DataAccessRoleArn](#cfn-cloudwatch-space-dataaccessrolearn)" : {{String}},
      "[DomainId](#cfn-cloudwatch-space-domainid)" : {{String}},
      "[EncryptionConfiguration](#cfn-cloudwatch-space-encryptionconfiguration)" : {{EncryptionConfiguration}},
      "[Name](#cfn-cloudwatch-space-name)" : {{String}},
      "[Tags](#cfn-cloudwatch-space-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudwatch-space-syntax.yaml"></a>

```
Type: AWS::CloudWatch::Space
Properties:
  [AgentCoreEvaluationRoleArn](#cfn-cloudwatch-space-agentcoreevaluationrolearn): {{String}}
  [DataAccessRoleArn](#cfn-cloudwatch-space-dataaccessrolearn): {{String}}
  [DomainId](#cfn-cloudwatch-space-domainid): {{String}}
  [EncryptionConfiguration](#cfn-cloudwatch-space-encryptionconfiguration): {{
    EncryptionConfiguration}}
  [Name](#cfn-cloudwatch-space-name): {{String}}
  [Tags](#cfn-cloudwatch-space-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudwatch-space-properties"></a>

`AgentCoreEvaluationRoleArn`  <a name="cfn-cloudwatch-space-agentcoreevaluationrolearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:.+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataAccessRoleArn`  <a name="cfn-cloudwatch-space-dataaccessrolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainId`  <a name="cfn-cloudwatch-space-domainid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^d-[0-9a-z]{1,25}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncryptionConfiguration`  <a name="cfn-cloudwatch-space-encryptionconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [EncryptionConfiguration](aws-properties-cloudwatch-space-encryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudwatch-space-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]+(-[a-z0-9]+)*$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cloudwatch-space-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-space-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudwatch-space-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-space-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudwatch-space-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudwatch-space-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`OwnerAccountId`  <a name="OwnerAccountId-fn::getatt"></a>
Property description not available.

`Region`  <a name="Region-fn::getatt"></a>
Property description not available.

`SpaceId`  <a name="SpaceId-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Property description not available.
