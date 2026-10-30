---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-domain.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Domain
<a name="aws-resource-cloudwatch-domain"></a>

The account-level boundary for CloudWatch Omni. A domain configures the identity providers users sign in through and exposes the endpoint URLs used to reach CloudWatch Omni. Spaces are created within a domain.

## Syntax
<a name="aws-resource-cloudwatch-domain-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-domain-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::Domain",
  "Properties" : {
      "[IdentityProviderConfiguration](#cfn-cloudwatch-domain-identityproviderconfiguration)" : {{IdentityProviderConfiguration}},
      "[IdentityProviders](#cfn-cloudwatch-domain-identityproviders)" : {{[ String, ... ]}},
      "[Name](#cfn-cloudwatch-domain-name)" : {{String}},
      "[Tags](#cfn-cloudwatch-domain-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudwatch-domain-syntax.yaml"></a>

```
Type: AWS::CloudWatch::Domain
Properties:
  [IdentityProviderConfiguration](#cfn-cloudwatch-domain-identityproviderconfiguration): {{
    IdentityProviderConfiguration}}
  [IdentityProviders](#cfn-cloudwatch-domain-identityproviders): {{
    - String}}
  [Name](#cfn-cloudwatch-domain-name): {{String}}
  [Tags](#cfn-cloudwatch-domain-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudwatch-domain-properties"></a>

`IdentityProviderConfiguration`  <a name="cfn-cloudwatch-domain-identityproviderconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [IdentityProviderConfiguration](aws-properties-cloudwatch-domain-identityproviderconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityProviders`  <a name="cfn-cloudwatch-domain-identityproviders"></a>
The identity providers configured for the domain.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `IAM | IDC`
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudwatch-domain-name"></a>
A name that identifies the domain.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]+(-[a-z0-9]+)*$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cloudwatch-domain-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-domain-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudwatch-domain-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-domain-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the value of the `Arn` property.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudwatch-domain-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudwatch-domain-return-values-fn--getatt-fn--getatt"></a>

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

`Region`  <a name="Region-fn::getatt"></a>
The Region where this domain was created.

`Status`  <a name="Status-fn::getatt"></a>
Current status of the domain.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the domain was last updated.
