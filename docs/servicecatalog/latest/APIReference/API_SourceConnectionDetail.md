---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_SourceConnectionDetail.html
---

# SourceConnectionDetail
<a name="API_SourceConnectionDetail"></a>

Provides details about the configured `SourceConnection`.

## Contents
<a name="API_SourceConnectionDetail_Contents"></a>

 ** ConnectionParameters **   <a name="servicecatalog-Type-SourceConnectionDetail-ConnectionParameters"></a>
The connection details based on the connection `Type`.
Type: [SourceConnectionParameters](API_SourceConnectionParameters.md) object
Required: No

 ** LastSync **   <a name="servicecatalog-Type-SourceConnectionDetail-LastSync"></a>
Provides details about the product's connection sync and contains the following sub-fields.
+  `LastSyncTime`
+  `LastSyncStatus`
+  `LastSyncStatusMessage`
+  `LastSuccessfulSyncTime`
+  `LastSuccessfulSyncProvisioningArtifactID`
Type: [LastSync](API_LastSync.md) object
Required: No

 ** Type **   <a name="servicecatalog-Type-SourceConnectionDetail-Type"></a>
The only supported `SourceConnection` type is Codestar.
Type: String
Valid Values: `CODESTAR`
Required: No

## See Also
<a name="API_SourceConnectionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/SourceConnectionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/SourceConnectionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/SourceConnectionDetail)
