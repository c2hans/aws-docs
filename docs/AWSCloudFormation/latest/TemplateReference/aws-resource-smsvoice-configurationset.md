---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-smsvoice-configurationset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::ConfigurationSet
<a name="aws-resource-smsvoice-configurationset"></a>

Creates a new configuration set. After you create the configuration set, you can add one or more event destinations to it.

A configuration set is a set of rules that you apply to the SMS and voice messages that you send.

When you send a message, you can optionally specify a single configuration set.

## Syntax
<a name="aws-resource-smsvoice-configurationset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-smsvoice-configurationset-syntax.json"></a>

```
{
  "Type" : "AWS::SMSVOICE::ConfigurationSet",
  "Properties" : {
      "[ConfigurationSetName](#cfn-smsvoice-configurationset-configurationsetname)" : {{String}},
      "[DefaultSenderId](#cfn-smsvoice-configurationset-defaultsenderid)" : {{String}},
      "[EventDestinations](#cfn-smsvoice-configurationset-eventdestinations)" : {{[ EventDestination, ... ]}},
      "[MessageFeedbackEnabled](#cfn-smsvoice-configurationset-messagefeedbackenabled)" : {{Boolean}},
      "[ProtectConfigurationId](#cfn-smsvoice-configurationset-protectconfigurationid)" : {{String}},
      "[Tags](#cfn-smsvoice-configurationset-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-smsvoice-configurationset-syntax.yaml"></a>

```
Type: AWS::SMSVOICE::ConfigurationSet
Properties:
  [ConfigurationSetName](#cfn-smsvoice-configurationset-configurationsetname): {{String}}
  [DefaultSenderId](#cfn-smsvoice-configurationset-defaultsenderid): {{String}}
  [EventDestinations](#cfn-smsvoice-configurationset-eventdestinations): {{
    - EventDestination}}
  [MessageFeedbackEnabled](#cfn-smsvoice-configurationset-messagefeedbackenabled): {{Boolean}}
  [ProtectConfigurationId](#cfn-smsvoice-configurationset-protectconfigurationid): {{String}}
  [Tags](#cfn-smsvoice-configurationset-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-smsvoice-configurationset-properties"></a>

`ConfigurationSetName`  <a name="cfn-smsvoice-configurationset-configurationsetname"></a>
The name of the ConfigurationSet.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DefaultSenderId`  <a name="cfn-smsvoice-configurationset-defaultsenderid"></a>
The default sender ID used by the ConfigurationSet.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventDestinations`  <a name="cfn-smsvoice-configurationset-eventdestinations"></a>
An array of EventDestination objects that describe any events to log and where to log them.
*Required*: No
*Type*: Array of [EventDestination](aws-properties-smsvoice-configurationset-eventdestination.md)
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessageFeedbackEnabled`  <a name="cfn-smsvoice-configurationset-messagefeedbackenabled"></a>
Set to true to enable feedback for the message.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtectConfigurationId`  <a name="cfn-smsvoice-configurationset-protectconfigurationid"></a>
The unique identifier for the protect configuration.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_:/-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-smsvoice-configurationset-tags"></a>
An array of key and value pair tags that's associated with the new configuration set.
*Required*: No
*Type*: Array of [Tag](aws-properties-smsvoice-configurationset-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-smsvoice-configurationset-return-values"></a>

### Ref
<a name="aws-resource-smsvoice-configurationset-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns`ConfigurationSetName`.

### Fn::GetAtt
<a name="aws-resource-smsvoice-configurationset-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-smsvoice-configurationset-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the ConfigurationSet.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
