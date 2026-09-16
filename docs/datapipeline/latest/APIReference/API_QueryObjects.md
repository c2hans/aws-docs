---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_QueryObjects.html
---

# QueryObjects
<a name="API_QueryObjects"></a>

Queries the specified pipeline for the names of objects that match the specified set of conditions.

## Request Syntax
<a name="API_QueryObjects_RequestSyntax"></a>

```
{
   "limit": {{number}},
   "marker": "{{string}}",
   "pipelineId": "{{string}}",
   "query": {
      "selectors": [
         {
            "fieldName": "{{string}}",
            "operator": {
               "type": "{{string}}",
               "values": [ "{{string}}" ]
            }
         }
      ]
   },
   "sphere": "{{string}}"
}
```

## Request Parameters
<a name="API_QueryObjects_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [limit](#API_QueryObjects_RequestSyntax) **   <a name="DP-QueryObjects-request-limit"></a>
The maximum number of object names that `QueryObjects` will return in a single call. The default value is 100.
Type: Integer
Required: No

 ** [marker](#API_QueryObjects_RequestSyntax) **   <a name="DP-QueryObjects-request-marker"></a>
The starting point for the results to be returned. For the first call, this value should be empty. As long as there are more results, continue to call `QueryObjects` with the marker value from the previous call to retrieve the next set of results.
Type: String
Required: No

 ** [pipelineId](#API_QueryObjects_RequestSyntax) **   <a name="DP-QueryObjects-request-pipelineId"></a>
The ID of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

 ** [query](#API_QueryObjects_RequestSyntax) **   <a name="DP-QueryObjects-request-query"></a>
The query that defines the objects to be returned. The `Query` object can contain a maximum of ten selectors. The conditions in the query are limited to top-level String fields in the object. These filters can be applied to components, instances, and attempts.
Type: [Query](API_Query.md) object
Required: No

 ** [sphere](#API_QueryObjects_RequestSyntax) **   <a name="DP-QueryObjects-request-sphere"></a>
Indicates whether the query applies to components or instances. The possible values are: `COMPONENT`, `INSTANCE`, and `ATTEMPT`.
Type: String
Required: Yes

## Response Syntax
<a name="API_QueryObjects_ResponseSyntax"></a>

```
{
   "hasMoreResults": boolean,
   "ids": [ "string" ],
   "marker": "string"
}
```

## Response Elements
<a name="API_QueryObjects_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [hasMoreResults](#API_QueryObjects_ResponseSyntax) **   <a name="DP-QueryObjects-response-hasMoreResults"></a>
Indicates whether there are more results that can be obtained by a subsequent call.
Type: Boolean

 ** [ids](#API_QueryObjects_ResponseSyntax) **   <a name="DP-QueryObjects-response-ids"></a>
The identifiers that match the query selectors.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`

 ** [marker](#API_QueryObjects_ResponseSyntax) **   <a name="DP-QueryObjects-response-marker"></a>
The starting point for the next page of results. To view the next page of results, call `QueryObjects` again with this marker value. If the value is null, there are no more results.
Type: String

## Errors
<a name="API_QueryObjects_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
An internal service error occurred.
 ** message **
Description of the error message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.
 ** message **
Description of the error message.
HTTP Status Code: 400

 ** PipelineDeletedException **
The specified pipeline has been deleted.
 ** message **
Description of the error message.
HTTP Status Code: 400

 ** PipelineNotFoundException **
The specified pipeline was not found. Verify that you used the correct user and account identifiers.
 ** message **
Description of the error message.
HTTP Status Code: 400

## Examples
<a name="API_QueryObjects_Examples"></a>

### Example
<a name="API_QueryObjects_Example_1"></a>

This example illustrates one usage of QueryObjects.

#### Sample Request
<a name="API_QueryObjects_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: DataPipeline.QueryObjects
Content-Length: 123
Host: datapipeline.us-east-1.amazonaws.com
X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT
Authorization: AuthParams

{"pipelineId": "df-06372391ZG65EXAMPLE",
 "query":
  {"selectors":
    [
    ]
  },
 "sphere": "INSTANCE",
 "marker": "",
 "limit": 10}
```

#### Sample Response
<a name="API_QueryObjects_Example_1_Response"></a>

```
x-amzn-RequestId: 14d704c1-0775-11e2-af6f-6bc7a6be60d9
Content-Type: application/x-amz-json-1.1
Content-Length: 72
Date: Mon, 12 Nov 2012 17:50:53 GMT

{"hasMoreResults": false,
 "ids":
  ["@SayHello_1_2012-09-25T17:00:00"]
}
```

## See Also
<a name="API_QueryObjects_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datapipeline-2012-10-29/QueryObjects)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datapipeline-2012-10-29/QueryObjects)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/QueryObjects)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datapipeline-2012-10-29/QueryObjects)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/QueryObjects)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datapipeline-2012-10-29/QueryObjects)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datapipeline-2012-10-29/QueryObjects)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datapipeline-2012-10-29/QueryObjects)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datapipeline-2012-10-29/QueryObjects)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/QueryObjects)
