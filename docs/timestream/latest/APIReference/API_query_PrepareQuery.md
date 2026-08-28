---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_PrepareQuery.html
---

# PrepareQuery
<a name="API_query_PrepareQuery"></a>

A synchronous operation that allows you to submit a query with parameters to be stored by Timestream for later running. Timestream only supports using this operation with `ValidateOnly` set to `true`.

## Request Syntax
<a name="API_query_PrepareQuery_RequestSyntax"></a>

```
{
   "QueryString": "{{string}}",
   "ValidateOnly": {{boolean}}
}
```

## Request Parameters
<a name="API_query_PrepareQuery_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [QueryString](#API_query_PrepareQuery_RequestSyntax) **   <a name="timestream-query_PrepareQuery-request-QueryString"></a>
The Timestream query string that you want to use as a prepared statement. Parameter names can be specified in the query string `@` character followed by an identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Required: Yes

 ** [ValidateOnly](#API_query_PrepareQuery_RequestSyntax) **   <a name="timestream-query_PrepareQuery-request-ValidateOnly"></a>
By setting this value to `true`, Timestream will only validate that the query string is a valid Timestream query, and not store the prepared query for later use.
Type: Boolean
Required: No

## Response Syntax
<a name="API_query_PrepareQuery_ResponseSyntax"></a>

```
{
   "Columns": [
      {
         "Aliased": boolean,
         "DatabaseName": "string",
         "Name": "string",
         "TableName": "string",
         "Type": {
            "ArrayColumnInfo": {
               "Name": "string",
               "Type": "Type"
            },
            "RowColumnInfo": [
               {
                  "Name": "string",
                  "Type": "Type"
               }
            ],
            "ScalarType": "string",
            "TimeSeriesMeasureValueColumnInfo": {
               "Name": "string",
               "Type": "Type"
            }
         }
      }
   ],
   "Parameters": [
      {
         "Name": "string",
         "Type": {
            "ArrayColumnInfo": {
               "Name": "string",
               "Type": "Type"
            },
            "RowColumnInfo": [
               {
                  "Name": "string",
                  "Type": "Type"
               }
            ],
            "ScalarType": "string",
            "TimeSeriesMeasureValueColumnInfo": {
               "Name": "string",
               "Type": "Type"
            }
         }
      }
   ],
   "QueryString": "string"
}
```

## Response Elements
<a name="API_query_PrepareQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Columns](#API_query_PrepareQuery_ResponseSyntax) **   <a name="timestream-query_PrepareQuery-response-Columns"></a>
A list of SELECT clause columns of the submitted query string.
Type: Array of [SelectColumn](API_query_SelectColumn.md) objects

 ** [Parameters](#API_query_PrepareQuery_ResponseSyntax) **   <a name="timestream-query_PrepareQuery-response-Parameters"></a>
A list of parameters used in the submitted query string.
Type: Array of [ParameterMapping](API_query_ParameterMapping.md) objects

 ** [QueryString](#API_query_PrepareQuery_ResponseSyntax) **   <a name="timestream-query_PrepareQuery-response-QueryString"></a>
The query string that you want prepare.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.

## Errors
<a name="API_query_PrepareQuery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have the necessary permissions to access the account settings.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request.
HTTP Status Code: 400

 ** InvalidEndpointException **
The requested endpoint is invalid.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled due to excessive requests.
HTTP Status Code: 400

 ** ValidationException **
 Invalid or malformed request.
HTTP Status Code: 400

## See Also
<a name="API_query_PrepareQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-query-2018-11-01/PrepareQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-query-2018-11-01/PrepareQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/PrepareQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-query-2018-11-01/PrepareQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/PrepareQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-query-2018-11-01/PrepareQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-query-2018-11-01/PrepareQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-query-2018-11-01/PrepareQuery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/timestream-query-2018-11-01/PrepareQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/PrepareQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
