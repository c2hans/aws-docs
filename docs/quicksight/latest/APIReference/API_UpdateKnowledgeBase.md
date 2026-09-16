---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateKnowledgeBase.html
---

# UpdateKnowledgeBase
<a name="API_UpdateKnowledgeBase"></a>

Updates the properties of an existing knowledge base.

## Request Syntax
<a name="API_UpdateKnowledgeBase_RequestSyntax"></a>

```
POST /v1/accounts/{{AwsAccountId}}/knowledge-bases/{{KnowledgeBaseId}} HTTP/1.1
Content-type: application/json

{
   "AccessControlConfiguration": {
      "isACLEnabled": {{boolean}}
   },
   "Description": "{{string}}",
   "IsEmailNotificationOptedForIngestionFailures": {{boolean}},
   "KnowledgeBaseConfiguration": {
      "templateConfiguration": {
         "template": {{JSON value}}
      }
   },
   "MediaExtractionConfiguration": {
      "audioExtractionConfiguration": {
         "audioExtractionStatus": "{{string}}"
      },
      "imageExtractionConfiguration": {
         "imageExtractionStatus": "{{string}}"
      },
      "videoExtractionConfiguration": {
         "videoExtractionStatus": "{{string}}",
         "videoExtractionType": "{{string}}"
      }
   },
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateKnowledgeBase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateKnowledgeBase_RequestSyntax) **   <a name="QS-UpdateKnowledgeBase-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the knowledge base.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]*`
Required: Yes

 ** [KnowledgeBaseId](#API_UpdateKnowledgeBase_RequestSyntax) **   <a name="QS-UpdateKnowledgeBase-request-uri-KnowledgeBaseId"></a>
The unique identifier for the knowledge base.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z-_=.+]+`
Required: Yes

## Request Body
<a name="API_UpdateKnowledgeBase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccessControlConfiguration](#API_UpdateKnowledgeBase_RequestSyntax) **   <a name="QS-UpdateKnowledgeBase-request-AccessControlConfiguration"></a>
The access control configuration for the knowledge base. If you don't specify this parameter, the existing setting is retained.
Type: [AccessControlConfiguration](API_AccessControlConfiguration.md) object
Required: No

 ** [Description](#API_UpdateKnowledgeBase_RequestSyntax) **   <a name="QS-UpdateKnowledgeBase-request-Description"></a>
A description for the knowledge base. If you don't specify a description, the existing description is retained.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `\P{C}*`
Required: No

 ** [IsEmailNotificationOptedForIngestionFailures](#API_UpdateKnowledgeBase_RequestSyntax) **   <a name="QS-UpdateKnowledgeBase-request-IsEmailNotificationOptedForIngestionFailures"></a>
Specifies whether email notifications are enabled for ingestion failures.
Type: Boolean
Required: No

 ** [KnowledgeBaseConfiguration](#API_UpdateKnowledgeBase_RequestSyntax) **   <a name="QS-UpdateKnowledgeBase-request-KnowledgeBaseConfiguration"></a>
The configuration settings for a knowledge base.
Type: [KnowledgeBaseConfiguration](API_KnowledgeBaseConfiguration.md) object
Required: No

 ** [MediaExtractionConfiguration](#API_UpdateKnowledgeBase_RequestSyntax) **   <a name="QS-UpdateKnowledgeBase-request-MediaExtractionConfiguration"></a>
The configuration for media extraction from knowledge base documents.
Type: [MediaExtractionConfiguration](API_MediaExtractionConfiguration.md) object
Required: No

 ** [Name](#API_UpdateKnowledgeBase_RequestSyntax) **   <a name="QS-UpdateKnowledgeBase-request-Name"></a>
The name of the knowledge base. If you don't specify a name, the existing name is retained.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[\p{L}\p{N}][\p{L}\p{N} _\-\.]*`
Required: No

## Response Syntax
<a name="API_UpdateKnowledgeBase_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "KnowledgeBaseArn": "string",
   "KnowledgeBaseId": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateKnowledgeBase_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateKnowledgeBase_ResponseSyntax) **   <a name="QS-UpdateKnowledgeBase-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [KnowledgeBaseArn](#API_UpdateKnowledgeBase_ResponseSyntax) **   <a name="QS-UpdateKnowledgeBase-response-KnowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [KnowledgeBaseId](#API_UpdateKnowledgeBase_ResponseSyntax) **   <a name="QS-UpdateKnowledgeBase-response-KnowledgeBaseId"></a>
The unique identifier for the knowledge base.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z-_=.+]+`

 ** [RequestId](#API_UpdateKnowledgeBase_ResponseSyntax) **   <a name="QS-UpdateKnowledgeBase-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateKnowledgeBase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** InvalidRequestException **
You don't have this feature activated for your account. To fix this issue, contact AWS support.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** PreconditionNotMetException **
One or more preconditions aren't met.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateKnowledgeBase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateKnowledgeBase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateKnowledgeBase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateKnowledgeBase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateKnowledgeBase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateKnowledgeBase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateKnowledgeBase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateKnowledgeBase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateKnowledgeBase)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateKnowledgeBase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateKnowledgeBase)
