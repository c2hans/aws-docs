---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rolesanywhere-crl.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RolesAnywhere::CRL
<a name="aws-resource-rolesanywhere-crl"></a>

<a name="aws-resource-rolesanywhere-crl-description"></a>The `AWS::RolesAnywhere::CRL` resource Property description not available. for RolesAnywhere.

## Syntax
<a name="aws-resource-rolesanywhere-crl-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rolesanywhere-crl-syntax.json"></a>

```
{
  "Type" : "AWS::RolesAnywhere::CRL",
  "Properties" : {
      "[CrlData](#cfn-rolesanywhere-crl-crldata)" : {{String}},
      "[Enabled](#cfn-rolesanywhere-crl-enabled)" : {{Boolean}},
      "[Name](#cfn-rolesanywhere-crl-name)" : {{String}},
      "[Tags](#cfn-rolesanywhere-crl-tags)" : {{[ Tag, ... ]}},
      "[TrustAnchorArn](#cfn-rolesanywhere-crl-trustanchorarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-rolesanywhere-crl-syntax.yaml"></a>

```
Type: AWS::RolesAnywhere::CRL
Properties:
  [CrlData](#cfn-rolesanywhere-crl-crldata): {{String}}
  [Enabled](#cfn-rolesanywhere-crl-enabled): {{Boolean}}
  [Name](#cfn-rolesanywhere-crl-name): {{String}}
  [Tags](#cfn-rolesanywhere-crl-tags): {{
    - Tag}}
  [TrustAnchorArn](#cfn-rolesanywhere-crl-trustanchorarn): {{String}}
```

## Properties
<a name="aws-resource-rolesanywhere-crl-properties"></a>

`CrlData`  <a name="cfn-rolesanywhere-crl-crldata"></a>
The x509 v3 specified certificate revocation list (CRL).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-rolesanywhere-crl-enabled"></a>
Specifies whether the certificate revocation list (CRL) is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-rolesanywhere-crl-name"></a>
The name of the certificate revocation list (CRL).
*Required*: Yes
*Type*: String
*Pattern*: `[ a-zA-Z0-9-_]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-rolesanywhere-crl-tags"></a>
A list of tags to attach to the certificate revocation list (CRL).
*Required*: No
*Type*: Array of [Tag](aws-properties-rolesanywhere-crl-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrustAnchorArn`  <a name="cfn-rolesanywhere-crl-trustanchorarn"></a>
The ARN of the TrustAnchor the certificate revocation list (CRL) will provide revocation for.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:rolesanywhere(:.*){2}(:trust-anchor.*)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rolesanywhere-crl-return-values"></a>

### Ref
<a name="aws-resource-rolesanywhere-crl-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns`CrlId`.

### Fn::GetAtt
<a name="aws-resource-rolesanywhere-crl-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-rolesanywhere-crl-return-values-fn--getatt-fn--getatt"></a>

`CrlId`  <a name="CrlId-fn::getatt"></a>
The unique primary identifier of the Crl
