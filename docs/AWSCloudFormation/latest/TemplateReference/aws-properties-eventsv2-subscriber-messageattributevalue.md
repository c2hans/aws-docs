---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-messageattributevalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber MessageAttributeValue
<a name="aws-properties-eventsv2-subscriber-messageattributevalue"></a>

A message attribute value and its data type, for Amazon SQS and Amazon SNS targets.

## Syntax
<a name="aws-properties-eventsv2-subscriber-messageattributevalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-messageattributevalue-syntax.json"></a>

```
{
  "[BinaryValue](#cfn-eventsv2-subscriber-messageattributevalue-binaryvalue)" : {{String}},
  "[DataType](#cfn-eventsv2-subscriber-messageattributevalue-datatype)" : {{String}},
  "[StringValue](#cfn-eventsv2-subscriber-messageattributevalue-stringvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-messageattributevalue-syntax.yaml"></a>

```
  [BinaryValue](#cfn-eventsv2-subscriber-messageattributevalue-binaryvalue): {{String}}
  [DataType](#cfn-eventsv2-subscriber-messageattributevalue-datatype): {{String}}
  [StringValue](#cfn-eventsv2-subscriber-messageattributevalue-stringvalue): {{
    String}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-messageattributevalue-properties"></a>

`BinaryValue`  <a name="cfn-eventsv2-subscriber-messageattributevalue-binaryvalue"></a>
The attribute value for the Binary data type, Base64-encoded.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataType`  <a name="cfn-eventsv2-subscriber-messageattributevalue-datatype"></a>
The attribute data type. For Amazon SQS targets, specify String, Number, or Binary, optionally with a custom label suffix such as Number.float. For Amazon SNS targets, specify String, String.Array, Number, or Binary.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringValue`  <a name="cfn-eventsv2-subscriber-messageattributevalue-stringvalue"></a>
The attribute value for the String and Number data types (and String.Array for Amazon SNS targets).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
