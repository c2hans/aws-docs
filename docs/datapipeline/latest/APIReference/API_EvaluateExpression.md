---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_EvaluateExpression.html
---

# EvaluateExpression
<a name="API_EvaluateExpression"></a>

Task runners call `EvaluateExpression` to evaluate a string in the context of the specified object. For example, a task runner can evaluate SQL queries stored in Amazon S3.

## Request Syntax
<a name="API_EvaluateExpression_RequestSyntax"></a>

```
{
   "expression": "{{string}}",
   "objectId": "{{string}}",
   "pipelineId": "{{string}}"
}
```

## Request Parameters
<a name="API_EvaluateExpression_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [expression](#API_EvaluateExpression_RequestSyntax) **   <a name="DP-EvaluateExpression-request-expression"></a>
The expression to evaluate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20971520.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** [objectId](#API_EvaluateExpression_RequestSyntax) **   <a name="DP-EvaluateExpression-request-objectId"></a>
The ID of the object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

 ** [pipelineId](#API_EvaluateExpression_RequestSyntax) **   <a name="DP-EvaluateExpression-request-pipelineId"></a>
The ID of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

## Response Syntax
<a name="API_EvaluateExpression_ResponseSyntax"></a>

```
{
   "evaluatedExpression": "string"
}
```

## Response Elements
<a name="API_EvaluateExpression_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [evaluatedExpression](#API_EvaluateExpression_ResponseSyntax) **   <a name="DP-EvaluateExpression-response-evaluatedExpression"></a>
The evaluated expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20971520.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

## Errors
<a name="API_EvaluateExpression_Errors"></a>

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

 ** TaskNotFoundException **
The specified task was not found.
 ** message **
Description of the error message.
HTTP Status Code: 400

## Examples
<a name="API_EvaluateExpression_Examples"></a>

### Example
<a name="API_EvaluateExpression_Example_1"></a>

This example illustrates one usage of EvaluateExpression.

#### Sample Request
<a name="API_EvaluateExpression_Example_1_Request"></a>

```

POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: DataPipeline.DescribePipelines
Content-Length: 164
Host: datapipeline.us-east-1.amazonaws.com
X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT
Authorization: AuthParams

{"pipelineId": "df-08785951KAKJEXAMPLE",
        "objectId": "Schedule",
        "expression": "Transform started at #{startDateTime} and finished at #{endDateTime}"}
```

#### Sample Response
<a name="API_EvaluateExpression_Example_1_Response"></a>

```

x-amzn-RequestId: 02870eb7-0736-11e2-af6f-6bc7a6be60d9
Content-Type: application/x-amz-json-1.1
Content-Length: 103
Date: Mon, 12 Nov 2012 17:50:53 GMT

{"evaluatedExpression": "Transform started at 2012-12-12T00:00:00 and finished at 2012-12-21T18:00:00"}
```

## See Also
<a name="API_EvaluateExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datapipeline-2012-10-29/EvaluateExpression)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datapipeline-2012-10-29/EvaluateExpression)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/EvaluateExpression)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datapipeline-2012-10-29/EvaluateExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/EvaluateExpression)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datapipeline-2012-10-29/EvaluateExpression)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datapipeline-2012-10-29/EvaluateExpression)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datapipeline-2012-10-29/EvaluateExpression)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datapipeline-2012-10-29/EvaluateExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/EvaluateExpression)
