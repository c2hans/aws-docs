---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rtbfabric-link.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::Link
<a name="aws-resource-rtbfabric-link"></a>

Creates a new link between gateways.

Establishes a connection that allows gateways to communicate and exchange bid requests and responses.

## Syntax
<a name="aws-resource-rtbfabric-link-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rtbfabric-link-syntax.json"></a>

```
{
  "Type" : "AWS::RTBFabric::Link",
  "Properties" : {
      "[GatewayId](#cfn-rtbfabric-link-gatewayid)" : {{String}},
      "[HttpResponderAllowed](#cfn-rtbfabric-link-httpresponderallowed)" : {{Boolean}},
      "[LinkAttributes](#cfn-rtbfabric-link-linkattributes)" : {{LinkAttributes}},
      "[LinkLogSettings](#cfn-rtbfabric-link-linklogsettings)" : {{LinkLogSettings}},
      "[ModuleConfigurationList](#cfn-rtbfabric-link-moduleconfigurationlist)" : {{[ ModuleConfiguration, ... ]}},
      "[PeerGatewayId](#cfn-rtbfabric-link-peergatewayid)" : {{String}},
      "[Tags](#cfn-rtbfabric-link-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rtbfabric-link-syntax.yaml"></a>

```
Type: AWS::RTBFabric::Link
Properties:
  [GatewayId](#cfn-rtbfabric-link-gatewayid): {{String}}
  [HttpResponderAllowed](#cfn-rtbfabric-link-httpresponderallowed): {{Boolean}}
  [LinkAttributes](#cfn-rtbfabric-link-linkattributes): {{
    LinkAttributes}}
  [LinkLogSettings](#cfn-rtbfabric-link-linklogsettings): {{
    LinkLogSettings}}
  [ModuleConfigurationList](#cfn-rtbfabric-link-moduleconfigurationlist): {{
    - ModuleConfiguration}}
  [PeerGatewayId](#cfn-rtbfabric-link-peergatewayid): {{String}}
  [Tags](#cfn-rtbfabric-link-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-rtbfabric-link-properties"></a>

`GatewayId`  <a name="cfn-rtbfabric-link-gatewayid"></a>
The unique identifier of the gateway.
*Required*: Yes
*Type*: String
*Pattern*: `^rtb-gw-[a-z0-9-]{1,25}$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`HttpResponderAllowed`  <a name="cfn-rtbfabric-link-httpresponderallowed"></a>
Boolean to specify if an HTTP responder is allowed.
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LinkAttributes`  <a name="cfn-rtbfabric-link-linkattributes"></a>
Attributes of the link.
*Required*: No
*Type*: [LinkAttributes](aws-properties-rtbfabric-link-linkattributes.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LinkLogSettings`  <a name="cfn-rtbfabric-link-linklogsettings"></a>
Application log settings for the link. This value is required. Under `applicationLogs.sampling`, the `errorLog` and `filterLog` fields set the percentage of eligible events to log. Valid values range from `0` through `100`. To turn off application logs, set both fields to `0`, as in `{"applicationLogs":{"sampling":{"errorLog":0,"filterLog":0}}}`.
*Required*: Yes
*Type*: [LinkLogSettings](aws-properties-rtbfabric-link-linklogsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModuleConfigurationList`  <a name="cfn-rtbfabric-link-moduleconfigurationlist"></a>
Property description not available.
*Required*: No
*Type*: Array of [ModuleConfiguration](aws-properties-rtbfabric-link-moduleconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PeerGatewayId`  <a name="cfn-rtbfabric-link-peergatewayid"></a>
The unique identifier of the peer gateway.
*Required*: Yes
*Type*: String
*Pattern*: `^rtb-gw-[a-z0-9-]{1,25}$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Tags`  <a name="cfn-rtbfabric-link-tags"></a>
A map of the key-value pairs of the tag or tags to assign to the resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-rtbfabric-link-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rtbfabric-link-return-values"></a>

### Ref
<a name="aws-resource-rtbfabric-link-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-rtbfabric-link-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-rtbfabric-link-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedTimestamp`  <a name="CreatedTimestamp-fn::getatt"></a>
Property description not available.

`LinkDirection`  <a name="LinkDirection-fn::getatt"></a>
Property description not available.

`LinkId`  <a name="LinkId-fn::getatt"></a>
The unique identifier of the link.

`LinkStatus`  <a name="LinkStatus-fn::getatt"></a>
Property description not available.

`UpdatedTimestamp`  <a name="UpdatedTimestamp-fn::getatt"></a>
Property description not available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
