---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataSource.html
---

# UpdateDataSource
<a name="API_UpdateDataSource"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Updates an existing Amazon Q Business data source connector.

## Request Syntax
<a name="API_UpdateDataSource_RequestSyntax"></a>

```
PUT /applications/{{applicationId}}/indices/{{indexId}}/datasources/{{dataSourceId}} HTTP/1.1
Content-type: application/json

{
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
   "vpcConfiguration": {
      "securityGroupIds": [ "{{string}}" ],
      "subnetIds": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_UpdateDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_UpdateDataSource_RequestSyntax) **   <a name="qbusiness-UpdateDataSource-request-uri-applicationId"></a>
 The identifier of the Amazon Q Business application the data source is attached to.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [dataSourceId](#API_UpdateDataSource_RequestSyntax) **   <a name="qbusiness-UpdateDataSource-request-uri-dataSourceId"></a>
The identifier of the data source connector.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [indexId](#API_UpdateDataSource_RequestSyntax) **   <a name="qbusiness-UpdateDataSource-request-uri-indexId"></a>
The identifier of the index attached to the data source connector.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## Request Body
<a name="API_UpdateDataSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuration](#API_UpdateDataSource_RequestSyntax) **   <a name="qbusiness-UpdateDataSource-request-configuration"></a>
Provides the configuration information for an Amazon Q Business data source.
Type: JSON value
Required: No

 ** [description](#API_UpdateDataSource_RequestSyntax) **   <a name="qbusiness-UpdateDataSource-request-description"></a>
The description of the data source connector.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `[\s\S]*`
Required: No

 ** [displayName](#API_UpdateDataSource_RequestSyntax) **   <a name="qbusiness-UpdateDataSource-request-displayName"></a>
A name of the data source connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** [documentEnrichmentConfiguration](#API_UpdateDataSource_RequestSyntax) **   <a name="qbusiness-UpdateDataSource-request-documentEnrichmentConfiguration"></a>
Provides the configuration information for altering document metadata and content during the document ingestion process.
For more information, see [Custom document enrichment](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html).
Type: [DocumentEnrichmentConfiguration](API_DocumentEnrichmentConfiguration.md) object
Required: No

 ** [mediaExtractionConfiguration](#API_UpdateDataSource_RequestSyntax) **   <a name="qbusiness-UpdateDataSource-request-mediaExtractionConfiguration"></a>
The configuration for extracting information from media in documents for your data source.
Type: [MediaExtractionConfiguration](API_MediaExtractionConfiguration.md) object
Required: No

 ** [roleArn](#API_UpdateDataSource_RequestSyntax) **   <a name="qbusiness-UpdateDataSource-request-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** [syncSchedule](#API_UpdateDataSource_RequestSyntax) **   <a name="qbusiness-UpdateDataSource-request-syncSchedule"></a>
The chosen update frequency for your data source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 998.
Pattern: `[\s\S]*`
Required: No

 ** [vpcConfiguration](#API_UpdateDataSource_RequestSyntax) **   <a name="qbusiness-UpdateDataSource-request-vpcConfiguration"></a>
Provides configuration information needed to connect to an Amazon VPC (Virtual Private Cloud).
Type: [DataSourceVpcConfiguration](API_DataSourceVpcConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateDataSource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateDataSource_Errors"></a>

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
<a name="API_UpdateDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/UpdateDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/UpdateDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/UpdateDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/UpdateDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/UpdateDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/UpdateDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/UpdateDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/UpdateDataSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/UpdateDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/UpdateDataSource)
