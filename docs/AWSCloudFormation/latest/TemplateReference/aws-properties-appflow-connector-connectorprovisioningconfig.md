---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connector-connectorprovisioningconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Connector ConnectorProvisioningConfig
<a name="aws-properties-appflow-connector-connectorprovisioningconfig"></a>

Contains information about the configuration of the connector being registered.

## Syntax
<a name="aws-properties-appflow-connector-connectorprovisioningconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connector-connectorprovisioningconfig-syntax.json"></a>

```
{
  "[Lambda](#cfn-appflow-connector-connectorprovisioningconfig-lambda)" : {{LambdaConnectorProvisioningConfig}}
}
```

### YAML
<a name="aws-properties-appflow-connector-connectorprovisioningconfig-syntax.yaml"></a>

```
  [Lambda](#cfn-appflow-connector-connectorprovisioningconfig-lambda): {{
    LambdaConnectorProvisioningConfig}}
```

## Properties
<a name="aws-properties-appflow-connector-connectorprovisioningconfig-properties"></a>

`Lambda`  <a name="cfn-appflow-connector-connectorprovisioningconfig-lambda"></a>
Contains information about the configuration of the lambda which is being registered as the connector.
*Required*: No
*Type*: [LambdaConnectorProvisioningConfig](aws-properties-appflow-connector-lambdaconnectorprovisioningconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
