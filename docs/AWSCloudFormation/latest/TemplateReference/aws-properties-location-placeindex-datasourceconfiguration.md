---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-location-placeindex-datasourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Location::PlaceIndex DataSourceConfiguration
<a name="aws-properties-location-placeindex-datasourceconfiguration"></a>

Specifies the data storage option requesting Places.

## Syntax
<a name="aws-properties-location-placeindex-datasourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-location-placeindex-datasourceconfiguration-syntax.json"></a>

```
{
  "[IntendedUse](#cfn-location-placeindex-datasourceconfiguration-intendeduse)" : {{String}}
}
```

### YAML
<a name="aws-properties-location-placeindex-datasourceconfiguration-syntax.yaml"></a>

```
  [IntendedUse](#cfn-location-placeindex-datasourceconfiguration-intendeduse): {{String}}
```

## Properties
<a name="aws-properties-location-placeindex-datasourceconfiguration-properties"></a>

`IntendedUse`  <a name="cfn-location-placeindex-datasourceconfiguration-intendeduse"></a>
Specifies how the results of an operation will be stored by the caller.
Valid values include:
+ `SingleUse` specifies that the results won't be stored.
+ `Storage` specifies that the result can be cached or stored in a database.
Default value: `SingleUse`
*Required*: No
*Type*: String
*Allowed values*: `SingleUse | Storage`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
