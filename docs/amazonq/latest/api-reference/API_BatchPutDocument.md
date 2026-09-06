---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BatchPutDocument.html
---

# BatchPutDocument
<a name="API_BatchPutDocument"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Adds one or more documents to an Amazon Q Business index.

You use this API to:
+ ingest your structured and unstructured documents and documents stored in an Amazon S3 bucket into an Amazon Q Business index.
+ add custom attributes to documents in an Amazon Q Business index.
+ attach an access control list to the documents added to an Amazon Q Business index.

You can see the progress of the deletion, and any error messages related to the process, by using CloudWatch.

## Request Syntax
<a name="API_BatchPutDocument_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/indices/{{indexId}}/documents HTTP/1.1
Content-type: application/json

{
   "dataSourceSyncId": "{{string}}",
   "documents": [
      {
         "accessConfiguration": {
            "accessControls": [
               {
                  "memberRelation": "{{string}}",
                  "principals": [
                     { ... }
                  ]
               }
            ],
            "memberRelation": "{{string}}"
         },
         "attributes": [
            {
               "name": "{{string}}",
               "value": { ... }
            }
         ],
         "content": { ... },
         "contentType": "{{string}}",
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
         "id": "{{string}}",
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
         "title": "{{string}}"
      }
   ],
   "roleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_BatchPutDocument_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_BatchPutDocument_RequestSyntax) **   <a name="qbusiness-BatchPutDocument-request-uri-applicationId"></a>
The identifier of the Amazon Q Business application.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [indexId](#API_BatchPutDocument_RequestSyntax) **   <a name="qbusiness-BatchPutDocument-request-uri-indexId"></a>
The identifier of the Amazon Q Business index to add the documents to.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## Request Body
<a name="API_BatchPutDocument_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [dataSourceSyncId](#API_BatchPutDocument_RequestSyntax) **   <a name="qbusiness-BatchPutDocument-request-dataSourceSyncId"></a>
The identifier of the data source sync during which the documents were added.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** [documents](#API_BatchPutDocument_RequestSyntax) **   <a name="qbusiness-BatchPutDocument-request-documents"></a>
One or more documents to add to the index.
Ensure that the name of your document doesn't contain any confidential information. Amazon Q Business returns document names in chat responses and citations when relevant.
Type: Array of [Document](API_Document.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [roleArn](#API_BatchPutDocument_RequestSyntax) **   <a name="qbusiness-BatchPutDocument-request-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role with permission to access your S3 bucket.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

## Response Syntax
<a name="API_BatchPutDocument_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failedDocuments": [
      {
         "dataSourceId": "string",
         "error": {
            "errorCode": "string",
            "errorMessage": "string"
         },
         "id": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchPutDocument_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedDocuments](#API_BatchPutDocument_ResponseSyntax) **   <a name="qbusiness-BatchPutDocument-response-failedDocuments"></a>
 A list of documents that were not added to the Amazon Q Business index because the document failed a validation check. Each document contains an error message that indicates why the document couldn't be added to the index.
Type: Array of [FailedDocument](API_FailedDocument.md) objects

## Errors
<a name="API_BatchPutDocument_Errors"></a>

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
<a name="API_BatchPutDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/BatchPutDocument)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/BatchPutDocument)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/BatchPutDocument)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/BatchPutDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/BatchPutDocument)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/BatchPutDocument)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/BatchPutDocument)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/BatchPutDocument)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/BatchPutDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/BatchPutDocument)
