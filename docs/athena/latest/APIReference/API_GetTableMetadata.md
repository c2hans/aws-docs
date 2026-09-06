---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_GetTableMetadata.html
---

# GetTableMetadata
<a name="API_GetTableMetadata"></a>

Returns table metadata for the specified catalog, database, and table.

## Request Syntax
<a name="API_GetTableMetadata_RequestSyntax"></a>

```
{
   "CatalogName": "{{string}}",
   "DatabaseName": "{{string}}",
   "TableName": "{{string}}",
   "WorkGroup": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTableMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogName](#API_GetTableMetadata_RequestSyntax) **   <a name="athena-GetTableMetadata-request-CatalogName"></a>
The name of the data catalog that contains the database and table metadata to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [DatabaseName](#API_GetTableMetadata_RequestSyntax) **   <a name="athena-GetTableMetadata-request-DatabaseName"></a>
The name of the database that contains the table metadata to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [TableName](#API_GetTableMetadata_RequestSyntax) **   <a name="athena-GetTableMetadata-request-TableName"></a>
The name of the table for which metadata is returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [WorkGroup](#API_GetTableMetadata_RequestSyntax) **   <a name="athena-GetTableMetadata-request-WorkGroup"></a>
The name of the workgroup for which the metadata is being fetched. Required if requesting an IAM Identity Center enabled AWS Glue Data Catalog.
Type: String
Pattern: `[a-zA-Z0-9._-]{1,128}`
Required: No

## Response Syntax
<a name="API_GetTableMetadata_ResponseSyntax"></a>

```
{
   "TableMetadata": {
      "Columns": [
         {
            "Comment": "string",
            "Name": "string",
            "Type": "string"
         }
      ],
      "CreateTime": number,
      "LastAccessTime": number,
      "Name": "string",
      "Parameters": {
         "string" : "string"
      },
      "PartitionKeys": [
         {
            "Comment": "string",
            "Name": "string",
            "Type": "string"
         }
      ],
      "TableType": "string"
   }
}
```

## Response Elements
<a name="API_GetTableMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TableMetadata](#API_GetTableMetadata_ResponseSyntax) **   <a name="athena-GetTableMetadata-response-TableMetadata"></a>
An object that contains table metadata.
Type: [TableMetadata](API_TableMetadata.md) object

## Errors
<a name="API_GetTableMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

 ** MetadataException **
An exception that Athena received when it called a custom metastore. Occurs if the error is not caused by user input (`InvalidRequestException`) or from the Athena platform (`InternalServerException`). For example, if a user-created Lambda function is missing permissions, the Lambda `4XX` exception is returned in a `MetadataException`.
HTTP Status Code: 400

## See Also
<a name="API_GetTableMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/GetTableMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/GetTableMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/GetTableMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/GetTableMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/GetTableMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/GetTableMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/GetTableMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/GetTableMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetTableMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/GetTableMetadata)
