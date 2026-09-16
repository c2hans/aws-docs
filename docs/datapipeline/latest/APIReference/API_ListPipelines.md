---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ListPipelines.html
---

# ListPipelines
<a name="API_ListPipelines"></a>

Lists the pipeline identifiers for all active pipelines that you have permission to access.

## Request Syntax
<a name="API_ListPipelines_RequestSyntax"></a>

```
{
   "marker": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPipelines_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [marker](#API_ListPipelines_RequestSyntax) **   <a name="DP-ListPipelines-request-marker"></a>
The starting point for the results to be returned. For the first call, this value should be empty. As long as there are more results, continue to call `ListPipelines` with the marker value from the previous call to retrieve the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListPipelines_ResponseSyntax"></a>

```
{
   "hasMoreResults": boolean,
   "marker": "string",
   "pipelineIdList": [
      {
         "id": "string",
         "name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPipelines_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [hasMoreResults](#API_ListPipelines_ResponseSyntax) **   <a name="DP-ListPipelines-response-hasMoreResults"></a>
Indicates whether there are more results that can be obtained by a subsequent call.
Type: Boolean

 ** [marker](#API_ListPipelines_ResponseSyntax) **   <a name="DP-ListPipelines-response-marker"></a>
The starting point for the next page of results. To view the next page of results, call `ListPipelinesOutput` again with this marker value. If the value is null, there are no more results.
Type: String

 ** [pipelineIdList](#API_ListPipelines_ResponseSyntax) **   <a name="DP-ListPipelines-response-pipelineIdList"></a>
The pipeline identifiers. If you require additional information about the pipelines, you can use these identifiers to call [DescribePipelines](API_DescribePipelines.md) and [GetPipelineDefinition](API_GetPipelineDefinition.md).
Type: Array of [PipelineIdName](API_PipelineIdName.md) objects

## Errors
<a name="API_ListPipelines_Errors"></a>

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

## Examples
<a name="API_ListPipelines_Examples"></a>

### Example
<a name="API_ListPipelines_Example_1"></a>

This example illustrates one usage of ListPipelines.

#### Sample Request
<a name="API_ListPipelines_Example_1_Request"></a>

```

POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: DataPipeline.ListPipelines
Content-Length: 14
Host: datapipeline.us-east-1.amazonaws.com
X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT
Authorization: AuthParams

{}
```

#### Sample Response
<a name="API_ListPipelines_Example_1_Response"></a>

```

Status:
x-amzn-RequestId: b3104dc5-0734-11e2-af6f-6bc7a6be60d9
Content-Type: application/x-amz-json-1.1
Content-Length: 39
Date: Mon, 12 Nov 2012 17:50:53 GMT

{"PipelineIdList":
  [
    {"id": "df-08785951KAKJEXAMPLE",
     "name": "MyPipeline"},
    {"id": "df-08662578ISYEXAMPLE",
     "name": "MySecondPipeline"}
  ]
}
```

## See Also
<a name="API_ListPipelines_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datapipeline-2012-10-29/ListPipelines)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datapipeline-2012-10-29/ListPipelines)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/ListPipelines)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datapipeline-2012-10-29/ListPipelines)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/ListPipelines)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datapipeline-2012-10-29/ListPipelines)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datapipeline-2012-10-29/ListPipelines)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datapipeline-2012-10-29/ListPipelines)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datapipeline-2012-10-29/ListPipelines)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/ListPipelines)
