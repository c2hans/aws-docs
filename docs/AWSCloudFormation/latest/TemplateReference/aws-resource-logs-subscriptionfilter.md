---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-subscriptionfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::SubscriptionFilter
<a name="aws-resource-logs-subscriptionfilter"></a>

The `AWS::Logs::SubscriptionFilter` resource specifies a subscription filter and associates it with the specified log group. Subscription filters allow you to subscribe to a real-time stream of log events and have them delivered to a specific destination. Currently, the supported destinations are:
+ An Amazon Kinesis data stream belonging to the same account as the subscription filter, for same-account delivery.
+ A logical destination that belongs to a different account, for cross-account delivery.
+ An Amazon Kinesis Firehose delivery stream that belongs to the same account as the subscription filter, for same-account delivery.
+ An AWS Lambda function that belongs to the same account as the subscription filter, for same-account delivery.

There can be as many as two subscription filters associated with a log group.

## Syntax
<a name="aws-resource-logs-subscriptionfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-logs-subscriptionfilter-syntax.json"></a>

```
{
  "Type" : "AWS::Logs::SubscriptionFilter",
  "Properties" : {
      "[ApplyOnTransformedLogs](#cfn-logs-subscriptionfilter-applyontransformedlogs)" : {{Boolean}},
      "[DestinationArn](#cfn-logs-subscriptionfilter-destinationarn)" : {{String}},
      "[Distribution](#cfn-logs-subscriptionfilter-distribution)" : {{String}},
      "[EmitSystemFields](#cfn-logs-subscriptionfilter-emitsystemfields)" : {{[ String, ... ]}},
      "[FieldSelectionCriteria](#cfn-logs-subscriptionfilter-fieldselectioncriteria)" : {{String}},
      "[FilterName](#cfn-logs-subscriptionfilter-filtername)" : {{String}},
      "[FilterPattern](#cfn-logs-subscriptionfilter-filterpattern)" : {{String}},
      "[LogGroupName](#cfn-logs-subscriptionfilter-loggroupname)" : {{String}},
      "[RoleArn](#cfn-logs-subscriptionfilter-rolearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-logs-subscriptionfilter-syntax.yaml"></a>

```
Type: AWS::Logs::SubscriptionFilter
Properties:
  [ApplyOnTransformedLogs](#cfn-logs-subscriptionfilter-applyontransformedlogs): {{Boolean}}
  [DestinationArn](#cfn-logs-subscriptionfilter-destinationarn): {{String}}
  [Distribution](#cfn-logs-subscriptionfilter-distribution): {{String}}
  [EmitSystemFields](#cfn-logs-subscriptionfilter-emitsystemfields): {{
    - String}}
  [FieldSelectionCriteria](#cfn-logs-subscriptionfilter-fieldselectioncriteria): {{String}}
  [FilterName](#cfn-logs-subscriptionfilter-filtername): {{String}}
  [FilterPattern](#cfn-logs-subscriptionfilter-filterpattern): {{String}}
  [LogGroupName](#cfn-logs-subscriptionfilter-loggroupname): {{String}}
  [RoleArn](#cfn-logs-subscriptionfilter-rolearn): {{String}}
```

## Properties
<a name="aws-resource-logs-subscriptionfilter-properties"></a>

`ApplyOnTransformedLogs`  <a name="cfn-logs-subscriptionfilter-applyontransformedlogs"></a>
This parameter is valid only for log groups that have an active log transformer. For more information about log transformers, see [PutTransformer](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html).
If this value is `true`, the subscription filter is applied on the transformed version of the log events instead of the original ingested log events.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationArn`  <a name="cfn-logs-subscriptionfilter-destinationarn"></a>
The Amazon Resource Name (ARN) of the destination.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Distribution`  <a name="cfn-logs-subscriptionfilter-distribution"></a>
The method used to distribute log data to the destination, which can be either random or grouped by log stream.
*Required*: No
*Type*: String
*Allowed values*: `Random | ByLogStream`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmitSystemFields`  <a name="cfn-logs-subscriptionfilter-emitsystemfields"></a>
The list of system fields that are included in the log events sent to the subscription destination. Returns the `emitSystemFields` value if it was specified when the subscription filter was created.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldSelectionCriteria`  <a name="cfn-logs-subscriptionfilter-fieldselectioncriteria"></a>
The filter expression that specifies which log events are processed by this subscription filter based on system fields. Returns the `fieldSelectionCriteria` value if it was specified when the subscription filter was created.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterName`  <a name="cfn-logs-subscriptionfilter-filtername"></a>
The name of the subscription filter.
*Required*: No
*Type*: String
*Pattern*: `[^:*]*`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FilterPattern`  <a name="cfn-logs-subscriptionfilter-filterpattern"></a>
The filtering expressions that restrict what gets delivered to the destination AWS resource. For more information about the filter pattern syntax, see [Filter and Pattern Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroupName`  <a name="cfn-logs-subscriptionfilter-loggroupname"></a>
The log group to associate with the subscription filter. All log events that are uploaded to this log group are filtered and delivered to the specified AWS resource if the filter pattern matches the log events.
*Required*: Yes
*Type*: String
*Pattern*: `[\.\-_/#A-Za-z0-9]+`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-logs-subscriptionfilter-rolearn"></a>
The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-logs-subscriptionfilter-return-values"></a>

### Ref
<a name="aws-resource-logs-subscriptionfilter-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-logs-subscriptionfilter--examples"></a>

### Create a Subscription Filter
<a name="aws-resource-logs-subscriptionfilter--examples--Create_a_Subscription_Filter"></a>

The following example sends log events that are associated with the `Root` user to a Kinesis data stream.

#### JSON
<a name="aws-resource-logs-subscriptionfilter--examples--Create_a_Subscription_Filter--json"></a>

```
"SubscriptionFilter" : {
  "Type" : "AWS::Logs::SubscriptionFilter",
  "Properties" : {
    "RoleArn" : { "Fn::GetAtt" : [ "CloudWatchIAMRole", "Arn" ] },
    "LogGroupName" : { "Ref" : "LogGroup" },
    "Distribution" : "Random",
    "FilterName" : "filterNameString",
    "FilterPattern" : "{$.userIdentity.type = Root}",
    "DestinationArn" : { "Fn::GetAtt" : [ "KinesisStream", "Arn" ] }
  }
}
```

#### YAML
<a name="aws-resource-logs-subscriptionfilter--examples--Create_a_Subscription_Filter--yaml"></a>

```
SubscriptionFilter:
  Type: AWS::Logs::SubscriptionFilter
  Properties:
    RoleArn:
      Fn::GetAtt:
        - "CloudWatchIAMRole"
        - "Arn"
    LogGroupName:
      Ref: "LogGroup"
    Distribution: "Random"
    FilterName: "filterNameString"
    FilterPattern: "{$.userIdentity.type = Root}"
    DestinationArn:
      Fn::GetAtt:
        - "KinesisStream"
        - "Arn"
```
