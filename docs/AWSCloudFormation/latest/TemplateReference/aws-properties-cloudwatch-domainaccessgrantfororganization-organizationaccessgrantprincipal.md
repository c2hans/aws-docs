---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-domainaccessgrantfororganization-organizationaccessgrantprincipal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::DomainAccessGrantForOrganization OrganizationAccessGrantPrincipal
<a name="aws-properties-cloudwatch-domainaccessgrantfororganization-organizationaccessgrantprincipal"></a>

<a name="aws-properties-cloudwatch-domainaccessgrantfororganization-organizationaccessgrantprincipal-description"></a>The `OrganizationAccessGrantPrincipal` property type specifies Property description not available. for an [AWS::CloudWatch::DomainAccessGrantForOrganization](aws-resource-cloudwatch-domainaccessgrantfororganization.md).

## Syntax
<a name="aws-properties-cloudwatch-domainaccessgrantfororganization-organizationaccessgrantprincipal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-domainaccessgrantfororganization-organizationaccessgrantprincipal-syntax.json"></a>

```
{
  "[PrincipalAttributes](#cfn-cloudwatch-domainaccessgrantfororganization-organizationaccessgrantprincipal-principalattributes)" : {{[ PrincipalAttribute, ... ]}},
  "[PrincipalId](#cfn-cloudwatch-domainaccessgrantfororganization-organizationaccessgrantprincipal-principalid)" : {{String}},
  "[PrincipalType](#cfn-cloudwatch-domainaccessgrantfororganization-organizationaccessgrantprincipal-principaltype)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-domainaccessgrantfororganization-organizationaccessgrantprincipal-syntax.yaml"></a>

```
  [PrincipalAttributes](#cfn-cloudwatch-domainaccessgrantfororganization-organizationaccessgrantprincipal-principalattributes): {{
    - PrincipalAttribute}}
  [PrincipalId](#cfn-cloudwatch-domainaccessgrantfororganization-organizationaccessgrantprincipal-principalid): {{String}}
  [PrincipalType](#cfn-cloudwatch-domainaccessgrantfororganization-organizationaccessgrantprincipal-principaltype): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-domainaccessgrantfororganization-organizationaccessgrantprincipal-properties"></a>

`PrincipalAttributes`  <a name="cfn-cloudwatch-domainaccessgrantfororganization-organizationaccessgrantprincipal-principalattributes"></a>
Property description not available.
*Required*: No
*Type*: Array of [PrincipalAttribute](aws-properties-cloudwatch-domainaccessgrantfororganization-principalattribute.md)
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrincipalId`  <a name="cfn-cloudwatch-domainaccessgrantfororganization-organizationaccessgrantprincipal-principalid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9:/_+=,.@-]*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrincipalType`  <a name="cfn-cloudwatch-domainaccessgrantfororganization-organizationaccessgrantprincipal-principaltype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `IDC_USER | IDC_GROUP | IAM_USER | IAM_ROLE | IAM_ROOT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
