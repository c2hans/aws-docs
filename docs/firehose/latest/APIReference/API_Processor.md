---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_Processor.html
---

# Processor
<a name="API_Processor"></a>

Describes a data processor.

**Note**
If you want to add a new line delimiter between records in objects that are delivered to Amazon S3, choose `AppendDelimiterToRecord` as a processor type. You don’t have to put a processor parameter when you select `AppendDelimiterToRecord`.

## Contents
<a name="API_Processor_Contents"></a>

 ** Type **   <a name="Firehose-Type-Processor-Type"></a>
The type of processor.
Type: String
Valid Values: `RecordDeAggregation | Decompression | CloudWatchLogProcessing | Lambda | MetadataExtraction | AppendDelimiterToRecord`
Required: Yes

 ** Parameters **   <a name="Firehose-Type-Processor-Parameters"></a>
The processor parameters.
Type: Array of [ProcessorParameter](API_ProcessorParameter.md) objects
Required: No

## See Also
<a name="API_Processor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/Processor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/Processor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/Processor)
