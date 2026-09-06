---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_OutboundConnectionStatus.html
---

# OutboundConnectionStatus
<a name="API_OutboundConnectionStatus"></a>

The status of an outbound cross-cluster connection.

## Contents
<a name="API_OutboundConnectionStatus_Contents"></a>

 ** Message **   <a name="opensearchservice-Type-OutboundConnectionStatus-Message"></a>
Verbose information for the outbound connection.
Type: String
Required: No

 ** StatusCode **   <a name="opensearchservice-Type-OutboundConnectionStatus-StatusCode"></a>
The status code for the outbound connection. Can be one of the following:
+  **VALIDATING** - The outbound connection request is being validated.
+  **VALIDATION\_FAILED** - Validation failed for the connection request.
+  **PENDING\_ACCEPTANCE**: Outbound connection request is validated and is not yet accepted by the remote domain owner.
+  **APPROVED** - Outbound connection has been approved by the remote domain owner for getting provisioned.
+  **PROVISIONING** - Outbound connection request is in process.
+  **ACTIVE** - Outbound connection is active and ready to use.
+  **REJECTING** - Outbound connection rejection by remote domain owner is in progress.
+  **REJECTED** - Outbound connection request is rejected by remote domain owner.
+  **DELETING** - Outbound connection deletion is in progress.
+  **DELETED** - Outbound connection is deleted and can no longer be used.
Type: String
Valid Values: `VALIDATING | VALIDATION_FAILED | PENDING_ACCEPTANCE | APPROVED | PROVISIONING | ACTIVE | REJECTING | REJECTED | DELETING | DELETED`
Required: No

## See Also
<a name="API_OutboundConnectionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/OutboundConnectionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/OutboundConnectionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/OutboundConnectionStatus)
