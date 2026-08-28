---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ActiveDirectoryIdentityProvider.html
---

# ActiveDirectoryIdentityProvider
<a name="API_ActiveDirectoryIdentityProvider"></a>

Details about an Active Directory identity provider.

## Contents
<a name="API_ActiveDirectoryIdentityProvider_Contents"></a>

 ** ActiveDirectorySettings **   <a name="licensemanagerusersubscriptions-Type-ActiveDirectoryIdentityProvider-ActiveDirectorySettings"></a>
The `ActiveDirectorySettings` resource contains details about the Active Directory, including network access details such as domain name and IP addresses, and the credential provider for user administration.
Type: [ActiveDirectorySettings](API_ActiveDirectorySettings.md) object
Required: No

 ** ActiveDirectoryType **   <a name="licensemanagerusersubscriptions-Type-ActiveDirectoryIdentityProvider-ActiveDirectoryType"></a>
The type of Active Directory – either a self-managed Active Directory or an AWS Managed Active Directory.
Type: String
Valid Values: `SELF_MANAGED | AWS_MANAGED`
Required: No

 ** DirectoryId **   <a name="licensemanagerusersubscriptions-Type-ActiveDirectoryIdentityProvider-DirectoryId"></a>
The directory ID for an Active Directory identity provider.
Type: String
Pattern: `(d|sd)-[0-9a-f]{10}`
Required: No

 ** IsSharedActiveDirectory **   <a name="licensemanagerusersubscriptions-Type-ActiveDirectoryIdentityProvider-IsSharedActiveDirectory"></a>
Whether this directory is shared from an AWS Managed Active Directory. The default value is false.
Type: Boolean
Required: No

## See Also
<a name="API_ActiveDirectoryIdentityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/ActiveDirectoryIdentityProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/ActiveDirectoryIdentityProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/ActiveDirectoryIdentityProvider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager User Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-user-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
