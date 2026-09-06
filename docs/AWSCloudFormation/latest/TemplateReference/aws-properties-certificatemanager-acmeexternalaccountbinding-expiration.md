---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-certificatemanager-acmeexternalaccountbinding-expiration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CertificateManager::AcmeExternalAccountBinding Expiration
<a name="aws-properties-certificatemanager-acmeexternalaccountbinding-expiration"></a>

Specifies an expiration configuration.

## Syntax
<a name="aws-properties-certificatemanager-acmeexternalaccountbinding-expiration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-certificatemanager-acmeexternalaccountbinding-expiration-syntax.json"></a>

```
{
  "[Type](#cfn-certificatemanager-acmeexternalaccountbinding-expiration-type)" : {{String}},
  "[Value](#cfn-certificatemanager-acmeexternalaccountbinding-expiration-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-certificatemanager-acmeexternalaccountbinding-expiration-syntax.yaml"></a>

```
  [Type](#cfn-certificatemanager-acmeexternalaccountbinding-expiration-type): {{String}}
  [Value](#cfn-certificatemanager-acmeexternalaccountbinding-expiration-value): {{Integer}}
```

## Properties
<a name="aws-properties-certificatemanager-acmeexternalaccountbinding-expiration-properties"></a>

`Type`  <a name="cfn-certificatemanager-acmeexternalaccountbinding-expiration-type"></a>
The time unit for the expiration value.
*Required*: Yes
*Type*: String
*Allowed values*: `MINUTES | HOURS | DAYS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-certificatemanager-acmeexternalaccountbinding-expiration-value"></a>
The numeric value of the expiration.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
