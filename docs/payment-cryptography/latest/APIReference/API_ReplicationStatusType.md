---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ReplicationStatusType.html
---

# ReplicationStatusType
<a name="API_ReplicationStatusType"></a>

Represents the replication status information for a key in a replication region for [Multi-Region key replication](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html).

This structure contains details about the current state of key replication, including any status messages and operational information about the replication process.

## Contents
<a name="API_ReplicationStatusType_Contents"></a>

 ** Status **   <a name="paymentcryptography-Type-ReplicationStatusType-Status"></a>
The current status of key replication in this AWS Region.
This field indicates whether the key replication is in progress, completed successfully, or has encountered an error. Possible values include states such as `SYNCRHONIZED`, `IN_PROGRESS`, `DELETE_IN_PROGRESS`, or `FAILED`. This provides visibility into the replication process for monitoring and troubleshooting purposes.
Type: String
Valid Values: `IN_PROGRESS | DELETE_IN_PROGRESS | FAILED | SYNCHRONIZED`
Required: Yes

 ** StatusMessage **   <a name="paymentcryptography-Type-ReplicationStatusType-StatusMessage"></a>
A message that provides additional information about the current replication status of the key.
This field contains details about any issues or progress updates related to key replication operations. It may include information about replication failures, synchronization status, or other operational details.
Type: String
Required: No

## See Also
<a name="API_ReplicationStatusType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/ReplicationStatusType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/ReplicationStatusType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/ReplicationStatusType)
