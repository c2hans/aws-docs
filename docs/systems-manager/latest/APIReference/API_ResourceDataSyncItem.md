---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ResourceDataSyncItem.html
---

# ResourceDataSyncItem
<a name="API_ResourceDataSyncItem"></a>

Information about a resource data sync configuration, including its current status and last successful sync.

## Contents
<a name="API_ResourceDataSyncItem_Contents"></a>

 ** LastStatus **   <a name="systemsmanager-Type-ResourceDataSyncItem-LastStatus"></a>
The status reported by the last sync.
Type: String
Valid Values: `Successful | Failed | InProgress`
Required: No

 ** LastSuccessfulSyncTime **   <a name="systemsmanager-Type-ResourceDataSyncItem-LastSuccessfulSyncTime"></a>
The last time the sync operations returned a status of `SUCCESSFUL` (UTC).
Type: Timestamp
Required: No

 ** LastSyncStatusMessage **   <a name="systemsmanager-Type-ResourceDataSyncItem-LastSyncStatusMessage"></a>
The status message details reported by the last sync.
Type: String
Required: No

 ** LastSyncTime **   <a name="systemsmanager-Type-ResourceDataSyncItem-LastSyncTime"></a>
The last time the configuration attempted to sync (UTC).
Type: Timestamp
Required: No

 ** S3Destination **   <a name="systemsmanager-Type-ResourceDataSyncItem-S3Destination"></a>
Configuration information for the target S3 bucket.
Type: [ResourceDataSyncS3Destination](API_ResourceDataSyncS3Destination.md) object
Required: No

 ** SyncCreatedTime **   <a name="systemsmanager-Type-ResourceDataSyncItem-SyncCreatedTime"></a>
The date and time the configuration was created (UTC).
Type: Timestamp
Required: No

 ** SyncLastModifiedTime **   <a name="systemsmanager-Type-ResourceDataSyncItem-SyncLastModifiedTime"></a>
The date and time the resource data sync was changed.
Type: Timestamp
Required: No

 ** SyncName **   <a name="systemsmanager-Type-ResourceDataSyncItem-SyncName"></a>
The name of the resource data sync.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** SyncSource **   <a name="systemsmanager-Type-ResourceDataSyncItem-SyncSource"></a>
Information about the source where the data was synchronized.
Type: [ResourceDataSyncSourceWithState](API_ResourceDataSyncSourceWithState.md) object
Required: No

 ** SyncType **   <a name="systemsmanager-Type-ResourceDataSyncItem-SyncType"></a>
The type of resource data sync. If `SyncType` is `SyncToDestination`, then the resource data sync synchronizes data to an S3 bucket. If the `SyncType` is `SyncFromSource` then the resource data sync synchronizes data from AWS Organizations or from multiple AWS Regions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_ResourceDataSyncItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ResourceDataSyncItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ResourceDataSyncItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ResourceDataSyncItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
