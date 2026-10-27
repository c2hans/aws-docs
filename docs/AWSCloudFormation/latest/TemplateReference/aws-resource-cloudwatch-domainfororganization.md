---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-domainfororganization.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::DomainForOrganization
<a name="aws-resource-cloudwatch-domainfororganization"></a>

<a name="aws-resource-cloudwatch-domainfororganization-description"></a>The `AWS::CloudWatch::DomainForOrganization` resource Property description not available. for CloudWatch.

## Syntax
<a name="aws-resource-cloudwatch-domainfororganization-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-domainfororganization-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::DomainForOrganization",
  "Properties" : {
      "[DomainAccessRoleArn](#cfn-cloudwatch-domainfororganization-domainaccessrolearn)" : {{String}},
      "[IdentityProviderConfiguration](#cfn-cloudwatch-domainfororganization-identityproviderconfiguration)" : {{IdentityProviderConfiguration}},
      "[IdentityProviders](#cfn-cloudwatch-domainfororganization-identityproviders)" : {{[ String, ... ]}},
      "[Name](#cfn-cloudwatch-domainfororganization-name)" : {{String}},
      "[Tags](#cfn-cloudwatch-domainfororganization-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudwatch-domainfororganization-syntax.yaml"></a>

```
Type: AWS::CloudWatch::DomainForOrganization
Properties:
  [DomainAccessRoleArn](#cfn-cloudwatch-domainfororganization-domainaccessrolearn): {{String}}
  [IdentityProviderConfiguration](#cfn-cloudwatch-domainfororganization-identityproviderconfiguration): {{
    IdentityProviderConfiguration}}
  [IdentityProviders](#cfn-cloudwatch-domainfororganization-identityproviders): {{
    - String}}
  [Name](#cfn-cloudwatch-domainfororganization-name): {{String}}
  [Tags](#cfn-cloudwatch-domainfororganization-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudwatch-domainfororganization-properties"></a>

`DomainAccessRoleArn`  <a name="cfn-cloudwatch-domainfororganization-domainaccessrolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:iam::[0-9]{12}:role/.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdentityProviderConfiguration`  <a name="cfn-cloudwatch-domainfororganization-identityproviderconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [IdentityProviderConfiguration](aws-properties-cloudwatch-domainfororganization-identityproviderconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityProviders`  <a name="cfn-cloudwatch-domainfororganization-identityproviders"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `IAM | IDC`
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudwatch-domainfororganization-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]+(-[a-z0-9]+)*$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cloudwatch-domainfororganization-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-domainfororganization-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudwatch-domainfororganization-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-domainfororganization-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudwatch-domainfororganization-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudwatch-domainfororganization-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`CustomEndpointUrls`  <a name="CustomEndpointUrls-fn::getatt"></a>
Property description not available.

`DomainEndpointUrl`  <a name="DomainEndpointUrl-fn::getatt"></a>
Property description not available.

`DomainId`  <a name="DomainId-fn::getatt"></a>
Property description not available.

`IdentityCenterApplicationArn`  <a name="IdentityCenterApplicationArn-fn::getatt"></a>
Property description not available.

`OrganizationId`  <a name="OrganizationId-fn::getatt"></a>
Property description not available.

`OwnerAccountId`  <a name="OwnerAccountId-fn::getatt"></a>
Property description not available.

`Region`  <a name="Region-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Property description not available.
