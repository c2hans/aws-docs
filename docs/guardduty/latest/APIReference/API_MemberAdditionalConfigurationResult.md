---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_MemberAdditionalConfigurationResult.html
---

# MemberAdditionalConfigurationResult
<a name="API_MemberAdditionalConfigurationResult"></a>

Information about the additional configuration for the member account.

## Contents
<a name="API_MemberAdditionalConfigurationResult_Contents"></a>

 ** name **   <a name="guardduty-Type-MemberAdditionalConfigurationResult-name"></a>
Indicates the name of the additional configuration that is set for the member account.
Type: String
Valid Values: `EKS_ADDON_MANAGEMENT | ECS_FARGATE_AGENT_MANAGEMENT | EC2_AGENT_MANAGEMENT`
Required: No

 ** status **   <a name="guardduty-Type-MemberAdditionalConfigurationResult-status"></a>
Indicates the status of the additional configuration that is set for the member account.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** updatedAt **   <a name="guardduty-Type-MemberAdditionalConfigurationResult-updatedAt"></a>
The timestamp at which the additional configuration was set for the member account. This is in UTC format.
Type: Timestamp
Required: No

## See Also
<a name="API_MemberAdditionalConfigurationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/MemberAdditionalConfigurationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/MemberAdditionalConfigurationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/MemberAdditionalConfigurationResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
