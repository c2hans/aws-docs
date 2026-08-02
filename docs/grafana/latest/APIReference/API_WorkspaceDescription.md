---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_WorkspaceDescription.html
---

# WorkspaceDescription
<a name="API_WorkspaceDescription"></a>

A structure containing information about an Amazon Managed Grafana workspace in your account.

## Contents
<a name="API_WorkspaceDescription_Contents"></a>

 ** authentication **   <a name="ManagedGrafana-Type-WorkspaceDescription-authentication"></a>
A structure that describes whether the workspace uses SAML, IAM Identity Center, or both methods for user authentication.
Type: [AuthenticationSummary](API_AuthenticationSummary.md) object
Required: Yes

 ** created **   <a name="ManagedGrafana-Type-WorkspaceDescription-created"></a>
The date that the workspace was created.
Type: Timestamp
Required: Yes

 ** dataSources **   <a name="ManagedGrafana-Type-WorkspaceDescription-dataSources"></a>
Specifies the AWS data sources that have been configured to have IAM roles and permissions created to allow Amazon Managed Grafana to read data from these sources.
This list is only used when the workspace was created through the AWS console, and the `permissionType` is `SERVICE_MANAGED`.
Type: Array of strings
Valid Values: `AMAZON_OPENSEARCH_SERVICE | CLOUDWATCH | PROMETHEUS | XRAY | TIMESTREAM | SITEWISE | ATHENA | REDSHIFT | TWINMAKER`
Required: Yes

 ** endpoint **   <a name="ManagedGrafana-Type-WorkspaceDescription-endpoint"></a>
The URL that users can use to access the Grafana console in the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** grafanaVersion **   <a name="ManagedGrafana-Type-WorkspaceDescription-grafanaVersion"></a>
The version of Grafana supported in this workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** id **   <a name="ManagedGrafana-Type-WorkspaceDescription-id"></a>
The unique ID of this workspace.
Type: String
Pattern: `g-[0-9a-f]{10}`
Required: Yes

 ** modified **   <a name="ManagedGrafana-Type-WorkspaceDescription-modified"></a>
The most recent date that the workspace was modified.
Type: Timestamp
Required: Yes

 ** status **   <a name="ManagedGrafana-Type-WorkspaceDescription-status"></a>
The current status of the workspace.
Type: String
Valid Values: `ACTIVE | CREATING | DELETING | FAILED | UPDATING | UPGRADING | DELETION_FAILED | CREATION_FAILED | UPDATE_FAILED | UPGRADE_FAILED | LICENSE_REMOVAL_FAILED | VERSION_UPDATING | VERSION_UPDATE_FAILED | DEGRADED`
Required: Yes

 ** accountAccessType **   <a name="ManagedGrafana-Type-WorkspaceDescription-accountAccessType"></a>
Specifies whether the workspace can access AWS resources in this AWS account only, or whether it can also access AWS resources in other accounts in the same organization. If this is `ORGANIZATION`, the `workspaceOrganizationalUnits` parameter specifies which organizational units the workspace can access.
Type: String
Valid Values: `CURRENT_ACCOUNT | ORGANIZATION`
Required: No

 ** degradedWorkspaceReason **   <a name="ManagedGrafana-Type-WorkspaceDescription-degradedWorkspaceReason"></a>
If the workspace is in the `DEGRADED` status, this field describes the reason the workspace is degraded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** description **   <a name="ManagedGrafana-Type-WorkspaceDescription-description"></a>
The user-defined description of the workspace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** freeTrialConsumed **   <a name="ManagedGrafana-Type-WorkspaceDescription-freeTrialConsumed"></a>
Specifies whether this workspace has already fully used its free trial for Grafana Enterprise.
Amazon Managed Grafana workspaces no longer support Grafana Enterprise free trials.
Type: Boolean
Required: No

 ** freeTrialExpiration **   <a name="ManagedGrafana-Type-WorkspaceDescription-freeTrialExpiration"></a>
If this workspace is currently in the free trial period for Grafana Enterprise, this value specifies when that free trial ends.
Amazon Managed Grafana workspaces no longer support Grafana Enterprise free trials.
Type: Timestamp
Required: No

 ** grafanaToken **   <a name="ManagedGrafana-Type-WorkspaceDescription-grafanaToken"></a>
