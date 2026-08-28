---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-personalize-eventtracker.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::EventTracker
<a name="aws-resource-personalize-eventtracker"></a>

Creates an event tracker that you use when adding event data to a specified dataset group using the [PutEvents](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutEvents.html) API.

**Note**
Only one event tracker can be associated with a dataset group. You will get an error if you call `CreateEventTracker` using the same dataset group as an existing event tracker.

When you create an event tracker, the response includes a tracking ID, which you pass as a parameter when you use the [PutEvents](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutEvents.html) operation. Amazon Personalize then appends the event data to the Item interactions dataset of the dataset group you specify in your event tracker.

The event tracker can be in one of the following states:
+ CREATE PENDING > CREATE IN\_PROGRESS > ACTIVE -or- CREATE FAILED
+ DELETE PENDING > DELETE IN\_PROGRESS

To get the status of the event tracker, call [DescribeEventTracker](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeEventTracker.html).

**Note**
The event tracker must be in the ACTIVE state before using the tracking ID.

**Related APIs**
+  [ListEventTrackers](https://docs.aws.amazon.com/personalize/latest/dg/API_ListEventTrackers.html)
+  [DescribeEventTracker](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeEventTracker.html)
+  [DeleteEventTracker](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteEventTracker.html)

## Syntax
<a name="aws-resource-personalize-eventtracker-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-personalize-eventtracker-syntax.json"></a>

```
{
  "Type" : "AWS::Personalize::EventTracker",
  "Properties" : {
      "[DatasetGroupArn](#cfn-personalize-eventtracker-datasetgrouparn)" : {{String}},
      "[Name](#cfn-personalize-eventtracker-name)" : {{String}},
      "[Tags](#cfn-personalize-eventtracker-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-personalize-eventtracker-syntax.yaml"></a>

```
Type: AWS::Personalize::EventTracker
Properties:
  [DatasetGroupArn](#cfn-personalize-eventtracker-datasetgrouparn): {{String}}
  [Name](#cfn-personalize-eventtracker-name): {{String}}
  [Tags](#cfn-personalize-eventtracker-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-personalize-eventtracker-properties"></a>

`DatasetGroupArn`  <a name="cfn-personalize-eventtracker-datasetgrouparn"></a>
The Amazon Resource Name (ARN) of the dataset group that receives the event data.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:([a-z\d-]+):personalize:.*:.*:.+$`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-personalize-eventtracker-name"></a>
The name of the event tracker.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-personalize-eventtracker-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-personalize-eventtracker-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-personalize-eventtracker-return-values"></a>

### Ref
<a name="aws-resource-personalize-eventtracker-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-personalize-eventtracker-return-values-fn--getatt"></a>

####
<a name="aws-resource-personalize-eventtracker-return-values-fn--getatt-fn--getatt"></a>

`EventTrackerArn`  <a name="EventTrackerArn-fn::getatt"></a>
The ARN of the event tracker.

`TrackingId`  <a name="TrackingId-fn::getatt"></a>
The ID of the event tracker. Include this ID in requests to the [PutEvents](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutEvents.html) API.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
