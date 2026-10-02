---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DetectorAdditionalConfigurationResult.html
---

# DetectorAdditionalConfigurationResult
<a name="API_DetectorAdditionalConfigurationResult"></a>

Information about the additional configuration.

## Contents
<a name="API_DetectorAdditionalConfigurationResult_Contents"></a>

 ** managedBy **   <a name="guardduty-Type-DetectorAdditionalConfigurationResult-managedBy"></a>
Indicates what manages the additional configuration. A value of `GUARDDUTY_POLICY` means a GuardDuty policy manages the additional configuration.
Type: String
Valid Values: `GUARDDUTY_POLICY`
Required: No

 ** name **   <a name="guardduty-Type-DetectorAdditionalConfigurationResult-name"></a>
Name of the additional configuration.
Type: String
Valid Values: `EKS_ADDON_MANAGEMENT | ECS_FARGATE_AGENT_MANAGEMENT | EC2_AGENT_MANAGEMENT`
Required: No

 ** status **   <a name="guardduty-Type-DetectorAdditionalConfigurationResult-status"></a>
Status of the additional configuration.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** updatedAt **   <a name="guardduty-Type-DetectorAdditionalConfigurationResult-updatedAt"></a>
The timestamp at which the additional configuration was last updated. This is in UTC format.
Type: Timestamp
Required: No

## See Also
<a name="API_DetectorAdditionalConfigurationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DetectorAdditionalConfigurationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DetectorAdditionalConfigurationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DetectorAdditionalConfigurationResult)
