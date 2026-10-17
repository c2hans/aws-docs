---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-healthlake-fhirdatastore-analyticsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::HealthLake::FHIRDatastore AnalyticsConfiguration
<a name="aws-properties-healthlake-fhirdatastore-analyticsconfiguration"></a>

The analytics configuration for a data store.

## Syntax
<a name="aws-properties-healthlake-fhirdatastore-analyticsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-healthlake-fhirdatastore-analyticsconfiguration-syntax.json"></a>

```
{
  "[Status](#cfn-healthlake-fhirdatastore-analyticsconfiguration-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-healthlake-fhirdatastore-analyticsconfiguration-syntax.yaml"></a>

```
  [Status](#cfn-healthlake-fhirdatastore-analyticsconfiguration-status): {{String}}
```

## Properties
<a name="aws-properties-healthlake-fhirdatastore-analyticsconfiguration-properties"></a>

`Status`  <a name="cfn-healthlake-fhirdatastore-analyticsconfiguration-status"></a>
The status of the analytics configuration.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | PAUSED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
