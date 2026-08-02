---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_CreateTable.html
---

# CreateTable
<a name="API_CreateTable"></a>

Adds a new table to an existing database in your account. In an AWS account, table names must be at least unique within each Region if they are in the same database. You might have identical table names in the same Region if the tables are in separate databases. While creating the table, you must specify the table name, database name, and the retention properties. [Service quotas apply](https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html). See [code sample](https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.create-table.html) for details.

## Request Syntax
<a name="API_CreateTable_RequestSyntax"></a>

```
{
   "DatabaseName": "{{string}}",
   "MagneticStoreWriteProperties": {
      "EnableMagneticStoreWrites": {{boolean}},
      "MagneticStoreRejectedDataLocation": {
         "S3Configuration": {
            "BucketName": "{{string}}",
            "EncryptionOption": "{{string}}",
            "KmsKeyId": "{{string}}",
            "ObjectKeyPrefix": "{{string}}"
         }
      }
   },
   "RetentionProperties": {
      "MagneticStoreRetentionPeriodInDays": {{number}},
      "MemoryStoreRetentionPeriodInHours": {{number}}
   },
   "Schema": {
      "CompositePartitionKey": [
         {
            "EnforcementInRecord": "{{string}}",
            "Name": "{{string}}",
            "Type": "{{string}}"
         }
      ]
   },
   "TableName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateTable_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DatabaseName](#API_CreateTable_RequestSyntax) **   <a name="timestream-CreateTable-request-DatabaseName"></a>
The name of the Timestream database.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [MagneticStoreWriteProperties](#API_CreateTable_RequestSyntax) **   <a name="timestream-CreateTable-request-MagneticStoreWriteProperties"></a>
Contains properties to set on the table when enabling magnetic store writes.
Type: [MagneticStoreWriteProperties](API_MagneticStoreWriteProperties.md) object
Required: No

 ** [RetentionProperties](#API_CreateTable_RequestSyntax) **   <a name="timestream-CreateTable-request-RetentionProperties"></a>
The duration for which your time-series data must be stored in the memory store and the magnetic store.
Type: [RetentionProperties](API_RetentionProperties.md) object
Required: No

 ** [Schema](#API_CreateTable_RequestSyntax) **   <a name="timestream-CreateTable-request-Schema"></a>
 The schema of the table.
Type: [Schema](API_Schema.md) object
Required: No

 ** [TableName](#API_CreateTable_RequestSyntax) **   <a name="timestream-CreateTable-request-TableName"></a>
The name of the Timestream table.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [Tags](#API_CreateTable_RequestSyntax) **   <a name="timestream-CreateTable-request-Tags"></a>
 A list of key-value pairs to label the table.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateTable_ResponseSyntax"></a>

```
{
   "Table": {
      "Arn": "string",
      "CreationTime": number,
      "DatabaseName": "string",
      "LastUpdatedTime": number,
      "MagneticStoreWriteProperties": {
         "EnableMagneticStoreWrites": boolean,
         "MagneticStoreRejectedDataLocation": {
            "S3Configuration": {
               "BucketName": "string",
               "EncryptionOption": "string",
               "KmsKeyId": "string",
               "ObjectKeyPrefix": "string"
            }
         }
      },
      "RetentionProperties": {
         "MagneticStoreRetentionPeriodInDays": number,
         "MemoryStoreRetentionPeriodInHours": number
      },
      "Schema": {
         "CompositePartitionKey": [
            {
               "EnforcementInRecord": "string",
               "Name": "string",
               "Type": "string"
            }
         ]
      },
      "TableName": "string",
      "TableStatus": "string"
   }
}
```

## Response Elements
<a name="API_CreateTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Table](#API_CreateTable_ResponseSyntax) **   <a name="timestream-CreateTable-response-Table"></a>
The newly created Timestream table.
Type: [Table](API_Table.md) object

## Errors
<a name="API_CreateTable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform this action.
HTTP Status Code: 400

 ** ConflictException **
Timestream was unable to process this request because it contains resource that already exists.
HTTP Status Code: 400

 ** InternalServerException **
 Timestream was unable to fully process this request because of an internal server error.
HTTP Status Code: 500

 ** InvalidEndpointException **
The requested endpoint was not valid.
HTTP Status Code: 400

 ** InvalidEndpointException **
The requested endpoint was not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
 The instance quota of resource exceeded for this account.
HTTP Status Code: 400

 ** ThrottlingException **
 Too many requests were made by a user and they exceeded the service quotas. The request was throttled.
HTTP Status Code: 400

 ** ValidationException **
 An invalid or malformed request.
HTTP Status Code: 400

## See Also
<a name="API_CreateTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-write-2018-11-01/CreateTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-write-2018-11-01/CreateTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/CreateTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-write-2018-11-01/CreateTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/CreateTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-write-2018-11-01/CreateTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-write-2018-11-01/CreateTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-write-2018-11-01/CreateTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/timestream-write-2018-11-01/CreateTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/CreateTable)
