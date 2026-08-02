---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_AddApplicationOutput.html
---

# AddApplicationOutput
<a name="API_AddApplicationOutput"></a>

Adds an external destination to your SQL-based Kinesis Data Analytics application.

If you want Kinesis Data Analytics to deliver data from an in-application stream within your application to an external destination (such as an Kinesis data stream, a Kinesis Data Firehose delivery stream, or an Amazon Lambda function), you add the relevant configuration to your application using this operation. You can configure one or more outputs for your application. Each output configuration maps an in-application stream and an external destination.

 You can use one of the output configurations to deliver data from your in-application error stream to an external destination so that you can analyze the errors.

 Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the [DescribeApplication](API_DescribeApplication.md) operation to find the current application version.

## Request Syntax
<a name="API_AddApplicationOutput_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "CurrentApplicationVersionId": {{number}},
   "Output": {
      "DestinationSchema": {
         "RecordFormatType": "{{string}}"
      },
      "KinesisFirehoseOutput": {
         "ResourceARN": "{{string}}"
      },
      "KinesisStreamsOutput": {
         "ResourceARN": "{{string}}"
      },
      "LambdaOutput": {
         "ResourceARN": "{{string}}"
      },
      "Name": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_AddApplicationOutput_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_AddApplicationOutput_RequestSyntax) **   <a name="APIReference-AddApplicationOutput-request-ApplicationName"></a>
The name of the application to which you want to add the output configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [CurrentApplicationVersionId](#API_AddApplicationOutput_RequestSyntax) **   <a name="APIReference-AddApplicationOutput-request-CurrentApplicationVersionId"></a>
The version of the application to which you want to add the output configuration. You can use the [DescribeApplication](API_DescribeApplication.md) operation to get the current application version. If the version specified is not the current version, the `ConcurrentModificationException` is returned.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: Yes

 ** [Output](#API_AddApplicationOutput_RequestSyntax) **   <a name="APIReference-AddApplicationOutput-request-Output"></a>
An array of objects, each describing one output configuration. In the output configuration, you specify the name of an in-application stream, a destination (that is, a Kinesis data stream, a Kinesis Data Firehose delivery stream, or an Amazon Lambda function), and record the formation to use when writing to the destination.
Type: [Output](API_Output.md) object
Required: Yes

## Response Syntax
<a name="API_AddApplicationOutput_ResponseSyntax"></a>

```
{
   "ApplicationARN": "string",
   "ApplicationVersionId": number,
   "OutputDescriptions": [
      {
         "DestinationSchema": {
            "RecordFormatType": "string"
         },
         "KinesisFirehoseOutputDescription": {
            "ResourceARN": "string",
            "RoleARN": "string"
         },
         "KinesisStreamsOutputDescription": {
            "ResourceARN": "string",
            "RoleARN": "string"
         },
         "LambdaOutputDescription": {
            "ResourceARN": "string",
            "RoleARN": "string"
         },
         "Name": "string",
         "OutputId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_AddApplicationOutput_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationARN](#API_AddApplicationOutput_ResponseSyntax) **   <a name="APIReference-AddApplicationOutput-response-ApplicationARN"></a>
The application Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`

 ** [ApplicationVersionId](#API_AddApplicationOutput_ResponseSyntax) **   <a name="APIReference-AddApplicationOutput-response-ApplicationVersionId"></a>
The updated application version ID. Kinesis Data Analytics increments this ID when the application is updated.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.

 ** [OutputDescriptions](#API_AddApplicationOutput_ResponseSyntax) **   <a name="APIReference-AddApplicationOutput-response-OutputDescriptions"></a>
Describes the application output configuration. For more information, see [Configuring Application Output](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html).
Type: Array of [OutputDescription](API_OutputDescription.md) objects

## Errors
<a name="API_AddApplicationOutput_Errors"></a>

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
<a name="API_AddApplicationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/AddApplicationOutput)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/AddApplicationOutput)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/AddApplicationOutput)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/AddApplicationOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/AddApplicationOutput)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/AddApplicationOutput)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/AddApplicationOutput)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/AddApplicationOutput)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/AddApplicationOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/AddApplicationOutput)
