---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeIndex.html
---

# DescribeIndex
<a name="API_DescribeIndex"></a>

Describes a search index.

Requires permission to access the [DescribeIndex](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeIndex_RequestSyntax"></a>

```
GET /indices/{{indexName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeIndex_RequestParameters"></a>

The request uses the following URI parameters.

 ** [indexName](#API_DescribeIndex_RequestSyntax) **   <a name="iot-DescribeIndex-request-uri-indexName"></a>
The index name.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_DescribeIndex_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeIndex_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "indexName": "string",
   "indexStatus": "string",
   "schema": "string"
}
```

## Response Elements
<a name="API_DescribeIndex_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [indexName](#API_DescribeIndex_ResponseSyntax) **   <a name="iot-DescribeIndex-response-indexName"></a>
The index name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [indexStatus](#API_DescribeIndex_ResponseSyntax) **   <a name="iot-DescribeIndex-response-indexStatus"></a>
The index status.
Type: String
Valid Values: `ACTIVE | BUILDING | REBUILDING`

 ** [schema](#API_DescribeIndex_ResponseSyntax) **   <a name="iot-DescribeIndex-response-schema"></a>
Contains a value that specifies the type of indexing performed. Valid values are:
+ REGISTRY – Your thing index contains only registry data.
+ REGISTRY\_AND\_SHADOW - Your thing index contains registry data and shadow data.
+ REGISTRY\_AND\_CONNECTIVITY\_STATUS - Your thing index contains registry data and thing connectivity status data.
+ REGISTRY\_AND\_SHADOW\_AND\_CONNECTIVITY\_STATUS - Your thing index contains registry data, shadow data, and thing connectivity status data.
+ MULTI\_INDEXING\_MODE - Your thing index contains multiple data sources. For more information, see [GetIndexingConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_GetIndexingConfiguration.html).
Type: String

## Errors
<a name="API_DescribeIndex_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

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
<a name="API_DescribeIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeIndex)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeIndex)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeIndex)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeIndex)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeIndex)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeIndex)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeIndex)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeIndex)
