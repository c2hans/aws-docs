---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_OrganizationStatus.html
---

# OrganizationStatus
<a name="API_OrganizationStatus"></a>

The status of an Amazon Web Services Organization and the accounts within that organization.

## Contents
<a name="API_OrganizationStatus_Contents"></a>

 ** AccountStatusList **   <a name="networkmanager-Type-OrganizationStatus-AccountStatusList"></a>
The current service-linked role (SLR) deployment status for an Amazon Web Services Organization's accounts. This will be either `SUCCEEDED` or `IN_PROGRESS`.
Type: Array of [AccountStatus](API_AccountStatus.md) objects
Required: No

 ** OrganizationAwsServiceAccessStatus **   <a name="networkmanager-Type-OrganizationStatus-OrganizationAwsServiceAccessStatus"></a>
The status of the organization's AWS service access. This will be `ENABLED` or `DISABLED`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: No

 ** OrganizationId **   <a name="networkmanager-Type-OrganizationStatus-OrganizationId"></a>
The ID of an Amazon Web Services Organization.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^o-([0-9a-f]{8,17})$`
Required: No

 ** SLRDeploymentStatus **   <a name="networkmanager-Type-OrganizationStatus-SLRDeploymentStatus"></a>
The status of the SLR deployment for the account. This will be either `SUCCEEDED` or `IN_PROGRESS`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: No

## See Also
<a name="API_OrganizationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/OrganizationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/OrganizationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/OrganizationStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
