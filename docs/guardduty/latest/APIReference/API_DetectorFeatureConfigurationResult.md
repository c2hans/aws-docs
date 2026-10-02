---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DetectorFeatureConfigurationResult.html
---

# DetectorFeatureConfigurationResult
<a name="API_DetectorFeatureConfigurationResult"></a>

Contains information about a GuardDuty feature.

Specifying both EKS Runtime Monitoring (`EKS_RUNTIME_MONITORING`) and Runtime Monitoring (`RUNTIME_MONITORING`) will cause an error. You can add only one of these two features because Runtime Monitoring already includes the threat detection for Amazon EKS resources. For more information, see [Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html).

## Contents
<a name="API_DetectorFeatureConfigurationResult_Contents"></a>

 ** additionalConfiguration **   <a name="guardduty-Type-DetectorFeatureConfigurationResult-additionalConfiguration"></a>
Additional configuration for a resource.
Type: Array of [DetectorAdditionalConfigurationResult](API_DetectorAdditionalConfigurationResult.md) objects
Required: No

 ** managedBy **   <a name="guardduty-Type-DetectorFeatureConfigurationResult-managedBy"></a>
Indicates what manages the feature. A value of `GUARDDUTY_POLICY` means a GuardDuty policy manages the feature.
Type: String
Valid Values: `GUARDDUTY_POLICY`
Required: No

 ** name **   <a name="guardduty-Type-DetectorFeatureConfigurationResult-name"></a>
Indicates the name of the feature that can be enabled for the detector.
Type: String
Valid Values: `FLOW_LOGS | CLOUD_TRAIL | DNS_LOGS | S3_DATA_EVENTS | EKS_AUDIT_LOGS | EBS_MALWARE_PROTECTION | RDS_LOGIN_EVENTS | LAMBDA_NETWORK_LOGS | EKS_RUNTIME_MONITORING | RUNTIME_MONITORING | AI_PROTECTION | AI_ANALYST`
Required: No

 ** status **   <a name="guardduty-Type-DetectorFeatureConfigurationResult-status"></a>
Indicates the status of the feature that is enabled for the detector.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** updatedAt **   <a name="guardduty-Type-DetectorFeatureConfigurationResult-updatedAt"></a>
The timestamp at which the feature object was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_DetectorFeatureConfigurationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DetectorFeatureConfigurationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DetectorFeatureConfigurationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DetectorFeatureConfigurationResult)
