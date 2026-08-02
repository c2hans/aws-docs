---
source_url: https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_CreateInvestigationGroup.html
---

# CreateInvestigationGroup
<a name="API_CreateInvestigationGroup"></a>

Creates an *investigation group* in your account. Creating an investigation group is a one-time setup task for each Region in your account. It is a necessary task to be able to perform investigations.

Settings in the investigation group help you centrally manage the common properties of your investigations, such as the following:
+ Who can access the investigations
+ Whether investigation data is encrypted with a customer managed AWS Key Management Service key.
+ How long investigations and their data are retained by default.

Currently, you can have one investigation group in each Region in your account. Each investigation in a Region is a part of the investigation group in that Region

To create an investigation group and set up CloudWatch investigations, you must be signed in to an IAM principal that has either the `AIOpsConsoleAdminPolicy` or the `AdministratorAccess` IAM policy attached, or to an account that has similar permissions.

**Important**
You can configure CloudWatch alarms to start investigations and add events to investigations. If you create your investigation group with `CreateInvestigationGroup` and you want to enable alarms to do this, you must use `PutInvestigationGroupPolicy` to create a resource policy that grants this permission to CloudWatch alarms.
For more information about configuring CloudWatch alarms, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

## Request Syntax
<a name="API_CreateInvestigationGroup_RequestSyntax"></a>

