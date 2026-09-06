---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_MessageAttributeValue.html
---

# MessageAttributeValue
<a name="API_MessageAttributeValue"></a>

The user-specified message attribute value. For string data types, the `Value` attribute has the same restrictions on the content as the message body. For more information, see ` SendMessage.`

 `Name`, `type`, `value` and the message body must not be empty or null. All parts of the message attribute, including `Name`, `Type`, and `Value`, are part of the message size restriction (1 MiB or 1,048,576 bytes).

## Contents
<a name="API_MessageAttributeValue_Contents"></a>

 ** DataType **   <a name="SQS-Type-MessageAttributeValue-DataType"></a>
Amazon SQS supports the following logical data types: `String`, `Number`, and `Binary`. For the `Number` data type, you must use `StringValue`.
You can also append custom labels. For more information, see [Amazon SQS Message Attributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html#sqs-message-attributes) in the *Amazon SQS Developer Guide*.
Type: String
Required: Yes

 ** BinaryListValues **   <a name="SQS-Type-MessageAttributeValue-BinaryListValues"></a>
Not implemented. Reserved for future use.
Type: Array of Base64-encoded binary data objects
Required: No

 ** BinaryValue **   <a name="SQS-Type-MessageAttributeValue-BinaryValue"></a>
Binary type attributes can store any binary data, such as compressed data, encrypted data, or images.
Type: Base64-encoded binary data object
Required: No

 ** StringListValues **   <a name="SQS-Type-MessageAttributeValue-StringListValues"></a>
Not implemented. Reserved for future use.
Type: Array of strings
Required: No

 ** StringValue **   <a name="SQS-Type-MessageAttributeValue-StringValue"></a>
Strings are Unicode with UTF-8 binary encoding. For a list of code values, see [ASCII Printable Characters](http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters).
Type: String
Required: No

## See Also
<a name="API_MessageAttributeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/MessageAttributeValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/MessageAttributeValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/MessageAttributeValue)
