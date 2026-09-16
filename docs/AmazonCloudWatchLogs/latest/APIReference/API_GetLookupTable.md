---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLookupTable.html
---

# GetLookupTable
<a name="API_GetLookupTable"></a>

Retrieves the full content of a lookup table, including the CSV data.

## Request Syntax
<a name="API_GetLookupTable_RequestSyntax"></a>

```
{
   "lookupTableArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetLookupTable_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [lookupTableArn](#API_GetLookupTable_RequestSyntax) **   <a name="CWL-GetLookupTable-request-lookupTableArn"></a>
The ARN of the lookup table to retrieve.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetLookupTable_ResponseSyntax"></a>

```
{
   "description": "string",
   "kmsKeyId": "string",
   "lastUpdatedTime": number,
   "lookupTableArn": "string",
   "lookupTableName": "string",
   "sizeBytes": number,
   "tableBody": "string"
}
```

## Response Elements
<a name="API_GetLookupTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_GetLookupTable_ResponseSyntax) **   <a name="CWL-GetLookupTable-response-description"></a>
The description of the lookup table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [kmsKeyId](#API_GetLookupTable_ResponseSyntax) **   <a name="CWL-GetLookupTable-response-kmsKeyId"></a>
The ARN of the AWS KMS key used to encrypt the lookup table data, if applicable.
Type: String
Length Constraints: Maximum length of 256.

 ** [lastUpdatedTime](#API_GetLookupTable_ResponseSyntax) **   <a name="CWL-GetLookupTable-response-lastUpdatedTime"></a>
The time when the lookup table was last updated, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`.
Type: Long
Valid Range: Minimum value of 0.

 ** [lookupTableArn](#API_GetLookupTable_ResponseSyntax) **   <a name="CWL-GetLookupTable-response-lookupTableArn"></a>
The ARN of the lookup table.
Type: String

 ** [lookupTableName](#API_GetLookupTable_ResponseSyntax) **   <a name="CWL-GetLookupTable-response-lookupTableName"></a>
The name of the lookup table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_]+$`

 ** [sizeBytes](#API_GetLookupTable_ResponseSyntax) **   <a name="CWL-GetLookupTable-response-sizeBytes"></a>
The size of the lookup table in bytes.
Type: Long
Valid Range: Minimum value of 0.

 ** [tableBody](#API_GetLookupTable_ResponseSyntax) **   <a name="CWL-GetLookupTable-response-tableBody"></a>
The full CSV content of the lookup table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10485760.

## Errors
<a name="API_GetLookupTable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## See Also
<a name="API_GetLookupTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/GetLookupTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/GetLookupTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/GetLookupTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/GetLookupTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/GetLookupTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/GetLookupTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/GetLookupTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/GetLookupTable)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/GetLookupTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/GetLookupTable)
