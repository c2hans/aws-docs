---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_AddNotificationChannel.html
---

# AddNotificationChannel
<a name="API_AddNotificationChannel"></a>

 Adds a notification channel to DevOps Guru. A notification channel is used to notify you about important DevOps Guru events, such as when an insight is generated.

If you use an Amazon SNS topic in another account, you must attach a policy to it that grants DevOps Guru permission to send it notifications. DevOps Guru adds the required policy on your behalf to send notifications using Amazon SNS in your account. DevOps Guru only supports standard SNS topics. For more information, see [Permissions for Amazon SNS topics](https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-required-permissions.html).

If you use an Amazon SNS topic that is encrypted by an AWS Key Management Service customer-managed key (CMK), then you must add permissions to the CMK. For more information, see [Permissions for AWS KMS–encrypted Amazon SNS topics](https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-kms-permissions.html).

## Request Syntax
<a name="API_AddNotificationChannel_RequestSyntax"></a>

```
PUT /channels HTTP/1.1
Content-type: application/json

{
   "Config": {
      "Filters": {
         "MessageTypes": [ "{{string}}" ],
         "Severities": [ "{{string}}" ]
      },
      "Sns": {
         "TopicArn": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_AddNotificationChannel_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AddNotificationChannel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Config](#API_AddNotificationChannel_RequestSyntax) **   <a name="DevOpsGuru-AddNotificationChannel-request-Config"></a>
 A `NotificationChannelConfig` object that specifies what type of notification channel to add. The one supported notification channel is Amazon Simple Notification Service (Amazon SNS).
Type: [NotificationChannelConfig](API_NotificationChannelConfig.md) object
Required: Yes

## Response Syntax
<a name="API_AddNotificationChannel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Id": "string"
}
```

## Response Elements
<a name="API_AddNotificationChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Id](#API_AddNotificationChannel_ResponseSyntax) **   <a name="DevOpsGuru-AddNotificationChannel-response-Id"></a>
 The ID of the added notification channel.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

## Errors
<a name="API_AddNotificationChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.
HTTP Status Code: 403

 ** ConflictException **
 An exception that is thrown when a conflict occurs.
 ** ResourceId **
 The ID of the AWS resource in which a conflict occurred.
 ** ResourceType **
 The type of the AWS resource in which a conflict occurred.
HTTP Status Code: 409

 ** InternalServerException **
An internal failure in an Amazon service occurred.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the internal server exception can be retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A requested resource could not be found
 ** ResourceId **
 The ID of the AWS resource that could not be found.
 ** ResourceType **
 The type of the AWS resource that could not be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request contains a value that exceeds a maximum quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to a request throttling.
 ** QuotaCode **
 The code of the quota that was exceeded, causing the throttling exception.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the throttling exception can be retried.
 ** ServiceCode **
 The code of the service that caused the throttling exception.
HTTP Status Code: 429

 ** ValidationException **
 Contains information about data passed in to a field during a request that is not valid.
 ** Fields **
 An array of fields that are associated with the validation exception.
 ** Message **
 A message that describes the validation exception.
 ** Reason **
 The reason the validation exception was thrown.
HTTP Status Code: 400

## See Also
<a name="API_AddNotificationChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-guru-2020-12-01/AddNotificationChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-guru-2020-12-01/AddNotificationChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/AddNotificationChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-guru-2020-12-01/AddNotificationChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/AddNotificationChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-guru-2020-12-01/AddNotificationChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-guru-2020-12-01/AddNotificationChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-guru-2020-12-01/AddNotificationChannel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-guru-2020-12-01/AddNotificationChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/AddNotificationChannel)
