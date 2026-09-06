---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_FailoverConfig.html
---

# FailoverConfig
<a name="API_FailoverConfig"></a>

The failover configuration for an endpoint. This includes what triggers failover and what happens when it's triggered.

## Contents
<a name="API_FailoverConfig_Contents"></a>

 ** Primary **   <a name="eventbridge-Type-FailoverConfig-Primary"></a>
The main Region of the endpoint.
Type: [Primary](API_Primary.md) object
Required: Yes

 ** Secondary **   <a name="eventbridge-Type-FailoverConfig-Secondary"></a>
The Region that events are routed to when failover is triggered or event replication is enabled.
Type: [Secondary](API_Secondary.md) object
Required: Yes

## See Also
<a name="API_FailoverConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/FailoverConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/FailoverConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/FailoverConfig)
