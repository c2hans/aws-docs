---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DiscoverInputSchema.html
---

# DiscoverInputSchema
<a name="API_DiscoverInputSchema"></a>

Infers a schema for a SQL-based Kinesis Data Analytics application by evaluating sample records on the specified streaming source (Kinesis data stream or Kinesis Data Firehose delivery stream) or Amazon S3 object. In the response, the operation returns the inferred schema and also the sample records that the operation used to infer the schema.

 You can use the inferred schema when configuring a streaming source for your application. When you create an application using the Kinesis Data Analytics console, the console uses this operation to infer a schema and show it in the console user interface.

## Request Syntax
<a name="API_DiscoverInputSchema_RequestSyntax"></a>

```
{
   "InputProcessingConfiguration": {
      "InputLambdaProcessor": {
         "ResourceARN": "{{string}}"
      }
   },
   "InputStartingPositionConfiguration": {
      "InputStartingPosition": "{{string}}"
   },
   "ResourceARN": "{{string}}",
   "S3Configuration": {
      "BucketARN": "{{string}}",
      "FileKey": "{{string}}"
   },
   "ServiceExecutionRole": "{{string}}"
}
```

## Request Parameters
<a name="API_DiscoverInputSchema_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [InputProcessingConfiguration](#API_DiscoverInputSchema_RequestSyntax) **   <a name="APIReference-DiscoverInputSchema-request-InputProcessingConfiguration"></a>
The [InputProcessingConfiguration](API_InputProcessingConfiguration.md) to use to preprocess the records before discovering the schema of the records.
Type: [InputProcessingConfiguration](API_InputProcessingConfiguration.md) object
Required: No

 ** [InputStartingPositionConfiguration](#API_DiscoverInputSchema_RequestSyntax) **   <a name="APIReference-DiscoverInputSchema-request-InputStartingPositionConfiguration"></a>
The point at which you want Kinesis Data Analytics to start reading records from the specified streaming source for discovery purposes.
Type: [InputStartingPositionConfiguration](API_InputStartingPositionConfiguration.md) object
Required: No

 ** [ResourceARN](#API_DiscoverInputSchema_RequestSyntax) **   <a name="APIReference-DiscoverInputSchema-request-ResourceARN"></a>
The Amazon Resource Name (ARN) of the streaming source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

 ** [S3Configuration](#API_DiscoverInputSchema_RequestSyntax) **   <a name="APIReference-DiscoverInputSchema-request-S3Configuration"></a>
Specify this parameter to discover a schema from data in an Amazon S3 object.
Type: [S3Configuration](API_S3Configuration.md) object
Required: No

 ** [ServiceExecutionRole](#API_DiscoverInputSchema_RequestSyntax) **   <a name="APIReference-DiscoverInputSchema-request-ServiceExecutionRole"></a>
The ARN of the role that is used to access the streaming source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

## Response Syntax
<a name="API_DiscoverInputSchema_ResponseSyntax"></a>

```
{
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
   "ParsedInputRecords": [
      [ "string" ]
   ],
   "ProcessedInputRecords": [ "string" ],
   "RawInputRecords": [ "string" ]
}
```

## Response Elements
<a name="API_DiscoverInputSchema_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InputSchema](#API_DiscoverInputSchema_ResponseSyntax) **   <a name="APIReference-DiscoverInputSchema-response-InputSchema"></a>
The schema inferred from the streaming source. It identifies the format of the data in the streaming source and how each data element maps to corresponding columns in the in-application stream that you can create.
Type: [SourceSchema](API_SourceSchema.md) object

 ** [ParsedInputRecords](#API_DiscoverInputSchema_ResponseSyntax) **   <a name="APIReference-DiscoverInputSchema-response-ParsedInputRecords"></a>
An array of elements, where each element corresponds to a row in a stream record (a stream record can have more than one row).
Type: Array of arrays of strings

 ** [ProcessedInputRecords](#API_DiscoverInputSchema_ResponseSyntax) **   <a name="APIReference-DiscoverInputSchema-response-ProcessedInputRecords"></a>
The stream data that was modified by the processor specified in the `InputProcessingConfiguration` parameter.
Type: Array of strings

 ** [RawInputRecords](#API_DiscoverInputSchema_ResponseSyntax) **   <a name="APIReference-DiscoverInputSchema-response-RawInputRecords"></a>
The raw stream data that was sampled to infer the schema.
Type: Array of strings

## Errors
<a name="API_DiscoverInputSchema_Errors"></a>

 ** InvalidArgumentException **
The specified input parameter value is not valid.
HTTP Status Code: 400

 ** InvalidRequestException **
The request JSON is not valid for the operation.
HTTP Status Code: 400

 ** ResourceProvisionedThroughputExceededException **
Discovery failed to get a record from the streaming source because of the Kinesis Streams `ProvisionedThroughputExceededException`. For more information, see [GetRecords](http://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetRecords.html) in the Amazon Kinesis Streams API Reference.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

 ** UnableToDetectSchemaException **
The data format is not valid. Kinesis Data Analytics cannot detect the schema for the given streaming source.
 ** ProcessedInputRecords **
Stream data that was modified by the processor specified in the `InputProcessingConfiguration` parameter.
 ** RawInputRecords **
Raw stream data that was sampled to infer the schema.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## See Also
<a name="API_DiscoverInputSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/DiscoverInputSchema)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/DiscoverInputSchema)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/DiscoverInputSchema)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/DiscoverInputSchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/DiscoverInputSchema)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/DiscoverInputSchema)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/DiscoverInputSchema)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/DiscoverInputSchema)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/DiscoverInputSchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/DiscoverInputSchema)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
