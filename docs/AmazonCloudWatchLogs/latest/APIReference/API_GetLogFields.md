---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogFields.html
---

# GetLogFields
<a name="API_GetLogFields"></a>

Discovers available fields for a specific data source and type. The response includes any field modifications introduced through pipelines, such as new fields or changed field types.

## Request Syntax
<a name="API_GetLogFields_RequestSyntax"></a>

```
{
   "dataSourceName": "{{string}}",
   "dataSourceType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetLogFields_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [dataSourceName](#API_GetLogFields_RequestSyntax) **   <a name="CWL-GetLogFields-request-dataSourceName"></a>
The name of the data source to retrieve log fields for.
Type: String
Required: Yes

 ** [dataSourceType](#API_GetLogFields_RequestSyntax) **   <a name="CWL-GetLogFields-request-dataSourceType"></a>
The type of the data source to retrieve log fields for.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetLogFields_ResponseSyntax"></a>

```
{
   "logFields": [
      {
         "logFieldName": "string",
         "logFieldType": {
            "element": "LogFieldType",
            "fields": [
               "LogFieldsListItem"
            ],
            "type": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_GetLogFields_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [logFields](#API_GetLogFields_ResponseSyntax) **   <a name="CWL-GetLogFields-response-logFields"></a>
The list of log fields for the specified data source, including field names and their data types.
Type: Array of [LogFieldsListItem](API_LogFieldsListItem.md) objects

## Errors
<a name="API_GetLogFields_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** OperationAbortedException **
Multiple concurrent requests to update the same resource were in conflict.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## See Also
<a name="API_GetLogFields_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/GetLogFields)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/GetLogFields)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/GetLogFields)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/GetLogFields)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/GetLogFields)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/GetLogFields)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/GetLogFields)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/GetLogFields)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/GetLogFields)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/GetLogFields)
