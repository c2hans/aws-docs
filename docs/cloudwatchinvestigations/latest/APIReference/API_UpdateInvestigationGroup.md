---
source_url: https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_UpdateInvestigationGroup.html
---

# UpdateInvestigationGroup
<a name="API_UpdateInvestigationGroup"></a>

Updates the configuration of the specified investigation group.

## Request Syntax
<a name="API_UpdateInvestigationGroup_RequestSyntax"></a>

```
PATCH /investigationGroups/{{identifier}} HTTP/1.1
Content-type: application/json

{
   "chatbotNotificationChannel": {
      "{{string}}" : [ "{{string}}" ]
   },
   "crossAccountConfigurations": [
      {
         "sourceRoleArn": "{{string}}"
      }
   ],
   "encryptionConfiguration": {
      "kmsKeyId": "{{string}}",
      "type": "{{string}}"
   },
   "isCloudTrailEventHistoryEnabled": {{boolean}},
   "roleArn": "{{string}}",
   "tagKeyBoundaries": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateInvestigationGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [identifier](#API_UpdateInvestigationGroup_RequestSyntax) **   <a name="cloudwatchinvestigations-UpdateInvestigationGroup-request-uri-identifier"></a>
Specify either the name or the ARN of the investigation group that you want to modify.
Pattern: `(?:[\-_A-Za-z0-9]{1,512}|arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):aiops:[a-zA-Z0-9-]*:[0-9]{12}:investigation-group\/[A-Za-z0-9]{16})`
Required: Yes

## Request Body
<a name="API_UpdateInvestigationGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [chatbotNotificationChannel](#API_UpdateInvestigationGroup_RequestSyntax) **   <a name="cloudwatchinvestigations-UpdateInvestigationGroup-request-chatbotNotificationChannel"></a>
Use this structure to integrate CloudWatch investigations with chat applications. This structure is a string array. For the first string, specify the ARN of an Amazon SNS topic. For the array of strings, specify the ARNs of one or more chat applications configurations that you want to associate with that topic. For more information about these configuration ARNs, see [Getting started with Amazon Q in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-started.html) and [Resource type defined by AWS Chatbot](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awschatbot.html#awschatbot-resources-for-iam-policies).
Type: String to array of strings map
Key Length Constraints: Minimum length of 20. Maximum length of 2048.
Key Pattern: `arn:.*`
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

 ** [crossAccountConfigurations](#API_UpdateInvestigationGroup_RequestSyntax) **   <a name="cloudwatchinvestigations-UpdateInvestigationGroup-request-crossAccountConfigurations"></a>
Used to configure cross-account access for an investigation group. It allows the investigation group to access resources in other accounts.
Type: Array of [CrossAccountConfiguration](API_CrossAccountConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: No

 ** [encryptionConfiguration](#API_UpdateInvestigationGroup_RequestSyntax) **   <a name="cloudwatchinvestigations-UpdateInvestigationGroup-request-encryptionConfiguration"></a>
Use this structure if you want to use a customer managed AWS KMS key to encrypt your investigation data. If you omit this parameter, CloudWatch investigations will use an AWS key to encrypt the data. For more information, see [Encryption of investigation data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html#Investigations-KMS).
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** [isCloudTrailEventHistoryEnabled](#API_UpdateInvestigationGroup_RequestSyntax) **   <a name="cloudwatchinvestigations-UpdateInvestigationGroup-request-isCloudTrailEventHistoryEnabled"></a>
Specify `true` to enable CloudWatch investigations to have access to change events that are recorded by CloudTrail. The default is `true`.
Type: Boolean
Required: No

 ** [roleArn](#API_UpdateInvestigationGroup_RequestSyntax) **   <a name="cloudwatchinvestigations-UpdateInvestigationGroup-request-roleArn"></a>
Specify this field if you want to change the IAM role that CloudWatch investigations will use when it gathers investigation data. To do so, specify the ARN of the new role.
The permissions in this role determine which of your resources that CloudWatch investigations will have access to during investigations.
For more information, see [How to control what data CloudWatch investigations has access to during investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html#Investigations-Security-Data).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

 ** [tagKeyBoundaries](#API_UpdateInvestigationGroup_RequestSyntax) **   <a name="cloudwatchinvestigations-UpdateInvestigationGroup-request-tagKeyBoundaries"></a>
Enter the existing custom tag keys for custom applications in your system. Resource tags help CloudWatch investigations narrow the search space when it is unable to discover definite relationships between resources. For example, to discover that an Amazon ECS service depends on an Amazon RDS database, CloudWatch investigations can discover this relationship using data sources such as X-Ray and CloudWatch Application Signals. However, if you haven't deployed these features, CloudWatch investigations will attempt to identify possible relationships. Tag boundaries can be used to narrow the resources that will be discovered by CloudWatch investigations in these cases.
You don't need to enter tags created by myApplications or CloudFormation, because CloudWatch investigations can automatically detect those tags.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]+)`
Required: No

## Response Syntax
<a name="API_UpdateInvestigationGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateInvestigationGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateInvestigationGroup_Errors"></a>

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
<a name="API_UpdateInvestigationGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/aiops-2018-05-10/UpdateInvestigationGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/aiops-2018-05-10/UpdateInvestigationGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/aiops-2018-05-10/UpdateInvestigationGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/aiops-2018-05-10/UpdateInvestigationGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/aiops-2018-05-10/UpdateInvestigationGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/aiops-2018-05-10/UpdateInvestigationGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/aiops-2018-05-10/UpdateInvestigationGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/aiops-2018-05-10/UpdateInvestigationGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/aiops-2018-05-10/UpdateInvestigationGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/aiops-2018-05-10/UpdateInvestigationGroup)
