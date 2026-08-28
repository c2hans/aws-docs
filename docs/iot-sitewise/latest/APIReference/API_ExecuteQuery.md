---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ExecuteQuery.html
---

# ExecuteQuery
<a name="API_ExecuteQuery"></a>

Run SQL queries to retrieve metadata and time-series data from asset models, assets, measurements, metrics, transforms, and aggregates.

## Request Syntax
<a name="API_ExecuteQuery_RequestSyntax"></a>

```
POST /queries/execution HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "queryStatement": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ExecuteQuery_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ExecuteQuery_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_ExecuteQuery_RequestSyntax) **   <a name="iotsitewise-ExecuteQuery-request-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [maxResults](#API_ExecuteQuery_RequestSyntax) **   <a name="iotsitewise-ExecuteQuery-request-maxResults"></a>
The maximum number of results to return at one time.
+ Minimum is 1
+ Maximum is 20000
+ Default is 20000
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [nextToken](#API_ExecuteQuery_RequestSyntax) **   <a name="iotsitewise-ExecuteQuery-request-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [queryStatement](#API_ExecuteQuery_RequestSyntax) **   <a name="iotsitewise-ExecuteQuery-request-queryStatement"></a>
The AWS IoT SiteWise query statement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Pattern: `^[\s\S]+$`
Required: Yes

## Response Syntax
<a name="API_ExecuteQuery_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "columns": [
      {
         "name": "string",
         "type": {
            "scalarType": "string"
         }
      }
   ],
   "nextToken": "string",
   "rows": [
      {
         "data": [
            {
               "arrayValue": [
                  "Datum"
               ],
               "nullValue": boolean,
               "rowValue": "Row",
               "scalarValue": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_ExecuteQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [columns](#API_ExecuteQuery_ResponseSyntax) **   <a name="iotsitewise-ExecuteQuery-response-columns"></a>
Represents a single column in the query results.
Type: Array of [ColumnInfo](API_ColumnInfo.md) objects

 ** [nextToken](#API_ExecuteQuery_ResponseSyntax) **   <a name="iotsitewise-ExecuteQuery-response-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [rows](#API_ExecuteQuery_ResponseSyntax) **   <a name="iotsitewise-ExecuteQuery-response-rows"></a>
Represents a single row in the query results.
Type: Array of [Row](API_Row.md) objects

## Errors
<a name="API_ExecuteQuery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** QueryTimeoutException **
The query timed out.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The requested service is unavailable.
HTTP Status Code: 503

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

 ** ValidationException **
The validation failed for this query.
HTTP Status Code: 400

## See Also
<a name="API_ExecuteQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/ExecuteQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/ExecuteQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ExecuteQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/ExecuteQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ExecuteQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/ExecuteQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/ExecuteQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/ExecuteQuery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/ExecuteQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ExecuteQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
