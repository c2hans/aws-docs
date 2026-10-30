---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-domainaccessgrantfororganization-principalattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::DomainAccessGrantForOrganization PrincipalAttribute
<a name="aws-properties-cloudwatch-domainaccessgrantfororganization-principalattribute"></a>

An attribute key-value pair used to select principals.

## Syntax
<a name="aws-properties-cloudwatch-domainaccessgrantfororganization-principalattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-domainaccessgrantfororganization-principalattribute-syntax.json"></a>

```
{
  "[Key](#cfn-cloudwatch-domainaccessgrantfororganization-principalattribute-key)" : {{String}},
  "[Value](#cfn-cloudwatch-domainaccessgrantfororganization-principalattribute-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-domainaccessgrantfororganization-principalattribute-syntax.yaml"></a>

```
  [Key](#cfn-cloudwatch-domainaccessgrantfororganization-principalattribute-key): {{String}}
  [Value](#cfn-cloudwatch-domainaccessgrantfororganization-principalattribute-value): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-domainaccessgrantfororganization-principalattribute-properties"></a>

`Key`  <a name="cfn-cloudwatch-domainaccessgrantfororganization-principalattribute-key"></a>
The attribute name.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-cloudwatch-domainaccessgrantfororganization-principalattribute-value"></a>
The attribute value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
