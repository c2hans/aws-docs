---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-domain-identitycenterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Domain IdentityCenterConfiguration
<a name="aws-properties-cloudwatch-domain-identitycenterconfiguration"></a>

Identity Center configuration. Required when identityProviders includes IDC.

## Syntax
<a name="aws-properties-cloudwatch-domain-identitycenterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-domain-identitycenterconfiguration-syntax.json"></a>

```
{
  "[IdentityCenterInstanceArn](#cfn-cloudwatch-domain-identitycenterconfiguration-identitycenterinstancearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-domain-identitycenterconfiguration-syntax.yaml"></a>

```
  [IdentityCenterInstanceArn](#cfn-cloudwatch-domain-identitycenterconfiguration-identitycenterinstancearn): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-domain-identitycenterconfiguration-properties"></a>

`IdentityCenterInstanceArn`  <a name="cfn-cloudwatch-domain-identitycenterconfiguration-identitycenterinstancearn"></a>
Identity Center instance ARN
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z-]*:sso:::instance/[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
