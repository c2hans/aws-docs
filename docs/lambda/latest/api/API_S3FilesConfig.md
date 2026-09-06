---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_S3FilesConfig.html
---

# S3FilesConfig
<a name="API_S3FilesConfig"></a>

Setting controls how your function accesses data from an Amazon S3 file system.

## Contents
<a name="API_S3FilesConfig_Contents"></a>

 ** DirectS3Read **   <a name="lambda-Type-S3FilesConfig-DirectS3Read"></a>
Specifies if a function reads from the file system for the lowest latency, or through Amazon S3 Files feature "direct Amazon S3 bucket reads" for the highest throughput. Valid values:
+  `AUTO` (default) – Direct reads are active for functions you configure with 512 MB or more of memory.
+  `ENABLED` – Enforces all reads are directly from the Amazon S3 bucket, regardless of available memory (less than 512 MB).
+  `DISABLED` – Routes all reads through the file system, regardless of memory configuration.
To use direct reads, you must grant the execution role the `s3:GetObject` and `s3:GetObjectVersion` permissions. If a direct read fails, Lambda automatically falls back to reading through the file system.
Type: String
Valid Values: `ENABLED | DISABLED | AUTO`
Required: No

## See Also
<a name="API_S3FilesConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/S3FilesConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/S3FilesConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/S3FilesConfig)
