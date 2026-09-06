---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-mlflowpropertiesinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection MlflowPropertiesInput
<a name="aws-properties-datazone-connection-mlflowpropertiesinput"></a>

The MLflow properties of a connection.

## Syntax
<a name="aws-properties-datazone-connection-mlflowpropertiesinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-mlflowpropertiesinput-syntax.json"></a>

```
{
  "[TrackingServerArn](#cfn-datazone-connection-mlflowpropertiesinput-trackingserverarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-connection-mlflowpropertiesinput-syntax.yaml"></a>

```
  [TrackingServerArn](#cfn-datazone-connection-mlflowpropertiesinput-trackingserverarn): {{String}}
```

## Properties
<a name="aws-properties-datazone-connection-mlflowpropertiesinput-properties"></a>

`TrackingServerArn`  <a name="cfn-datazone-connection-mlflowpropertiesinput-trackingserverarn"></a>
The tracking server ARN as part of the MLflow properties of a connection.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
