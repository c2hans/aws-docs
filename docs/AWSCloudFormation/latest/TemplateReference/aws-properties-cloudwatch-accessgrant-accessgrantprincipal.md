---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-accessgrant-accessgrantprincipal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::AccessGrant AccessGrantPrincipal
<a name="aws-properties-cloudwatch-accessgrant-accessgrantprincipal"></a>

The principal receiving the grant. Specify PrincipalId, PrincipalAttributes, or both.

## Syntax
<a name="aws-properties-cloudwatch-accessgrant-accessgrantprincipal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-accessgrant-accessgrantprincipal-syntax.json"></a>

```
{
  "[PrincipalAttributes](#cfn-cloudwatch-accessgrant-accessgrantprincipal-principalattributes)" : {{[ AccessGrantPrincipalAttribute, ... ]}},
  "[PrincipalId](#cfn-cloudwatch-accessgrant-accessgrantprincipal-principalid)" : {{String}},
  "[PrincipalType](#cfn-cloudwatch-accessgrant-accessgrantprincipal-principaltype)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-accessgrant-accessgrantprincipal-syntax.yaml"></a>

```
  [PrincipalAttributes](#cfn-cloudwatch-accessgrant-accessgrantprincipal-principalattributes): {{
    - AccessGrantPrincipalAttribute}}
  [PrincipalId](#cfn-cloudwatch-accessgrant-accessgrantprincipal-principalid): {{String}}
  [PrincipalType](#cfn-cloudwatch-accessgrant-accessgrantprincipal-principaltype): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-accessgrant-accessgrantprincipal-properties"></a>

`PrincipalAttributes`  <a name="cfn-cloudwatch-accessgrant-accessgrantprincipal-principalattributes"></a>
Attribute conditions for attribute-based access. When provided, the grant targets any principal matching all specified conditions. Supported only for IDC\_USER principals.
*Required*: No
*Type*: Array of [AccessGrantPrincipalAttribute](aws-properties-cloudwatch-accessgrant-accessgrantprincipalattribute.md)
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrincipalId`  <a name="cfn-cloudwatch-accessgrant-accessgrantprincipal-principalid"></a>
The ID of the principal receiving the grant. An IAM principal ARN, an Identity Center UUID, or a service-defined identifier.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9:/_+=,.@-]*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrincipalType`  <a name="cfn-cloudwatch-accessgrant-accessgrantprincipal-principaltype"></a>
The type of principal receiving the grant.
*Required*: Yes
*Type*: String
*Allowed values*: `IDC_USER | IDC_GROUP | IAM_USER | IAM_ROLE | IAM_ROOT | ACCESS_PROFILE | ALERT | AGENT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
