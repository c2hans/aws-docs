---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networkfirewall-tlsinspectionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::TLSInspectionConfiguration
<a name="aws-resource-networkfirewall-tlsinspectionconfiguration"></a>

The object that defines a TLS inspection configuration.

AWS Network Firewall uses a TLS inspection configuration to decrypt traffic. Network Firewall re-encrypts the traffic before sending it to its destination.

To use a TLS inspection configuration, you add it to a new Network Firewall firewall policy, then you apply the firewall policy to a firewall. Network Firewall acts as a proxy service to decrypt and inspect the traffic traveling through your firewalls. You can reference a TLS inspection configuration from more than one firewall policy, and you can use a firewall policy in more than one firewall. For more information about using TLS inspection configurations, see [Inspecting SSL/TLS traffic with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html) in the *AWS Network Firewall Developer Guide*.

## Syntax
<a name="aws-resource-networkfirewall-tlsinspectionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-networkfirewall-tlsinspectionconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::NetworkFirewall::TLSInspectionConfiguration",
  "Properties" : {
      "[Description](#cfn-networkfirewall-tlsinspectionconfiguration-description)" : {{String}},
      "[Tags](#cfn-networkfirewall-tlsinspectionconfiguration-tags)" : {{[ Tag, ... ]}},
      "[TLSInspectionConfiguration](#cfn-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfiguration)" : {{TLSInspectionConfiguration}},
      "[TLSInspectionConfigurationName](#cfn-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfigurationname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-networkfirewall-tlsinspectionconfiguration-syntax.yaml"></a>

```
Type: AWS::NetworkFirewall::TLSInspectionConfiguration
Properties:
  [Description](#cfn-networkfirewall-tlsinspectionconfiguration-description): {{String}}
  [Tags](#cfn-networkfirewall-tlsinspectionconfiguration-tags): {{
    - Tag}}
  [TLSInspectionConfiguration](#cfn-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfiguration): {{
    TLSInspectionConfiguration}}
  [TLSInspectionConfigurationName](#cfn-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfigurationname): {{String}}
```

## Properties
<a name="aws-resource-networkfirewall-tlsinspectionconfiguration-properties"></a>

`Description`  <a name="cfn-networkfirewall-tlsinspectionconfiguration-description"></a>
A description of the TLS inspection configuration.
*Required*: No
*Type*: String
*Pattern*: `^.*$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-networkfirewall-tlsinspectionconfiguration-tags"></a>
The key:value pairs to associate with the resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-networkfirewall-tlsinspectionconfiguration-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TLSInspectionConfiguration`  <a name="cfn-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfiguration"></a>
The object that defines a TLS inspection configuration. AWS Network Firewall uses TLS inspection configurations to decrypt your firewall's inbound and outbound SSL/TLS traffic. After decryption, AWS Network Firewall inspects the traffic according to your firewall policy's stateful rules, and then re-encrypts it before sending it to its destination. You can enable inspection of your firewall's inbound traffic, outbound traffic, or both. To use TLS inspection with your firewall, you must first import or provision certificates using AWS Certificate Manager, create a TLS inspection configuration, add that configuration to a new firewall policy, and then associate that policy with your firewall. For more information about using TLS inspection configurations, see [Inspecting SSL/TLS traffic with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html) in the *AWS Network Firewall Developer Guide*.
*Required*: Yes
*Type*: [TLSInspectionConfiguration](aws-properties-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TLSInspectionConfigurationName`  <a name="cfn-networkfirewall-tlsinspectionconfiguration-tlsinspectionconfigurationname"></a>
The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-networkfirewall-tlsinspectionconfiguration-return-values"></a>

### Ref
<a name="aws-resource-networkfirewall-tlsinspectionconfiguration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-networkfirewall-tlsinspectionconfiguration-return-values-fn--getatt"></a>

####
<a name="aws-resource-networkfirewall-tlsinspectionconfiguration-return-values-fn--getatt-fn--getatt"></a>

`TLSInspectionConfigurationArn`  <a name="TLSInspectionConfigurationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the TLS inspection configuration.

`TLSInspectionConfigurationId`  <a name="TLSInspectionConfigurationId-fn::getatt"></a>
A unique identifier for the TLS inspection configuration. This ID is returned in the responses to create and list commands. You provide it to operations such as update and delete.
