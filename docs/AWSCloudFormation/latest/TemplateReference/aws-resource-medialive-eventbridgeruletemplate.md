---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-medialive-eventbridgeruletemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::EventBridgeRuleTemplate
<a name="aws-resource-medialive-eventbridgeruletemplate"></a>

<a name="aws-resource-medialive-eventbridgeruletemplate-description"></a>The `AWS::MediaLive::EventBridgeRuleTemplate` resource Property description not available. for MediaLive.

## Syntax
<a name="aws-resource-medialive-eventbridgeruletemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-medialive-eventbridgeruletemplate-syntax.json"></a>

```
{
  "Type" : "AWS::MediaLive::EventBridgeRuleTemplate",
  "Properties" : {
      "[Description](#cfn-medialive-eventbridgeruletemplate-description)" : {{String}},
      "[EventTargets](#cfn-medialive-eventbridgeruletemplate-eventtargets)" : {{[ EventBridgeRuleTemplateTarget, ... ]}},
      "[EventType](#cfn-medialive-eventbridgeruletemplate-eventtype)" : {{String}},
      "[GroupIdentifier](#cfn-medialive-eventbridgeruletemplate-groupidentifier)" : {{String}},
      "[Name](#cfn-medialive-eventbridgeruletemplate-name)" : {{String}},
      "[Tags](#cfn-medialive-eventbridgeruletemplate-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-medialive-eventbridgeruletemplate-syntax.yaml"></a>

```
Type: AWS::MediaLive::EventBridgeRuleTemplate
Properties:
  [Description](#cfn-medialive-eventbridgeruletemplate-description): {{String}}
  [EventTargets](#cfn-medialive-eventbridgeruletemplate-eventtargets): {{
    - EventBridgeRuleTemplateTarget}}
  [EventType](#cfn-medialive-eventbridgeruletemplate-eventtype): {{String}}
  [GroupIdentifier](#cfn-medialive-eventbridgeruletemplate-groupidentifier): {{String}}
  [Name](#cfn-medialive-eventbridgeruletemplate-name): {{String}}
  [Tags](#cfn-medialive-eventbridgeruletemplate-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-medialive-eventbridgeruletemplate-properties"></a>

`Description`  <a name="cfn-medialive-eventbridgeruletemplate-description"></a>
A resource's optional description.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventTargets`  <a name="cfn-medialive-eventbridgeruletemplate-eventtargets"></a>
The destinations that will receive the event notifications.
*Required*: No
*Type*: Array of [EventBridgeRuleTemplateTarget](aws-properties-medialive-eventbridgeruletemplate-eventbridgeruletemplatetarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventType`  <a name="cfn-medialive-eventbridgeruletemplate-eventtype"></a>
The type of event to match with the rule.
*Required*: Yes
*Type*: String
*Allowed values*: `MEDIALIVE_MULTIPLEX_ALERT | MEDIALIVE_MULTIPLEX_STATE_CHANGE | MEDIALIVE_CHANNEL_ALERT | MEDIALIVE_CHANNEL_INPUT_CHANGE | MEDIALIVE_CHANNEL_STATE_CHANGE | MEDIAPACKAGE_INPUT_NOTIFICATION | MEDIAPACKAGE_KEY_PROVIDER_NOTIFICATION | MEDIAPACKAGE_HARVEST_JOB_NOTIFICATION | SIGNAL_MAP_ACTIVE_ALARM | MEDIACONNECT_ALERT | MEDIACONNECT_SOURCE_HEALTH | MEDIACONNECT_OUTPUT_HEALTH | MEDIACONNECT_FLOW_STATUS_CHANGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupIdentifier`  <a name="cfn-medialive-eventbridgeruletemplate-groupidentifier"></a>
An eventbridge rule template group's identifier. Can be either be its id or current name.
*Required*: No
*Type*: String
*Pattern*: `^[^\s]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-medialive-eventbridgeruletemplate-name"></a>
A resource's name. Names must be unique within the scope of a resource type in a specific region.
*Required*: Yes
*Type*: String
*Pattern*: `^[^\s]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-medialive-eventbridgeruletemplate-tags"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-medialive-eventbridgeruletemplate-return-values"></a>

### Ref
<a name="aws-resource-medialive-eventbridgeruletemplate-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-medialive-eventbridgeruletemplate-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-medialive-eventbridgeruletemplate-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Target ARNs must be either an SNS topic or CloudWatch log group.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time of resource creation.

`GroupId`  <a name="GroupId-fn::getatt"></a>
An eventbridge rule template group's id. Amazon Web Services provided template groups have ids that start with <code>`aws-`</code>.

`Id`  <a name="Id-fn::getatt"></a>
An eventbridge rule template's id. Amazon Web Services provided templates have ids that start with <code>`aws-`</code>

`Identifier`  <a name="Identifier-fn::getatt"></a>
Property description not available.

`ModifiedAt`  <a name="ModifiedAt-fn::getatt"></a>
The date and time of latest resource modification.