The token that ties this workspace to a Grafana Labs account. For more information, see [Link your account with Grafana Labs](https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html#AMG-workspace-register-enterprise).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: No

 ** ipAddressType **   <a name="ManagedGrafana-Type-WorkspaceDescription-ipAddressType"></a>
The type of IP addresses supported for connection to the workspace. Valid values are `IPv4` and `DualStack`.
Type: String
Valid Values: `IPv4 | DualStack`
Required: No

 ** kmsKeyId **   <a name="ManagedGrafana-Type-WorkspaceDescription-kmsKeyId"></a>
The ID or ARN of the AWS Key Management Service key used for encrypting workspace data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]+`
Required: No

 ** licenseExpiration **   <a name="ManagedGrafana-Type-WorkspaceDescription-licenseExpiration"></a>
If this workspace has a full Grafana Enterprise license purchased through AWS Marketplace, this specifies when the license ends and will need to be renewed. Purchasing the Enterprise plugins option through Amazon Managed Grafana does not have an expiration. It is valid until the license is removed.
Type: Timestamp
Required: No

 ** licenseType **   <a name="ManagedGrafana-Type-WorkspaceDescription-licenseType"></a>
Specifies whether this workspace has a full Grafana Enterprise license.
Amazon Managed Grafana workspaces no longer support Grafana Enterprise free trials.
Type: String
Valid Values: `ENTERPRISE | ENTERPRISE_FREE_TRIAL`
Required: No

 ** name **   <a name="ManagedGrafana-Type-WorkspaceDescription-name"></a>
The name of the workspace.
Type: String
Pattern: `[a-zA-Z0-9-._~]{1,255}`
Required: No

 ** networkAccessControl **   <a name="ManagedGrafana-Type-WorkspaceDescription-networkAccessControl"></a>
The configuration settings for network access to your workspace.
Type: [NetworkAccessConfiguration](API_NetworkAccessConfiguration.md) object
Required: No

 ** notificationDestinations **   <a name="ManagedGrafana-Type-WorkspaceDescription-notificationDestinations"></a>
The AWS notification channels that Amazon Managed Grafana can automatically create IAM roles and permissions for, to allow Amazon Managed Grafana to use these channels.
Type: Array of strings
Valid Values: `SNS`
Required: No

 ** organizationalUnits **   <a name="ManagedGrafana-Type-WorkspaceDescription-organizationalUnits"></a>
Specifies the organizational units that this workspace is allowed to use data sources from, if this workspace is in an account that is part of an organization.
Type: Array of strings
Required: No

 ** organizationRoleName **   <a name="ManagedGrafana-Type-WorkspaceDescription-organizationRoleName"></a>
The name of the IAM role that is used to access resources through Organizations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** permissionType **   <a name="ManagedGrafana-Type-WorkspaceDescription-permissionType"></a>
If this is `SERVICE_MANAGED`, and the workplace was created through the Amazon Managed Grafana console, then Amazon Managed Grafana automatically creates the IAM roles and provisions the permissions that the workspace needs to use AWS data sources and notification channels.
If this is `CUSTOMER_MANAGED`, you must manage those roles and permissions yourself.
If you are working with a workspace in a member account of an organization and that account is not a delegated administrator account, and you want the workspace to access data sources in other AWS accounts in the organization, this parameter must be set to `CUSTOMER_MANAGED`.
For more information about converting between customer and service managed, see [Managing permissions for data sources and notification channels](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-datasource-and-notification.html). For more information about the roles and permissions that must be managed for customer managed workspaces, see [Amazon Managed Grafana permissions and policies for AWS data sources and notification channels](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-permissions.html)
Type: String
Valid Values: `CUSTOMER_MANAGED | SERVICE_MANAGED`
Required: No

 ** stackSetName **   <a name="ManagedGrafana-Type-WorkspaceDescription-stackSetName"></a>
The name of the AWS CloudFormation stack set that is used to generate IAM roles to be used for this workspace.
Type: String
Required: No

 ** tags **   <a name="ManagedGrafana-Type-WorkspaceDescription-tags"></a>
The list of tags associated with the workspace.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** vpcConfiguration **   <a name="ManagedGrafana-Type-WorkspaceDescription-vpcConfiguration"></a>
The configuration for connecting to data sources in a private VPC (Amazon Virtual Private Cloud).
Type: [VpcConfiguration](API_VpcConfiguration.md) object
Required: No

 ** workspaceRoleArn **   <a name="ManagedGrafana-Type-WorkspaceDescription-workspaceRoleArn"></a>
The IAM role that grants permissions to the AWS resources that the workspace will view data from. This role must already exist.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_WorkspaceDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/WorkspaceDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/WorkspaceDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/WorkspaceDescription)
