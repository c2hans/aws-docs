---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DetectorFeatureConfiguration.html
---

# DetectorFeatureConfiguration
<a name="API_DetectorFeatureConfiguration"></a>

Contains information about a GuardDuty feature.

Specifying both EKS Runtime Monitoring (`EKS_RUNTIME_MONITORING`) and Runtime Monitoring (`RUNTIME_MONITORING`) will cause an error. You can add only one of these two features because Runtime Monitoring already includes the threat detection for Amazon EKS resources. For more information, see [Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html).

## Contents
<a name="API_DetectorFeatureConfiguration_Contents"></a>

 ** additionalConfiguration **   <a name="guardduty-Type-DetectorFeatureConfiguration-additionalConfiguration"></a>
Additional configuration for a resource.
Type: Array of [DetectorAdditionalConfiguration](API_DetectorAdditionalConfiguration.md) objects
Required: No

 ** name **   <a name="guardduty-Type-DetectorFeatureConfiguration-name"></a>
The name of the feature.
Type: String
Valid Values: `S3_DATA_EVENTS | EKS_AUDIT_LOGS | EBS_MALWARE_PROTECTION | RDS_LOGIN_EVENTS | LAMBDA_NETWORK_LOGS | EKS_RUNTIME_MONITORING | RUNTIME_MONITORING | AI_PROTECTION | AI_ANALYST`
Required: No

 ** status **   <a name="guardduty-Type-DetectorFeatureConfiguration-status"></a>
The status of the feature.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_DetectorFeatureConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DetectorFeatureConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DetectorFeatureConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DetectorFeatureConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
