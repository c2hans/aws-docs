---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-smsvoice-phonenumber.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::PhoneNumber
<a name="aws-resource-smsvoice-phonenumber"></a>

Request an origination phone number for use in your account. For more information on phone number request see [Request a phone number](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-request.html) in the *AWS End User Messaging SMS User Guide*.

**Note**
Registering phone numbers is not supported by AWS CloudFormation. You can import phone numbers and sender IDs that are automatically provisioned at registration.

## Syntax
<a name="aws-resource-smsvoice-phonenumber-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-smsvoice-phonenumber-syntax.json"></a>

```
{
  "Type" : "AWS::SMSVOICE::PhoneNumber",
  "Properties" : {
      "[DeletionProtectionEnabled](#cfn-smsvoice-phonenumber-deletionprotectionenabled)" : {{Boolean}},
      "[IsoCountryCode](#cfn-smsvoice-phonenumber-isocountrycode)" : {{String}},
      "[MandatoryKeywords](#cfn-smsvoice-phonenumber-mandatorykeywords)" : {{MandatoryKeywords}},
      "[NumberCapabilities](#cfn-smsvoice-phonenumber-numbercapabilities)" : {{[ String, ... ]}},
      "[NumberType](#cfn-smsvoice-phonenumber-numbertype)" : {{String}},
      "[OptionalKeywords](#cfn-smsvoice-phonenumber-optionalkeywords)" : {{[ OptionalKeyword, ... ]}},
      "[OptOutListName](#cfn-smsvoice-phonenumber-optoutlistname)" : {{String}},
      "[SelfManagedOptOutsEnabled](#cfn-smsvoice-phonenumber-selfmanagedoptoutsenabled)" : {{Boolean}},
      "[Tags](#cfn-smsvoice-phonenumber-tags)" : {{[ Tag, ... ]}},
      "[TwoWay](#cfn-smsvoice-phonenumber-twoway)" : {{TwoWay}}
    }
}
```

### YAML
<a name="aws-resource-smsvoice-phonenumber-syntax.yaml"></a>

```
Type: AWS::SMSVOICE::PhoneNumber
Properties:
  [DeletionProtectionEnabled](#cfn-smsvoice-phonenumber-deletionprotectionenabled): {{Boolean}}
  [IsoCountryCode](#cfn-smsvoice-phonenumber-isocountrycode): {{String}}
  [MandatoryKeywords](#cfn-smsvoice-phonenumber-mandatorykeywords): {{
    MandatoryKeywords}}
  [NumberCapabilities](#cfn-smsvoice-phonenumber-numbercapabilities): {{
    - String}}
  [NumberType](#cfn-smsvoice-phonenumber-numbertype): {{String}}
  [OptionalKeywords](#cfn-smsvoice-phonenumber-optionalkeywords): {{
    - OptionalKeyword}}
  [OptOutListName](#cfn-smsvoice-phonenumber-optoutlistname): {{String}}
  [SelfManagedOptOutsEnabled](#cfn-smsvoice-phonenumber-selfmanagedoptoutsenabled): {{Boolean}}
  [Tags](#cfn-smsvoice-phonenumber-tags): {{
    - Tag}}
  [TwoWay](#cfn-smsvoice-phonenumber-twoway): {{
    TwoWay}}
```

## Properties
<a name="aws-resource-smsvoice-phonenumber-properties"></a>

`DeletionProtectionEnabled`  <a name="cfn-smsvoice-phonenumber-deletionprotectionenabled"></a>
By default this is set to false. When set to true the phone number can't be deleted.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsoCountryCode`  <a name="cfn-smsvoice-phonenumber-isocountrycode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Z]{2}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MandatoryKeywords`  <a name="cfn-smsvoice-phonenumber-mandatorykeywords"></a>
Creates or updates a `MandatoryKeyword` configuration on an origination phone number For more information, see [Keywords](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html) in the AWS End User Messaging SMS User Guide.
*Required*: Yes
*Type*: [MandatoryKeywords](aws-properties-smsvoice-phonenumber-mandatorykeywords.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberCapabilities`  <a name="cfn-smsvoice-phonenumber-numbercapabilities"></a>
Indicates if the phone number will be used for text messages, voice messages, or both.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `SMS | VOICE | MMS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NumberType`  <a name="cfn-smsvoice-phonenumber-numbertype"></a>
The type of phone number to request.
The `ShortCode` number type is not supported in AWS CloudFormation.
*Required*: Yes
*Type*: String
*Allowed values*: `LONG_CODE | TOLL_FREE | TEN_DLC | SIMULATOR`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OptionalKeywords`  <a name="cfn-smsvoice-phonenumber-optionalkeywords"></a>
A keyword is a word that you can search for on a particular phone number or pool. It is also a specific word or phrase that an end user can send to your number to elicit a response, such as an informational message or a special offer. When your number receives a message that begins with a keyword, AWS End User Messaging SMS responds with a customizable message. Optional keywords are differentiated from mandatory keywords. For more information, see [Keywords](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html) in the AWS End User Messaging SMS User Guide.
*Required*: No
*Type*: Array of [OptionalKeyword](aws-properties-smsvoice-phonenumber-optionalkeyword.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OptOutListName`  <a name="cfn-smsvoice-phonenumber-optoutlistname"></a>
The name of the OptOutList associated with the phone number.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_:/-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelfManagedOptOutsEnabled`  <a name="cfn-smsvoice-phonenumber-selfmanagedoptoutsenabled"></a>
When set to false and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, AWS End User Messaging SMS automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out request. For more information see [Self-managed opt-outs](https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-self-managed.html)
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-smsvoice-phonenumber-tags"></a>
An array of tags (key and value pairs) to associate with the requested phone number.
*Required*: No
*Type*: Array of [Tag](aws-properties-smsvoice-phonenumber-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TwoWay`  <a name="cfn-smsvoice-phonenumber-twoway"></a>
Describes the two-way SMS configuration for a phone number. For more information, see [Two-way SMS messaging](https://docs.aws.amazon.com/sms-voice/latest/userguide/two-way-sms.html) in the AWS End User Messaging SMS User Guide.
*Required*: No
*Type*: [TwoWay](aws-properties-smsvoice-phonenumber-twoway.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-smsvoice-phonenumber-return-values"></a>

### Ref
<a name="aws-resource-smsvoice-phonenumber-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns`PhoneNumberId`.

### Fn::GetAtt
<a name="aws-resource-smsvoice-phonenumber-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-smsvoice-phonenumber-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The `PhoneNumber`'s Amazon Resource Name (ARN)

`PhoneNumber`  <a name="PhoneNumber-fn::getatt"></a>
The phone number in E.164 format.

`PhoneNumberId`  <a name="PhoneNumberId-fn::getatt"></a>
The unique identifier for the phone number.
