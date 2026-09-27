---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_KinesisParameters.html
---

# KinesisParameters
<a name="API_KinesisParameters"></a>

Kinesis Data Streams invocation parameters for subscribers. Values are forwarded to the Kinesis PutRecords API. All scalar values accept a literal or a JSONata expression (e.g. "{% $events.Data.partitionKey %}").

## Contents
<a name="API_KinesisParameters_Contents"></a>

 ** ExplicitHashKey **   <a name="eventbridgev2-Type-KinesisParameters-ExplicitHashKey"></a>
Explicit hash key forwarded to PutRecords unchanged. Accepts JSONata expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** PartitionKey **   <a name="eventbridgev2-Type-KinesisParameters-PartitionKey"></a>
Required by PutRecords even when an explicit hash key is supplied. Accepts JSONata expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

## See Also
<a name="API_KinesisParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/KinesisParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/KinesisParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/KinesisParameters)
