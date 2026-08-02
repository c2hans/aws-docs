---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_MessageAttributeValue.html
---

# MessageAttributeValue
<a name="API_MessageAttributeValue"></a>

The user-specified message attribute value. For string data types, the value attribute has the same restrictions on the content as the message body. For more information, see [Publish](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html).

Name, type, and value must not be empty or null. In addition, the message body should not be empty or null. All parts of the message attribute, including name, type, and value, are included in the message size restriction, which is currently 256 KB (262,144 bytes). For more information, see [Amazon SNS message attributes](https://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html) and [Publishing to a mobile phone](https://docs.aws.amazon.com/sns/latest/dg/sms_publish-to-phone.html) in the *Amazon SNS Developer Guide.*

## Contents
<a name="API_MessageAttributeValue_Contents"></a>

 ** DataType **
Amazon SNS supports the following logical data types: String, String.Array, Number, and Binary. For more information, see [Message Attribute Data Types](https://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html#SNSMessageAttributes.DataTypes).
Type: String
Required: Yes

 ** BinaryValue **
Binary type attributes can store any binary data, for example, compressed data, encrypted data, or images.
Type: Base64-encoded binary data object
Required: No

 ** StringValue **
Strings are Unicode with UTF8 binary encoding. For a list of code values, see [ASCII Printable Characters](https://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters).
Type: String
Required: No

## See Also
<a name="API_MessageAttributeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/MessageAttributeValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/MessageAttributeValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/MessageAttributeValue)
