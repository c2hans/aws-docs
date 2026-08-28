---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_UpdateSettings.html
---

# UpdateSettings
<a name="API_UpdateSettings"></a>

Updates the registered identity provider’s product related configuration settings such as the subnets to provision VPC endpoints.

## Contents
<a name="API_UpdateSettings_Contents"></a>

 ** AddSubnets **   <a name="licensemanagerusersubscriptions-Type-UpdateSettings-AddSubnets"></a>
The ID of one or more subnets in which License Manager will create a VPC endpoint for products that require connectivity to activation servers.
Type: Array of strings
Pattern: `subnet-[a-z0-9]{8,17}.*`
Required: Yes

 ** RemoveSubnets **   <a name="licensemanagerusersubscriptions-Type-UpdateSettings-RemoveSubnets"></a>
The ID of one or more subnets to remove.
Type: Array of strings
Pattern: `subnet-[a-z0-9]{8,17}.*`
Required: Yes

 ** SecurityGroupId **   <a name="licensemanagerusersubscriptions-Type-UpdateSettings-SecurityGroupId"></a>
A security group ID that allows inbound TCP port 1688 communication between resources in your VPC and the VPC endpoints for activation servers.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
Required: No

## See Also
<a name="API_UpdateSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/UpdateSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/UpdateSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/UpdateSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager User Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-user-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
