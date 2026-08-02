---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_OrcSerDe.html
---

# OrcSerDe
<a name="API_OrcSerDe"></a>

A serializer to use for converting data to the ORC format before storing it in Amazon S3. For more information, see [Apache ORC](https://orc.apache.org/docs/).

## Contents
<a name="API_OrcSerDe_Contents"></a>

 ** BlockSizeBytes **   <a name="Firehose-Type-OrcSerDe-BlockSizeBytes"></a>
The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Firehose uses this value for padding calculations.
Type: Integer
Valid Range: Minimum value of 67108864.
Required: No

 ** BloomFilterColumns **   <a name="Firehose-Type-OrcSerDe-BloomFilterColumns"></a>
The column names for which you want Firehose to create bloom filters. The default is `null`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^\S+$`
Required: No

 ** BloomFilterFalsePositiveProbability **   <a name="Firehose-Type-OrcSerDe-BloomFilterFalsePositiveProbability"></a>
The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** Compression **   <a name="Firehose-Type-OrcSerDe-Compression"></a>
The compression code to use over data blocks. The default is `SNAPPY`.
Type: String
Valid Values: `NONE | ZLIB | SNAPPY`
Required: No

 ** DictionaryKeyThreshold **   <a name="Firehose-Type-OrcSerDe-DictionaryKeyThreshold"></a>
Represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to 1.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** EnablePadding **   <a name="Firehose-Type-OrcSerDe-EnablePadding"></a>
Set this to `true` to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is `false`.
Type: Boolean
Required: No

 ** FormatVersion **   <a name="Firehose-Type-OrcSerDe-FormatVersion"></a>
The version of the file to write. The possible values are `V0_11` and `V0_12`. The default is `V0_12`.
Type: String
Valid Values: `V0_11 | V0_12`
Required: No

 ** PaddingTolerance **   <a name="Firehose-Type-OrcSerDe-PaddingTolerance"></a>
A number between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is 0.05, which means 5 percent of stripe size.
For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task.
Firehose ignores this parameter when [OrcSerDe:EnablePadding](#Firehose-Type-OrcSerDe-EnablePadding) is `false`.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** RowIndexStride **   <a name="Firehose-Type-OrcSerDe-RowIndexStride"></a>
The number of rows between index entries. The default is 10,000 and the minimum is 1,000.
Type: Integer
Valid Range: Minimum value of 1000.
Required: No

 ** StripeSizeBytes **   <a name="Firehose-Type-OrcSerDe-StripeSizeBytes"></a>
The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.
Type: Integer
Valid Range: Minimum value of 8388608.
Required: No

## See Also
<a name="API_OrcSerDe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/OrcSerDe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/OrcSerDe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/OrcSerDe)
