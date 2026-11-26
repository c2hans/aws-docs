---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_ProxyStatus.html
---

# ProxyStatus

The status of a proxy.

## Contents
<a name="API_ProxyStatus_Contents"></a>

 ** code **   <a name="elasticloadbalancing-Type-ProxyStatus-code"></a>
The status code of the proxy.
Type: String
Valid Values: `action-required | active | create-failed | create-in-progress | deleted | delete-in-progress | update-in-progress | cancel-update-in-progress`
Required: Yes

 ** reasons **   <a name="elasticloadbalancing-Type-ProxyStatus-reasons"></a>
The reasons for the current status of the proxy.
Type: Array of [ProxyStatusReason](API_ProxyStatusReason.md) objects
Required: Yes

## See Also
<a name="API_ProxyStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elb-proxy-2026-11-20/ProxyStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elb-proxy-2026-11-20/ProxyStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elb-proxy-2026-11-20/ProxyStatus)
