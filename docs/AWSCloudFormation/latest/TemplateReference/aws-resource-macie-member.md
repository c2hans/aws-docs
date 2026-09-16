---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-macie-member.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Macie::Member
<a name="aws-resource-macie-member"></a>

<a name="aws-resource-macie-member-description"></a>The `AWS::Macie::Member` resource Property description not available. for Macie.

## Syntax
<a name="aws-resource-macie-member-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-macie-member-syntax.json"></a>

```
{
  "Type" : "AWS::Macie::Member",
  "Properties" : {
      "[AccountId](#cfn-macie-member-accountid)" : {{String}},
      "[Email](#cfn-macie-member-email)" : {{String}},
      "[Tags](#cfn-macie-member-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-macie-member-syntax.yaml"></a>

```
Type: AWS::Macie::Member
Properties:
  [AccountId](#cfn-macie-member-accountid): {{String}}
  [Email](#cfn-macie-member-email): {{String}}
  [Tags](#cfn-macie-member-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-macie-member-properties"></a>

`AccountId`  <a name="cfn-macie-member-accountid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Email`  <a name="cfn-macie-member-email"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-macie-member-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-macie-member-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-macie-member-return-values"></a>

### Ref
<a name="aws-resource-macie-member-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-macie-member-return-values-fn--getatt"></a>

####
<a name="aws-resource-macie-member-return-values-fn--getatt-fn--getatt"></a>

`AdministratorAccountId`  <a name="AdministratorAccountId-fn::getatt"></a>
Property description not available.

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`RelationshipStatus`  <a name="RelationshipStatus-fn::getatt"></a>
Property description not available.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Property description not available.
