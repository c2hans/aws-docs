---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_SplunkBufferingHints.html
---

# SplunkBufferingHints
<a name="API_SplunkBufferingHints"></a>

The buffering options. If no value is specified, the default values for Splunk are used.

## Contents
<a name="API_SplunkBufferingHints_Contents"></a>

 ** IntervalInSeconds **   <a name="Firehose-Type-SplunkBufferingHints-IntervalInSeconds"></a>
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 60 (1 minute).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 60.
Required: No

 ** SizeInMBs **   <a name="Firehose-Type-SplunkBufferingHints-SizeInMBs"></a>
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: No

## See Also
<a name="API_SplunkBufferingHints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/SplunkBufferingHints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/SplunkBufferingHints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/SplunkBufferingHints)
