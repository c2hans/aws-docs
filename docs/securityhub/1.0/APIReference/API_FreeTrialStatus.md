---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_FreeTrialStatus.html
---

# FreeTrialStatus
<a name="API_FreeTrialStatus"></a>

The free trial period for a Security Hub feature, and whether the trial is currently active.

## Contents
<a name="API_FreeTrialStatus_Contents"></a>

 ** ExpiresAt **   <a name="securityhub-Type-FreeTrialStatus-ExpiresAt"></a>
The date and time at which the free trial period ends.
Type: Timestamp
Required: Yes

 ** FeatureType **   <a name="securityhub-Type-FreeTrialStatus-FeatureType"></a>
The feature that the free trial period applies to. Valid values:
+  `SECURITY_HUB_V2` specifies Security Hub.
+  `SECURITY_HUB_V2_MULTI_CLOUD_AZURE` specifies Security Hub coverage for Microsoft Azure resources.
Type: String
Valid Values: `SECURITY_HUB_V2 | SECURITY_HUB_V2_MULTI_CLOUD_AZURE`
Required: Yes

 ** StartedAt **   <a name="securityhub-Type-FreeTrialStatus-StartedAt"></a>
The date and time at which the free trial period began.
Type: Timestamp
Required: Yes

 ** Status **   <a name="securityhub-Type-FreeTrialStatus-Status"></a>
Specifies whether the free trial period is currently active. Valid values:
+  `ACTIVE` specifies that the free trial period is ongoing.
+  `INACTIVE` specifies that the free trial period has ended, or that it never started.
To determine whether a trial has expired, compare `ExpiresAt` to the current time.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

## See Also
<a name="API_FreeTrialStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/FreeTrialStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/FreeTrialStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/FreeTrialStatus)
