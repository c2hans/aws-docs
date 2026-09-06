---
source_url: https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_StatusReason.html
---

# StatusReason
<a name="API_StatusReason"></a>

Stream status reason with error and timestamp.

## Contents
<a name="API_StatusReason_Contents"></a>

 ** error **   <a name="auroradsql-Type-StatusReason-error"></a>
The error code for the stream failure.
Type: String
Valid Values: `KINESIS_THROUGHPUT_EXCEEDED | KINESIS_STREAM_NOT_FOUND | ROLE_ACCESS_DENIED | KINESIS_ACCESS_DENIED | KINESIS_KMS_ACCESS_DENIED | KINESIS_OVERSIZE_RECORD | CLUSTER_CMK_INACCESSIBLE | INTERNAL_ERROR`
Required: Yes

 ** updatedAt **   <a name="auroradsql-Type-StatusReason-updatedAt"></a>
The timestamp when the status was updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_StatusReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dsql-2018-05-10/StatusReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dsql-2018-05-10/StatusReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dsql-2018-05-10/StatusReason)
