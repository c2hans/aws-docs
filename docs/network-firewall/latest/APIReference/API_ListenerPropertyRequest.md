---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ListenerPropertyRequest.html
---

# ListenerPropertyRequest
<a name="API_ListenerPropertyRequest"></a>

This data type is used specifically for the [CreateProxy](API_CreateProxy.md) and [UpdateProxy](API_UpdateProxy.md) APIs.

Open port for taking HTTP or HTTPS traffic.

## Contents
<a name="API_ListenerPropertyRequest_Contents"></a>

 ** Port **   <a name="networkfirewall-Type-ListenerPropertyRequest-Port"></a>
Port for processing traffic.
Type: Integer
Required: Yes

 ** Type **   <a name="networkfirewall-Type-ListenerPropertyRequest-Type"></a>
Selection of HTTP or HTTPS traffic.
Type: String
Valid Values: `HTTP | HTTPS`
Required: Yes

## See Also
<a name="API_ListenerPropertyRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ListenerPropertyRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ListenerPropertyRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ListenerPropertyRequest)
