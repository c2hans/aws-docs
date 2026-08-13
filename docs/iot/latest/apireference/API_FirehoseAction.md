---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_FirehoseAction.html
---

# FirehoseAction
<a name="API_FirehoseAction"></a>

Describes an action that writes data to an Amazon Kinesis Firehose stream.

## Contents
<a name="API_FirehoseAction_Contents"></a>

 ** deliveryStreamName **   <a name="iot-Type-FirehoseAction-deliveryStreamName"></a>
The delivery stream name.
Type: String
Required: Yes

 ** roleArn **   <a name="iot-Type-FirehoseAction-roleArn"></a>
The IAM role that grants access to the Amazon Kinesis Firehose stream.
Type: String
Required: Yes

 ** batchMode **   <a name="iot-Type-FirehoseAction-batchMode"></a>
Whether to deliver the Kinesis Data Firehose stream as a batch by using [`PutRecordBatch`](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch.html). The default value is `false`.
When `batchMode` is `true` and the rule's SQL statement evaluates to an Array, each Array element forms one record in the [`PutRecordBatch`](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch.html) request. The resulting array can't have more than 500 records.
Type: Boolean
Required: No

 ** separator **   <a name="iot-Type-FirehoseAction-separator"></a>
A character separator that will be used to separate records written to the Firehose stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).
Type: String
Pattern: `([\n\t])|(\r\n)|(,)`
Required: No

## See Also
<a name="API_FirehoseAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/FirehoseAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/FirehoseAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/FirehoseAction)
