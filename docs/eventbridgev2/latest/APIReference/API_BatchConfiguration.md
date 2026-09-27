---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_BatchConfiguration.html
---

# BatchConfiguration
<a name="API_BatchConfiguration"></a>

Batching configuration for a subscriber.

## Contents
<a name="API_BatchConfiguration_Contents"></a>

 ** MaxBatchSize **   <a name="eventbridgev2-Type-BatchConfiguration-MaxBatchSize"></a>
The maximum number of events to include in a single batch delivered to the target. The service delivers up to this many events per batch; fewer may be delivered when the batch window elapses or the target's per-batch limit is smaller. This is a maximum, not a guaranteed count. Valid range is 1-500 (default: 10, or the target API's per-batch maximum). The resolved value applied by the service is returned on read.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** MaxBatchWindowInSeconds **   <a name="eventbridgev2-Type-BatchConfiguration-MaxBatchWindowInSeconds"></a>
The maximum time in seconds to wait for a batch to fill before delivering it to the target. This is a maximum; a batch may be delivered sooner if it reaches MaxBatchSize or another delivery condition is met. Valid range is 0-300 (default: 0, meaning no wait). The resolved value applied by the service is always returned on read.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 300.
Required: No

## See Also
<a name="API_BatchConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/BatchConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/BatchConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/BatchConfiguration)
