---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-smsvoice-pool.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::Pool
<a name="aws-resource-smsvoice-pool"></a>

Creates a new pool and associates the specified origination identity to the pool. A pool can include one or more phone numbers and SenderIds that are associated with your AWS account.

The new pool inherits its configuration from the specified origination identity. This includes keywords, message type, opt-out list, two-way configuration, and self-managed opt-out configuration. Deletion protection isn't inherited from the origination identity and defaults to false.

If the origination identity is a phone number and is already associated with another pool, an error is returned. A sender ID can be associated with multiple pools.

## Syntax
<a name="aws-resource-smsvoice-pool-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-smsvoice-pool-syntax.json"></a>

```
{
  "Type" : "AWS::SMSVOICE::Pool",
  "Properties" : {
      "[DeletionProtectionEnabled](#cfn-smsvoice-pool-deletionprotectionenabled)" : {{Boolean}},
      "[MandatoryKeywords](#cfn-smsvoice-pool-mandatorykeywords)" : {{MandatoryKeywords}},
      "[OptionalKeywords](#cfn-smsvoice-pool-optionalkeywords)" : {{[ OptionalKeyword, ... ]}},
      "[OptOutListName](#cfn-smsvoice-pool-optoutlistname)" : {{String}},
      "[OriginationIdentities](#cfn-smsvoice-pool-originationidentities)" : {{[ String, ... ]}},
      "[SelfManagedOptOutsEnabled](#cfn-smsvoice-pool-selfmanagedoptoutsenabled)" : {{Boolean}},
      "[SharedRoutesEnabled](#cfn-smsvoice-pool-sharedroutesenabled)" : {{Boolean}},
      "[Tags](#cfn-smsvoice-pool-tags)" : {{[ Tag, ... ]}},
      "[TwoWay](#cfn-smsvoice-pool-twoway)" : {{TwoWay}}
    }
}
```

### YAML
<a name="aws-resource-smsvoice-pool-syntax.yaml"></a>

```
Type: AWS::SMSVOICE::Pool
Properties:
  [DeletionProtectionEnabled](#cfn-smsvoice-pool-deletionprotectionenabled): {{Boolean}}
  [MandatoryKeywords](#cfn-smsvoice-pool-mandatorykeywords): {{
    MandatoryKeywords}}
  [OptionalKeywords](#cfn-smsvoice-pool-optionalkeywords): {{
    - OptionalKeyword}}
  [OptOutListName](#cfn-smsvoice-pool-optoutlistname): {{String}}
  [OriginationIdentities](#cfn-smsvoice-pool-originationidentities): {{
    - String}}
  [SelfManagedOptOutsEnabled](#cfn-smsvoice-pool-selfmanagedoptoutsenabled): {{Boolean}}
  [SharedRoutesEnabled](#cfn-smsvoice-pool-sharedroutesenabled): {{Boolean}}
  [Tags](#cfn-smsvoice-pool-tags): {{
    - Tag}}
  [TwoWay](#cfn-smsvoice-pool-twoway): {{
    TwoWay}}
```

## Properties
<a name="aws-resource-smsvoice-pool-properties"></a>

`DeletionProtectionEnabled`  <a name="cfn-smsvoice-pool-deletionprotectionenabled"></a>
When set to true the pool can't be deleted.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MandatoryKeywords`  <a name="cfn-smsvoice-pool-mandatorykeywords"></a>
Creates or updates the pool's `MandatoryKeyword` configuration. For more information, see [Keywords](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html) in the AWS End User Messaging SMS User Guide.
*Required*: Yes
*Type*: [MandatoryKeywords](aws-properties-smsvoice-pool-mandatorykeywords.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OptionalKeywords`  <a name="cfn-smsvoice-pool-optionalkeywords"></a>
Specifies any optional keywords to associate with the pool. For more information, see [Keywords](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html) in the AWS End User Messaging SMS User Guide.
*Required*: No
*Type*: Array of [OptionalKeyword](aws-properties-smsvoice-pool-optionalkeyword.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OptOutListName`  <a name="cfn-smsvoice-pool-optoutlistname"></a>
The name of the OptOutList associated with the pool.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_:/-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OriginationIdentities`  <a name="cfn-smsvoice-pool-originationidentities"></a>
The list of origination identities to apply to the pool, either `PhoneNumberArn` or `SenderIdArn`. For more information, see [Registrations](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations.html) in the AWS End User Messaging SMS User Guide.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name (ARN).
*Required*: Yes
*Type*: Array of String
*Maximum*: `256`
*Minimum*: `20 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelfManagedOptOutsEnabled`  <a name="cfn-smsvoice-pool-selfmanagedoptoutsenabled"></a>
When set to false, an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, AWS End User Messaging SMS automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests. For more information see [Self-managed opt-outs](https://docs.aws.amazon.com/pinpoint/latest/userguide/settings-sms-managing.html#settings-account-sms-self-managed-opt-out)
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SharedRoutesEnabled`  <a name="cfn-smsvoice-pool-sharedroutesenabled"></a>
Allows you to enable shared routes on your pool.
By default, this is set to `False`. If you set this value to `True`, your messages are sent using phone numbers or sender IDs (depending on the country) that are shared with other users. In some countries, such as the United States, senders aren't allowed to use shared routes and must use a dedicated phone number or short code.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-smsvoice-pool-tags"></a>
An array of tags (key and value pairs) associated with the pool.
*Required*: No
*Type*: Array of [Tag](aws-properties-smsvoice-pool-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TwoWay`  <a name="cfn-smsvoice-pool-twoway"></a>
Describes the two-way SMS configuration for a phone number. For more information, see [Two-way SMS messaging](https://docs.aws.amazon.com/sms-voice/latest/userguide/two-way-sms.html) in the AWS End User Messaging SMS User Guide.
*Required*: No
*Type*: [TwoWay](aws-properties-smsvoice-pool-twoway.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-smsvoice-pool-return-values"></a>

### Ref
<a name="aws-resource-smsvoice-pool-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns`PoolId`.

### Fn::GetAtt
<a name="aws-resource-smsvoice-pool-return-values-fn--getatt"></a>

####
<a name="aws-resource-smsvoice-pool-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name of the `Pool`.

`PoolId`  <a name="PoolId-fn::getatt"></a>
The unique identifier for the pool.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
