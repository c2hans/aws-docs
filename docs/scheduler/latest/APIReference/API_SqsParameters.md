---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_SqsParameters.html
---

# SqsParameters
<a name="API_SqsParameters"></a>

The templated target type for the Amazon SQS [https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html) API operation. Contains the message group ID to use when the target is a FIFO queue. If you specify an Amazon SQS FIFO queue as a target, the queue must have content-based deduplication enabled. For more information, see [Using the Amazon SQS message deduplication ID](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html) in the *Amazon SQS Developer Guide*.

## Contents
<a name="API_SqsParameters_Contents"></a>

 ** MessageGroupId **   <a name="scheduler-Type-SqsParameters-MessageGroupId"></a>
The FIFO message group ID to use as the target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_SqsParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/SqsParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/SqsParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/SqsParameters)
