---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_InboundConnectionStatus.html
---

# InboundConnectionStatus
<a name="API_InboundConnectionStatus"></a>

The status of an inbound cross-cluster connection for OpenSearch Service.

## Contents
<a name="API_InboundConnectionStatus_Contents"></a>

 ** Message **   <a name="opensearchservice-Type-InboundConnectionStatus-Message"></a>
Information about the connection.
Type: String
Required: No

 ** StatusCode **   <a name="opensearchservice-Type-InboundConnectionStatus-StatusCode"></a>
The status code for the connection. Can be one of the following:
+  **PENDING\_ACCEPTANCE** - Inbound connection is not yet accepted by the remote domain owner.
+  **APPROVED**: Inbound connection is pending acceptance by the remote domain owner.
+  **PROVISIONING**: Inbound connection is being provisioned.
+  **ACTIVE**: Inbound connection is active and ready to use.
+  **REJECTING**: Inbound connection rejection is in process.
+  **REJECTED**: Inbound connection is rejected.
+  **DELETING**: Inbound connection deletion is in progress.
+  **DELETED**: Inbound connection is deleted and can no longer be used.
Type: String
Valid Values: `PENDING_ACCEPTANCE | APPROVED | PROVISIONING | ACTIVE | REJECTING | REJECTED | DELETING | DELETED`
Required: No

## See Also
<a name="API_InboundConnectionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/InboundConnectionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/InboundConnectionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/InboundConnectionStatus)
