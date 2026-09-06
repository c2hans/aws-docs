---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3ComputeObjectChecksumOperation.html
---

# S3ComputeObjectChecksumOperation
<a name="API_control_S3ComputeObjectChecksumOperation"></a>

Directs the specified job to invoke the ComputeObjectChecksum operation on every object listed in the job's manifest.

## Contents
<a name="API_control_S3ComputeObjectChecksumOperation_Contents"></a>

 ** ChecksumAlgorithm **   <a name="AmazonS3-Type-control_S3ComputeObjectChecksumOperation-ChecksumAlgorithm"></a>
Indicates the algorithm that you want Amazon S3 to use to create the checksum. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the Amazon S3 User Guide.
Type: String
Valid Values: `CRC32 | CRC32C | CRC64NVME | MD5 | SHA1 | SHA256 | SHA512 | XXHASH64 | XXHASH3 | XXHASH128`
Required: No

 ** ChecksumType **   <a name="AmazonS3-Type-control_S3ComputeObjectChecksumOperation-ChecksumType"></a>
Indicates the checksum type that you want Amazon S3 to use to calculate the object's checksum value. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the Amazon S3 User Guide.
Type: String
Valid Values: `FULL_OBJECT | COMPOSITE`
Required: No

## See Also
<a name="API_control_S3ComputeObjectChecksumOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3ComputeObjectChecksumOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3ComputeObjectChecksumOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3ComputeObjectChecksumOperation)
