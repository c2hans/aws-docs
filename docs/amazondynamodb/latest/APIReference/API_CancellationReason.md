---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CancellationReason.html
---

# CancellationReason
<a name="API_CancellationReason"></a>

An ordered list of errors for each item in the request which caused the transaction to get cancelled. The values of the list are ordered according to the ordering of the `TransactWriteItems` request parameter. If no error occurred for the associated item an error with a Null code and Null message will be present.

## Contents
<a name="API_CancellationReason_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Code **   <a name="DDB-Type-CancellationReason-Code"></a>
Status code for the result of the cancelled transaction.
Type: String
Required: No

 ** Item **   <a name="DDB-Type-CancellationReason-Item"></a>
Item in the request which caused the transaction to get cancelled.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Key Length Constraints: Maximum length of 65535.
Required: No

 ** Message **   <a name="DDB-Type-CancellationReason-Message"></a>
Cancellation reason message description.
Type: String
Required: No

## See Also
<a name="API_CancellationReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/CancellationReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/CancellationReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/CancellationReason)
