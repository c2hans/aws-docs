---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_AmazonOpenSearchServerlessRetryOptions.html
---

# AmazonOpenSearchServerlessRetryOptions
<a name="API_AmazonOpenSearchServerlessRetryOptions"></a>

Configures retry behavior in case Firehose is unable to deliver documents to the Serverless offering for Amazon OpenSearch Service.

## Contents
<a name="API_AmazonOpenSearchServerlessRetryOptions_Contents"></a>

 ** DurationInSeconds **   <a name="Firehose-Type-AmazonOpenSearchServerlessRetryOptions-DurationInSeconds"></a>
After an initial failure to deliver to the Serverless offering for Amazon OpenSearch Service, the total amount of time during which Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 7200.
Required: No

## See Also
<a name="API_AmazonOpenSearchServerlessRetryOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/AmazonOpenSearchServerlessRetryOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/AmazonOpenSearchServerlessRetryOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/AmazonOpenSearchServerlessRetryOptions)
