---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_VectorData.html
---

# VectorData
<a name="API_S3VectorBuckets_VectorData"></a>

The vector data in different formats.

## Contents
<a name="API_S3VectorBuckets_VectorData_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** float32 **   <a name="AmazonS3-Type-S3VectorBuckets_VectorData-float32"></a>
The vector data as 32-bit floating point numbers. The number of elements in this array must exactly match the dimension of the vector index where the operation is being performed.
Type: Array of floats
Required: No

## See Also
<a name="API_S3VectorBuckets_VectorData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/VectorData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/VectorData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/VectorData)
