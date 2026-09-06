---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-inspectorv2-connector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::Connector
<a name="aws-resource-inspectorv2-connector"></a>

<a name="aws-resource-inspectorv2-connector-description"></a>The `AWS::InspectorV2::Connector` resource Property description not available. for InspectorV2.

## Syntax
<a name="aws-resource-inspectorv2-connector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-inspectorv2-connector-syntax.json"></a>

```
{
  "Type" : "AWS::InspectorV2::Connector",
  "Properties" : {
      "[Description](#cfn-inspectorv2-connector-description)" : {{String}},
      "[Name](#cfn-inspectorv2-connector-name)" : {{String}},
      "[Provider](#cfn-inspectorv2-connector-provider)" : {{String}},
      "[ProviderConfiguration](#cfn-inspectorv2-connector-providerconfiguration)" : {{ProviderConfiguration}},
      "[Tags](#cfn-inspectorv2-connector-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-inspectorv2-connector-syntax.yaml"></a>

```
Type: AWS::InspectorV2::Connector
Properties:
  [Description](#cfn-inspectorv2-connector-description): {{String}}
  [Name](#cfn-inspectorv2-connector-name): {{String}}
  [Provider](#cfn-inspectorv2-connector-provider): {{String}}
  [ProviderConfiguration](#cfn-inspectorv2-connector-providerconfiguration): {{
    ProviderConfiguration}}
  [Tags](#cfn-inspectorv2-connector-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-inspectorv2-connector-properties"></a>

`Description`  <a name="cfn-inspectorv2-connector-description"></a>
A description of the connector.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-inspectorv2-connector-name"></a>
The name of the connector.
*Required*: Yes
*Type*: String
*Pattern*: `^[\p{L}\p{N}_-]+$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Provider`  <a name="cfn-inspectorv2-connector-provider"></a>
The cloud provider for the connector.
*Required*: Yes
*Type*: String
*Allowed values*: `AZURE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProviderConfiguration`  <a name="cfn-inspectorv2-connector-providerconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [ProviderConfiguration](aws-properties-inspectorv2-connector-providerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-inspectorv2-connector-tags"></a>
The tags associated with the connector.
*Required*: No
*Type*: Array of [Tag](aws-properties-inspectorv2-connector-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-inspectorv2-connector-return-values"></a>

### Ref
<a name="aws-resource-inspectorv2-connector-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-inspectorv2-connector-return-values-fn--getatt"></a>

####
<a name="aws-resource-inspectorv2-connector-return-values-fn--getatt-fn--getatt"></a>

`ConnectorArn`  <a name="ConnectorArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the connector.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the connector was created.

`EnablementStatus`  <a name="EnablementStatus-fn::getatt"></a>
The enablement status of the connector, which indicates whether the connector is active and scanning resources.

`EnablementStatusReason`  <a name="EnablementStatusReason-fn::getatt"></a>
Additional information about the current enablement status of the connector.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
Property description not available.

`ProviderConfiguration.Azure.ScopeConfiguration.ContainerImageScanning.State`  <a name="ProviderConfiguration.Azure.ScopeConfiguration.ContainerImageScanning.State-fn::getatt"></a>
Property description not available.

`ProviderConfiguration.Azure.ScopeConfiguration.ContainerImageScanning.StateReason`  <a name="ProviderConfiguration.Azure.ScopeConfiguration.ContainerImageScanning.StateReason-fn::getatt"></a>
Property description not available.

`ProviderConfiguration.Azure.ScopeConfiguration.ServerlessScanning.State`  <a name="ProviderConfiguration.Azure.ScopeConfiguration.ServerlessScanning.State-fn::getatt"></a>
Property description not available.

`ProviderConfiguration.Azure.ScopeConfiguration.ServerlessScanning.StateReason`  <a name="ProviderConfiguration.Azure.ScopeConfiguration.ServerlessScanning.StateReason-fn::getatt"></a>
Property description not available.

`ProviderConfiguration.Azure.ScopeConfiguration.VmScanning.State`  <a name="ProviderConfiguration.Azure.ScopeConfiguration.VmScanning.State-fn::getatt"></a>
Property description not available.

`ProviderConfiguration.Azure.ScopeConfiguration.VmScanning.StateReason`  <a name="ProviderConfiguration.Azure.ScopeConfiguration.VmScanning.StateReason-fn::getatt"></a>
Property description not available.
