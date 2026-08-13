---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-routingprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::RoutingProfile
<a name="aws-resource-connect-routingprofile"></a>

Creates a new routing profile.

## Syntax
<a name="aws-resource-connect-routingprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-routingprofile-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::RoutingProfile",
  "Properties" : {
      "[AgentAvailabilityTimer](#cfn-connect-routingprofile-agentavailabilitytimer)" : {{String}},
      "[DefaultOutboundQueueArn](#cfn-connect-routingprofile-defaultoutboundqueuearn)" : {{String}},
      "[Description](#cfn-connect-routingprofile-description)" : {{String}},
      "[InstanceArn](#cfn-connect-routingprofile-instancearn)" : {{String}},
      "[ManualAssignmentQueueConfigs](#cfn-connect-routingprofile-manualassignmentqueueconfigs)" : {{[ RoutingProfileManualAssignmentQueueConfig, ... ]}},
      "[MediaConcurrencies](#cfn-connect-routingprofile-mediaconcurrencies)" : {{[ MediaConcurrency, ... ]}},
      "[Name](#cfn-connect-routingprofile-name)" : {{String}},
      "[QueueConfigs](#cfn-connect-routingprofile-queueconfigs)" : {{[ RoutingProfileQueueConfig, ... ]}},
      "[Tags](#cfn-connect-routingprofile-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-connect-routingprofile-syntax.yaml"></a>

```
Type: AWS::Connect::RoutingProfile
Properties:
  [AgentAvailabilityTimer](#cfn-connect-routingprofile-agentavailabilitytimer): {{String}}
  [DefaultOutboundQueueArn](#cfn-connect-routingprofile-defaultoutboundqueuearn): {{String}}
  [Description](#cfn-connect-routingprofile-description): {{String}}
  [InstanceArn](#cfn-connect-routingprofile-instancearn): {{String}}
  [ManualAssignmentQueueConfigs](#cfn-connect-routingprofile-manualassignmentqueueconfigs): {{
    - RoutingProfileManualAssignmentQueueConfig}}
  [MediaConcurrencies](#cfn-connect-routingprofile-mediaconcurrencies): {{
    - MediaConcurrency}}
  [Name](#cfn-connect-routingprofile-name): {{String}}
  [QueueConfigs](#cfn-connect-routingprofile-queueconfigs): {{
    - RoutingProfileQueueConfig}}
  [Tags](#cfn-connect-routingprofile-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-connect-routingprofile-properties"></a>

`AgentAvailabilityTimer`  <a name="cfn-connect-routingprofile-agentavailabilitytimer"></a>
Whether agents with this routing profile will have their routing order calculated based on *time since their last inbound contact* or *longest idle time*.
*Required*: No
*Type*: String
*Allowed values*: `TIME_SINCE_LAST_ACTIVITY | TIME_SINCE_LAST_INBOUND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultOutboundQueueArn`  <a name="cfn-connect-routingprofile-defaultoutboundqueuearn"></a>
The Amazon Resource Name (ARN) of the default outbound queue for the routing profile.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/queue/[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-connect-routingprofile-description"></a>
The description of the routing profile.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-connect-routingprofile-instancearn"></a>
The identifier of the Connect Customer instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManualAssignmentQueueConfigs`  <a name="cfn-connect-routingprofile-manualassignmentqueueconfigs"></a>
Contains information about the queue and channel for manual assignment behaviour can be enabled.
*Required*: No
*Type*: Array of [RoutingProfileManualAssignmentQueueConfig](aws-properties-connect-routingprofile-routingprofilemanualassignmentqueueconfig.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaConcurrencies`  <a name="cfn-connect-routingprofile-mediaconcurrencies"></a>
The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.
*Required*: Yes
*Type*: Array of [MediaConcurrency](aws-properties-connect-routingprofile-mediaconcurrency.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-connect-routingprofile-name"></a>
The name of the routing profile.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueueConfigs`  <a name="cfn-connect-routingprofile-queueconfigs"></a>
The inbound queues associated with the routing profile. If no queue is added, the agent can make only outbound calls.
*Required*: No
*Type*: Array of [RoutingProfileQueueConfig](aws-properties-connect-routingprofile-routingprofilequeueconfig.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-connect-routingprofile-tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-routingprofile-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-routingprofile-return-values"></a>

### Ref
<a name="aws-resource-connect-routingprofile-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the routing profile name. For example:

 `{ "Ref": "myRoutingProfileName" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-connect-routingprofile-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-routingprofile-return-values-fn--getatt-fn--getatt"></a>

`RoutingProfileArn`  <a name="RoutingProfileArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the routing profile.
