---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_SetStatus.html
---

# SetStatus
<a name="API_SetStatus"></a>

Requests that the status of the specified physical or logical pipeline objects be updated in the specified pipeline. This update might not occur immediately, but is eventually consistent. The status that can be set depends on the type of object (for example, DataNode or Activity). You cannot perform this operation on `FINISHED` pipelines and attempting to do so returns `InvalidRequestException`.

## Request Syntax
<a name="API_SetStatus_RequestSyntax"></a>

```
{
   "objectIds": [ "{{string}}" ],
   "pipelineId": "{{string}}",
   "status": "{{string}}"
}
```

## Request Parameters
<a name="API_SetStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [objectIds](#API_SetStatus_RequestSyntax) **   <a name="DP-SetStatus-request-objectIds"></a>
The IDs of the objects. The corresponding objects can be either physical or components, but not a mix of both types.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

 ** [pipelineId](#API_SetStatus_RequestSyntax) **   <a name="DP-SetStatus-request-pipelineId"></a>
The ID of the pipeline that contains the objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

 ** [status](#API_SetStatus_RequestSyntax) **   <a name="DP-SetStatus-request-status"></a>
The status to be set on all the objects specified in `objectIds`. For components, use `PAUSE` or `RESUME`. For instances, use `TRY_CANCEL`, `RERUN`, or `MARK_FINISHED`.
Type: String
Required: Yes

## Response Elements
<a name="API_SetStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SetStatus_Errors"></a>

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
<a name="API_SetStatus_Examples"></a>

### Example
<a name="API_SetStatus_Example_1"></a>

This example illustrates one usage of SetStatus.

#### Sample Request
<a name="API_SetStatus_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: DataPipeline.SetStatus
Content-Length: 100
Host: datapipeline.us-east-1.amazonaws.com
X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT
Authorization: AuthParams

{"pipelineId": "df-0634701J7KEXAMPLE",
 "objectIds":
  ["o-08600941GHJWMBR9E2"],
 "status": "pause"}
```

#### Sample Response
<a name="API_SetStatus_Example_1_Response"></a>

```
x-amzn-RequestId: e83b8ab7-076a-11e2-af6f-6bc7a6be60d9
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Mon, 12 Nov 2012 17:50:53 GMT

Unexpected response: 200, OK, undefined
```

## See Also
<a name="API_SetStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datapipeline-2012-10-29/SetStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datapipeline-2012-10-29/SetStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/SetStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datapipeline-2012-10-29/SetStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/SetStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datapipeline-2012-10-29/SetStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datapipeline-2012-10-29/SetStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datapipeline-2012-10-29/SetStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datapipeline-2012-10-29/SetStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/SetStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
