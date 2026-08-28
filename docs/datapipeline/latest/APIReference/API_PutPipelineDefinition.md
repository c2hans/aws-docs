---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_PutPipelineDefinition.html
---

# PutPipelineDefinition
<a name="API_PutPipelineDefinition"></a>

Adds tasks, schedules, and preconditions to the specified pipeline. You can use `PutPipelineDefinition` to populate a new pipeline.

 `PutPipelineDefinition` also validates the configuration as it adds it to the pipeline. Changes to the pipeline are saved unless one of the following validation errors exist in the pipeline.

1. An object is missing a name or identifier field.

1. A string or reference field is empty.

1. The number of objects in the pipeline exceeds the allowed maximum number of objects.

1. The pipeline is in a FINISHED state.

 Pipeline object definitions are passed to the `PutPipelineDefinition` action and returned by the [GetPipelineDefinition](API_GetPipelineDefinition.md) action.

## Request Syntax
<a name="API_PutPipelineDefinition_RequestSyntax"></a>

```
{
   "parameterObjects": [
      {
         "attributes": [
            {
               "key": "{{string}}",
               "stringValue": "{{string}}"
            }
         ],
         "id": "{{string}}"
      }
   ],
   "parameterValues": [
      {
         "id": "{{string}}",
         "stringValue": "{{string}}"
      }
   ],
   "pipelineId": "{{string}}",
   "pipelineObjects": [
      {
         "fields": [
            {
               "key": "{{string}}",
               "refValue": "{{string}}",
               "stringValue": "{{string}}"
            }
         ],
         "id": "{{string}}",
         "name": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_PutPipelineDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [parameterObjects](#API_PutPipelineDefinition_RequestSyntax) **   <a name="DP-PutPipelineDefinition-request-parameterObjects"></a>
The parameter objects used with the pipeline.
Type: Array of [ParameterObject](API_ParameterObject.md) objects
Required: No

 ** [parameterValues](#API_PutPipelineDefinition_RequestSyntax) **   <a name="DP-PutPipelineDefinition-request-parameterValues"></a>
The parameter values used with the pipeline.
Type: Array of [ParameterValue](API_ParameterValue.md) objects
Required: No

 ** [pipelineId](#API_PutPipelineDefinition_RequestSyntax) **   <a name="DP-PutPipelineDefinition-request-pipelineId"></a>
The ID of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

 ** [pipelineObjects](#API_PutPipelineDefinition_RequestSyntax) **   <a name="DP-PutPipelineDefinition-request-pipelineObjects"></a>
The objects that define the pipeline. These objects overwrite the existing pipeline definition.
Type: Array of [PipelineObject](API_PipelineObject.md) objects
Required: Yes

## Response Syntax
<a name="API_PutPipelineDefinition_ResponseSyntax"></a>

```
{
   "errored": boolean,
   "validationErrors": [
      {
         "errors": [ "string" ],
         "id": "string"
      }
   ],
   "validationWarnings": [
      {
         "id": "string",
         "warnings": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_PutPipelineDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errored](#API_PutPipelineDefinition_ResponseSyntax) **   <a name="DP-PutPipelineDefinition-response-errored"></a>
Indicates whether there were validation errors, and the pipeline definition is stored but cannot be activated until you correct the pipeline and call `PutPipelineDefinition` to commit the corrected pipeline.
Type: Boolean

 ** [validationErrors](#API_PutPipelineDefinition_ResponseSyntax) **   <a name="DP-PutPipelineDefinition-response-validationErrors"></a>
The validation errors that are associated with the objects defined in `pipelineObjects`.
Type: Array of [ValidationError](API_ValidationError.md) objects

 ** [validationWarnings](#API_PutPipelineDefinition_ResponseSyntax) **   <a name="DP-PutPipelineDefinition-response-validationWarnings"></a>
The validation warnings that are associated with the objects defined in `pipelineObjects`.
Type: Array of [ValidationWarning](API_ValidationWarning.md) objects

## Errors
<a name="API_PutPipelineDefinition_Errors"></a>

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
<a name="API_PutPipelineDefinition_Examples"></a>

### Example 1
<a name="API_PutPipelineDefinition_Example_1"></a>

 This example sets a valid pipeline configuration and returns success.

#### Sample Request
<a name="API_PutPipelineDefinition_Example_1_Request"></a>

```

POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: DataPipeline.PutPipelineDefinition
Content-Length: 914
Host: datapipeline.us-east-1.amazonaws.com
X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT
Authorization: AuthParams

{"pipelineId": "df-0937003356ZJEXAMPLE",
 "pipelineObjects":
  [
   {"id": "Default",
     "name": "Default",
     "fields":
      [
        {"key": "workerGroup",
         "stringValue": "workerGroup"}
      ]
    },
    {"id": "Schedule",
     "name": "Schedule",
     "fields":
      [
       {"key": "startDateTime",
         "stringValue": "2012-12-12T00:00:00"},
        {"key": "type",
         "stringValue": "Schedule"},
        {"key": "period",
         "stringValue": "1 hour"},
        {"key": "endDateTime",
         "stringValue": "2012-12-21T18:00:00"}
      ]
    },
    {"id": "SayHello",
     "name": "SayHello",
     "fields":
      [
        {"key": "type",
         "stringValue": "ShellCommandActivity"},
        {"key": "command",
         "stringValue": "echo hello"},
        {"key": "parent",
         "refValue": "Default"},
        {"key": "schedule",
         "refValue": "Schedule"}
      ]
    }
  ]
}
```

#### Sample Response
<a name="API_PutPipelineDefinition_Example_1_Response"></a>

```

HTTP/1.1 200
x-amzn-RequestId: f74afc14-0754-11e2-af6f-6bc7a6be60d9
Content-Type: application/x-amz-json-1.1
Content-Length: 18
Date: Mon, 12 Nov 2012 17:50:53 GMT

{"errored": false}
```

### Example 2
<a name="API_PutPipelineDefinition_Example_2"></a>

 This example sets an invalid pipeline configuration (the value for `workerGroup` is an empty string) and returns an error message.

#### Sample Request
<a name="API_PutPipelineDefinition_Example_2_Request"></a>

```

POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: DataPipeline.PutPipelineDefinition
Content-Length: 903
Host: datapipeline.us-east-1.amazonaws.com
X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT
Authorization: AuthParams

{"pipelineId": "df-06372391ZG65EXAMPLE",
 "pipelineObjects":
  [
    {"id": "Default",
     "name": "Default",
     "fields":
      [
        {"key": "workerGroup",
         "stringValue": ""}
      ]
    },
    {"id": "Schedule",
     "name": "Schedule",
     "fields":
      [
       {"key": "startDateTime",
         "stringValue": "2012-09-25T17:00:00"},
        {"key": "type",
         "stringValue": "Schedule"},
        {"key": "period",
         "stringValue": "1 hour"},
        {"key": "endDateTime",
         "stringValue": "2012-09-25T18:00:00"}
      ]
    },
    {"id": "SayHello",
     "name": "SayHello",
     "fields":
      [
        {"key": "type",
         "stringValue": "ShellCommandActivity"},
        {"key": "command",
         "stringValue": "echo hello"},
        {"key": "parent",
         "refValue": "Default"},
        {"key": "schedule",
         "refValue": "Schedule"}

      ]
    }
  ]
}
```

#### Sample Response
<a name="API_PutPipelineDefinition_Example_2_Response"></a>

```

HTTP/1.1 200
x-amzn-RequestId: f74afc14-0754-11e2-af6f-6bc7a6be60d9
Content-Type: application/x-amz-json-1.1
Content-Length: 18
Date: Mon, 12 Nov 2012 17:50:53 GMT

{"__type": "com.amazon.setl.webservice#InvalidRequestException",
 "message": "Pipeline definition has errors: Could not save the pipeline definition due to FATAL errors: [com.amazon.setl.webservice.ValidationError@108d7ea9] Please call Validate to validate your pipeline"}
```

## See Also
<a name="API_PutPipelineDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datapipeline-2012-10-29/PutPipelineDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datapipeline-2012-10-29/PutPipelineDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/PutPipelineDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datapipeline-2012-10-29/PutPipelineDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/PutPipelineDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datapipeline-2012-10-29/PutPipelineDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datapipeline-2012-10-29/PutPipelineDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datapipeline-2012-10-29/PutPipelineDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datapipeline-2012-10-29/PutPipelineDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/PutPipelineDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
