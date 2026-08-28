---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DetectorAdditionalConfigurationResult.html
---

# DetectorAdditionalConfigurationResult
<a name="API_DetectorAdditionalConfigurationResult"></a>

Information about the additional configuration.

## Contents
<a name="API_DetectorAdditionalConfigurationResult_Contents"></a>

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
