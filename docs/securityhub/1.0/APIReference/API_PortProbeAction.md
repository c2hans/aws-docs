---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_PortProbeAction.html
---

# PortProbeAction
<a name="API_PortProbeAction"></a>

Provided if `ActionType` is `PORT_PROBE`. It provides details about the attempted port probe that was detected.

## Contents
<a name="API_PortProbeAction_Contents"></a>

 ** Blocked **   <a name="securityhub-Type-PortProbeAction-Blocked"></a>
Indicates whether the port probe was blocked.
Type: Boolean
Required: No

 ** PortProbeDetails **   <a name="securityhub-Type-PortProbeAction-PortProbeDetails"></a>
Information about the ports affected by the port probe.
Type: Array of [PortProbeDetail](API_PortProbeDetail.md) objects
Required: No

## See Also
<a name="API_PortProbeAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/PortProbeAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/PortProbeAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/PortProbeAction)
