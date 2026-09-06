---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-panorama-applicationinstance-manifestoverridespayload.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Panorama::ApplicationInstance ManifestOverridesPayload
<a name="aws-properties-panorama-applicationinstance-manifestoverridespayload"></a>

Parameter overrides for an application instance. This is a JSON document that has a single key (`PayloadData`) where the value is an escaped string representation of the overrides document.

## Syntax
<a name="aws-properties-panorama-applicationinstance-manifestoverridespayload-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-panorama-applicationinstance-manifestoverridespayload-syntax.json"></a>

```
{
  "[PayloadData](#cfn-panorama-applicationinstance-manifestoverridespayload-payloaddata)" : {{String}}
}
```

### YAML
<a name="aws-properties-panorama-applicationinstance-manifestoverridespayload-syntax.yaml"></a>

```
  [PayloadData](#cfn-panorama-applicationinstance-manifestoverridespayload-payloaddata): {{String}}
```

## Properties
<a name="aws-properties-panorama-applicationinstance-manifestoverridespayload-properties"></a>

`PayloadData`  <a name="cfn-panorama-applicationinstance-manifestoverridespayload-payloaddata"></a>
The overrides document.
*Required*: No
*Type*: String
*Pattern*: `^.+$`
*Minimum*: `0`
*Maximum*: `51200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
