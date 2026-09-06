---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_NetworkStatus.html
---

# NetworkStatus
<a name="API_NetworkStatus"></a>

The network status of a device.

## Contents
<a name="API_NetworkStatus_Contents"></a>

 ** Ethernet0Status **   <a name="panorama-Type-NetworkStatus-Ethernet0Status"></a>
The status of Ethernet port 0.
Type: [EthernetStatus](API_EthernetStatus.md) object
Required: No

 ** Ethernet1Status **   <a name="panorama-Type-NetworkStatus-Ethernet1Status"></a>
The status of Ethernet port 1.
Type: [EthernetStatus](API_EthernetStatus.md) object
Required: No

 ** LastUpdatedTime **   <a name="panorama-Type-NetworkStatus-LastUpdatedTime"></a>
When the network status changed.
Type: Timestamp
Required: No

 ** NtpStatus **   <a name="panorama-Type-NetworkStatus-NtpStatus"></a>
Details about a network time protocol (NTP) server connection.
Type: [NtpStatus](API_NtpStatus.md) object
Required: No

## See Also
<a name="API_NetworkStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/NetworkStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/NetworkStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/NetworkStatus)
