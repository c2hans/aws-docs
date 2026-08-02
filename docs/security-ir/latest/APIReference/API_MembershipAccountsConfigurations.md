---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_MembershipAccountsConfigurations.html
---

# MembershipAccountsConfigurations
<a name="API_MembershipAccountsConfigurations"></a>

The `MembershipAccountsConfigurations` structure defines the configuration settings for managing membership accounts withinAWS.

This structure contains settings that determine how member accounts are configured and managed within your organization, including:
+ Account configuration preferences
+ Membership validation rules
+ Account access settings

You can use this structure to define and maintain standardized configurations across multiple member accounts in your organization.

## Contents
<a name="API_MembershipAccountsConfigurations_Contents"></a>

 ** coverEntireOrganization **   <a name="securityir-Type-MembershipAccountsConfigurations-coverEntireOrganization"></a>
The `coverEntireOrganization` field is a boolean value that determines whether the membership configuration applies to all accounts within an AWS Organization.
When set to `true`, the configuration will be applied across all accounts in the organization. When set to `false`, the configuration will only apply to specifically designated accounts under the AWS Organizational Units specificied.
Type: Boolean
Required: No

 ** organizationalUnits **   <a name="securityir-Type-MembershipAccountsConfigurations-organizationalUnits"></a>
A list of organizational unit IDs that follow the pattern `ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}`. These IDs represent the organizational units within an AWS Organizations structure that are covered by the membership.
Each organizational unit ID in the list must:
+ Begin with the prefix 'ou-'
+ Contain between 4 and 32 alphanumeric characters in the first segment
+ Contain between 8 and 32 alphanumeric characters in the second segment
Type: Array of strings
Pattern: `ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}`
Required: No

## See Also
<a name="API_MembershipAccountsConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/MembershipAccountsConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/MembershipAccountsConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/MembershipAccountsConfigurations)
