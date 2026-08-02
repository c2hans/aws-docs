---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeLookupTables.html
---

# DescribeLookupTables
<a name="API_DescribeLookupTables"></a>

Retrieves metadata about lookup tables in your account. You can optionally filter the results by table name prefix. Results are sorted by table name in ascending order.

## Request Syntax
<a name="API_DescribeLookupTables_RequestSyntax"></a>

```
{
   "lookupTableNamePrefix": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeLookupTables_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [lookupTableNamePrefix](#API_DescribeLookupTables_RequestSyntax) **   <a name="CWL-DescribeLookupTables-request-lookupTableNamePrefix"></a>
A prefix to filter lookup tables by name. Only tables whose names start with this prefix are returned. If you don't specify a prefix, all tables in the account and Region are returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_]+$`
Required: No

 ** [maxResults](#API_DescribeLookupTables_RequestSyntax) **   <a name="CWL-DescribeLookupTables-request-maxResults"></a>
The maximum number of lookup tables to return in the response. The default value is 50 and the maximum value is 100.
Type: Integer
Valid Range: Maximum value of 100.
Required: No

 ** [nextToken](#API_DescribeLookupTables_RequestSyntax) **   <a name="CWL-DescribeLookupTables-request-nextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeLookupTables_ResponseSyntax"></a>

```
{
   "lookupTables": [
      {
         "description": "string",
         "kmsKeyId": "string",
         "lastUpdatedTime": number,
         "lookupTableArn": "string",
         "lookupTableName": "string",
         "recordsCount": number,
         "sizeBytes": number,
         "tableFields": [ "string" ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeLookupTables_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lookupTables](#API_DescribeLookupTables_ResponseSyntax) **   <a name="CWL-DescribeLookupTables-response-lookupTables"></a>
An array of structures, where each structure contains metadata about one lookup table.
Type: Array of [LookupTable](API_LookupTable.md) objects

 ** [nextToken](#API_DescribeLookupTables_ResponseSyntax) **   <a name="CWL-DescribeLookupTables-response-nextToken"></a>
The token to use when requesting the next set of items.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeLookupTables_Errors"></a>

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
<a name="API_DescribeLookupTables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DescribeLookupTables)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DescribeLookupTables)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DescribeLookupTables)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DescribeLookupTables)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DescribeLookupTables)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DescribeLookupTables)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DescribeLookupTables)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DescribeLookupTables)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DescribeLookupTables)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DescribeLookupTables)
