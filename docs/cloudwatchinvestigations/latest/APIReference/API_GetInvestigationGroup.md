---
source_url: https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_GetInvestigationGroup.html
---

# GetInvestigationGroup
<a name="API_GetInvestigationGroup"></a>

Returns the configuration information for the specified investigation group.

## Request Syntax
<a name="API_GetInvestigationGroup_RequestSyntax"></a>

```
GET /investigationGroups/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetInvestigationGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [identifier](#API_GetInvestigationGroup_RequestSyntax) **   <a name="cloudwatchinvestigations-GetInvestigationGroup-request-uri-identifier"></a>
Specify either the name or the ARN of the investigation group that you want to view. This is used to set the name of the investigation group.
Pattern: `(?:[\-_A-Za-z0-9]{1,512}|arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):aiops:[a-zA-Z0-9-]*:[0-9]{12}:investigation-group\/[A-Za-z0-9]{16})`
Required: Yes

## Request Body
<a name="API_GetInvestigationGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetInvestigationGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "chatbotNotificationChannel": {
      "string" : [ "string" ]
   },
   "createdAt": number,
   "createdBy": "string",
   "crossAccountConfigurations": [
      {
         "sourceRoleArn": "string"
      }
   ],
   "encryptionConfiguration": {
      "kmsKeyId": "string",
      "type": "string"
   },
   "isCloudTrailEventHistoryEnabled": boolean,
   "lastModifiedAt": number,
   "lastModifiedBy": "string",
   "name": "string",
   "retentionInDays": number,
   "roleArn": "string",
   "tagKeyBoundaries": [ "string" ]
}
```

## Response Elements
<a name="API_GetInvestigationGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetInvestigationGroup_ResponseSyntax) **   <a name="cloudwatchinvestigations-GetInvestigationGroup-response-arn"></a>
The Amazon Resource Name (ARN) of the investigation group.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):aiops:[a-zA-Z0-9-]*:[0-9]{12}:investigation-group\/[A-Za-z0-9]{16}`

 ** [chatbotNotificationChannel](#API_GetInvestigationGroup_ResponseSyntax) **   <a name="cloudwatchinvestigations-GetInvestigationGroup-response-chatbotNotificationChannel"></a>
This structure is a string array. The first string is the ARN of a Amazon SNS topic. The array of strings display the ARNs of chat applications configurations that are associated with that topic. For more information about these configuration ARNs, see [Getting started with Amazon Q in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-started.html) and [Resource type defined by AWS Chatbot](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awschatbot.html#awschatbot-resources-for-iam-policies).
Type: String to array of strings map
Key Length Constraints: Minimum length of 20. Maximum length of 2048.
Key Pattern: `arn:.*`
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`

 ** [createdAt](#API_GetInvestigationGroup_ResponseSyntax) **   <a name="cloudwatchinvestigations-GetInvestigationGroup-response-createdAt"></a>
The date and time that the investigation group was created.
Type: Long

 ** [createdBy](#API_GetInvestigationGroup_ResponseSyntax) **   <a name="cloudwatchinvestigations-GetInvestigationGroup-response-createdBy"></a>
The name of the user who created the investigation group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\-_\/A-Za-z0-9:\.]+`

 ** [crossAccountConfigurations](#API_GetInvestigationGroup_ResponseSyntax) **   <a name="cloudwatchinvestigations-GetInvestigationGroup-response-crossAccountConfigurations"></a>
Lists the `AWSAccountId` of the accounts configured for cross-account access and the results of the last scan performed on each account.
Type: Array of [CrossAccountConfiguration](API_CrossAccountConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [encryptionConfiguration](#API_GetInvestigationGroup_ResponseSyntax) **   <a name="cloudwatchinvestigations-GetInvestigationGroup-response-encryptionConfiguration"></a>
Specifies the customer managed AWS KMS key that the investigation group uses to encrypt data, if there is one. If not, the investigation group uses an AWS key to encrypt the data.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object

 ** [isCloudTrailEventHistoryEnabled](#API_GetInvestigationGroup_ResponseSyntax) **   <a name="cloudwatchinvestigations-GetInvestigationGroup-response-isCloudTrailEventHistoryEnabled"></a>
Specifies whether CloudWatch investigationshas access to change events that are recorded by CloudTrail.
Type: Boolean

 ** [lastModifiedAt](#API_GetInvestigationGroup_ResponseSyntax) **   <a name="cloudwatchinvestigations-GetInvestigationGroup-response-lastModifiedAt"></a>
The date and time that the investigation group was most recently modified.
Type: Long

 ** [lastModifiedBy](#API_GetInvestigationGroup_ResponseSyntax) **   <a name="cloudwatchinvestigations-GetInvestigationGroup-response-lastModifiedBy"></a>
The name of the user who created the investigation group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\-_\/A-Za-z0-9:\.]+`

 ** [name](#API_GetInvestigationGroup_ResponseSyntax) **   <a name="cloudwatchinvestigations-GetInvestigationGroup-response-name"></a>
The name of the investigation group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\-_A-Za-z0-9\[\]\(\)\{\}\.: ]+`

 ** [retentionInDays](#API_GetInvestigationGroup_ResponseSyntax) **   <a name="cloudwatchinvestigations-GetInvestigationGroup-response-retentionInDays"></a>
Specifies how long that investigation data is kept.
Type: Long
Valid Range: Minimum value of 7. Maximum value of 90.

 ** [roleArn](#API_GetInvestigationGroup_ResponseSyntax) **   <a name="cloudwatchinvestigations-GetInvestigationGroup-response-roleArn"></a>
The ARN of the IAM role that the investigation group uses for permissions to gather data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`

 ** [tagKeyBoundaries](#API_GetInvestigationGroup_ResponseSyntax) **   <a name="cloudwatchinvestigations-GetInvestigationGroup-response-tagKeyBoundaries"></a>
Displays the custom tag keys for custom applications in your system that you have specified in the investigation group. Resource tags help CloudWatch investigations narrow the search space when it is unable to discover definite relationships between resources.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]+)`

## Errors
<a name="API_GetInvestigationGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
This operation couldn't be completed because of a conflict in resource states.
HTTP Status Code: 409

 ** ForbiddenException **
Access id denied for this operation, or this operation is not valid for the specified resource.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. You can try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because of quota limits. You can try again later.
HTTP Status Code: 429

 ** ValidationException **
This operation or its parameters aren't formatted correctly.
HTTP Status Code: 400

## See Also
<a name="API_GetInvestigationGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/aiops-2018-05-10/GetInvestigationGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/aiops-2018-05-10/GetInvestigationGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/aiops-2018-05-10/GetInvestigationGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/aiops-2018-05-10/GetInvestigationGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/aiops-2018-05-10/GetInvestigationGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/aiops-2018-05-10/GetInvestigationGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/aiops-2018-05-10/GetInvestigationGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/aiops-2018-05-10/GetInvestigationGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/aiops-2018-05-10/GetInvestigationGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/aiops-2018-05-10/GetInvestigationGroup)
