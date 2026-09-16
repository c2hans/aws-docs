---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html
---

# CreateDataSource
<a name="API_CreateDataSource"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Creates a data source connector for an Amazon Q Business application.

 `CreateDataSource` is a synchronous operation. The operation returns 200 if the data source was successfully created. Otherwise, an exception is raised.

## Request Syntax
<a name="API_CreateDataSource_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/indices/{{indexId}}/datasources HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "configuration": {{JSON value}},
   "description": "{{string}}",
   "displayName": "{{string}}",
   "documentEnrichmentConfiguration": {
      "inlineConfigurations": [
         {
            "condition": {
               "key": "{{string}}",
               "operator": "{{string}}",
               "value": { ... }
            },
            "documentContentOperator": "{{string}}",
            "target": {
               "attributeValueOperator": "{{string}}",
               "key": "{{string}}",
               "value": { ... }
            }
         }
      ],
      "postExtractionHookConfiguration": {
         "invocationCondition": {
            "key": "{{string}}",
            "operator": "{{string}}",
            "value": { ... }
         },
         "lambdaArn": "{{string}}",
         "roleArn": "{{string}}",
         "s3BucketName": "{{string}}"
      },
      "preExtractionHookConfiguration": {
         "invocationCondition": {
            "key": "{{string}}",
            "operator": "{{string}}",
            "value": { ... }
         },
         "lambdaArn": "{{string}}",
         "roleArn": "{{string}}",
         "s3BucketName": "{{string}}"
      }
   },
   "mediaExtractionConfiguration": {
      "audioExtractionConfiguration": {
         "audioExtractionStatus": "{{string}}"
      },
      "imageExtractionConfiguration": {
         "imageExtractionStatus": "{{string}}"
      },
      "videoExtractionConfiguration": {
         "videoExtractionStatus": "{{string}}"
      }
   },
   "roleArn": "{{string}}",
   "syncSchedule": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "vpcConfiguration": {
      "securityGroupIds": [ "{{string}}" ],
      "subnetIds": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_CreateDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_CreateDataSource_RequestSyntax) **   <a name="qbusiness-CreateDataSource-request-uri-applicationId"></a>
 The identifier of the Amazon Q Business application the data source will be attached to.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [indexId](#API_CreateDataSource_RequestSyntax) **   <a name="qbusiness-CreateDataSource-request-uri-indexId"></a>
The identifier of the index that you want to use with the data source connector.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## Request Body
<a name="API_CreateDataSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateDataSource_RequestSyntax) **   <a name="qbusiness-CreateDataSource-request-clientToken"></a>
A token you provide to identify a request to create a data source connector. Multiple calls to the `CreateDataSource` API with the same client token will create only one data source connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [configuration](#API_CreateDataSource_RequestSyntax) **   <a name="qbusiness-CreateDataSource-request-configuration"></a>
Configuration information to connect your data source repository to Amazon Q Business. Use this parameter to provide a JSON schema with configuration information specific to your data source connector.
Each data source has a JSON schema provided by Amazon Q Business that you must use. For example, the Amazon S3 and Web Crawler connectors require the following JSON schemas:
+  [Amazon S3 JSON schema](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-api.html)
+  [Web Crawler JSON schema](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/web-crawler-api.html)
You can find configuration templates for your specific data source using the following steps:

1. Navigate to the [Supported connectors](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connectors-list.html) page in the Amazon Q Business User Guide, and select the data source of your choice.

1. Then, from your specific data source connector page, select **Using the API**. You will find the JSON schema for your data source, including parameter descriptions, in this section.
Type: JSON value
Required: Yes

 ** [description](#API_CreateDataSource_RequestSyntax) **   <a name="qbusiness-CreateDataSource-request-description"></a>
A description for the data source connector.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `[\s\S]*`
Required: No

 ** [displayName](#API_CreateDataSource_RequestSyntax) **   <a name="qbusiness-CreateDataSource-request-displayName"></a>
A name for the data source connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

 ** [documentEnrichmentConfiguration](#API_CreateDataSource_RequestSyntax) **   <a name="qbusiness-CreateDataSource-request-documentEnrichmentConfiguration"></a>
Provides the configuration information for altering document metadata and content during the document ingestion process.
For more information, see [Custom document enrichment](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html).
Type: [DocumentEnrichmentConfiguration](API_DocumentEnrichmentConfiguration.md) object
Required: No

 ** [mediaExtractionConfiguration](#API_CreateDataSource_RequestSyntax) **   <a name="qbusiness-CreateDataSource-request-mediaExtractionConfiguration"></a>
The configuration for extracting information from media in documents during ingestion.
Type: [MediaExtractionConfiguration](API_MediaExtractionConfiguration.md) object
Required: No

 ** [roleArn](#API_CreateDataSource_RequestSyntax) **   <a name="qbusiness-CreateDataSource-request-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources. This field is required for all connector types except custom connectors, where it is optional.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** [syncSchedule](#API_CreateDataSource_RequestSyntax) **   <a name="qbusiness-CreateDataSource-request-syncSchedule"></a>
Sets the frequency for Amazon Q Business to check the documents in your data source repository and update your index. If you don't set a schedule, Amazon Q Business won't periodically update the index.
Specify a `cron-` format schedule string or an empty string to indicate that the index is updated on demand. You can't specify the `Schedule` parameter when the `Type` parameter is set to `CUSTOM`. If you do, you receive a `ValidationException` exception.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 998.
Pattern: `[\s\S]*`
Required: No

 ** [tags](#API_CreateDataSource_RequestSyntax) **   <a name="qbusiness-CreateDataSource-request-tags"></a>
A list of key-value pairs that identify or categorize the data source connector. You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: \_ . : / = \+ - @.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [vpcConfiguration](#API_CreateDataSource_RequestSyntax) **   <a name="qbusiness-CreateDataSource-request-vpcConfiguration"></a>
Configuration information for an Amazon VPC (Virtual Private Cloud) to connect to your data source. For more information, see [Using Amazon VPC with Amazon Q Business connectors](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connector-vpc.html).
Type: [DataSourceVpcConfiguration](API_DataSourceVpcConfiguration.md) object
Required: No

## Response Syntax
<a name="API_CreateDataSource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dataSourceArn": "string",
   "dataSourceId": "string"
}
```

## Response Elements
<a name="API_CreateDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dataSourceArn](#API_CreateDataSource_ResponseSyntax) **   <a name="qbusiness-CreateDataSource-response-dataSourceArn"></a>
 The Amazon Resource Name (ARN) of a data source in an Amazon Q Business application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [dataSourceId](#API_CreateDataSource_ResponseSyntax) **   <a name="qbusiness-CreateDataSource-response-dataSourceId"></a>
The identifier of the data source connector.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

## Errors
<a name="API_CreateDataSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** ConflictException **
You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.
 ** message **
The message describing a `ConflictException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.
 ** message **
The message describing a `ResourceNotFoundException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have exceeded the set limits for your Amazon Q Business service.
 ** message **
The message describing a `ServiceQuotaExceededException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to throttling. Reduce the number of requests and try again.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.
 ** fields **
The input field(s) that failed validation.
 ** message **
The message describing the `ValidationException`.
 ** reason **
The reason for the `ValidationException`.
HTTP Status Code: 400

## See Also
<a name="API_CreateDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/CreateDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/CreateDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/CreateDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/CreateDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/CreateDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/CreateDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/CreateDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/CreateDataSource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/CreateDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/CreateDataSource)
