---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_BatchResultErrorEntry.html
---

# BatchResultErrorEntry
<a name="API_BatchResultErrorEntry"></a>

Gives a detailed description of the result of an action on each entry in the request.

## Contents
<a name="API_BatchResultErrorEntry_Contents"></a>

 ** Code **   <a name="SQS-Type-BatchResultErrorEntry-Code"></a>
An error code representing why the action failed on this entry.
Type: String
Required: Yes

 ** Id **   <a name="SQS-Type-BatchResultErrorEntry-Id"></a>
The `Id` of an entry in a batch request.
Type: String
Required: Yes

 ** SenderFault **   <a name="SQS-Type-BatchResultErrorEntry-SenderFault"></a>
Specifies whether the error happened due to the caller of the batch API action.
Type: Boolean
Required: Yes

 ** Message **   <a name="SQS-Type-BatchResultErrorEntry-Message"></a>
A message explaining why the action failed on this entry.
Type: String
Required: No

## See Also
<a name="API_BatchResultErrorEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/BatchResultErrorEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/BatchResultErrorEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/BatchResultErrorEntry)
