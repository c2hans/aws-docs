---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-smsvoice-optoutlist.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::OptOutList
<a name="aws-resource-smsvoice-optoutlist"></a>

Creates a new opt-out list.

If the opt-out list name already exists, an error is returned.

An opt-out list is a list of phone numbers that are opted out, meaning you can't send SMS or voice messages to them. If end user replies with the keyword "STOP," an entry for the phone number is added to the opt-out list. In addition to STOP, your recipients can use any supported opt-out keyword, such as CANCEL or OPTOUT. For a list of supported opt-out keywords, see [ SMS opt out ](https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-keywords.html) in the AWS End User Messaging SMS User Guide.

## Syntax
<a name="aws-resource-smsvoice-optoutlist-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-smsvoice-optoutlist-syntax.json"></a>

```
{
  "Type" : "AWS::SMSVOICE::OptOutList",
  "Properties" : {
      "[OptOutListName](#cfn-smsvoice-optoutlist-optoutlistname)" : {{String}},
      "[Tags](#cfn-smsvoice-optoutlist-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-smsvoice-optoutlist-syntax.yaml"></a>

```
Type: AWS::SMSVOICE::OptOutList
Properties:
  [OptOutListName](#cfn-smsvoice-optoutlist-optoutlistname): {{String}}
  [Tags](#cfn-smsvoice-optoutlist-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-smsvoice-optoutlist-properties"></a>

`OptOutListName`  <a name="cfn-smsvoice-optoutlist-optoutlistname"></a>
The name of the OptOutList.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-smsvoice-optoutlist-tags"></a>
An array of tags (key and value pairs) to associate with the new OptOutList.
*Required*: No
*Type*: Array of [Tag](aws-properties-smsvoice-optoutlist-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-smsvoice-optoutlist-return-values"></a>

### Ref
<a name="aws-resource-smsvoice-optoutlist-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns`OptOutListName`.

### Fn::GetAtt
<a name="aws-resource-smsvoice-optoutlist-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-smsvoice-optoutlist-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the `OptOutList`.
