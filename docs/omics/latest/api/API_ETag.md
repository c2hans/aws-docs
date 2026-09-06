---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ETag.html
---

# ETag
<a name="API_ETag"></a>

The entity tag (ETag) is a hash of the object representing its semantic content.

## Contents
<a name="API_ETag_Contents"></a>

 ** algorithm **   <a name="omics-Type-ETag-algorithm"></a>
The algorithm used to calculate the read set’s ETag(s).
Type: String
Valid Values: `FASTQ_MD5up | BAM_MD5up | CRAM_MD5up | FASTQ_SHA256up | BAM_SHA256up | CRAM_SHA256up | FASTQ_SHA512up | BAM_SHA512up | CRAM_SHA512up`
Required: No

 ** source1 **   <a name="omics-Type-ETag-source1"></a>
The ETag hash calculated on Source1 of the read set.
Type: String
Required: No

 ** source2 **   <a name="omics-Type-ETag-source2"></a>
The ETag hash calculated on Source2 of the read set.
Type: String
Required: No

## See Also
<a name="API_ETag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ETag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ETag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ETag)
