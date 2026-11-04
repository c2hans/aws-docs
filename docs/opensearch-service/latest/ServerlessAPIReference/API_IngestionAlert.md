---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_IngestionAlert.html
---

# IngestionAlert
<a name="API_IngestionAlert"></a>

An alert about an operational issue that currently affects a running ingestion. Alerts are cleared when the issue is resolved.

## Contents
<a name="API_IngestionAlert_Contents"></a>

 ** code **   <a name="opensearchserverless-Type-IngestionAlert-code"></a>
The code that identifies the alert.
Type: String
Valid Values: `SOURCE_ACCESS_DENIED | SOURCE_RESOURCE_NOT_FOUND | DESTINATION_ACCESS_DENIED | DESTINATION_RESOURCE_NOT_FOUND | INTERNAL_SERVER_ERROR`
Required: No

 ** message **   <a name="opensearchserverless-Type-IngestionAlert-message"></a>
A description of the alert.
Type: String
Required: No

## See Also
<a name="API_IngestionAlert_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/IngestionAlert)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/IngestionAlert)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/IngestionAlert)
