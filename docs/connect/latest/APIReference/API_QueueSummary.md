---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_QueueSummary.html
---

# QueueSummary
<a name="API_QueueSummary"></a>

Contains summary information about a queue.

## Contents
<a name="API_QueueSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-QueueSummary-Arn"></a>
The Amazon Resource Name (ARN) of the queue.
Type: String
Required: No

 ** Id **   <a name="connect-Type-QueueSummary-Id"></a>
The identifier of the queue.
Type: String
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-QueueSummary-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-QueueSummary-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-QueueSummary-Name"></a>
The name of the queue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** QueueType **   <a name="connect-Type-QueueSummary-QueueType"></a>
The type of queue.
Type: String
Valid Values: `STANDARD | AGENT`
Required: No

## See Also
<a name="API_QueueSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/QueueSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/QueueSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/QueueSummary)
