---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-destination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Destination
<a name="aws-resource-logs-destination"></a>

The AWS::Logs::Destination resource specifies a CloudWatch Logs destination. A destination encapsulates a physical resource (such as an Amazon Kinesis data stream) and enables you to subscribe that resource to a stream of log events.

## Syntax
<a name="aws-resource-logs-destination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-logs-destination-syntax.json"></a>

```
{
  "Type" : "AWS::Logs::Destination",
  "Properties" : {
      "[DestinationName](#cfn-logs-destination-destinationname)" : {{String}},
      "[DestinationPolicy](#cfn-logs-destination-destinationpolicy)" : {{String}},
      "[RoleArn](#cfn-logs-destination-rolearn)" : {{String}},
      "[Tags](#cfn-logs-destination-tags)" : {{[ Tag, ... ]}},
      "[TargetArn](#cfn-logs-destination-targetarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-logs-destination-syntax.yaml"></a>

```
Type: AWS::Logs::Destination
Properties:
  [DestinationName](#cfn-logs-destination-destinationname): {{String}}
  [DestinationPolicy](#cfn-logs-destination-destinationpolicy): {{String}}
  [RoleArn](#cfn-logs-destination-rolearn): {{String}}
  [Tags](#cfn-logs-destination-tags): {{
    - Tag}}
  [TargetArn](#cfn-logs-destination-targetarn): {{String}}
```

## Properties
<a name="aws-resource-logs-destination-properties"></a>

`DestinationName`  <a name="cfn-logs-destination-destinationname"></a>
The name of the destination.
*Required*: Yes
*Type*: String
*Pattern*: `^[^:*]{1,512}$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DestinationPolicy`  <a name="cfn-logs-destination-destinationpolicy"></a>
An IAM policy document that governs which AWS accounts can create subscription filters against this destination.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-logs-destination-rolearn"></a>
The ARN of an IAM role that permits CloudWatch Logs to send data to the specified AWS resource.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-logs-destination-tags"></a>
The tags that have been assigned to this delivery destination.
*Required*: No
*Type*: Array of [Tag](aws-properties-logs-destination-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetArn`  <a name="cfn-logs-destination-targetarn"></a>
The Amazon Resource Name (ARN) of the physical target where the log events are delivered (for example, a Kinesis stream).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-logs-destination-return-values"></a>

### Ref
<a name="aws-resource-logs-destination-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name, such as `TestDestination`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-logs-destination-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-logs-destination-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the CloudWatch Logs destination, such as `arn:aws:logs:us-west-1:123456789012:destination:MyDestination`.

## Examples
<a name="aws-resource-logs-destination--examples"></a>

### Create a Destination
<a name="aws-resource-logs-destination--examples--Create_a_Destination"></a>

In the following example, the target stream (`TestStream`) can receive log events from CloudWatch Logs. CloudWatch Logs can use only the `PutSubscriptionFilter` action against the `TestDestination` destination.

#### JSON
<a name="aws-resource-logs-destination--examples--Create_a_Destination--json"></a>

```
"DestinationWithName" : {
  "Type" : "AWS::Logs::Destination",
  "Properties" : {
    "DestinationName": "TestDestination",
    "RoleArn": "arn:aws:iam::123456789012:role/LogKinesisRole",
    "TargetArn": "arn:aws:kinesis:us-east-1:123456789012:stream/TestStream",
    "DestinationPolicy": "{ \"Version\": \"2012-10-17\", \"Statement\": [{ \"Effect\": \"Allow\", \"Principal\": { \"AWS\": \"logs.amazonaws.com\"}, \"Action\": \"logs:PutSubscriptionFilter\",\"Resource\": \"arn:aws:logs:us-east-1:123456789012:destination:TestDestination\"}]}"
  }
}
```

#### YAML
<a name="aws-resource-logs-destination--examples--Create_a_Destination--yaml"></a>

```
DestinationWithName:
  Type: AWS::Logs::Destination
  Properties:
    DestinationName: "TestDestination"
    RoleArn: "arn:aws:iam::123456789012:role/LogKinesisRole"
    TargetArn: "arn:aws:kinesis:us-east-1:123456789012:stream/TestStream"
    DestinationPolicy: >
      {"Version" : "2012-10-17","Statement" : [{"Effect" : "Allow", "Principal" : {"AWS" : "logs.amazonaws.com"}, "Action" : "logs:PutSubscriptionFilter", "Resource" : "arn:aws:logs:us-east-1:123456789012:destination:TestDestination"}]}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
