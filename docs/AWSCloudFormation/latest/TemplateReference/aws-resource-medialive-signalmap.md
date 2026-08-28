---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-medialive-signalmap.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::SignalMap
<a name="aws-resource-medialive-signalmap"></a>

<a name="aws-resource-medialive-signalmap-description"></a>The `AWS::MediaLive::SignalMap` resource Property description not available. for MediaLive.

## Syntax
<a name="aws-resource-medialive-signalmap-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-medialive-signalmap-syntax.json"></a>

```
{
  "Type" : "AWS::MediaLive::SignalMap",
  "Properties" : {
      "[CloudWatchAlarmTemplateGroupIdentifiers](#cfn-medialive-signalmap-cloudwatchalarmtemplategroupidentifiers)" : {{[ String, ... ]}},
      "[Description](#cfn-medialive-signalmap-description)" : {{String}},
      "[DiscoveryEntryPointArn](#cfn-medialive-signalmap-discoveryentrypointarn)" : {{String}},
      "[EventBridgeRuleTemplateGroupIdentifiers](#cfn-medialive-signalmap-eventbridgeruletemplategroupidentifiers)" : {{[ String, ... ]}},
      "[ForceRediscovery](#cfn-medialive-signalmap-forcerediscovery)" : {{Boolean}},
      "[Name](#cfn-medialive-signalmap-name)" : {{String}},
      "[Tags](#cfn-medialive-signalmap-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-medialive-signalmap-syntax.yaml"></a>

```
Type: AWS::MediaLive::SignalMap
Properties:
  [CloudWatchAlarmTemplateGroupIdentifiers](#cfn-medialive-signalmap-cloudwatchalarmtemplategroupidentifiers): {{
    - String}}
  [Description](#cfn-medialive-signalmap-description): {{String}}
  [DiscoveryEntryPointArn](#cfn-medialive-signalmap-discoveryentrypointarn): {{String}}
  [EventBridgeRuleTemplateGroupIdentifiers](#cfn-medialive-signalmap-eventbridgeruletemplategroupidentifiers): {{
    - String}}
  [ForceRediscovery](#cfn-medialive-signalmap-forcerediscovery): {{Boolean}}
  [Name](#cfn-medialive-signalmap-name): {{String}}
  [Tags](#cfn-medialive-signalmap-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-medialive-signalmap-properties"></a>

`CloudWatchAlarmTemplateGroupIdentifiers`  <a name="cfn-medialive-signalmap-cloudwatchalarmtemplategroupidentifiers"></a>
A cloudwatch alarm template group's identifier. Can be either be its id or current name.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-medialive-signalmap-description"></a>
A resource's optional description.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DiscoveryEntryPointArn`  <a name="cfn-medialive-signalmap-discoveryentrypointarn"></a>
A top-level supported Amazon Web Services resource ARN to discover a signal map from.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventBridgeRuleTemplateGroupIdentifiers`  <a name="cfn-medialive-signalmap-eventbridgeruletemplategroupidentifiers"></a>
An eventbridge rule template group's identifier. Can be either be its id or current name.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ForceRediscovery`  <a name="cfn-medialive-signalmap-forcerediscovery"></a>
If true, will force a rediscovery of a signal map if an unchanged discoveryEntryPointArn is provided.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-medialive-signalmap-name"></a>
A resource's name. Names must be unique within the scope of a resource type in a specific region.
*Required*: Yes
*Type*: String
*Pattern*: `^[^\s]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-medialive-signalmap-tags"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-medialive-signalmap-return-values"></a>

### Ref
<a name="aws-resource-medialive-signalmap-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-medialive-signalmap-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-medialive-signalmap-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
A signal map's ARN (Amazon Resource Name)

`CloudWatchAlarmTemplateGroupIds`  <a name="CloudWatchAlarmTemplateGroupIds-fn::getatt"></a>
An alarm template group's id.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time of resource creation.

`ErrorMessage`  <a name="ErrorMessage-fn::getatt"></a>
Error message associated with a failed creation or failed update attempt of a signal map.

`EventBridgeRuleTemplateGroupIds`  <a name="EventBridgeRuleTemplateGroupIds-fn::getatt"></a>
An eventbridge rule template group's id.

`Id`  <a name="Id-fn::getatt"></a>
A signal map's id.

`Identifier`  <a name="Identifier-fn::getatt"></a>
Property description not available.

`LastDiscoveredAt`  <a name="LastDiscoveredAt-fn::getatt"></a>
The date and time of latest discovery.

`ModifiedAt`  <a name="ModifiedAt-fn::getatt"></a>
The date and time of latest resource modification.

`MonitorChangesPendingDeployment`  <a name="MonitorChangesPendingDeployment-fn::getatt"></a>
If true, there are pending monitor changes for this signal map that can be deployed.

`Status`  <a name="Status-fn::getatt"></a>
A signal map's current status, which is dependent on its lifecycle actions or associated jobs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
