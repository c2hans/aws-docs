---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_MembershipAccountsConfigurationsUpdate.html
---

# MembershipAccountsConfigurationsUpdate
<a name="API_MembershipAccountsConfigurationsUpdate"></a>

The `MembershipAccountsConfigurationsUpdate`structure represents the configuration updates for member accounts within an AWS organization.

This structure is used to modify existing account configurations and settings for members in the organization. When applying updates, ensure all required fields are properly specified to maintain account consistency.

Key considerations when using this structure:
+ All configuration changes are validated before being applied
+ Updates are processed asynchronously in the background
+ Configuration changes may take several minutes to propagate across all affected accounts

## Contents
<a name="API_MembershipAccountsConfigurationsUpdate_Contents"></a>

 ** coverEntireOrganization **   <a name="securityir-Type-MembershipAccountsConfigurationsUpdate-coverEntireOrganization"></a>
The `coverEntireOrganization` field is a boolean value that determines whether the membership configuration should be applied across the entire AWS Organization.
When set to `true`, the configuration will be applied to all accounts within the organization. When set to `false`, the configuration will only apply to specifically designated accounts.
Type: Boolean
Required: No

 ** organizationalUnitsToAdd **   <a name="securityir-Type-MembershipAccountsConfigurationsUpdate-organizationalUnitsToAdd"></a>
A list of organizational unit IDs to add to the membership configuration. Each organizational unit ID must match the pattern `ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}`.
The list must contain between 1 and 5 organizational unit IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Pattern: `ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}`
Required: No

 ** organizationalUnitsToRemove **   <a name="securityir-Type-MembershipAccountsConfigurationsUpdate-organizationalUnitsToRemove"></a>
A list of organizational unit IDs to remove from the membership configuration. Each organizational unit ID must match the pattern `ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}`.
The list must contain between 1 and 5 organizational unit IDs per invocation of the API request.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Pattern: `ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}`
Required: No

## See Also
<a name="API_MembershipAccountsConfigurationsUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/MembershipAccountsConfigurationsUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/MembershipAccountsConfigurationsUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/MembershipAccountsConfigurationsUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
