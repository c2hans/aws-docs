---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-healthlake-fhirdatastore-nlpconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::HealthLake::FHIRDatastore NlpConfiguration
<a name="aws-properties-healthlake-fhirdatastore-nlpconfiguration"></a>

The natural language processing (NLP) configuration for a data store.

## Syntax
<a name="aws-properties-healthlake-fhirdatastore-nlpconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-healthlake-fhirdatastore-nlpconfiguration-syntax.json"></a>

```
{
  "[Status](#cfn-healthlake-fhirdatastore-nlpconfiguration-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-healthlake-fhirdatastore-nlpconfiguration-syntax.yaml"></a>

```
  [Status](#cfn-healthlake-fhirdatastore-nlpconfiguration-status): {{String}}
```

## Properties
<a name="aws-properties-healthlake-fhirdatastore-nlpconfiguration-properties"></a>

`Status`  <a name="cfn-healthlake-fhirdatastore-nlpconfiguration-status"></a>
The status of the NLP configuration.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
