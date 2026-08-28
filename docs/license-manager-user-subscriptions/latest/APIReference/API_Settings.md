---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_Settings.html
---

# Settings
<a name="API_Settings"></a>

The registered identity provider’s product related configuration settings such as the subnets to provision VPC endpoints, and the security group ID that is associated with the VPC endpoints. The security group should permit inbound TCP port 1688 communication from resources in the VPC.

## Contents
<a name="API_Settings_Contents"></a>

 ** SecurityGroupId **   <a name="licensemanagerusersubscriptions-Type-Settings-SecurityGroupId"></a>
A security group ID that allows inbound TCP port 1688 communication between resources in your VPC and the VPC endpoint for activation servers.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
Required: Yes

 ** Subnets **   <a name="licensemanagerusersubscriptions-Type-Settings-Subnets"></a>
The subnets defined for the registered identity provider.
Type: Array of strings
Array Members: Minimum number of 1 item.
Pattern: `subnet-[a-z0-9]{8,17}.*`
Required: Yes

## See Also
<a name="API_Settings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/Settings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/Settings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/Settings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager User Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-user-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
