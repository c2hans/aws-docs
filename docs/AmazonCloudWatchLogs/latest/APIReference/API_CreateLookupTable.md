---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLookupTable.html
---

# CreateLookupTable
<a name="API_CreateLookupTable"></a>

Creates a lookup table by uploading CSV data or from CloudWatch Logs query results. You can use lookup tables to enrich log data in CloudWatch Logs queries with reference data such as user details, application names, or error descriptions.

The table name must be unique within your account and Region. You must specify either `tableBody` or `queryId`, but not both. If you use `tableBody`, the CSV content must include a header row with column names, use UTF-8 encoding, and not exceed 10 MB.

## Request Syntax
<a name="API_CreateLookupTable_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "kmsKeyId": "{{string}}",
   "lookupTableName": "{{string}}",
   "queryId": "{{string}}",
   "tableBody": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateLookupTable_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_CreateLookupTable_RequestSyntax) **   <a name="CWL-CreateLookupTable-request-description"></a>
A description of the lookup table. The description can be up to 1024 characters long.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [kmsKeyId](#API_CreateLookupTable_RequestSyntax) **   <a name="CWL-CreateLookupTable-request-kmsKeyId"></a>
The ARN of the AWS KMS key to use to encrypt the lookup table data. If you don't specify a key, the data is encrypted with an AWS-owned key.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [lookupTableName](#API_CreateLookupTable_RequestSyntax) **   <a name="CWL-CreateLookupTable-request-lookupTableName"></a>
The name of the lookup table. The name must be unique within your account and Region. The name can contain only alphanumeric characters and underscores, and can be up to 256 characters long.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_]+$`
Required: Yes

 ** [queryId](#API_CreateLookupTable_RequestSyntax) **   <a name="CWL-CreateLookupTable-request-queryId"></a>
The ID of a completed or cancelled CloudWatch Logs query whose results populate the lookup table. A cancelled query populates the table with the partial results that were available when the query was stopped.
You must specify either `tableBody` or `queryId`, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [tableBody](#API_CreateLookupTable_RequestSyntax) **   <a name="CWL-CreateLookupTable-request-tableBody"></a>
The CSV content of the lookup table. The first row must be a header row with column names. The content must use UTF-8 encoding and not exceed 10 MB.
You must specify either `tableBody` or `queryId`, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10485760.
Required: No

 ** [tags](#API_CreateLookupTable_RequestSyntax) **   <a name="CWL-CreateLookupTable-request-tags"></a>
A list of key-value pairs to associate with the lookup table. You can associate as many as 50 tags with a lookup table. Tags can help you organize and categorize your resources.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_CreateLookupTable_ResponseSyntax"></a>

```
{
   "createdAt": number,
   "lookupTableArn": "string"
}
```

## Response Elements
<a name="API_CreateLookupTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateLookupTable_ResponseSyntax) **   <a name="CWL-CreateLookupTable-response-createdAt"></a>
The time when the lookup table was created, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`.
Type: Long
Valid Range: Minimum value of 0.

 ** [lookupTableArn](#API_CreateLookupTable_ResponseSyntax) **   <a name="CWL-CreateLookupTable-response-lookupTableArn"></a>
The ARN of the lookup table that was created.
Type: String

## Errors
<a name="API_CreateLookupTable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** LimitExceededException **
You have reached the maximum number of resources that can be created.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The specified resource already exists.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

 ** ValidationException **
One of the parameters for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_CreateLookupTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/CreateLookupTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/CreateLookupTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/CreateLookupTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/CreateLookupTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/CreateLookupTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/CreateLookupTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/CreateLookupTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/CreateLookupTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/CreateLookupTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/CreateLookupTable)
