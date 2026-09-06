---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-telemetryrule-singleheader.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::TelemetryRule SingleHeader
<a name="aws-properties-observabilityadmin-telemetryrule-singleheader"></a>

 Structure containing a name field limited to 64 characters for header or query parameter identification.

## Syntax
<a name="aws-properties-observabilityadmin-telemetryrule-singleheader-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-telemetryrule-singleheader-syntax.json"></a>

```
{
  "[Name](#cfn-observabilityadmin-telemetryrule-singleheader-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-telemetryrule-singleheader-syntax.yaml"></a>

```
  [Name](#cfn-observabilityadmin-telemetryrule-singleheader-name): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-telemetryrule-singleheader-properties"></a>

`Name`  <a name="cfn-observabilityadmin-telemetryrule-singleheader-name"></a>
 The name value, limited to 64 characters.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
