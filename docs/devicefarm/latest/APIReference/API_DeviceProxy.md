---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeviceProxy.html
---

# DeviceProxy
<a name="API_DeviceProxy"></a>

Represents the http/s proxy configuration that will be applied to a device during a run.

## Contents
<a name="API_DeviceProxy_Contents"></a>

 ** host **   <a name="devicefarm-Type-DeviceProxy-host"></a>
Hostname or IPv4 address of the proxy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^([a-zA-Z0-9])([a-zA-Z0-9-.]+)([a-zA-Z0-9])$`
Required: Yes

 ** port **   <a name="devicefarm-Type-DeviceProxy-port"></a>
The port number on which the http/s proxy is listening.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: Yes

## See Also
<a name="API_DeviceProxy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/DeviceProxy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/DeviceProxy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/DeviceProxy)
