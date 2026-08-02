---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_DriftStatusSummary.html
---

# DriftStatusSummary
<a name="API_DriftStatusSummary"></a>

The drift summary of the enabled control.

 AWS Control Tower expects the enabled control configuration to include all supported and governed Regions. If the enabled control differs from the expected configuration, it is defined to be in a state of drift. You can repair this drift by resetting the enabled control.

## Contents
<a name="API_DriftStatusSummary_Contents"></a>

 ** driftStatus **   <a name="controltower-Type-DriftStatusSummary-driftStatus"></a>
 The drift status of the enabled control.
Valid values:
+  `DRIFTED`: The `enabledControl` deployed in this configuration doesn’t match the configuration that AWS Control Tower expected.
+  `IN_SYNC`: The `enabledControl` deployed in this configuration matches the configuration that AWS Control Tower expected.
+  `NOT_CHECKING`: AWS Control Tower does not check drift for this enabled control. Drift is not supported for the control type.
+  `UNKNOWN`: AWS Control Tower is not able to check the drift status for the enabled control.
Type: String
Valid Values: `DRIFTED | IN_SYNC | NOT_CHECKING | UNKNOWN`
Required: No

 ** types **   <a name="controltower-Type-DriftStatusSummary-types"></a>
An object that categorizes the different types of drift detected for the enabled control.
Type: [EnabledControlDriftTypes](API_EnabledControlDriftTypes.md) object
Required: No

## See Also
<a name="API_DriftStatusSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/DriftStatusSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/DriftStatusSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/DriftStatusSummary)
