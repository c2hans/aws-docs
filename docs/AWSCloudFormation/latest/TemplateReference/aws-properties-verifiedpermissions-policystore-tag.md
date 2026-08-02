---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-verifiedpermissions-policystore-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VerifiedPermissions::PolicyStore Tag
<a name="aws-properties-verifiedpermissions-policystore-tag"></a>

A key-value pair associated with an AWS resource. In Verified Permissions, policy stores support tagging.

## Syntax
<a name="aws-properties-verifiedpermissions-policystore-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-verifiedpermissions-policystore-tag-syntax.json"></a>

```
{
  "[Key](#cfn-verifiedpermissions-policystore-tag-key)" : {{String}},
  "[Value](#cfn-verifiedpermissions-policystore-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-verifiedpermissions-policystore-tag-syntax.yaml"></a>

```
  [Key](#cfn-verifiedpermissions-policystore-tag-key): {{String}}
  [Value](#cfn-verifiedpermissions-policystore-tag-value): {{String}}
```

## Properties
<a name="aws-properties-verifiedpermissions-policystore-tag-properties"></a>

`Key`  <a name="cfn-verifiedpermissions-policystore-tag-key"></a>
A string you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-verifiedpermissions-policystore-tag-value"></a>
The value for the specified tag key.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
