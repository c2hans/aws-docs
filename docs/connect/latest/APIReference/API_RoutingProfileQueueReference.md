---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfileQueueReference.html
---

# RoutingProfileQueueReference
<a name="API_RoutingProfileQueueReference"></a>

Contains the channel and queue identifier for a routing profile.

## Contents
<a name="API_RoutingProfileQueueReference_Contents"></a>

 ** Channel **   <a name="connect-Type-RoutingProfileQueueReference-Channel"></a>
The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.
Type: String
Valid Values: `VOICE | CHAT | TASK | EMAIL`
Required: Yes

 ** QueueId **   <a name="connect-Type-RoutingProfileQueueReference-QueueId"></a>
The identifier for the queue.
Type: String
Required: Yes

## See Also
<a name="API_RoutingProfileQueueReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RoutingProfileQueueReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RoutingProfileQueueReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RoutingProfileQueueReference)
