---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rtbfabric-inboundexternallink.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::InboundExternalLink
<a name="aws-resource-rtbfabric-inboundexternallink"></a>

<a name="aws-resource-rtbfabric-inboundexternallink-description"></a>The `AWS::RTBFabric::InboundExternalLink` resource Property description not available. for RTBFabric.

## Syntax
<a name="aws-resource-rtbfabric-inboundexternallink-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rtbfabric-inboundexternallink-syntax.json"></a>

```
{
  "Type" : "AWS::RTBFabric::InboundExternalLink",
  "Properties" : {
      "[GatewayId](#cfn-rtbfabric-inboundexternallink-gatewayid)" : {{String}},
      "[LinkAttributes](#cfn-rtbfabric-inboundexternallink-linkattributes)" : {{LinkAttributes}},
      "[LinkLogSettings](#cfn-rtbfabric-inboundexternallink-linklogsettings)" : {{LinkLogSettings}},
      "[Tags](#cfn-rtbfabric-inboundexternallink-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rtbfabric-inboundexternallink-syntax.yaml"></a>

```
Type: AWS::RTBFabric::InboundExternalLink
Properties:
  [GatewayId](#cfn-rtbfabric-inboundexternallink-gatewayid): {{String}}
  [LinkAttributes](#cfn-rtbfabric-inboundexternallink-linkattributes): {{
    LinkAttributes}}
  [LinkLogSettings](#cfn-rtbfabric-inboundexternallink-linklogsettings): {{
    LinkLogSettings}}
  [Tags](#cfn-rtbfabric-inboundexternallink-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-rtbfabric-inboundexternallink-properties"></a>

`GatewayId`  <a name="cfn-rtbfabric-inboundexternallink-gatewayid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^rtb-gw-[a-z0-9-]{1,25}$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LinkAttributes`  <a name="cfn-rtbfabric-inboundexternallink-linkattributes"></a>
Property description not available.
*Required*: No
*Type*: [LinkAttributes](aws-properties-rtbfabric-inboundexternallink-linkattributes.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LinkLogSettings`  <a name="cfn-rtbfabric-inboundexternallink-linklogsettings"></a>
Property description not available.
*Required*: Yes
*Type*: [LinkLogSettings](aws-properties-rtbfabric-inboundexternallink-linklogsettings.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Tags`  <a name="cfn-rtbfabric-inboundexternallink-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-rtbfabric-inboundexternallink-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rtbfabric-inboundexternallink-return-values"></a>

### Ref
<a name="aws-resource-rtbfabric-inboundexternallink-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-rtbfabric-inboundexternallink-return-values-fn--getatt"></a>

####
<a name="aws-resource-rtbfabric-inboundexternallink-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedTimestamp`  <a name="CreatedTimestamp-fn::getatt"></a>
Property description not available.

`DomainName`  <a name="DomainName-fn::getatt"></a>
Property description not available.

`LinkId`  <a name="LinkId-fn::getatt"></a>
Property description not available.

`LinkStatus`  <a name="LinkStatus-fn::getatt"></a>
Property description not available.

`UpdatedTimestamp`  <a name="UpdatedTimestamp-fn::getatt"></a>
Property description not available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
