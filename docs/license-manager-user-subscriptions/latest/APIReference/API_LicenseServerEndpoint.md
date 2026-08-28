---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_LicenseServerEndpoint.html
---

# LicenseServerEndpoint
<a name="API_LicenseServerEndpoint"></a>

Contains details about a network endpoint for a Remote Desktop Services (RDS) license server.

## Contents
<a name="API_LicenseServerEndpoint_Contents"></a>

 ** CreationTime **   <a name="licensemanagerusersubscriptions-Type-LicenseServerEndpoint-CreationTime"></a>
The timestamp when License Manager created the license server endpoint.
Type: Timestamp
Required: No

 ** IdentityProviderArn **   <a name="licensemanagerusersubscriptions-Type-LicenseServerEndpoint-IdentityProviderArn"></a>
The Amazon Resource Name (ARN) of the identity provider that's associated with the RDS license server endpoint.
Type: String
Required: No

 ** LicenseServerEndpointArn **   <a name="licensemanagerusersubscriptions-Type-LicenseServerEndpoint-LicenseServerEndpointArn"></a>
The ARN of the `ServerEndpoint` resource for the RDS license server.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-zA-Z0-9-\.]{1,510}/[a-zA-Z0-9-\.]{1,510}`
Required: No

 ** LicenseServerEndpointId **   <a name="licensemanagerusersubscriptions-Type-LicenseServerEndpoint-LicenseServerEndpointId"></a>
The ID of the license server endpoint.
Type: String
Required: No

 ** LicenseServerEndpointProvisioningStatus **   <a name="licensemanagerusersubscriptions-Type-LicenseServerEndpoint-LicenseServerEndpointProvisioningStatus"></a>
The current state of the provisioning process for the RDS license server endpoint
Type: String
Valid Values: `PROVISIONING | PROVISIONING_FAILED | PROVISIONED | DELETING | DELETION_FAILED | DELETED`
Required: No

 ** LicenseServers **   <a name="licensemanagerusersubscriptions-Type-LicenseServerEndpoint-LicenseServers"></a>
An array of `LicenseServer` resources that represent the license servers that are accessed through this endpoint.
Type: Array of [LicenseServer](API_LicenseServer.md) objects
Required: No

 ** ServerEndpoint **   <a name="licensemanagerusersubscriptions-Type-LicenseServerEndpoint-ServerEndpoint"></a>
The `ServerEndpoint` resource contains the network address of the RDS license server endpoint.
Type: [ServerEndpoint](API_ServerEndpoint.md) object
Required: No

 ** ServerType **   <a name="licensemanagerusersubscriptions-Type-LicenseServerEndpoint-ServerType"></a>
The type of license server.
Type: String
Valid Values: `RDS_SAL`
Required: No

 ** StatusMessage **   <a name="licensemanagerusersubscriptions-Type-LicenseServerEndpoint-StatusMessage"></a>
The message associated with the provisioning status, if there is one.
Type: String
Required: No

## See Also
<a name="API_LicenseServerEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/LicenseServerEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/LicenseServerEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/LicenseServerEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager User Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-user-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
