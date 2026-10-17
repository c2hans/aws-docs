---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-firewall-listenerproperty.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::Firewall ListenerProperty
<a name="aws-properties-networkfirewall-firewall-listenerproperty"></a>

Open port for taking HTTP or HTTPS traffic.

## Syntax
<a name="aws-properties-networkfirewall-firewall-listenerproperty-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-firewall-listenerproperty-syntax.json"></a>

```
{
  "[Port](#cfn-networkfirewall-firewall-listenerproperty-port)" : {{Integer}},
  "[Type](#cfn-networkfirewall-firewall-listenerproperty-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkfirewall-firewall-listenerproperty-syntax.yaml"></a>

```
  [Port](#cfn-networkfirewall-firewall-listenerproperty-port): {{Integer}}
  [Type](#cfn-networkfirewall-firewall-listenerproperty-type): {{String}}
```

## Properties
<a name="aws-properties-networkfirewall-firewall-listenerproperty-properties"></a>

`Port`  <a name="cfn-networkfirewall-firewall-listenerproperty-port"></a>
Port for processing traffic.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-networkfirewall-firewall-listenerproperty-type"></a>
Selection of HTTP or HTTPS traffic.
*Required*: No
*Type*: String
*Allowed values*: `HTTP | HTTPS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
