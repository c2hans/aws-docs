---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_BatchConfig.html
---

# BatchConfig
<a name="API_BatchConfig"></a>

Configuration settings for batching.

## Contents
<a name="API_BatchConfig_Contents"></a>

 ** batchAcrossTopics **   <a name="iot-Type-BatchConfig-batchAcrossTopics"></a>
Whether to allow batching messages from different MQTT topics into a single HTTP request. By default, only messages from the same topic are batched together. The default value is `false`.
When `batchAcrossTopics` is enabled, the error payload format changes: the `topic` field moves from the top level to inside each entry in the `payloadsWithMetadata` array, since each message in the batch may originate from a different topic.
Messages are always batched within the scope of the same account, rule name, target HTTP endpoint URL, and billing group. Messages that differ in any of these attributes are never combined into the same batch, regardless of the `batchAcrossTopics` setting.
Type: Boolean
Required: No

 ** maxBatchOpenMs **   <a name="iot-Type-BatchConfig-maxBatchOpenMs"></a>
The maximum amount of time (in milliseconds) that an outgoing call waits for other calls with which it batches messages of the same type. The higher the setting, the longer the latency of the batched HTTP Action will be.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 200.
Required: No

 ** maxBatchSize **   <a name="iot-Type-BatchConfig-maxBatchSize"></a>
The maximum number of messages that are batched together in a single action execution.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 10.
Required: No

 ** maxBatchSizeBytes **   <a name="iot-Type-BatchConfig-maxBatchSizeBytes"></a>
Maximum size of a message batch, in bytes.
Type: Integer
Valid Range: Minimum value of 100. Maximum value of 131072.
Required: No

## See Also
<a name="API_BatchConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/BatchConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/BatchConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/BatchConfig)
