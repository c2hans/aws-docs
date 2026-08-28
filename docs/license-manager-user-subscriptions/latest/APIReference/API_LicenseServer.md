---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_LicenseServer.html
---

# LicenseServer
<a name="API_LicenseServer"></a>

Information about a Remote Desktop Services (RDS) license server.

## Contents
<a name="API_LicenseServer_Contents"></a>

 ** HealthStatus **   <a name="licensemanagerusersubscriptions-Type-LicenseServer-HealthStatus"></a>
The health status of the RDS license server.
Type: String
Valid Values: `HEALTHY | UNHEALTHY | NOT_APPLICABLE`
Required: No

 ** Ipv4Address **   <a name="licensemanagerusersubscriptions-Type-LicenseServer-Ipv4Address"></a>
A list of domain IPv4 addresses that are used for the RDS license server.
Type: String
Required: No

 ** Ipv6Address **   <a name="licensemanagerusersubscriptions-Type-LicenseServer-Ipv6Address"></a>
A list of domain IPv6 addresses that are used for the RDS license server.
Type: String
Required: No

 ** ProvisioningStatus **   <a name="licensemanagerusersubscriptions-Type-LicenseServer-ProvisioningStatus"></a>
The current state of the provisioning process for the RDS license server.
Type: String
Valid Values: `PROVISIONING | PROVISIONING_FAILED | PROVISIONED | DELETING | DELETION_FAILED | DELETED`
Required: No

## See Also
<a name="API_LicenseServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/LicenseServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/LicenseServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/LicenseServer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager User Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-user-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
