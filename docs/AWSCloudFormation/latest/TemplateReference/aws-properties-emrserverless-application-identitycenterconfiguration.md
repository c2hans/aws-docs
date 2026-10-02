---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-identitycenterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application IdentityCenterConfiguration
<a name="aws-properties-emrserverless-application-identitycenterconfiguration"></a>

The IAM Identity Center Configuration accepts the Identity Center instance parameter required to enable trusted identity propagation. This configuration allows identity propagation between integrated services and the Identity Center instance.

## Syntax
<a name="aws-properties-emrserverless-application-identitycenterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-identitycenterconfiguration-syntax.json"></a>

```
{
  "[IdentityCenterInstanceArn](#cfn-emrserverless-application-identitycenterconfiguration-identitycenterinstancearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-identitycenterconfiguration-syntax.yaml"></a>

```
  [IdentityCenterInstanceArn](#cfn-emrserverless-application-identitycenterconfiguration-identitycenterinstancearn): {{String}}
```

## Properties
<a name="aws-properties-emrserverless-application-identitycenterconfiguration-properties"></a>

`IdentityCenterInstanceArn`  <a name="cfn-emrserverless-application-identitycenterconfiguration-identitycenterinstancearn"></a>
The ARN of the IAM Identity Center instance.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z0-9-]*):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
