---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DomainMaintenanceDetails.html
---

# DomainMaintenanceDetails
<a name="API_DomainMaintenanceDetails"></a>

Container for the domain maintenance details.

## Contents
<a name="API_DomainMaintenanceDetails_Contents"></a>

 ** Action **   <a name="opensearchservice-Type-DomainMaintenanceDetails-Action"></a>
The name of the action.
Type: String
Valid Values: `REBOOT_NODE | RESTART_SEARCH_PROCESS | RESTART_DASHBOARD`
Required: No

 ** CreatedAt **   <a name="opensearchservice-Type-DomainMaintenanceDetails-CreatedAt"></a>
The time at which the action was created.
Type: Timestamp
Required: No

 ** DomainName **   <a name="opensearchservice-Type-DomainMaintenanceDetails-DomainName"></a>
The name of the domain.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: No

 ** MaintenanceId **   <a name="opensearchservice-Type-DomainMaintenanceDetails-MaintenanceId"></a>
The ID of the requested action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([\s\S]*)$`
Required: No

 ** NodeId **   <a name="opensearchservice-Type-DomainMaintenanceDetails-NodeId"></a>
The ID of the data node.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 40.
Required: No

 ** Status **   <a name="opensearchservice-Type-DomainMaintenanceDetails-Status"></a>
The status of the action.
Type: String
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | TIMED_OUT`
Required: No

 ** StatusMessage **   <a name="opensearchservice-Type-DomainMaintenanceDetails-StatusMessage"></a>
The status message for the action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `^([\s\S]*)$`
Required: No

 ** UpdatedAt **   <a name="opensearchservice-Type-DomainMaintenanceDetails-UpdatedAt"></a>
The time at which the action was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_DomainMaintenanceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DomainMaintenanceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DomainMaintenanceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DomainMaintenanceDetails)
