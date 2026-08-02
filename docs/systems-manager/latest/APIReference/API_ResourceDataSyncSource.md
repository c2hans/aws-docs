---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ResourceDataSyncSource.html
---

# ResourceDataSyncSource
<a name="API_ResourceDataSyncSource"></a>

Information about the source of the data included in the resource data sync.

## Contents
<a name="API_ResourceDataSyncSource_Contents"></a>

 ** SourceRegions **   <a name="systemsmanager-Type-ResourceDataSyncSource-SourceRegions"></a>
The `SyncSource` AWS Regions included in the resource data sync.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** SourceType **   <a name="systemsmanager-Type-ResourceDataSyncSource-SourceType"></a>
The type of data source for the resource data sync. `SourceType` is either `AwsOrganizations` (if an organization is present in AWS Organizations) or `SingleAccountMultiRegions`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** AwsOrganizationsSource **   <a name="systemsmanager-Type-ResourceDataSyncSource-AwsOrganizationsSource"></a>
Information about the `AwsOrganizationsSource` resource data sync source. A sync source of this type can synchronize data from AWS Organizations.
Type: [ResourceDataSyncAwsOrganizationsSource](API_ResourceDataSyncAwsOrganizationsSource.md) object
Required: No

 ** EnableAllOpsDataSources **   <a name="systemsmanager-Type-ResourceDataSyncSource-EnableAllOpsDataSources"></a>
When you create a resource data sync, if you choose one of the AWS Organizations options, then Systems Manager automatically enables all OpsData sources in the selected AWS Regions for all AWS accounts in your organization (or in the selected organization units). For more information, see [Setting up Systems Manager Explorer to display data from multiple accounts and Regions](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-resource-data-sync.html) in the * AWS Systems Manager User Guide*.
Type: Boolean
Required: No

 ** IncludeFutureRegions **   <a name="systemsmanager-Type-ResourceDataSyncSource-IncludeFutureRegions"></a>
Whether to automatically synchronize and aggregate data from new AWS Regions when those Regions come online.
Type: Boolean
Required: No

## See Also
<a name="API_ResourceDataSyncSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ResourceDataSyncSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ResourceDataSyncSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ResourceDataSyncSource)
