---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appflow-connector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Connector
<a name="aws-resource-appflow-connector"></a>

 Creates a new connector profile associated with your AWS account. There is a soft quota of 100 connector profiles per AWS account. If you need more connector profiles than this quota allows, you can submit a request to the Amazon AppFlow team through the Amazon AppFlow support channel. In each connector profile that you create, you can provide the credentials and properties for only one connector.

## Syntax
<a name="aws-resource-appflow-connector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appflow-connector-syntax.json"></a>

```
{
  "Type" : "AWS::AppFlow::Connector",
  "Properties" : {
      "[ConnectorLabel](#cfn-appflow-connector-connectorlabel)" : {{String}},
      "[ConnectorProvisioningConfig](#cfn-appflow-connector-connectorprovisioningconfig)" : {{ConnectorProvisioningConfig}},
      "[ConnectorProvisioningType](#cfn-appflow-connector-connectorprovisioningtype)" : {{String}},
      "[Description](#cfn-appflow-connector-description)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-appflow-connector-syntax.yaml"></a>

```
Type: AWS::AppFlow::Connector
Properties:
  [ConnectorLabel](#cfn-appflow-connector-connectorlabel): {{String}}
  [ConnectorProvisioningConfig](#cfn-appflow-connector-connectorprovisioningconfig): {{
    ConnectorProvisioningConfig}}
  [ConnectorProvisioningType](#cfn-appflow-connector-connectorprovisioningtype): {{String}}
  [Description](#cfn-appflow-connector-description): {{String}}
```

## Properties
<a name="aws-resource-appflow-connector-properties"></a>

`ConnectorLabel`  <a name="cfn-appflow-connector-connectorlabel"></a>
The label used for registering the connector.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9][\w!@#.-]+`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConnectorProvisioningConfig`  <a name="cfn-appflow-connector-connectorprovisioningconfig"></a>
The configuration required for registering the connector.
*Required*: Yes
*Type*: [ConnectorProvisioningConfig](aws-properties-appflow-connector-connectorprovisioningconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectorProvisioningType`  <a name="cfn-appflow-connector-connectorprovisioningtype"></a>
The provisioning type used to register the connector.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9][\w!@#.-]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-appflow-connector-description"></a>
A description about the connector runtime setting.
*Required*: No
*Type*: String
*Pattern*: `[\s\w/!@#+=.-]*`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-appflow-connector-return-values"></a>

### Ref
<a name="aws-resource-appflow-connector-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-appflow-connector-return-values-fn--getatt"></a>

####
<a name="aws-resource-appflow-connector-return-values-fn--getatt-fn--getatt"></a>

`ConnectorArn`  <a name="ConnectorArn-fn::getatt"></a>
Property description not available.
