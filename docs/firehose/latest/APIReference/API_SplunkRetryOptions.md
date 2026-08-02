---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_SplunkRetryOptions.html
---

# SplunkRetryOptions
<a name="API_SplunkRetryOptions"></a>

Configures retry behavior in case Firehose is unable to deliver documents to Splunk, or if it doesn't receive an acknowledgment from Splunk.

## Contents
<a name="API_SplunkRetryOptions_Contents"></a>

 ** DurationInSeconds **   <a name="Firehose-Type-SplunkRetryOptions-DurationInSeconds"></a>
The total amount of time that Firehose spends on retries. This duration starts after the initial attempt to send data to Splunk fails. It doesn't include the periods during which Firehose waits for acknowledgment from Splunk after each attempt.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 7200.
Required: No

## See Also
<a name="API_SplunkRetryOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/SplunkRetryOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/SplunkRetryOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/SplunkRetryOptions)
