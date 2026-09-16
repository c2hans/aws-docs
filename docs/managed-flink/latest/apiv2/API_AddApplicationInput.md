---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_AddApplicationInput.html
---

# AddApplicationInput
<a name="API_AddApplicationInput"></a>

 Adds a streaming source to your SQL-based Kinesis Data Analytics application.

You can add a streaming source when you create an application, or you can use this operation to add a streaming source after you create an application. For more information, see [CreateApplication](API_CreateApplication.md).

Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the [DescribeApplication](API_DescribeApplication.md) operation to find the current application version.

## Request Syntax
<a name="API_AddApplicationInput_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "CurrentApplicationVersionId": {{number}},
   "Input": {
      "InputParallelism": {
         "Count": {{number}}
      },
      "InputProcessingConfiguration": {
         "InputLambdaProcessor": {
            "ResourceARN": "{{string}}"
         }
      },
      "InputSchema": {
         "RecordColumns": [
            {
               "Mapping": "{{string}}",
               "Name": "{{string}}",
               "SqlType": "{{string}}"
            }
         ],
         "RecordEncoding": "{{string}}",
         "RecordFormat": {
            "MappingParameters": {
               "CSVMappingParameters": {
                  "RecordColumnDelimiter": "{{string}}",
                  "RecordRowDelimiter": "{{string}}"
               },
               "JSONMappingParameters": {
                  "RecordRowPath": "{{string}}"
               }
            },
            "RecordFormatType": "{{string}}"
         }
      },
      "KinesisFirehoseInput": {
         "ResourceARN": "{{string}}"
      },
      "KinesisStreamsInput": {
         "ResourceARN": "{{string}}"
      },
      "NamePrefix": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_AddApplicationInput_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_AddApplicationInput_RequestSyntax) **   <a name="APIReference-AddApplicationInput-request-ApplicationName"></a>
The name of your existing application to which you want to add the streaming source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [CurrentApplicationVersionId](#API_AddApplicationInput_RequestSyntax) **   <a name="APIReference-AddApplicationInput-request-CurrentApplicationVersionId"></a>
The current version of your application. You must provide the `ApplicationVersionID` or the `ConditionalToken`.You can use the [DescribeApplication](API_DescribeApplication.md) operation to find the current application version.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: Yes

 ** [Input](#API_AddApplicationInput_RequestSyntax) **   <a name="APIReference-AddApplicationInput-request-Input"></a>
The [Input](API_Input.md) to add.
Type: [Input](API_Input.md) object
Required: Yes

## Response Syntax
<a name="API_AddApplicationInput_ResponseSyntax"></a>

```
{
   "ApplicationARN": "string",
   "ApplicationVersionId": number,
   "InputDescriptions": [
      {
         "InAppStreamNames": [ "string" ],
         "InputId": "string",
         "InputParallelism": {
            "Count": number
         },
         "InputProcessingConfigurationDescription": {
            "InputLambdaProcessorDescription": {
               "ResourceARN": "string",
               "RoleARN": "string"
            }
         },
         "InputSchema": {
            "RecordColumns": [
               {
                  "Mapping": "string",
                  "Name": "string",
                  "SqlType": "string"
               }
            ],
            "RecordEncoding": "string",
            "RecordFormat": {
               "MappingParameters": {
                  "CSVMappingParameters": {
                     "RecordColumnDelimiter": "string",
                     "RecordRowDelimiter": "string"
                  },
                  "JSONMappingParameters": {
                     "RecordRowPath": "string"
                  }
               },
               "RecordFormatType": "string"
            }
         },
         "InputStartingPositionConfiguration": {
            "InputStartingPosition": "string"
         },
         "KinesisFirehoseInputDescription": {
            "ResourceARN": "string",
            "RoleARN": "string"
         },
         "KinesisStreamsInputDescription": {
            "ResourceARN": "string",
            "RoleARN": "string"
         },
         "NamePrefix": "string"
      }
   ]
}
```

## Response Elements
<a name="API_AddApplicationInput_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationARN](#API_AddApplicationInput_ResponseSyntax) **   <a name="APIReference-AddApplicationInput-response-ApplicationARN"></a>
The Amazon Resource Name (ARN) of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`

 ** [ApplicationVersionId](#API_AddApplicationInput_ResponseSyntax) **   <a name="APIReference-AddApplicationInput-response-ApplicationVersionId"></a>
Provides the current application version.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.

 ** [InputDescriptions](#API_AddApplicationInput_ResponseSyntax) **   <a name="APIReference-AddApplicationInput-response-InputDescriptions"></a>
Describes the application input configuration.
Type: Array of [InputDescription](API_InputDescription.md) objects

## Errors
<a name="API_AddApplicationInput_Errors"></a>

 ** CodeValidationException **
The user-provided application code (query) is not valid. This can be a simple syntax error.
HTTP Status Code: 400

 ** ConcurrentModificationException **
Exception thrown as a result of concurrent modifications to an application. This error can be the result of attempting to modify an application without using the current application ID.
HTTP Status Code: 400

 ** InvalidArgumentException **
The specified input parameter value is not valid.
HTTP Status Code: 400

 ** InvalidRequestException **
The request JSON is not valid for the operation.
HTTP Status Code: 400

 ** ResourceInUseException **
The application is not available for this operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Specified application can't be found.
HTTP Status Code: 400

## See Also
<a name="API_AddApplicationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/AddApplicationInput)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/AddApplicationInput)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/AddApplicationInput)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/AddApplicationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/AddApplicationInput)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/AddApplicationInput)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/AddApplicationInput)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/AddApplicationInput)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/AddApplicationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/AddApplicationInput)
