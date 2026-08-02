---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateKnowledgeBase.html
---

# CreateKnowledgeBase
<a name="API_CreateKnowledgeBase"></a>

Creates a knowledge base from a specified data source. Supported data source connector types include:
+  `S3_KNOWLEDGE_BASE` – Uses an Amazon S3 bucket as the data source.
+  `WEB_CRAWLER` – Uses web pages indexed by the built-in web crawler as the data source.
+  `GOOGLE_DRIVE` – Uses Google Drive as the data source. Supports service account authentication only.
+  `SHAREPOINT` – Uses SharePoint as the data source. Supports two-legged OAuth only.
+  `ONE_DRIVE` – Uses OneDrive as the data source. Supports two-legged OAuth only.

## Request Syntax
<a name="API_CreateKnowledgeBase_RequestSyntax"></a>

```
POST /v1/accounts/{{AwsAccountId}}/knowledge-bases HTTP/1.1
Content-type: application/json

{
   "AccessControlConfiguration": {
      "isACLEnabled": {{boolean}}
   },
   "DataSourceArn": "{{string}}",
   "Description": "{{string}}",
   "KnowledgeBaseConfiguration": {
      "templateConfiguration": {
         "template": {{JSON value}}
      }
   },
   "KnowledgeBaseId": "{{string}}",
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
   "Name": "{{string}}",
   "Permissions": [
      {
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ],
   "PrimaryOwnerArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateKnowledgeBase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateKnowledgeBase_RequestSyntax) **   <a name="QS-CreateKnowledgeBase-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the knowledge base.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]*`
Required: Yes

## Request Body
<a name="API_CreateKnowledgeBase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DataSourceArn](#API_CreateKnowledgeBase_RequestSyntax) **   <a name="QS-CreateKnowledgeBase-request-DataSourceArn"></a>
The Amazon Resource Name (ARN) of the data source for the knowledge base.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [KnowledgeBaseConfiguration](#API_CreateKnowledgeBase_RequestSyntax) **   <a name="QS-CreateKnowledgeBase-request-KnowledgeBaseConfiguration"></a>
The configuration settings for a knowledge base.
Type: [KnowledgeBaseConfiguration](API_KnowledgeBaseConfiguration.md) object
Required: Yes

 ** [KnowledgeBaseId](#API_CreateKnowledgeBase_RequestSyntax) **   <a name="QS-CreateKnowledgeBase-request-KnowledgeBaseId"></a>
The unique identifier for the knowledge base.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z-_=.+]+`
Required: Yes

 ** [Name](#API_CreateKnowledgeBase_RequestSyntax) **   <a name="QS-CreateKnowledgeBase-request-Name"></a>
The name of the knowledge base.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[\p{L}\p{N}][\p{L}\p{N} _\-\.]*`
Required: Yes

 ** [AccessControlConfiguration](#API_CreateKnowledgeBase_RequestSyntax) **   <a name="QS-CreateKnowledgeBase-request-AccessControlConfiguration"></a>
The access control configuration for the knowledge base. If you don't specify this parameter, document-level ACLs are disabled.
Type: [AccessControlConfiguration](API_AccessControlConfiguration.md) object
Required: No

 ** [Description](#API_CreateKnowledgeBase_RequestSyntax) **   <a name="QS-CreateKnowledgeBase-request-Description"></a>
A description for the knowledge base. If you don't specify a description, the knowledge base is created without one.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `\P{C}*`
Required: No

 ** [MediaExtractionConfiguration](#API_CreateKnowledgeBase_RequestSyntax) **   <a name="QS-CreateKnowledgeBase-request-MediaExtractionConfiguration"></a>
The configuration for media extraction from knowledge base documents.
Type: [MediaExtractionConfiguration](API_MediaExtractionConfiguration.md) object
Required: No

 ** [Permissions](#API_CreateKnowledgeBase_RequestSyntax) **   <a name="QS-CreateKnowledgeBase-request-Permissions"></a>
A list of resource permissions on the knowledge base. Each entry grants a specified Amazon QuickSight principal either owner or viewer access. If you don't specify permissions, only the primary owner (if provided) receives owner access.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 64 items.
Required: No

 ** [PrimaryOwnerArn](#API_CreateKnowledgeBase_RequestSyntax) **   <a name="QS-CreateKnowledgeBase-request-PrimaryOwnerArn"></a>
The Amazon Resource Name (ARN) of the primary owner for the knowledge base. The specified user is always granted owner access, regardless of what is specified in the `Permissions` field. If you don't specify a primary owner, the knowledge base is created without one.
Type: String
Required: No

 ** [Tags](#API_CreateKnowledgeBase_RequestSyntax) **   <a name="QS-CreateKnowledgeBase-request-Tags"></a>
The tags to assign to the knowledge base. If you don't specify tags, the knowledge base is created without tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateKnowledgeBase_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "CreationStatus": "string",
   "KnowledgeBaseArn": "string",
   "KnowledgeBaseId": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_CreateKnowledgeBase_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateKnowledgeBase_ResponseSyntax) **   <a name="QS-CreateKnowledgeBase-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [CreationStatus](#API_CreateKnowledgeBase_ResponseSyntax) **   <a name="QS-CreateKnowledgeBase-response-CreationStatus"></a>
The creation status of the knowledge base.
Type: String
Valid Values: `CREATING | UPDATING | ACTIVE | FAILED | DELETING`

 ** [KnowledgeBaseArn](#API_CreateKnowledgeBase_ResponseSyntax) **   <a name="QS-CreateKnowledgeBase-response-KnowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [KnowledgeBaseId](#API_CreateKnowledgeBase_ResponseSyntax) **   <a name="QS-CreateKnowledgeBase-response-KnowledgeBaseId"></a>
The unique identifier for the knowledge base.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z-_=.+]+`

 ** [RequestId](#API_CreateKnowledgeBase_ResponseSyntax) **   <a name="QS-CreateKnowledgeBase-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_CreateKnowledgeBase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

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

 ** ResourceExistsException **
The resource specified already exists.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 409

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
<a name="API_CreateKnowledgeBase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateKnowledgeBase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateKnowledgeBase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateKnowledgeBase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateKnowledgeBase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateKnowledgeBase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateKnowledgeBase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateKnowledgeBase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateKnowledgeBase)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateKnowledgeBase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateKnowledgeBase)
