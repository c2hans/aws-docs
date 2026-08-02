---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_PortProbeAction.html
---

# PortProbeAction
<a name="API_PortProbeAction"></a>

Contains information about the PORT\_PROBE action described in the finding.

## Contents
<a name="API_PortProbeAction_Contents"></a>

 ** blocked **   <a name="guardduty-Type-PortProbeAction-blocked"></a>
Indicates whether EC2 blocked the port probe to the instance, such as with an ACL.
Type: Boolean
Required: No

 ** portProbeDetails **   <a name="guardduty-Type-PortProbeAction-portProbeDetails"></a>
A list of objects related to port probe details.
Type: Array of [PortProbeDetail](API_PortProbeDetail.md) objects
Required: No

## See Also
<a name="API_PortProbeAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/PortProbeAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/PortProbeAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/PortProbeAction)
