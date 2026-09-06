---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_PartitionInput.html
---

# PartitionInput
<a name="API_PartitionInput"></a>

The structure used to create and update a partition.

## Contents
<a name="API_PartitionInput_Contents"></a>

 ** LastAccessTime **   <a name="Glue-Type-PartitionInput-LastAccessTime"></a>
The last time at which the partition was accessed.
Type: Timestamp
Required: No

 ** LastAnalyzedTime **   <a name="Glue-Type-PartitionInput-LastAnalyzedTime"></a>
The last time at which column statistics were computed for this partition.
Type: Timestamp
Required: No

 ** Parameters **   <a name="Glue-Type-PartitionInput-Parameters"></a>
These key-value pairs define partition parameters.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 512000.
Required: No

 ** StorageDescriptor **   <a name="Glue-Type-PartitionInput-StorageDescriptor"></a>
Provides information about the physical location where the partition is stored.
Type: [StorageDescriptor](API_StorageDescriptor.md) object
Required: No

 ** Values **   <a name="Glue-Type-PartitionInput-Values"></a>
The values of the partition. Although this parameter is not required by the SDK, you must specify this parameter for a valid input.
The values for the keys for the new partition must be passed as an array of String objects that must be ordered in the same order as the partition keys appearing in the Amazon S3 prefix. Otherwise AWS Glue will add the values to the wrong keys.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_PartitionInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/PartitionInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/PartitionInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/PartitionInput)
