---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-connection-resourceparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Connection ResourceParameters
<a name="aws-properties-events-connection-resourceparameters"></a>

The parameters for EventBridge to use when invoking the resource endpoint.

## Syntax
<a name="aws-properties-events-connection-resourceparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-connection-resourceparameters-syntax.json"></a>

```
{
  "[ResourceAssociationArn](#cfn-events-connection-resourceparameters-resourceassociationarn)" : {{String}},
  "[ResourceConfigurationArn](#cfn-events-connection-resourceparameters-resourceconfigurationarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-events-connection-resourceparameters-syntax.yaml"></a>

```
  [ResourceAssociationArn](#cfn-events-connection-resourceparameters-resourceassociationarn): {{String}}
  [ResourceConfigurationArn](#cfn-events-connection-resourceparameters-resourceconfigurationarn): {{String}}
```

## Properties
<a name="aws-properties-events-connection-resourceparameters-properties"></a>

`ResourceAssociationArn`  <a name="cfn-events-connection-resourceparameters-resourceassociationarn"></a>
For connections to private APIs, the Amazon Resource Name (ARN) of the resource association EventBridge created between the connection and the private API's resource configuration.
The value of this property is set by EventBridge. Any value you specify in your template is ignored.
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkresourceassociation/snra-[0-9a-z]{17}$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceConfigurationArn`  <a name="cfn-events-connection-resourceparameters-resourceconfigurationarn"></a>
The Amazon Resource Name (ARN) of the Amazon VPC Lattice resource configuration for the resource endpoint.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9f\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
