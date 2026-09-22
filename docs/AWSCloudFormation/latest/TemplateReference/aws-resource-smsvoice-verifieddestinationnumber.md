---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-smsvoice-verifieddestinationnumber.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::VerifiedDestinationNumber
<a name="aws-resource-smsvoice-verifieddestinationnumber"></a>

You can only send messages to verified destination numbers when your account is in the sandbox. You can add up to 10 verified destination numbers.

## Syntax
<a name="aws-resource-smsvoice-verifieddestinationnumber-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-smsvoice-verifieddestinationnumber-syntax.json"></a>

```
{
  "Type" : "AWS::SMSVOICE::VerifiedDestinationNumber",
  "Properties" : {
      "[DestinationPhoneNumber](#cfn-smsvoice-verifieddestinationnumber-destinationphonenumber)" : {{String}},
      "[Tags](#cfn-smsvoice-verifieddestinationnumber-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-smsvoice-verifieddestinationnumber-syntax.yaml"></a>

```
Type: AWS::SMSVOICE::VerifiedDestinationNumber
Properties:
  [DestinationPhoneNumber](#cfn-smsvoice-verifieddestinationnumber-destinationphonenumber): {{String}}
  [Tags](#cfn-smsvoice-verifieddestinationnumber-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-smsvoice-verifieddestinationnumber-properties"></a>

`DestinationPhoneNumber`  <a name="cfn-smsvoice-verifieddestinationnumber-destinationphonenumber"></a>
The verified destination phone number, in E.164 format.
*Required*: Yes
*Type*: String
*Pattern*: `^\+?[1-9][0-9]{1,18}$`
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-smsvoice-verifieddestinationnumber-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-smsvoice-verifieddestinationnumber-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-smsvoice-verifieddestinationnumber-return-values"></a>

### Ref
<a name="aws-resource-smsvoice-verifieddestinationnumber-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-smsvoice-verifieddestinationnumber-return-values-fn--getatt"></a>

####
<a name="aws-resource-smsvoice-verifieddestinationnumber-return-values-fn--getatt-fn--getatt"></a>

`CreatedTimestamp`  <a name="CreatedTimestamp-fn::getatt"></a>
The time when the destination phone number was created, in [UNIX epoch time](https://www.epochconverter.com/) format.

`Status`  <a name="Status-fn::getatt"></a>
The status of the verified destination phone number.
+ `PENDING`: The phone number hasn't been verified yet.
+ `VERIFIED`: The phone number is verified and can receive messages.

`VerifiedDestinationNumberArn`  <a name="VerifiedDestinationNumberArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the verified destination phone number.

`VerifiedDestinationNumberId`  <a name="VerifiedDestinationNumberId-fn::getatt"></a>
The unique identifier for the verified destination phone number.
