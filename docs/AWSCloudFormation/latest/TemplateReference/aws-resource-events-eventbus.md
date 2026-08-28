---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-events-eventbus.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::EventBus
<a name="aws-resource-events-eventbus"></a>

Specifies an event bus within your account. This can be a custom event bus which you can use to receive events from your custom applications and services, or it can be a partner event bus which can be matched to a partner event source.

**Note**
As an aid to help you jumpstart developing CloudFormation templates, the EventBridge console enables you to create templates from the existing event buses in your account. For more information, see [Generating CloudFormation templates from an EventBridge event bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-generate-event-bus-template.html) in the *Amazon EventBridge User Guide*.

## Syntax
<a name="aws-resource-events-eventbus-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-events-eventbus-syntax.json"></a>

```
{
  "Type" : "AWS::Events::EventBus",
  "Properties" : {
      "[DeadLetterConfig](#cfn-events-eventbus-deadletterconfig)" : {{DeadLetterConfig}},
      "[Description](#cfn-events-eventbus-description)" : {{String}},
      "[EventSourceName](#cfn-events-eventbus-eventsourcename)" : {{String}},
      "[KmsKeyIdentifier](#cfn-events-eventbus-kmskeyidentifier)" : {{String}},
      "[LogConfig](#cfn-events-eventbus-logconfig)" : {{LogConfig}},
      "[Name](#cfn-events-eventbus-name)" : {{String}},
      "[Policy](#cfn-events-eventbus-policy)" : {{Json}},
      "[Tags](#cfn-events-eventbus-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-events-eventbus-syntax.yaml"></a>

```
Type: AWS::Events::EventBus
Properties:
  [DeadLetterConfig](#cfn-events-eventbus-deadletterconfig): {{
    DeadLetterConfig}}
  [Description](#cfn-events-eventbus-description): {{String}}
  [EventSourceName](#cfn-events-eventbus-eventsourcename): {{String}}
  [KmsKeyIdentifier](#cfn-events-eventbus-kmskeyidentifier): {{String}}
  [LogConfig](#cfn-events-eventbus-logconfig): {{
    LogConfig}}
  [Name](#cfn-events-eventbus-name): {{String}}
  [Policy](#cfn-events-eventbus-policy): {{Json}}
  [Tags](#cfn-events-eventbus-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-events-eventbus-properties"></a>

`DeadLetterConfig`  <a name="cfn-events-eventbus-deadletterconfig"></a>
Configuration details of the Amazon SQS queue for EventBridge to use as a dead-letter queue (DLQ).
For more information, see [Using dead-letter queues to process undelivered events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-event-delivery.html#eb-rule-dlq) in the *EventBridge User Guide*.
*Required*: No
*Type*: [DeadLetterConfig](aws-properties-events-eventbus-deadletterconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-events-eventbus-description"></a>
The event bus description.
*Required*: No
*Type*: String
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventSourceName`  <a name="cfn-events-eventbus-eventsourcename"></a>
If you are creating a partner event bus, this specifies the partner event source that the new event bus will be matched with.
*Required*: No
*Type*: String
*Pattern*: `aws\.partner(/[\.\-_A-Za-z0-9]+){2,}`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyIdentifier`  <a name="cfn-events-eventbus-kmskeyidentifier"></a>
The identifier of the AWS KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt events on this event bus. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.
If you do not specify a customer managed key identifier, EventBridge uses an AWS owned key to encrypt events on the event bus.
For more information, see [Identify and view keys](https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html) in the *AWS Key Management Service Developer Guide*.
Schema discovery is not supported for event buses encrypted using a customer managed key. EventBridge returns an error if:
+ You call ` [CreateDiscoverer](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-discoverers.html#CreateDiscoverer) ` on an event bus set to use a customer managed key for encryption.
+ You call ` [UpdatedEventBus](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdatedEventBus.html) ` to set a customer managed key on an event bus with schema discovery enabled.
To enable schema discovery on an event bus, choose to use an AWS owned key. For more information, see [Encrypting events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption-event-bus-cmkey.html) in the *Amazon EventBridge User Guide*.
If you have specified that EventBridge use a customer managed key for encrypting the source event bus, we strongly recommend you also specify a customer managed key for any archives for the event bus as well.
For more information, see [Encrypting archives](https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-archives.html) in the *Amazon EventBridge User Guide*.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-/:]*$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogConfig`  <a name="cfn-events-eventbus-logconfig"></a>
The logging configuration settings for the event bus.
For more information, see [Configuring logs for event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html) in the *Amazon EventBridge User Guide*.
*Required*: No
*Type*: [LogConfig](aws-properties-events-eventbus-logconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-events-eventbus-name"></a>
The name of the new event bus.
Custom event bus names can't contain the `/` character, but you can use the `/` character in partner event bus names. In addition, for partner event buses, the name must exactly match the name of the partner event source that this event bus is matched to.
You can't use the name `default` for a custom event bus, as this name is already used for your account's default event bus.
*Required*: Yes
*Type*: String
*Pattern*: `[/\.\-_A-Za-z0-9]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Policy`  <a name="cfn-events-eventbus-policy"></a>
The permissions policy of the event bus, describing which other AWS accounts can write events to this event bus.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-events-eventbus-tags"></a>
Tags to associate with the event bus.
*Required*: No
*Type*: Array of [Tag](aws-properties-events-eventbus-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-events-eventbus-return-values"></a>

### Ref
<a name="aws-resource-events-eventbus-return-values-ref"></a>

The name of the new event bus.

### Fn::GetAtt
<a name="aws-resource-events-eventbus-return-values-fn--getatt"></a>

The ARN of the task definition to use. If no task revision is supplied, it defaults to the most recent revision at the time of resource creation.

####
<a name="aws-resource-events-eventbus-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the event bus, such as `arn:aws:events:us-east-2:123456789012:event-bus/aws.partner/PartnerName/acct1/repo1`.

`Name`  <a name="Name-fn::getatt"></a>
The name of the event bus, such as `PartnerName/acct1/repo1`.

## Examples
<a name="aws-resource-events-eventbus--examples"></a>

**Topics**
+ [Create a partner event bus](#aws-resource-events-eventbus--examples--Create_a_partner_event_bus)
+ [Create a custom event bus](#aws-resource-events-eventbus--examples--Create_a_custom_event_bus)

### Create a partner event bus
<a name="aws-resource-events-eventbus--examples--Create_a_partner_event_bus"></a>

The following example creates a partner event bus named `aws.partner.repo1`.

#### JSON
<a name="aws-resource-events-eventbus--examples--Create_a_partner_event_bus--json"></a>

```
"SamplePartnerEventBus": {
    "Type": "AWS::Events::EventBus",
    "Properties": {
        "EventSourceName": "aws.partner/PartnerName/acct1/repo1",
        "Name": "aws.partner.repo1"
    }
}
```

#### YAML
<a name="aws-resource-events-eventbus--examples--Create_a_partner_event_bus--yaml"></a>

```
SamplePartnerEventBus:
    Type: AWS::Events::EventBus
    Properties:
        EventSourceName: "aws.partner/PartnerName/acct1/repo1"
        Name: "aws.partner.repo1"
```

### Create a custom event bus
<a name="aws-resource-events-eventbus--examples--Create_a_custom_event_bus"></a>

The following example creates a custom event bus named `MyCustomEventBus`.

#### JSON
<a name="aws-resource-events-eventbus--examples--Create_a_custom_event_bus--json"></a>

```
"SampleCustomEventBus": {
    "Type": "AWS::Events::EventBus",
    "Properties": {
        "Name": "MyCustomEventBus"
    }
}
```

#### YAML
<a name="aws-resource-events-eventbus--examples--Create_a_custom_event_bus--yaml"></a>

```
SampleCustomEventBus:
    Type: AWS::Events::EventBus
    Properties:
        Name: "MyCustomEventBus"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
