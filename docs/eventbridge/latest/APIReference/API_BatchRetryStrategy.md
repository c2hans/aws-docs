---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_BatchRetryStrategy.html
---

# BatchRetryStrategy
<a name="API_BatchRetryStrategy"></a>

The retry strategy to use for failed jobs, if the target is an AWS Batch job. If you specify a retry strategy here, it overrides the retry strategy defined in the job definition.

## Contents
<a name="API_BatchRetryStrategy_Contents"></a>

 ** Attempts **   <a name="eventbridge-Type-BatchRetryStrategy-Attempts"></a>
The number of times to attempt to retry, if the job fails. Valid values are 1–10.
Type: Integer
Required: No

## See Also
<a name="API_BatchRetryStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/BatchRetryStrategy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/BatchRetryStrategy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/BatchRetryStrategy)
