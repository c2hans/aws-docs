---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ValidatePipelineDefinition.html
---

# ValidatePipelineDefinition
<a name="API_ValidatePipelineDefinition"></a>

Validates the specified pipeline definition to ensure that it is well formed and can be run without error.

## Request Syntax
<a name="API_ValidatePipelineDefinition_RequestSyntax"></a>

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
<a name="API_ValidatePipelineDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [parameterObjects](#API_ValidatePipelineDefinition_RequestSyntax) **   <a name="DP-ValidatePipelineDefinition-request-parameterObjects"></a>
The parameter objects used with the pipeline.
Type: Array of [ParameterObject](API_ParameterObject.md) objects
Required: No

 ** [parameterValues](#API_ValidatePipelineDefinition_RequestSyntax) **   <a name="DP-ValidatePipelineDefinition-request-parameterValues"></a>
The parameter values used with the pipeline.
Type: Array of [ParameterValue](API_ParameterValue.md) objects
Required: No

 ** [pipelineId](#API_ValidatePipelineDefinition_RequestSyntax) **   <a name="DP-ValidatePipelineDefinition-request-pipelineId"></a>
The ID of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

 ** [pipelineObjects](#API_ValidatePipelineDefinition_RequestSyntax) **   <a name="DP-ValidatePipelineDefinition-request-pipelineObjects"></a>
The objects that define the pipeline changes to validate against the pipeline.
Type: Array of [PipelineObject](API_PipelineObject.md) objects
Required: Yes

## Response Syntax
<a name="API_ValidatePipelineDefinition_ResponseSyntax"></a>

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
<a name="API_ValidatePipelineDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errored](#API_ValidatePipelineDefinition_ResponseSyntax) **   <a name="DP-ValidatePipelineDefinition-response-errored"></a>
Indicates whether there were validation errors.
Type: Boolean

 ** [validationErrors](#API_ValidatePipelineDefinition_ResponseSyntax) **   <a name="DP-ValidatePipelineDefinition-response-validationErrors"></a>
Any validation errors that were found.
Type: Array of [ValidationError](API_ValidationError.md) objects

 ** [validationWarnings](#API_ValidatePipelineDefinition_ResponseSyntax) **   <a name="DP-ValidatePipelineDefinition-response-validationWarnings"></a>
Any validation warnings that were found.
Type: Array of [ValidationWarning](API_ValidationWarning.md) objects

## Errors
<a name="API_ValidatePipelineDefinition_Errors"></a>

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
<a name="API_ValidatePipelineDefinition_Examples"></a>

### Example 1
<a name="API_ValidatePipelineDefinition_Example_1"></a>

 This example sets an valid pipeline configuration and returns success.

#### Sample Request
<a name="API_ValidatePipelineDefinition_Example_1_Request"></a>

```

POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: DataPipeline.ValidatePipelineDefinition
Content-Length: 936
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
         "stringValue": "MyworkerGroup"}
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
<a name="API_ValidatePipelineDefinition_Example_1_Response"></a>

```

x-amzn-RequestId: 92c9f347-0776-11e2-8a14-21bb8a1f50ef
Content-Type: application/x-amz-json-1.1
Content-Length: 18
Date: Mon, 12 Nov 2012 17:50:53 GMT

{"errored": false}
```

### Example 2
<a name="API_ValidatePipelineDefinition_Example_2"></a>

 This example sets an invalid pipeline configuration and returns the associated set of validation errors.

#### Sample Request
<a name="API_ValidatePipelineDefinition_Example_2_Request"></a>

```

POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: DataPipeline.ValidatePipelineDefinition
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
         "stringValue": "MyworkerGroup"}
      ]
    },
    {"id": "Schedule",
     "name": "Schedule",
     "fields":
      [
       {"key": "startDateTime",
         "stringValue": "bad-time"},
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
<a name="API_ValidatePipelineDefinition_Example_2_Response"></a>

```

x-amzn-RequestId: 496a1f5a-0e6a-11e2-a61c-bd6312c92ddd
Content-Type: application/x-amz-json-1.1
Content-Length: 278
Date: Mon, 12 Nov 2012 17:50:53 GMT

{"errored": true,
 "validationErrors":
  [
    {"errors":
      ["INVALID_FIELD_VALUE:  'startDateTime' value must be a literal datetime value."],
     "id": "Schedule"}
  ]
}
```

## See Also
<a name="API_ValidatePipelineDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datapipeline-2012-10-29/ValidatePipelineDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datapipeline-2012-10-29/ValidatePipelineDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/ValidatePipelineDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datapipeline-2012-10-29/ValidatePipelineDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/ValidatePipelineDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datapipeline-2012-10-29/ValidatePipelineDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datapipeline-2012-10-29/ValidatePipelineDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datapipeline-2012-10-29/ValidatePipelineDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datapipeline-2012-10-29/ValidatePipelineDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/ValidatePipelineDefinition)
