---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_AddApplicationReferenceDataSource.html
---

# AddApplicationReferenceDataSource
<a name="API_AddApplicationReferenceDataSource"></a>

Adds a reference data source to an existing SQL-based Kinesis Data Analytics application.

Kinesis Data Analytics reads reference data (that is, an Amazon S3 object) and creates an in-application table within your application. In the request, you provide the source (S3 bucket name and object key name), name of the in-application table to create, and the necessary mapping information that describes how data in an Amazon S3 object maps to columns in the resulting in-application table.

## Request Syntax
<a name="API_AddApplicationReferenceDataSource_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "CurrentApplicationVersionId": {{number}},
   "ReferenceDataSource": {
      "ReferenceSchema": {
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
      "S3ReferenceDataSource": {
         "BucketARN": "{{string}}",
         "FileKey": "{{string}}"
      },
      "TableName": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_AddApplicationReferenceDataSource_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_AddApplicationReferenceDataSource_RequestSyntax) **   <a name="APIReference-AddApplicationReferenceDataSource-request-ApplicationName"></a>
The name of an existing application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [CurrentApplicationVersionId](#API_AddApplicationReferenceDataSource_RequestSyntax) **   <a name="APIReference-AddApplicationReferenceDataSource-request-CurrentApplicationVersionId"></a>
The version of the application for which you are adding the reference data source. You can use the [DescribeApplication](API_DescribeApplication.md) operation to get the current application version. If the version specified is not the current version, the `ConcurrentModificationException` is returned.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: Yes

 ** [ReferenceDataSource](#API_AddApplicationReferenceDataSource_RequestSyntax) **   <a name="APIReference-AddApplicationReferenceDataSource-request-ReferenceDataSource"></a>
The reference data source can be an object in your Amazon S3 bucket. Kinesis Data Analytics reads the object and copies the data into the in-application table that is created. You provide an S3 bucket, object key name, and the resulting in-application table that is created.
Type: [ReferenceDataSource](API_ReferenceDataSource.md) object
Required: Yes

## Response Syntax
<a name="API_AddApplicationReferenceDataSource_ResponseSyntax"></a>

```
{
   "ApplicationARN": "string",
   "ApplicationVersionId": number,
   "ReferenceDataSourceDescriptions": [
      {
         "ReferenceId": "string",
         "ReferenceSchema": {
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
         "S3ReferenceDataSourceDescription": {
            "BucketARN": "string",
            "FileKey": "string",
            "ReferenceRoleARN": "string"
         },
         "TableName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_AddApplicationReferenceDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationARN](#API_AddApplicationReferenceDataSource_ResponseSyntax) **   <a name="APIReference-AddApplicationReferenceDataSource-response-ApplicationARN"></a>
The application Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`

 ** [ApplicationVersionId](#API_AddApplicationReferenceDataSource_ResponseSyntax) **   <a name="APIReference-AddApplicationReferenceDataSource-response-ApplicationVersionId"></a>
The updated application version ID. Kinesis Data Analytics increments this ID when the application is updated.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.

 ** [ReferenceDataSourceDescriptions](#API_AddApplicationReferenceDataSource_ResponseSyntax) **   <a name="APIReference-AddApplicationReferenceDataSource-response-ReferenceDataSourceDescriptions"></a>
Describes reference data sources configured for the application.
Type: Array of [ReferenceDataSourceDescription](API_ReferenceDataSourceDescription.md) objects

## Errors
<a name="API_AddApplicationReferenceDataSource_Errors"></a>

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
<a name="API_AddApplicationReferenceDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/AddApplicationReferenceDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/AddApplicationReferenceDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/AddApplicationReferenceDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/AddApplicationReferenceDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/AddApplicationReferenceDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/AddApplicationReferenceDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/AddApplicationReferenceDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/AddApplicationReferenceDataSource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/AddApplicationReferenceDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/AddApplicationReferenceDataSource)
