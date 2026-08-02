---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_ListTables.html
---

# ListTables
<a name="API_ListTables"></a>

Provides a list of tables, along with the name, status, and retention properties of each table. See [code sample](https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.list-table.html) for details.

## Request Syntax
<a name="API_ListTables_RequestSyntax"></a>

```
{
   "DatabaseName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTables_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DatabaseName](#API_ListTables_RequestSyntax) **   <a name="timestream-ListTables-request-DatabaseName"></a>
The name of the Timestream database.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 256.
Required: No

 ** [MaxResults](#API_ListTables_RequestSyntax) **   <a name="timestream-ListTables-request-MaxResults"></a>
The total number of items to return in the output. If the total number of items available is more than the value specified, a NextToken is provided in the output. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** [NextToken](#API_ListTables_RequestSyntax) **   <a name="timestream-ListTables-request-NextToken"></a>
The pagination token. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.
Type: String
Required: No

## Response Syntax
<a name="API_ListTables_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Tables": [
      {
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
   ]
}
```

## Response Elements
<a name="API_ListTables_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTables_ResponseSyntax) **   <a name="timestream-ListTables-response-NextToken"></a>
A token to specify where to start paginating. This is the NextToken from a previously truncated response.
Type: String

 ** [Tables](#API_ListTables_ResponseSyntax) **   <a name="timestream-ListTables-response-Tables"></a>
A list of tables.
Type: Array of [Table](API_Table.md) objects

## Errors
<a name="API_ListTables_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
 Timestream was unable to fully process this request because of an internal server error.
HTTP Status Code: 500

 ** InvalidEndpointException **
The requested endpoint was not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.
HTTP Status Code: 400

 ** ThrottlingException **
 Too many requests were made by a user and they exceeded the service quotas. The request was throttled.
HTTP Status Code: 400

 ** ValidationException **
 An invalid or malformed request.
HTTP Status Code: 400

## See Also
<a name="API_ListTables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-write-2018-11-01/ListTables)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-write-2018-11-01/ListTables)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/ListTables)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-write-2018-11-01/ListTables)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/ListTables)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-write-2018-11-01/ListTables)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-write-2018-11-01/ListTables)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-write-2018-11-01/ListTables)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/timestream-write-2018-11-01/ListTables)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/ListTables)
