---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-frauddetector-eventtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FraudDetector::EventType
<a name="aws-resource-frauddetector-eventtype"></a>

Manages an event type. An event is a business activity that is evaluated for fraud risk. With Amazon Fraud Detector, you generate fraud predictions for events. An event type defines the structure for an event sent to Amazon Fraud Detector. This includes the variables sent as part of the event, the entity performing the event (such as a customer), and the labels that classify the event. Example event types include online payment transactions, account registrations, and authentications.

## Syntax
<a name="aws-resource-frauddetector-eventtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-frauddetector-eventtype-syntax.json"></a>

```
{
  "Type" : "AWS::FraudDetector::EventType",
  "Properties" : {
      "[Description](#cfn-frauddetector-eventtype-description)" : {{String}},
      "[EntityTypes](#cfn-frauddetector-eventtype-entitytypes)" : {{[ EntityType, ... ]}},
      "[EventVariables](#cfn-frauddetector-eventtype-eventvariables)" : {{[ EventVariable, ... ]}},
      "[Labels](#cfn-frauddetector-eventtype-labels)" : {{[ Label, ... ]}},
      "[Name](#cfn-frauddetector-eventtype-name)" : {{String}},
      "[Tags](#cfn-frauddetector-eventtype-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-frauddetector-eventtype-syntax.yaml"></a>

```
Type: AWS::FraudDetector::EventType
Properties:
  [Description](#cfn-frauddetector-eventtype-description): {{String}}
  [EntityTypes](#cfn-frauddetector-eventtype-entitytypes): {{
    - EntityType}}
  [EventVariables](#cfn-frauddetector-eventtype-eventvariables): {{
    - EventVariable}}
  [Labels](#cfn-frauddetector-eventtype-labels): {{
    - Label}}
  [Name](#cfn-frauddetector-eventtype-name): {{String}}
  [Tags](#cfn-frauddetector-eventtype-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-frauddetector-eventtype-properties"></a>

`Description`  <a name="cfn-frauddetector-eventtype-description"></a>
The event type description.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EntityTypes`  <a name="cfn-frauddetector-eventtype-entitytypes"></a>
The event type entity types.
*Required*: Yes
*Type*: Array of [EntityType](aws-properties-frauddetector-eventtype-entitytype.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventVariables`  <a name="cfn-frauddetector-eventtype-eventvariables"></a>
The event type event variables.
*Required*: Yes
*Type*: Array of [EventVariable](aws-properties-frauddetector-eventtype-eventvariable.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Labels`  <a name="cfn-frauddetector-eventtype-labels"></a>
The event type labels.
*Required*: Yes
*Type*: Array of [Label](aws-properties-frauddetector-eventtype-label.md)
*Minimum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-frauddetector-eventtype-name"></a>
The event type name.
Pattern : `^[0-9a-z_-]+$`
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-z_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-frauddetector-eventtype-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-frauddetector-eventtype-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-frauddetector-eventtype-return-values"></a>

### Ref
<a name="aws-resource-frauddetector-eventtype-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the primary identifier for the resource, which is the Arn.

Example: `{"Ref": "arn:aws:frauddetector:us-west-2:123123123123:outcome/outcome_name"}`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-frauddetector-eventtype-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-frauddetector-eventtype-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The event type ARN.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
Timestamp of when event type was created.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
Timestamp of when event type was last updated.

## See also
<a name="aws-resource-frauddetector-eventtype--seealso"></a>
+ [PutEventType](https://docs.aws.amazon.com/frauddetector/latest/api/API_PutEventType.html) in the *Amazon Fraud Detector API Reference*
+ [Create event types](https://docs.aws.amazon.com/frauddetector/latest/ug/create-event-type.html) in the *Amazon Fraud Detector User Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
