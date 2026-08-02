---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-verifiedpermissions-policy-entityidentifier.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::Policy EntityIdentifier
<a name="aws-properties-verifiedpermissions-policy-entityidentifier"></a>

Contains the identifier of an entity in a policy, including its ID and type.

## Syntax
<a name="aws-properties-verifiedpermissions-policy-entityidentifier-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-verifiedpermissions-policy-entityidentifier-syntax.json"></a>

```
{
  "[EntityId](#cfn-verifiedpermissions-policy-entityidentifier-entityid)" : {{String}},
  "[EntityType](#cfn-verifiedpermissions-policy-entityidentifier-entitytype)" : {{String}}
}
```

### YAML
<a name="aws-properties-verifiedpermissions-policy-entityidentifier-syntax.yaml"></a>

```
  [EntityId](#cfn-verifiedpermissions-policy-entityidentifier-entityid): {{String}}
  [EntityType](#cfn-verifiedpermissions-policy-entityidentifier-entitytype): {{String}}
```

## Properties
<a name="aws-properties-verifiedpermissions-policy-entityidentifier-properties"></a>

`EntityId`  <a name="cfn-verifiedpermissions-policy-entityidentifier-entityid"></a>
The identifier of an entity.
 `"entityId":"identifier"`
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EntityType`  <a name="cfn-verifiedpermissions-policy-entityidentifier-entitytype"></a>
The type of an entity.
Example: `"entityType":"typeName"`
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
