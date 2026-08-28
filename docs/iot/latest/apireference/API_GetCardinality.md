---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_GetCardinality.html
---

# GetCardinality
<a name="API_GetCardinality"></a>

Returns the approximate count of unique values that match the query.

Requires permission to access the [GetCardinality](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_GetCardinality_RequestSyntax"></a>

```
POST /indices/cardinality HTTP/1.1
Content-type: application/json

{
   "aggregationField": "{{string}}",
   "indexName": "{{string}}",
   "queryString": "{{string}}",
   "queryVersion": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetCardinality_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetCardinality_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [aggregationField](#API_GetCardinality_RequestSyntax) **   <a name="iot-GetCardinality-request-aggregationField"></a>
The field to aggregate.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [indexName](#API_GetCardinality_RequestSyntax) **   <a name="iot-GetCardinality-request-indexName"></a>
The name of the index to search.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** [queryString](#API_GetCardinality_RequestSyntax) **   <a name="iot-GetCardinality-request-queryString"></a>
The search query string.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [queryVersion](#API_GetCardinality_RequestSyntax) **   <a name="iot-GetCardinality-request-queryVersion"></a>
The query version.
Type: String
Required: No

## Response Syntax
<a name="API_GetCardinality_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "cardinality": number
}
```

## Response Elements
<a name="API_GetCardinality_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cardinality](#API_GetCardinality_ResponseSyntax) **   <a name="iot-GetCardinality-response-cardinality"></a>
The approximate count of unique values that match the query.
Type: Integer

## Errors
<a name="API_GetCardinality_Errors"></a>

 ** IndexNotReadyException **
The index is not ready.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidAggregationException **
The aggregation is invalid.
HTTP Status Code: 400

 ** InvalidQueryException **
The query is invalid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_GetCardinality_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/GetCardinality)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/GetCardinality)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/GetCardinality)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/GetCardinality)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/GetCardinality)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/GetCardinality)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/GetCardinality)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/GetCardinality)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/GetCardinality)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/GetCardinality)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
