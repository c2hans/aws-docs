---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-eventsource-awsserviceeventsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::EventSource AwsServiceEventsConfiguration
<a name="aws-properties-eventsv2-eventsource-awsserviceeventsconfiguration"></a>

Forward a single AWS service's events from the account's default event bus.

## Syntax
<a name="aws-properties-eventsv2-eventsource-awsserviceeventsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-eventsource-awsserviceeventsconfiguration-syntax.json"></a>

```
{
  "[AwsService](#cfn-eventsv2-eventsource-awsserviceeventsconfiguration-awsservice)" : {{String}},
  "[OnFailureConfiguration](#cfn-eventsv2-eventsource-awsserviceeventsconfiguration-onfailureconfiguration)" : {{OnFailureConfiguration}},
  "[Pattern](#cfn-eventsv2-eventsource-awsserviceeventsconfiguration-pattern)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-eventsource-awsserviceeventsconfiguration-syntax.yaml"></a>

```
  [AwsService](#cfn-eventsv2-eventsource-awsserviceeventsconfiguration-awsservice): {{String}}
  [OnFailureConfiguration](#cfn-eventsv2-eventsource-awsserviceeventsconfiguration-onfailureconfiguration): {{
    OnFailureConfiguration}}
  [Pattern](#cfn-eventsv2-eventsource-awsserviceeventsconfiguration-pattern): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-eventsource-awsserviceeventsconfiguration-properties"></a>

`AwsService`  <a name="cfn-eventsv2-eventsource-awsserviceeventsconfiguration-awsservice"></a>
A single AWS service source identifier, for example aws.s3. Wildcards and lists are not allowed.
*Required*: Yes
*Type*: String
*Pattern*: `^aws\.[a-z0-9\-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnFailureConfiguration`  <a name="cfn-eventsv2-eventsource-awsserviceeventsconfiguration-onfailureconfiguration"></a>
The destination for events that could not be forwarded.
*Required*: No
*Type*: [OnFailureConfiguration](aws-properties-eventsv2-eventsource-onfailureconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Pattern`  <a name="cfn-eventsv2-eventsource-awsserviceeventsconfiguration-pattern"></a>
A filter pattern, as a JSON string, that defines which events from the specified AWS service are forwarded to the event bus. Do not include source, account, or region as top-level fields. If you do not specify a pattern, all events from the service are forwarded.
*Required*: No
*Type*: String
*Maximum*: `3753`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
