---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_Ingestion.html
---

# Ingestion
<a name="API_Ingestion"></a>

Contains information about an ingestion.

## Contents
<a name="API_Ingestion_Contents"></a>

 ** app **   <a name="appfabric-Type-Ingestion-app"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** appBundleArn **   <a name="appfabric-Type-Ingestion-appBundleArn"></a>
The Amazon Resource Name (ARN) of the app bundle for the ingestion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+`
Required: Yes

 ** arn **   <a name="appfabric-Type-Ingestion-arn"></a>
The Amazon Resource Name (ARN) of the ingestion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+`
Required: Yes

 ** createdAt **   <a name="appfabric-Type-Ingestion-createdAt"></a>
The timestamp of when the ingestion was created.
Type: Timestamp
Required: Yes

 ** ingestionType **   <a name="appfabric-Type-Ingestion-ingestionType"></a>
The type of the ingestion.
Type: String
Valid Values: `auditLog`
Required: Yes

 ** state **   <a name="appfabric-Type-Ingestion-state"></a>
The status of the ingestion.
Type: String
Valid Values: `enabled | disabled`
Required: Yes

 ** tenantId **   <a name="appfabric-Type-Ingestion-tenantId"></a>
The ID of the application tenant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** updatedAt **   <a name="appfabric-Type-Ingestion-updatedAt"></a>
The timestamp of when the ingestion was last updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_Ingestion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/Ingestion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/Ingestion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/Ingestion)
