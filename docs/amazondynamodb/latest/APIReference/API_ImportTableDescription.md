---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ImportTableDescription.html
---

# ImportTableDescription
<a name="API_ImportTableDescription"></a>

 Represents the properties of the table being imported into.

## Contents
<a name="API_ImportTableDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClientToken **   <a name="DDB-Type-ImportTableDescription-ClientToken"></a>
 The client token that was provided for the import task. Reusing the client token on retry makes a call to `ImportTable` idempotent.
Type: String
Pattern: `^[^\$]+$`
Required: No

 ** CloudWatchLogGroupArn **   <a name="DDB-Type-ImportTableDescription-CloudWatchLogGroupArn"></a>
 The Amazon Resource Number (ARN) of the Cloudwatch Log Group associated with the target table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** EndTime **   <a name="DDB-Type-ImportTableDescription-EndTime"></a>
 The time at which the creation of the table associated with this import task completed.
Type: Timestamp
Required: No

 ** ErrorCount **   <a name="DDB-Type-ImportTableDescription-ErrorCount"></a>
 The number of errors occurred on importing the source file into the target table.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** FailureCode **   <a name="DDB-Type-ImportTableDescription-FailureCode"></a>
 The error code corresponding to the failure that the import job ran into during execution.
Type: String
Required: No

 ** FailureMessage **   <a name="DDB-Type-ImportTableDescription-FailureMessage"></a>
 The error message corresponding to the failure that the import job ran into during execution.
Type: String
Required: No

 ** ImportArn **   <a name="DDB-Type-ImportTableDescription-ImportArn"></a>
 The Amazon Resource Number (ARN) corresponding to the import request.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: No

 ** ImportedItemCount **   <a name="DDB-Type-ImportTableDescription-ImportedItemCount"></a>
 The number of items successfully imported into the new table.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** ImportStatus **   <a name="DDB-Type-ImportTableDescription-ImportStatus"></a>
 The status of the import.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | CANCELLING | CANCELLED | FAILED`
Required: No

 ** InputCompressionType **   <a name="DDB-Type-ImportTableDescription-InputCompressionType"></a>
 The compression options for the data that has been imported into the target table. The values are NONE, GZIP, or ZSTD.
Type: String
Valid Values: `GZIP | ZSTD | NONE`
Required: No

 ** InputFormat **   <a name="DDB-Type-ImportTableDescription-InputFormat"></a>
 The format of the source data going into the target table.
Type: String
Valid Values: `DYNAMODB_JSON | ION | CSV`
Required: No

 ** InputFormatOptions **   <a name="DDB-Type-ImportTableDescription-InputFormatOptions"></a>
 The format options for the data that was imported into the target table. There is one value, CsvOption.
Type: [InputFormatOptions](API_InputFormatOptions.md) object
Required: No

 ** ProcessedItemCount **   <a name="DDB-Type-ImportTableDescription-ProcessedItemCount"></a>
 The total number of items processed from the source file.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** ProcessedSizeBytes **   <a name="DDB-Type-ImportTableDescription-ProcessedSizeBytes"></a>
 The total size of data processed from the source file, in Bytes.
Type: Long
Required: No

 ** S3BucketSource **   <a name="DDB-Type-ImportTableDescription-S3BucketSource"></a>
 Values for the S3 bucket the source file is imported from. Includes bucket name (required), key prefix (optional) and bucket account owner ID (optional).
Type: [S3BucketSource](API_S3BucketSource.md) object
Required: No

 ** StartTime **   <a name="DDB-Type-ImportTableDescription-StartTime"></a>
 The time when this import task started.
Type: Timestamp
Required: No

 ** TableArn **   <a name="DDB-Type-ImportTableDescription-TableArn"></a>
 The Amazon Resource Number (ARN) of the table being imported into.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** TableCreationParameters **   <a name="DDB-Type-ImportTableDescription-TableCreationParameters"></a>
 The parameters for the new table that is being imported into.
Type: [TableCreationParameters](API_TableCreationParameters.md) object
Required: No

 ** TableId **   <a name="DDB-Type-ImportTableDescription-TableId"></a>
 The table id corresponding to the table created by import table process.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## See Also
<a name="API_ImportTableDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ImportTableDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ImportTableDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ImportTableDescription)
