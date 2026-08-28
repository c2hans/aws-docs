---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ResourceDataSyncSourceWithState.html
---

# ResourceDataSyncSourceWithState
<a name="API_ResourceDataSyncSourceWithState"></a>

The data type name for including resource data sync state. There are four sync states:

 `OrganizationNotExists` (Your organization doesn't exist)

 `NoPermissions` (The system can't locate the service-linked role. This role is automatically created when a user creates a resource data sync in AWS Systems Manager Explorer.)

 `InvalidOrganizationalUnit` (You specified or selected an invalid unit in the resource data sync configuration.)

 `TrustedAccessDisabled` (You disabled Systems Manager access in the organization in AWS Organizations.)

## Contents
<a name="API_ResourceDataSyncSourceWithState_Contents"></a>

 ** AwsOrganizationsSource **   <a name="systemsmanager-Type-ResourceDataSyncSourceWithState-AwsOrganizationsSource"></a>
The field name in `SyncSource` for the `ResourceDataSyncAwsOrganizationsSource` type.
Type: [ResourceDataSyncAwsOrganizationsSource](API_ResourceDataSyncAwsOrganizationsSource.md) object
Required: No

 ** EnableAllOpsDataSources **   <a name="systemsmanager-Type-ResourceDataSyncSourceWithState-EnableAllOpsDataSources"></a>
When you create a resource data sync, if you choose one of the AWS Organizations options, then Systems Manager automatically enables all OpsData sources in the selected AWS Regions for all AWS accounts in your organization (or in the selected organization units). For more information, see [Setting up Systems Manager Explorer to display data from multiple accounts and Regions](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-resource-data-sync.html) in the * AWS Systems Manager User Guide*.
Type: Boolean
Required: No

 ** IncludeFutureRegions **   <a name="systemsmanager-Type-ResourceDataSyncSourceWithState-IncludeFutureRegions"></a>
Whether to automatically synchronize and aggregate data from new AWS Regions when those Regions come online.
Type: Boolean
Required: No

 ** SourceRegions **   <a name="systemsmanager-Type-ResourceDataSyncSourceWithState-SourceRegions"></a>
The `SyncSource` AWS Regions included in the resource data sync.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** SourceType **   <a name="systemsmanager-Type-ResourceDataSyncSourceWithState-SourceType"></a>
The type of data source for the resource data sync. `SourceType` is either `AwsOrganizations` (if an organization is present in AWS Organizations) or `singleAccountMultiRegions`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** State **   <a name="systemsmanager-Type-ResourceDataSyncSourceWithState-State"></a>
The data type name for including resource data sync state. There are four sync states:
 `OrganizationNotExists`: Your organization doesn't exist.
 `NoPermissions`: The system can't locate the service-linked role. This role is automatically created when a user creates a resource data sync in Explorer.
 `InvalidOrganizationalUnit`: You specified or selected an invalid unit in the resource data sync configuration.
 `TrustedAccessDisabled`: You disabled Systems Manager access in the organization in AWS Organizations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_ResourceDataSyncSourceWithState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ResourceDataSyncSourceWithState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ResourceDataSyncSourceWithState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ResourceDataSyncSourceWithState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
