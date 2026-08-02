---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_LastSync.html
---

# LastSync
<a name="API_LastSync"></a>

Provides details about the product's connection sync and contains the following sub-fields.
+  `LastSyncTime`
+  `LastSyncStatus`
+  `LastSyncStatusMessage`
+  `LastSuccessfulSyncTime`
+  `LastSuccessfulSyncProvisioningArtifactID`

## Contents
<a name="API_LastSync_Contents"></a>

 ** LastSuccessfulSyncProvisioningArtifactId **   <a name="servicecatalog-Type-LastSync-LastSuccessfulSyncProvisioningArtifactId"></a>
The ProvisioningArtifactID of the ProvisioningArtifact created from the latest successful sync.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** LastSuccessfulSyncTime **   <a name="servicecatalog-Type-LastSync-LastSuccessfulSyncTime"></a>
The time of the latest successful sync from the source repo artifact to the AWS Service Catalog product.
Type: Timestamp
Required: No

 ** LastSyncStatus **   <a name="servicecatalog-Type-LastSync-LastSyncStatus"></a>
The current status of the sync. Responses include `SUCCEEDED` or `FAILED`.
Type: String
Valid Values: `SUCCEEDED | FAILED`
Required: No

 ** LastSyncStatusMessage **   <a name="servicecatalog-Type-LastSync-LastSyncStatusMessage"></a>
The sync's status message.
Type: String
Required: No

 ** LastSyncTime **   <a name="servicecatalog-Type-LastSync-LastSyncTime"></a>
The time of the last attempted sync from the repository to the AWS Service Catalog product.
Type: Timestamp
Required: No

## See Also
<a name="API_LastSync_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/LastSync)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/LastSync)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/LastSync)
