---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-domainfororganization.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::DomainForOrganization
<a name="aws-resource-cloudwatch-domainfororganization"></a>

Resource Type definition for `AWS::CloudWatch::DomainForOrganization`. The organization-level boundary for CloudWatch Omni: an organization domain configures the identity providers users sign in through for the whole AWS Organization and exposes the endpoint URLs used to reach CloudWatch Omni. It can only be created by the organization's management account.

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
The ARN of an IAM role in the management account that CloudWatch Omni assumes for domain-scoped credential vending.
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
The identity providers configured for the domain.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `IAM | IDC`
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudwatch-domainfororganization-name"></a>
A name that identifies the domain.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]+(-[a-z0-9]+)*$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cloudwatch-domainfororganization-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-domainfororganization-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudwatch-domainfororganization-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-domainfororganization-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the value of the `Arn` property.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudwatch-domainfororganization-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudwatch-domainfororganization-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the resource.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the domain was created.

`CustomEndpointUrls`  <a name="CustomEndpointUrls-fn::getatt"></a>
Additional endpoint URLs derived from the domain name.

`DomainEndpointUrl`  <a name="DomainEndpointUrl-fn::getatt"></a>
The HTTPS endpoint URL for accessing the domain.

`DomainId`  <a name="DomainId-fn::getatt"></a>
The unique ID of the domain.

`IdentityCenterApplicationArn`  <a name="IdentityCenterApplicationArn-fn::getatt"></a>
The ARN of the Identity Center application. Absent for IAM-only domains.

`OrganizationId`  <a name="OrganizationId-fn::getatt"></a>
The ID of the AWS Organization this domain belongs to.

`OwnerAccountId`  <a name="OwnerAccountId-fn::getatt"></a>
The account ID of the organization's management account, which owns this domain.

`Region`  <a name="Region-fn::getatt"></a>
The Region where this domain was created.

`Status`  <a name="Status-fn::getatt"></a>
Current status of the domain.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the domain was last updated.
