---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-rtmppushrouterinputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput RtmpPushRouterInputConfiguration
<a name="aws-properties-mediaconnect-routerinput-rtmppushrouterinputconfiguration"></a>

<a name="aws-properties-mediaconnect-routerinput-rtmppushrouterinputconfiguration-description"></a>The `RtmpPushRouterInputConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::RouterInput](aws-resource-mediaconnect-routerinput.md).

## Syntax
<a name="aws-properties-mediaconnect-routerinput-rtmppushrouterinputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-rtmppushrouterinputconfiguration-syntax.json"></a>

```
{
  "[NamingConfiguration](#cfn-mediaconnect-routerinput-rtmppushrouterinputconfiguration-namingconfiguration)" : {{RtmpPushNamingConfiguration}},
  "[NamingType](#cfn-mediaconnect-routerinput-rtmppushrouterinputconfiguration-namingtype)" : {{String}},
  "[Port](#cfn-mediaconnect-routerinput-rtmppushrouterinputconfiguration-port)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-rtmppushrouterinputconfiguration-syntax.yaml"></a>

```
  [NamingConfiguration](#cfn-mediaconnect-routerinput-rtmppushrouterinputconfiguration-namingconfiguration): {{
    RtmpPushNamingConfiguration}}
  [NamingType](#cfn-mediaconnect-routerinput-rtmppushrouterinputconfiguration-namingtype): {{String}}
  [Port](#cfn-mediaconnect-routerinput-rtmppushrouterinputconfiguration-port): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-rtmppushrouterinputconfiguration-properties"></a>

`NamingConfiguration`  <a name="cfn-mediaconnect-routerinput-rtmppushrouterinputconfiguration-namingconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [RtmpPushNamingConfiguration](aws-properties-mediaconnect-routerinput-rtmppushnamingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NamingType`  <a name="cfn-mediaconnect-routerinput-rtmppushrouterinputconfiguration-namingtype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `MANUAL | AUTOMATIC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-mediaconnect-routerinput-rtmppushrouterinputconfiguration-port"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `1935`
*Maximum*: `1935`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
