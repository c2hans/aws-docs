---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-location-apikey-androidapp.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Location::APIKey AndroidApp
<a name="aws-properties-location-apikey-androidapp"></a>

<a name="aws-properties-location-apikey-androidapp-description"></a>The `AndroidApp` property type specifies Property description not available. for an [AWS::Location::APIKey](aws-resource-location-apikey.md).

## Syntax
<a name="aws-properties-location-apikey-androidapp-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-location-apikey-androidapp-syntax.json"></a>

```
{
  "[CertificateFingerprint](#cfn-location-apikey-androidapp-certificatefingerprint)" : {{String}},
  "[Package](#cfn-location-apikey-androidapp-package)" : {{String}}
}
```

### YAML
<a name="aws-properties-location-apikey-androidapp-syntax.yaml"></a>

```
  [CertificateFingerprint](#cfn-location-apikey-androidapp-certificatefingerprint): {{String}}
  [Package](#cfn-location-apikey-androidapp-package): {{String}}
```

## Properties
<a name="aws-properties-location-apikey-androidapp-properties"></a>

`CertificateFingerprint`  <a name="cfn-location-apikey-androidapp-certificatefingerprint"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^([A-Fa-f0-9]{2}:){19}[A-Fa-f0-9]{2}$`
*Minimum*: `59`
*Maximum*: `59`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Package`  <a name="cfn-location-apikey-androidapp-package"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^([A-Za-z][A-Za-z\d_]*\.)+[A-Za-z][A-Za-z\d_]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
