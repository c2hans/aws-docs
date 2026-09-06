---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_ProcessorParameter.html
---

# ProcessorParameter
<a name="API_ProcessorParameter"></a>

Describes the processor parameter.

## Contents
<a name="API_ProcessorParameter_Contents"></a>

 ** ParameterName **   <a name="Firehose-Type-ProcessorParameter-ParameterName"></a>
The name of the parameter. Currently the following default values are supported: 3 for `NumberOfRetries` and 60 for the `BufferIntervalInSeconds`. The `BufferSizeInMBs` ranges between 0.2 MB and up to 3MB. The default buffering hint is 1MB for all destinations, except Splunk. For Splunk, the default buffering hint is 256 KB.
Type: String
Valid Values: `LambdaArn | NumberOfRetries | MetadataExtractionQuery | JsonParsingEngine | RoleArn | BufferSizeInMBs | BufferIntervalInSeconds | SubRecordType | Delimiter | CompressionFormat | DataMessageExtraction`
Required: Yes

 ** ParameterValue **   <a name="Firehose-Type-ProcessorParameter-ParameterValue"></a>
The parameter value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5120.
Pattern: `^(?!\s*$).+`
Required: Yes

## See Also
<a name="API_ProcessorParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/ProcessorParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/ProcessorParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/ProcessorParameter)
