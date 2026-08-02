---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_DirectPutSourceDescription.html
---

# DirectPutSourceDescription
<a name="API_DirectPutSourceDescription"></a>

The structure that configures parameters such as `ThroughputHintInMBs` for a stream configured with Direct PUT as a source.

## Contents
<a name="API_DirectPutSourceDescription_Contents"></a>

 ** ThroughputHintInMBs **   <a name="Firehose-Type-DirectPutSourceDescription-ThroughputHintInMBs"></a>
 The value that you configure for this parameter is for information purpose only and does not affect Firehose delivery throughput limit. You can use the [Firehose Limits form](https://support.console.aws.amazon.com/support/home#/case/create%3FissueType=service-limit-increase%26limitType=kinesis-firehose-limits) to request a throughput limit increase.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

## See Also
<a name="API_DirectPutSourceDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/DirectPutSourceDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/DirectPutSourceDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/DirectPutSourceDescription)
