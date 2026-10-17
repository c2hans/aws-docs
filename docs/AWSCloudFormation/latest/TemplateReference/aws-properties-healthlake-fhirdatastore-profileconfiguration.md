---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-healthlake-fhirdatastore-profileconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::HealthLake::FHIRDatastore ProfileConfiguration
<a name="aws-properties-healthlake-fhirdatastore-profileconfiguration"></a>

The profile configuration for a data store.

## Syntax
<a name="aws-properties-healthlake-fhirdatastore-profileconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-healthlake-fhirdatastore-profileconfiguration-syntax.json"></a>

```
{
  "[DefaultProfiles](#cfn-healthlake-fhirdatastore-profileconfiguration-defaultprofiles)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-healthlake-fhirdatastore-profileconfiguration-syntax.yaml"></a>

```
  [DefaultProfiles](#cfn-healthlake-fhirdatastore-profileconfiguration-defaultprofiles): {{
    - String}}
```

## Properties
<a name="aws-properties-healthlake-fhirdatastore-profileconfiguration-properties"></a>

`DefaultProfiles`  <a name="cfn-healthlake-fhirdatastore-profileconfiguration-defaultprofiles"></a>
The list of default profiles for the data store.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
