---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudtrail-channel-destination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudTrail::Channel Destination
<a name="aws-properties-cloudtrail-channel-destination"></a>

Contains information about the destination receiving events.

## Syntax
<a name="aws-properties-cloudtrail-channel-destination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudtrail-channel-destination-syntax.json"></a>

```
{
  "[Location](#cfn-cloudtrail-channel-destination-location)" : {{String}},
  "[Type](#cfn-cloudtrail-channel-destination-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudtrail-channel-destination-syntax.yaml"></a>

```
  [Location](#cfn-cloudtrail-channel-destination-location): {{String}}
  [Type](#cfn-cloudtrail-channel-destination-type): {{String}}
```

## Properties
<a name="aws-properties-cloudtrail-channel-destination-properties"></a>

`Location`  <a name="cfn-cloudtrail-channel-destination-location"></a>
 For channels used for a CloudTrail Lake integration, the location is the ARN of an event data store that receives events from a channel. For service-linked channels, the location is the name of the AWS service.
*Required*: Yes
*Type*: String
*Pattern*: `(^[a-zA-Z0-9._/\-:]+$)`
*Minimum*: `3`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-cloudtrail-channel-destination-type"></a>
The type of destination for events arriving from a channel. For channels used for a CloudTrail Lake integration, the value is `EVENT_DATA_STORE`. For service-linked channels, the value is `AWS_SERVICE`.
*Required*: Yes
*Type*: String
*Allowed values*: `EVENT_DATA_STORE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
