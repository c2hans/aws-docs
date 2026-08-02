---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PortalStatus.html
---

# PortalStatus
<a name="API_PortalStatus"></a>

Contains information about the current status of a portal.

## Contents
<a name="API_PortalStatus_Contents"></a>

 ** state **   <a name="iotsitewise-Type-PortalStatus-state"></a>
The current state of the portal.
Type: String
Valid Values: `CREATING | PENDING | UPDATING | DELETING | ACTIVE | FAILED`
Required: Yes

 ** error **   <a name="iotsitewise-Type-PortalStatus-error"></a>
Contains associated error information, if any.
Type: [MonitorErrorDetails](API_MonitorErrorDetails.md) object
Required: No

## See Also
<a name="API_PortalStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/PortalStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/PortalStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/PortalStatus)