```
POST /investigationGroups HTTP/1.1
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
   "name": "{{string}}",
   "retentionInDays": {{number}},
   "roleArn": "{{string}}",
   "tagKeyBoundaries": [ "{{string}}" ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateInvestigationGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateInvestigationGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [chatbotNotificationChannel](#API_CreateInvestigationGroup_RequestSyntax) **   <a name="cloudwatchinvestigations-CreateInvestigationGroup-request-chatbotNotificationChannel"></a>
Use this structure to integrate CloudWatch investigations with chat applications. This structure is a string array. For the first string, specify the ARN of an Amazon SNS topic. For the array of strings, specify the ARNs of one or more chat applications configurations that you want to associate with that topic. For more information about these configuration ARNs, see [Getting started with Amazon Q in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-started.html) and [Resource type defined by AWS Chatbot](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awschatbot.html#awschatbot-resources-for-iam-policies).
Type: String to array of strings map
Key Length Constraints: Minimum length of 20. Maximum length of 2048.
Key Pattern: `arn:.*`
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

 ** [crossAccountConfigurations](#API_CreateInvestigationGroup_RequestSyntax) **   <a name="cloudwatchinvestigations-CreateInvestigationGroup-request-crossAccountConfigurations"></a>
List of `sourceRoleArn` values that have been configured for cross-account access.
Type: Array of [CrossAccountConfiguration](API_CrossAccountConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: No

 ** [encryptionConfiguration](#API_CreateInvestigationGroup_RequestSyntax) **   <a name="cloudwatchinvestigations-CreateInvestigationGroup-request-encryptionConfiguration"></a>
Use this structure if you want to use a customer managed AWS KMS key to encrypt your investigation data. If you omit this parameter, CloudWatch investigations will use an AWS key to encrypt the data. For more information, see [Encryption of investigation data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html#Investigations-KMS).
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** [isCloudTrailEventHistoryEnabled](#API_CreateInvestigationGroup_RequestSyntax) **   <a name="cloudwatchinvestigations-CreateInvestigationGroup-request-isCloudTrailEventHistoryEnabled"></a>
Specify `true` to enable CloudWatch investigations to have access to change events that are recorded by CloudTrail. The default is `true`.
Type: Boolean
Required: No

 ** [name](#API_CreateInvestigationGroup_RequestSyntax) **   <a name="cloudwatchinvestigations-CreateInvestigationGroup-request-name"></a>
Provides a name for the investigation group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\-_A-Za-z0-9\[\]\(\)\{\}\.: ]+`
Required: Yes

 ** [retentionInDays](#API_CreateInvestigationGroup_RequestSyntax) **   <a name="cloudwatchinvestigations-CreateInvestigationGroup-request-retentionInDays"></a>
Specify how long that investigation data is kept. For more information, see [Operational investigation data retention](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Retention.html).
If you omit this parameter, the default of 90 days is used.
Type: Long
Valid Range: Minimum value of 7. Maximum value of 90.
Required: No

 ** [roleArn](#API_CreateInvestigationGroup_RequestSyntax) **   <a name="cloudwatchinvestigations-CreateInvestigationGroup-request-roleArn"></a>
Specify the ARN of the IAM role that CloudWatch investigations will use when it gathers investigation data. The permissions in this role determine which of your resources that CloudWatch investigations will have access to during investigations.
For more information, see [How to control what data CloudWatch investigations has access to during investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html#Investigations-Security-Data).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** [tagKeyBoundaries](#API_CreateInvestigationGroup_RequestSyntax) **   <a name="cloudwatchinvestigations-CreateInvestigationGroup-request-tagKeyBoundaries"></a>
Enter the existing custom tag keys for custom applications in your system. Resource tags help CloudWatch investigations narrow the search space when it is unable to discover definite relationships between resources. For example, to discover that an Amazon ECS service depends on an Amazon RDS database, CloudWatch investigations can discover this relationship using data sources such as X-Ray and CloudWatch Application Signals. However, if you haven't deployed these features, CloudWatch investigations will attempt to identify possible relationships. Tag boundaries can be used to narrow the resources that will be discovered by CloudWatch investigations in these cases.
You don't need to enter tags created by myApplications or CloudFormation, because CloudWatch investigations can automatically detect those tags.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]+)`
Required: No

 ** [tags](#API_CreateInvestigationGroup_RequestSyntax) **   <a name="cloudwatchinvestigations-CreateInvestigationGroup-request-tags"></a>
A list of key-value pairs to associate with the investigation group. You can associate as many as 50 tags with an investigation group. To be able to associate tags when you create the investigation group, you must have the `cloudwatch:TagResource` permission.
Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]+)`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## Response Syntax
<a name="API_CreateInvestigationGroup_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string"
}
```

## Response Elements
<a name="API_CreateInvestigationGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateInvestigationGroup_ResponseSyntax) **   <a name="cloudwatchinvestigations-CreateInvestigationGroup-response-arn"></a>
The ARN of the investigation group that you just created.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):aiops:[a-zA-Z0-9-]*:[0-9]{12}:investigation-group\/[A-Za-z0-9]{16}`

## Errors
<a name="API_CreateInvestigationGroup_Errors"></a>

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

 ** ServiceQuotaExceededException **
This request exceeds a service quota.
 ** quotaCode **
This quota that was exceeded.
 ** resourceId **
The resource that caused the quota exception.
 ** resourceType **
The type of resource that caused the quota exception.
 ** serviceCode **
This name of the service associated with the error.
HTTP Status Code: 402

 ** ThrottlingException **
The request was throttled because of quota limits. You can try again later.
HTTP Status Code: 429

 ** ValidationException **
This operation or its parameters aren't formatted correctly.
HTTP Status Code: 400

## Examples
<a name="API_CreateInvestigationGroup_Examples"></a>

### Example
<a name="API_CreateInvestigationGroup_Example_1"></a>

The following example creates an investigation group.

#### Sample Request
<a name="API_CreateInvestigationGroup_Example_1_Request"></a>

```
{
    "name:": "TestInvestigationGroup",
    "roleArn": "arn:aws:iam::123456789012:role/AdminNew",
    "retentionInDays": 30
}
```

## See Also
<a name="API_CreateInvestigationGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/aiops-2018-05-10/CreateInvestigationGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/aiops-2018-05-10/CreateInvestigationGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/aiops-2018-05-10/CreateInvestigationGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/aiops-2018-05-10/CreateInvestigationGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/aiops-2018-05-10/CreateInvestigationGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/aiops-2018-05-10/CreateInvestigationGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/aiops-2018-05-10/CreateInvestigationGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/aiops-2018-05-10/CreateInvestigationGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/aiops-2018-05-10/CreateInvestigationGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/aiops-2018-05-10/CreateInvestigationGroup)
