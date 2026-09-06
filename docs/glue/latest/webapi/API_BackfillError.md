---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BackfillError.html
---

# BackfillError
<a name="API_BackfillError"></a>

A list of errors that can occur when registering partition indexes for an existing table.

These errors give the details about why an index registration failed and provide a limited number of partitions in the response, so that you can fix the partitions at fault and try registering the index again. The most common set of errors that can occur are categorized as follows:
+ EncryptedPartitionError: The partitions are encrypted.
+ InvalidPartitionTypeDataError: The partition value doesn't match the data type for that partition column.
+ MissingPartitionValueError: The partitions are encrypted.
+ UnsupportedPartitionCharacterError: Characters inside the partition value are not supported. For example: U\+0000 , U\+0001, U\+0002.
+ InternalError: Any error which does not belong to other error codes.

## Contents
<a name="API_BackfillError_Contents"></a>

 ** Code **   <a name="Glue-Type-BackfillError-Code"></a>
The error code for an error that occurred when registering partition indexes for an existing table.
Type: String
Valid Values: `ENCRYPTED_PARTITION_ERROR | INTERNAL_ERROR | INVALID_PARTITION_TYPE_DATA_ERROR | MISSING_PARTITION_VALUE_ERROR | UNSUPPORTED_PARTITION_CHARACTER_ERROR`
Required: No

 ** Partitions **   <a name="Glue-Type-BackfillError-Partitions"></a>
A list of a limited number of partitions in the response.
Type: Array of [PartitionValueList](API_PartitionValueList.md) objects
Required: No

## See Also
<a name="API_BackfillError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BackfillError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BackfillError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BackfillError)
