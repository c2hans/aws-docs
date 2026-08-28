---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_OrganizationAdditionalConfigurationResult.html
---

# OrganizationAdditionalConfigurationResult
<a name="API_OrganizationAdditionalConfigurationResult"></a>

A list of additional configuration which will be configured for the organization.

## Contents
<a name="API_OrganizationAdditionalConfigurationResult_Contents"></a>

 ** autoEnable **   <a name="guardduty-Type-OrganizationAdditionalConfigurationResult-autoEnable"></a>
Describes the status of the additional configuration that is configured for the member accounts within the organization. One of the following values is the status for the entire organization:
+  `NEW`: Indicates that when a new account joins the organization, they will have the additional configuration enabled automatically.
+  `ALL`: Indicates that all accounts in the organization have the additional configuration enabled automatically. This includes `NEW` accounts that join the organization and accounts that may have been suspended or removed from the organization in GuardDuty.

  It may take up to 24 hours to update the configuration for all the member accounts.
+  `NONE`: Indicates that the additional configuration will not be automatically enabled for any account in the organization. The administrator must manage the additional configuration for each account individually.
Type: String
Valid Values: `NEW | NONE | ALL`
Required: No

 ** name **   <a name="guardduty-Type-OrganizationAdditionalConfigurationResult-name"></a>
The name of the additional configuration that is configured for the member accounts within the organization. These values are applicable to only Runtime Monitoring protection plan.
Type: String
Valid Values: `EKS_ADDON_MANAGEMENT | ECS_FARGATE_AGENT_MANAGEMENT | EC2_AGENT_MANAGEMENT`
Required: No

## See Also
<a name="API_OrganizationAdditionalConfigurationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/OrganizationAdditionalConfigurationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/OrganizationAdditionalConfigurationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/OrganizationAdditionalConfigurationResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
