---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_GetPipelineDefinition.html
---

# GetPipelineDefinition
<a name="API_GetPipelineDefinition"></a>

Gets the definition of the specified pipeline. You can call `GetPipelineDefinition` to retrieve the pipeline definition that you provided using [PutPipelineDefinition](API_PutPipelineDefinition.md).

## Request Syntax
<a name="API_GetPipelineDefinition_RequestSyntax"></a>

```
{
   "pipelineId": "{{string}}",
   "version": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPipelineDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [pipelineId](#API_GetPipelineDefinition_RequestSyntax) **   <a name="DP-GetPipelineDefinition-request-pipelineId"></a>
The ID of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

 ** [version](#API_GetPipelineDefinition_RequestSyntax) **   <a name="DP-GetPipelineDefinition-request-version"></a>
The version of the pipeline definition to retrieve. Set this parameter to `latest` (default) to use the last definition saved to the pipeline or `active` to use the last definition that was activated.
Type: String
Required: No

## Response Syntax
<a name="API_GetPipelineDefinition_ResponseSyntax"></a>

```
{
   "parameterObjects": [
      {
         "attributes": [
            {
               "key": "string",
               "stringValue": "string"
            }
         ],
         "id": "string"
      }
   ],
   "parameterValues": [
      {
         "id": "string",
         "stringValue": "string"
      }
   ],
   "pipelineObjects": [
      {
         "fields": [
            {
               "key": "string",
               "refValue": "string",
               "stringValue": "string"
            }
         ],
         "id": "string",
         "name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetPipelineDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [parameterObjects](#API_GetPipelineDefinition_ResponseSyntax) **   <a name="DP-GetPipelineDefinition-response-parameterObjects"></a>
The parameter objects used in the pipeline definition.
Type: Array of [ParameterObject](API_ParameterObject.md) objects

 ** [parameterValues](#API_GetPipelineDefinition_ResponseSyntax) **   <a name="DP-GetPipelineDefinition-response-parameterValues"></a>
The parameter values used in the pipeline definition.
Type: Array of [ParameterValue](API_ParameterValue.md) objects

 ** [pipelineObjects](#API_GetPipelineDefinition_ResponseSyntax) **   <a name="DP-GetPipelineDefinition-response-pipelineObjects"></a>
The objects defined in the pipeline.
Type: Array of [PipelineObject](API_PipelineObject.md) objects

## Errors
<a name="API_GetPipelineDefinition_Errors"></a>

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
<a name="API_GetPipelineDefinition_Examples"></a>

### Example
<a name="API_GetPipelineDefinition_Example_1"></a>

This example illustrates one usage of GetPipelineDefinition.

#### Sample Request
<a name="API_GetPipelineDefinition_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: DataPipeline.GetPipelineDefinition
Content-Length: 40
Host: datapipeline.us-east-1.amazonaws.com
X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT
Authorization: AuthParams

{"pipelineId": "df-06372391ZG65EXAMPLE"}
```

#### Sample Response
<a name="API_GetPipelineDefinition_Example_1_Response"></a>

```

x-amzn-RequestId: e28309e5-0776-11e2-8a14-21bb8a1f50ef
Content-Type: application/x-amz-json-1.1
Content-Length: 890
Date: Mon, 12 Nov 2012 17:50:53 GMT

{"pipelineObjects":
  [
    {"fields":
      [
        {"key": "workerGroup",
         "stringValue": "workerGroup"}
      ],
     "id": "Default",
     "name": "Default"},
    {"fields":
      [
        {"key": "startDateTime",
         "stringValue": "2012-09-25T17:00:00"},
        {"key": "type",
         "stringValue": "Schedule"},
        {"key": "period",
         "stringValue": "1 hour"},
        {"key": "endDateTime",
         "stringValue": "2012-09-25T18:00:00"}
      ],
     "id": "Schedule",
     "name": "Schedule"},
    {"fields":
      [
        {"key": "schedule",
         "refValue": "Schedule"},
        {"key": "command",
         "stringValue": "echo hello"},
        {"key": "parent",
         "refValue": "Default"},
        {"key": "type",
         "stringValue": "ShellCommandActivity"}
      ],
     "id": "SayHello",
     "name": "SayHello"}
  ]
}
```

## See Also
<a name="API_GetPipelineDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datapipeline-2012-10-29/GetPipelineDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datapipeline-2012-10-29/GetPipelineDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/GetPipelineDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datapipeline-2012-10-29/GetPipelineDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/GetPipelineDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datapipeline-2012-10-29/GetPipelineDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datapipeline-2012-10-29/GetPipelineDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datapipeline-2012-10-29/GetPipelineDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datapipeline-2012-10-29/GetPipelineDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/GetPipelineDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
