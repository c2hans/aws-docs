---
source_url: https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_SMBLocalGroups.html
---

# SMBLocalGroups
<a name="API_SMBLocalGroups"></a>

A list of Active Directory users and groups that have special permissions for SMB file shares on the gateway.

## Contents
<a name="API_SMBLocalGroups_Contents"></a>

 ** GatewayAdmins **   <a name="StorageGateway-Type-SMBLocalGroups-GatewayAdmins"></a>
A list of Active Directory users and groups that have local Gateway Admin permissions. Acceptable formats include: `DOMAIN\User1`, `user1`, `DOMAIN\group1`, and `group1`.
Gateway Admins can use the Shared Folders Microsoft Management Console snap-in to force-close files that are open and locked.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_SMBLocalGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/SMBLocalGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/SMBLocalGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/SMBLocalGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query storagegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
