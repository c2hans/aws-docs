---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetDataSource.html
---

# GetDataSource
<a name="API_GetDataSource"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Gets information about an existing Amazon Q Business data source connector.

## Request Syntax
<a name="API_GetDataSource_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/indices/{{indexId}}/datasources/{{dataSourceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetDataSource_RequestSyntax) **   <a name="qbusiness-GetDataSource-request-uri-applicationId"></a>
The identifier of the Amazon Q Business application.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [dataSourceId](#API_GetDataSource_RequestSyntax) **   <a name="qbusiness-GetDataSource-request-uri-dataSourceId"></a>
The identifier of the data source connector.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [indexId](#API_GetDataSource_RequestSyntax) **   <a name="qbusiness-GetDataSource-request-uri-indexId"></a>
The identfier of the index used with the data source connector.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## Request Body
<a name="API_GetDataSource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDataSource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationId": "string",
   "configuration": JSON value,
   "createdAt": number,
   "dataSourceArn": "string",
   "dataSourceId": "string",
   "description": "string",
   "displayName": "string",
   "documentEnrichmentConfiguration": {
      "inlineConfigurations": [
         {
            "condition": {
               "key": "string",
               "operator": "string",
               "value": { ... }
            },
            "documentContentOperator": "string",
            "target": {
               "attributeValueOperator": "string",
               "key": "string",
               "value": { ... }
            }
         }
      ],
      "postExtractionHookConfiguration": {
         "invocationCondition": {
            "key": "string",
            "operator": "string",
            "value": { ... }
         },
         "lambdaArn": "string",
         "roleArn": "string",
         "s3BucketName": "string"
      },
      "preExtractionHookConfiguration": {
         "invocationCondition": {
            "key": "string",
            "operator": "string",
            "value": { ... }
         },
         "lambdaArn": "string",
         "roleArn": "string",
         "s3BucketName": "string"
      }
   },
   "error": {
      "errorCode": "string",
      "errorMessage": "string"
   },
   "indexId": "string",
   "mediaExtractionConfiguration": {
      "audioExtractionConfiguration": {
         "audioExtractionStatus": "string"
      },
      "imageExtractionConfiguration": {
         "imageExtractionStatus": "string"
      },
      "videoExtractionConfiguration": {
         "videoExtractionStatus": "string"
      }
   },
   "roleArn": "string",
   "status": "string",
   "syncSchedule": "string",
   "type": "string",
   "updatedAt": number,
   "vpcConfiguration": {
      "securityGroupIds": [ "string" ],
      "subnetIds": [ "string" ]
   }
}
```

## Response Elements
<a name="API_GetDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationId](#API_GetDataSource_ResponseSyntax) **   <a name="qbusiness-GetDataSource-response-applicationId"></a>
The identifier of the Amazon Q Business application.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

 ** [configuration](#API_GetDataSource_ResponseSyntax) **   <a name="qbusiness-GetDataSource-response-configuration"></a>
The details of how the data source connector is configured.
Type: JSON value

 ** [createdAt](#API_GetDataSource_ResponseSyntax) **   <a name="qbusiness-GetDataSource-response-createdAt"></a>
The Unix timestamp when the data source connector was created.
Type: Timestamp

 ** [dataSourceArn](#API_GetDataSource_ResponseSyntax) **   <a name="qbusiness-GetDataSource-response-dataSourceArn"></a>
The Amazon Resource Name (ARN) of the data source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [dataSourceId](#API_GetDataSource_ResponseSyntax) **   <a name="qbusiness-GetDataSource-response-dataSourceId"></a>
The identifier of the data source connector.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

 ** [description](#API_GetDataSource_ResponseSyntax) **   <a name="qbusiness-GetDataSource-response-description"></a>
The description for the data source connector.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `[\s\S]*`

 ** [displayName](#API_GetDataSource_ResponseSyntax) **   <a name="qbusiness-GetDataSource-response-displayName"></a>
The name for the data source connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`

 ** [documentEnrichmentConfiguration](#API_GetDataSource_ResponseSyntax) **   <a name="qbusiness-GetDataSource-response-documentEnrichmentConfiguration"></a>
Provides the configuration information for altering document metadata and content during the document ingestion process.
For more information, see [Custom document enrichment](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html).
Type: [DocumentEnrichmentConfiguration](API_DocumentEnrichmentConfiguration.md) object

 ** [error](#API_GetDataSource_ResponseSyntax) **   <a name="qbusiness-GetDataSource-response-error"></a>
When the `Status` field value is `FAILED`, the `ErrorMessage` field contains a description of the error that caused the data source connector to fail.
Type: [ErrorDetail](API_ErrorDetail.md) object

 ** [indexId](#API_GetDataSource_ResponseSyntax) **   <a name="qbusiness-GetDataSource-response-indexId"></a>
The identifier of the index linked to the data source connector.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

 ** [mediaExtractionConfiguration](#API_GetDataSource_ResponseSyntax) **   <a name="qbusiness-GetDataSource-response-mediaExtractionConfiguration"></a>
The configuration for extracting information from media in documents for the data source.
Type: [MediaExtractionConfiguration](API_MediaExtractionConfiguration.md) object

 ** [roleArn](#API_GetDataSource_ResponseSyntax) **   <a name="qbusiness-GetDataSource-response-roleArn"></a>
The Amazon Resource Name (ARN) of the role with permission to access the data source and required resources.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [status](#API_GetDataSource_ResponseSyntax) **   <a name="qbusiness-GetDataSource-response-status"></a>
The current status of the data source connector. When the `Status` field value is `FAILED`, the `ErrorMessage` field contains a description of the error that caused the data source connector to fail.
Type: String
Valid Values: `PENDING_CREATION | CREATING | ACTIVE | DELETING | FAILED | UPDATING`

 ** [syncSchedule](#API_GetDataSource_ResponseSyntax) **   <a name="qbusiness-GetDataSource-response-syncSchedule"></a>
The schedule for Amazon Q Business to update the index.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 998.
Pattern: `[\s\S]*`

 ** [type](#API_GetDataSource_ResponseSyntax) **   <a name="qbusiness-GetDataSource-response-type"></a>
The type of the data source connector. For example, `S3`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [updatedAt](#API_GetDataSource_ResponseSyntax) **   <a name="qbusiness-GetDataSource-response-updatedAt"></a>
The Unix timestamp when the data source connector was last updated.
Type: Timestamp

 ** [vpcConfiguration](#API_GetDataSource_ResponseSyntax) **   <a name="qbusiness-GetDataSource-response-vpcConfiguration"></a>
Configuration information for an Amazon VPC (Virtual Private Cloud) to connect to your data source.
Type: [DataSourceVpcConfiguration](API_DataSourceVpcConfiguration.md) object

## Errors
<a name="API_GetDataSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

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
<a name="API_GetDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/GetDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/GetDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/GetDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/GetDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/GetDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/GetDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/GetDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/GetDataSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/GetDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/GetDataSource)
