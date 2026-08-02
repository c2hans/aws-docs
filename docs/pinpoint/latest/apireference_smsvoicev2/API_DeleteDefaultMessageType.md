---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteDefaultMessageType.html
---

# DeleteDefaultMessageType
<a name="API_DeleteDefaultMessageType"></a>

Deletes an existing default message type on a configuration set.

 A message type is a type of messages that you plan to send. If you send account-related messages or time-sensitive messages such as one-time passcodes, choose **Transactional**. If you plan to send messages that contain marketing material or other promotional content, choose **Promotional**. This setting applies to your entire AWS account.

## Request Syntax
<a name="API_DeleteDefaultMessageType_RequestSyntax"></a>

```
{
   "ConfigurationSetName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDefaultMessageType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationSetName](#API_DeleteDefaultMessageType_RequestSyntax) **   <a name="pinpoint-DeleteDefaultMessageType-request-ConfigurationSetName"></a>
The name of the configuration set or the configuration set Amazon Resource Name (ARN) to delete the default message type from. The ConfigurationSetName and ConfigurationSetArn can be found using the [DescribeConfigurationSets](API_DescribeConfigurationSets.md) action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteDefaultMessageType_ResponseSyntax"></a>

```
{
   "ConfigurationSetArn": "string",
   "ConfigurationSetName": "string",
   "MessageType": "string"
}
```

## Response Elements
<a name="API_DeleteDefaultMessageType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationSetArn](#API_DeleteDefaultMessageType_ResponseSyntax) **   <a name="pinpoint-DeleteDefaultMessageType-response-ConfigurationSetArn"></a>
The Amazon Resource Name (ARN) of the configuration set.
Type: String

 ** [ConfigurationSetName](#API_DeleteDefaultMessageType_ResponseSyntax) **   <a name="pinpoint-DeleteDefaultMessageType-response-ConfigurationSetName"></a>
The name of the configuration set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

 ** [MessageType](#API_DeleteDefaultMessageType_ResponseSyntax) **   <a name="pinpoint-DeleteDefaultMessageType-response-MessageType"></a>
The current message type for the configuration set.
Type: String
Valid Values: `TRANSACTIONAL | PROMOTIONAL`

## Errors
<a name="API_DeleteDefaultMessageType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because you don't have sufficient permissions to access the resource.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

 ** InternalServerException **
The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
 ** RequestId **
The unique identifier of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A requested resource couldn't be found.
 ** ResourceId **
The unique identifier of the resource.
 ** ResourceType **
The type of resource that caused the exception.
HTTP Status Code: 400

 ** ThrottlingException **
An error that occurred because too many requests were sent during a certain amount of time.
HTTP Status Code: 400

 ** ValidationException **
A validation exception for a field.
 ** Fields **
The field that failed validation.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDefaultMessageType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DeleteDefaultMessageType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DeleteDefaultMessageType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DeleteDefaultMessageType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DeleteDefaultMessageType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DeleteDefaultMessageType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DeleteDefaultMessageType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DeleteDefaultMessageType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DeleteDefaultMessageType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DeleteDefaultMessageType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DeleteDefaultMessageType)
