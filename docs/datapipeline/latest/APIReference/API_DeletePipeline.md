---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_DeletePipeline.html
---

# DeletePipeline
<a name="API_DeletePipeline"></a>

Deletes a pipeline, its pipeline definition, and its run history. AWS Data Pipeline attempts to cancel instances associated with the pipeline that are currently being processed by task runners.

Deleting a pipeline cannot be undone. You cannot query or restore a deleted pipeline. To temporarily pause a pipeline instead of deleting it, call [SetStatus](API_SetStatus.md) with the status set to `PAUSE` on individual components. Components that are paused by [SetStatus](API_SetStatus.md) can be resumed.

## Request Syntax
<a name="API_DeletePipeline_RequestSyntax"></a>

```
{
   "pipelineId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeletePipeline_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [pipelineId](#API_DeletePipeline_RequestSyntax) **   <a name="DP-DeletePipeline-request-pipelineId"></a>
The ID of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

## Response Elements
<a name="API_DeletePipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeletePipeline_Errors"></a>

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

 ** PipelineNotFoundException **
The specified pipeline was not found. Verify that you used the correct user and account identifiers.
 ** message **
Description of the error message.
HTTP Status Code: 400

## Examples
<a name="API_DeletePipeline_Examples"></a>

### Example
<a name="API_DeletePipeline_Example_1"></a>

This example illustrates one usage of DeletePipeline.

#### Sample Request
<a name="API_DeletePipeline_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: DataPipeline.DeletePipeline
Content-Length: 50
Host: datapipeline.us-east-1.amazonaws.com
X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT
Authorization: AuthParams

{"pipelineId": "df-06372391ZG65EXAMPLE"}
```

#### Sample Response
<a name="API_DeletePipeline_Example_1_Response"></a>

```

x-amzn-RequestId: b7a88c81-0754-11e2-af6f-6bc7a6be60d9
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Mon, 12 Nov 2012 17:50:53 GMT

Unexpected response: 200, OK, undefined
```

## See Also
<a name="API_DeletePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datapipeline-2012-10-29/DeletePipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datapipeline-2012-10-29/DeletePipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/DeletePipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datapipeline-2012-10-29/DeletePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/DeletePipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datapipeline-2012-10-29/DeletePipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datapipeline-2012-10-29/DeletePipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datapipeline-2012-10-29/DeletePipeline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datapipeline-2012-10-29/DeletePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/DeletePipeline)
