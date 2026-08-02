---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_WorkspaceSummary.html
---

# WorkspaceSummary
<a name="API_WorkspaceSummary"></a>

A structure that contains some information about one workspace in the account.

## Contents
<a name="API_WorkspaceSummary_Contents"></a>

 ** authentication **   <a name="ManagedGrafana-Type-WorkspaceSummary-authentication"></a>
A structure containing information about the authentication methods used in the workspace.
Type: [AuthenticationSummary](API_AuthenticationSummary.md) object
Required: Yes

 ** created **   <a name="ManagedGrafana-Type-WorkspaceSummary-created"></a>
The date that the workspace was created.
Type: Timestamp
Required: Yes

 ** endpoint **   <a name="ManagedGrafana-Type-WorkspaceSummary-endpoint"></a>
The URL endpoint to use to access the Grafana console in the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** grafanaVersion **   <a name="ManagedGrafana-Type-WorkspaceSummary-grafanaVersion"></a>
The Grafana version that the workspace is running.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** id **   <a name="ManagedGrafana-Type-WorkspaceSummary-id"></a>
The unique ID of the workspace.
Type: String
Pattern: `g-[0-9a-f]{10}`
Required: Yes

 ** modified **   <a name="ManagedGrafana-Type-WorkspaceSummary-modified"></a>
The most recent date that the workspace was modified.
Type: Timestamp
Required: Yes

 ** status **   <a name="ManagedGrafana-Type-WorkspaceSummary-status"></a>
The current status of the workspace.
Type: String
Valid Values: `ACTIVE | CREATING | DELETING | FAILED | UPDATING | UPGRADING | DELETION_FAILED | CREATION_FAILED | UPDATE_FAILED | UPGRADE_FAILED | LICENSE_REMOVAL_FAILED | VERSION_UPDATING | VERSION_UPDATE_FAILED | DEGRADED`
Required: Yes

 ** description **   <a name="ManagedGrafana-Type-WorkspaceSummary-description"></a>
The customer-entered description of the workspace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** grafanaToken **   <a name="ManagedGrafana-Type-WorkspaceSummary-grafanaToken"></a>
The token that ties this workspace to a Grafana Labs account. For more information, see [Link your account with Grafana Labs](https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html#AMG-workspace-register-enterprise).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: No

 ** licenseType **   <a name="ManagedGrafana-Type-WorkspaceSummary-licenseType"></a>
Specifies whether this workspace has a full Grafana Enterprise license.
Amazon Managed Grafana workspaces no longer support Grafana Enterprise free trials.
Type: String
Valid Values: `ENTERPRISE | ENTERPRISE_FREE_TRIAL`
Required: No

 ** name **   <a name="ManagedGrafana-Type-WorkspaceSummary-name"></a>
The name of the workspace.
Type: String
Pattern: `[a-zA-Z0-9-._~]{1,255}`
Required: No

 ** notificationDestinations **   <a name="ManagedGrafana-Type-WorkspaceSummary-notificationDestinations"></a>
The AWS notification channels that Amazon Managed Grafana can automatically create IAM roles and permissions for, which allows Amazon Managed Grafana to use these channels.
Type: Array of strings
Valid Values: `SNS`
Required: No

 ** tags **   <a name="ManagedGrafana-Type-WorkspaceSummary-tags"></a>
The list of tags associated with the workspace.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_WorkspaceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/WorkspaceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/WorkspaceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/WorkspaceSummary)
