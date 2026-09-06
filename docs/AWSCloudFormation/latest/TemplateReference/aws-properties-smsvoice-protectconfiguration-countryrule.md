---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-smsvoice-protectconfiguration-countryrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::ProtectConfiguration CountryRule
<a name="aws-properties-smsvoice-protectconfiguration-countryrule"></a>

Specifies the type of protection to use for a country.

For example, to set Canada as allowed, the `CountryRule` would be formatted as follows:

```
{
    "CountryCode": "CA",
    "ProtectStatus": "ALLOW"
}
```

## Syntax
<a name="aws-properties-smsvoice-protectconfiguration-countryrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-smsvoice-protectconfiguration-countryrule-syntax.json"></a>

```
{
  "[CountryCode](#cfn-smsvoice-protectconfiguration-countryrule-countrycode)" : {{String}},
  "[ProtectStatus](#cfn-smsvoice-protectconfiguration-countryrule-protectstatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-smsvoice-protectconfiguration-countryrule-syntax.yaml"></a>

```
  [CountryCode](#cfn-smsvoice-protectconfiguration-countryrule-countrycode): {{String}}
  [ProtectStatus](#cfn-smsvoice-protectconfiguration-countryrule-protectstatus): {{String}}
```

## Properties
<a name="aws-properties-smsvoice-protectconfiguration-countryrule-properties"></a>

`CountryCode`  <a name="cfn-smsvoice-protectconfiguration-countryrule-countrycode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Z]{2}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtectStatus`  <a name="cfn-smsvoice-protectconfiguration-countryrule-protectstatus"></a>
The types of protection that can be used.
*Required*: Yes
*Type*: String
*Allowed values*: `ALLOW | BLOCK | MONITOR | FILTER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
