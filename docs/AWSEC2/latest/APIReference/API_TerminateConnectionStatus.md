---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateConnectionStatus.html
---

# TerminateConnectionStatus
<a name="API_TerminateConnectionStatus"></a>

Information about a terminated Client VPN endpoint client connection.

## Contents
<a name="API_TerminateConnectionStatus_Contents"></a>

 ** connectionId **
The ID of the client connection.
Type: String
Required: No

 ** currentStatus **
A message about the status of the client connection, if applicable.
Type: [ClientVpnConnectionStatus](API_ClientVpnConnectionStatus.md) object
Required: No

 ** previousStatus **
The state of the client connection.
Type: [ClientVpnConnectionStatus](API_ClientVpnConnectionStatus.md) object
Required: No

## See Also
<a name="API_TerminateConnectionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TerminateConnectionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TerminateConnectionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TerminateConnectionStatus)
