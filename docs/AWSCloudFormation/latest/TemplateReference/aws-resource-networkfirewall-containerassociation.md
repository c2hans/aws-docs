---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networkfirewall-containerassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::ContainerAssociation
<a name="aws-resource-networkfirewall-containerassociation"></a>

Creates a AWS Network Firewall container association. The association monitors container lifecycle events in your Amazon ECS or Amazon EKS clusters and resolves running container addresses for use in firewall rules.

## Syntax
<a name="aws-resource-networkfirewall-containerassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-networkfirewall-containerassociation-syntax.json"></a>

```
{
  "Type" : "AWS::NetworkFirewall::ContainerAssociation",
  "Properties" : {
      "[ContainerAssociationName](#cfn-networkfirewall-containerassociation-containerassociationname)" : {{String}},
      "[ContainerMonitoringConfigurations](#cfn-networkfirewall-containerassociation-containermonitoringconfigurations)" : {{[ ContainerMonitoringConfiguration, ... ]}},
      "[Description](#cfn-networkfirewall-containerassociation-description)" : {{String}},
      "[Tags](#cfn-networkfirewall-containerassociation-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-networkfirewall-containerassociation-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-networkfirewall-containerassociation-syntax.yaml"></a>

```
Type: AWS::NetworkFirewall::ContainerAssociation
Properties:
  [ContainerAssociationName](#cfn-networkfirewall-containerassociation-containerassociationname): {{String}}
  [ContainerMonitoringConfigurations](#cfn-networkfirewall-containerassociation-containermonitoringconfigurations): {{
    - ContainerMonitoringConfiguration}}
  [Description](#cfn-networkfirewall-containerassociation-description): {{String}}
  [Tags](#cfn-networkfirewall-containerassociation-tags): {{
    - Tag}}
  [Type](#cfn-networkfirewall-containerassociation-type): {{String}}
```

## Properties
<a name="aws-resource-networkfirewall-containerassociation-properties"></a>

`ContainerAssociationName`  <a name="cfn-networkfirewall-containerassociation-containerassociationname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContainerMonitoringConfigurations`  <a name="cfn-networkfirewall-containerassociation-containermonitoringconfigurations"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [ContainerMonitoringConfiguration](aws-properties-networkfirewall-containerassociation-containermonitoringconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-networkfirewall-containerassociation-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^.*$`
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-networkfirewall-containerassociation-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-networkfirewall-containerassociation-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-networkfirewall-containerassociation-type"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ECS | EKS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-networkfirewall-containerassociation-return-values"></a>

### Ref
<a name="aws-resource-networkfirewall-containerassociation-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-networkfirewall-containerassociation-return-values-fn--getatt"></a>

####
<a name="aws-resource-networkfirewall-containerassociation-return-values-fn--getatt-fn--getatt"></a>

`ContainerAssociationArn`  <a name="ContainerAssociationArn-fn::getatt"></a>
Property description not available.

`ResolvedCidrCount`  <a name="ResolvedCidrCount-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.
