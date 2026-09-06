---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rtbfabric-outboundexternallink.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::OutboundExternalLink
<a name="aws-resource-rtbfabric-outboundexternallink"></a>

<a name="aws-resource-rtbfabric-outboundexternallink-description"></a>The `AWS::RTBFabric::OutboundExternalLink` resource Property description not available. for RTBFabric.

## Syntax
<a name="aws-resource-rtbfabric-outboundexternallink-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rtbfabric-outboundexternallink-syntax.json"></a>

```
{
  "Type" : "AWS::RTBFabric::OutboundExternalLink",
  "Properties" : {
      "[GatewayId](#cfn-rtbfabric-outboundexternallink-gatewayid)" : {{String}},
      "[LinkAttributes](#cfn-rtbfabric-outboundexternallink-linkattributes)" : {{LinkAttributes}},
      "[LinkLogSettings](#cfn-rtbfabric-outboundexternallink-linklogsettings)" : {{LinkLogSettings}},
      "[PublicEndpoint](#cfn-rtbfabric-outboundexternallink-publicendpoint)" : {{String}},
      "[Tags](#cfn-rtbfabric-outboundexternallink-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rtbfabric-outboundexternallink-syntax.yaml"></a>

```
Type: AWS::RTBFabric::OutboundExternalLink
Properties:
  [GatewayId](#cfn-rtbfabric-outboundexternallink-gatewayid): {{String}}
  [LinkAttributes](#cfn-rtbfabric-outboundexternallink-linkattributes): {{
    LinkAttributes}}
  [LinkLogSettings](#cfn-rtbfabric-outboundexternallink-linklogsettings): {{
    LinkLogSettings}}
  [PublicEndpoint](#cfn-rtbfabric-outboundexternallink-publicendpoint): {{String}}
  [Tags](#cfn-rtbfabric-outboundexternallink-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-rtbfabric-outboundexternallink-properties"></a>

`GatewayId`  <a name="cfn-rtbfabric-outboundexternallink-gatewayid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^rtb-gw-[a-z0-9-]{1,25}$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LinkAttributes`  <a name="cfn-rtbfabric-outboundexternallink-linkattributes"></a>
Property description not available.
*Required*: No
*Type*: [LinkAttributes](aws-properties-rtbfabric-outboundexternallink-linkattributes.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LinkLogSettings`  <a name="cfn-rtbfabric-outboundexternallink-linklogsettings"></a>
Property description not available.
*Required*: Yes
*Type*: [LinkLogSettings](aws-properties-rtbfabric-outboundexternallink-linklogsettings.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`PublicEndpoint`  <a name="cfn-rtbfabric-outboundexternallink-publicendpoint"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|http)://.+$`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Tags`  <a name="cfn-rtbfabric-outboundexternallink-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-rtbfabric-outboundexternallink-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rtbfabric-outboundexternallink-return-values"></a>

### Ref
<a name="aws-resource-rtbfabric-outboundexternallink-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-rtbfabric-outboundexternallink-return-values-fn--getatt"></a>

####
<a name="aws-resource-rtbfabric-outboundexternallink-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedTimestamp`  <a name="CreatedTimestamp-fn::getatt"></a>
Property description not available.

`LinkId`  <a name="LinkId-fn::getatt"></a>
Property description not available.

`LinkStatus`  <a name="LinkStatus-fn::getatt"></a>
Property description not available.

`UpdatedTimestamp`  <a name="UpdatedTimestamp-fn::getatt"></a>
Property description not available.
