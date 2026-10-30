---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-accessgrant-accessgrantprincipalattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::AccessGrant AccessGrantPrincipalAttribute
<a name="aws-properties-cloudwatch-accessgrant-accessgrantprincipalattribute"></a>

A single attribute condition used to match principals for attribute-based access.

## Syntax
<a name="aws-properties-cloudwatch-accessgrant-accessgrantprincipalattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-accessgrant-accessgrantprincipalattribute-syntax.json"></a>

```
{
  "[Key](#cfn-cloudwatch-accessgrant-accessgrantprincipalattribute-key)" : {{String}},
  "[Value](#cfn-cloudwatch-accessgrant-accessgrantprincipalattribute-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-accessgrant-accessgrantprincipalattribute-syntax.yaml"></a>

```
  [Key](#cfn-cloudwatch-accessgrant-accessgrantprincipalattribute-key): {{String}}
  [Value](#cfn-cloudwatch-accessgrant-accessgrantprincipalattribute-value): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-accessgrant-accessgrantprincipalattribute-properties"></a>

`Key`  <a name="cfn-cloudwatch-accessgrant-accessgrantprincipalattribute-key"></a>
The Identity Center user attribute to match on. One of userName, active, userStatus, displayName, email, name.givenName, name.familyName, enterprise.department, enterprise.division, enterprise.organization, enterprise.costCenter, or enterprise.employeeNumber.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-cloudwatch-accessgrant-accessgrantprincipalattribute-value"></a>
The attribute value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
