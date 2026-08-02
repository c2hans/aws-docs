---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_DescribePipelines.html
---

# DescribePipelines
<a name="API_DescribePipelines"></a>

Retrieves metadata about one or more pipelines. The information retrieved includes the name of the pipeline, the pipeline identifier, its current state, and the account that owns the pipeline. Using account credentials, you can retrieve metadata about pipelines that you or your users have created. As a user, you can retrieve metadata about only those pipelines for which you have read permissions.

To retrieve the full pipeline definition instead of metadata about the pipeline, call [GetPipelineDefinition](API_GetPipelineDefinition.md).

## Request Syntax
<a name="API_DescribePipelines_RequestSyntax"></a>

```
{
   "pipelineIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribePipelines_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [pipelineIds](#API_DescribePipelines_RequestSyntax) **   <a name="DP-DescribePipelines-request-pipelineIds"></a>
The IDs of the pipelines to describe. You can pass as many as 25 identifiers in a single call. To obtain pipeline IDs, call [ListPipelines](API_ListPipelines.md).
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

## Response Syntax
<a name="API_DescribePipelines_ResponseSyntax"></a>

```
{
   "pipelineDescriptionList": [
      {
         "description": "string",
         "fields": [
            {
               "key": "string",
               "refValue": "string",
               "stringValue": "string"
            }
         ],
         "name": "string",
         "pipelineId": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_DescribePipelines_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [pipelineDescriptionList](#API_DescribePipelines_ResponseSyntax) **   <a name="DP-DescribePipelines-response-pipelineDescriptionList"></a>
An array of descriptions for the specified pipelines.
Type: Array of [PipelineDescription](API_PipelineDescription.md) objects

## Errors
<a name="API_DescribePipelines_Errors"></a>

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
<a name="API_DescribePipelines_Examples"></a>

### Example
<a name="API_DescribePipelines_Example_1"></a>

This example illustrates one usage of DescribePipelines.

#### Sample Request
<a name="API_DescribePipelines_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: DataPipeline.DescribePipelines
Content-Length: 70
Host: datapipeline.us-east-1.amazonaws.com
X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT
Authorization: AuthParams

{"pipelineIds":
  ["df-08785951KAKJEXAMPLE"]
}
```

#### Sample Response
<a name="API_DescribePipelines_Example_1_Response"></a>

```

x-amzn-RequestId: 02870eb7-0736-11e2-af6f-6bc7a6be60d9
Content-Type: application/x-amz-json-1.1
Content-Length: 767
Date: Mon, 12 Nov 2012 17:50:53 GMT

{"pipelineDescriptionList":
  [
    {"description": "This is my first pipeline",
     "fields":
      [
        {"key": "@pipelineState",
         "stringValue": "SCHEDULED"},
        {"key": "description",
         "stringValue": "This is my first pipeline"},
        {"key": "name",
         "stringValue": "myPipeline"},
        {"key": "@creationTime",
         "stringValue": "2012-12-13T01:24:06"},
        {"key": "@id",
         "stringValue": "df-0937003356ZJEXAMPLE"},
        {"key": "@sphere",
         "stringValue": "PIPELINE"},
        {"key": "@version",
         "stringValue": "1"},
        {"key": "@userId",
         "stringValue": "924374875933"},
        {"key": "@accountId",
         "stringValue": "924374875933"},
        {"key": "uniqueId",
         "stringValue": "1234567890"}
      ],
     "name": "myPipeline",
     "pipelineId": "df-0937003356ZJEXAMPLE"}
  ]
}
```

## See Also
<a name="API_DescribePipelines_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datapipeline-2012-10-29/DescribePipelines)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datapipeline-2012-10-29/DescribePipelines)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/DescribePipelines)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datapipeline-2012-10-29/DescribePipelines)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/DescribePipelines)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datapipeline-2012-10-29/DescribePipelines)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datapipeline-2012-10-29/DescribePipelines)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datapipeline-2012-10-29/DescribePipelines)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datapipeline-2012-10-29/DescribePipelines)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/DescribePipelines)
