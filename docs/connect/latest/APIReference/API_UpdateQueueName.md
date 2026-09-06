---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateQueueName.html
---

# UpdateQueueName
<a name="API_UpdateQueueName"></a>

Updates the name and description of a queue. At least `Name` or `Description` must be provided.

## Request Syntax
<a name="API_UpdateQueueName_RequestSyntax"></a>

```
POST /queues/{{InstanceId}}/{{QueueId}}/name HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateQueueName_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_UpdateQueueName_RequestSyntax) **   <a name="connect-UpdateQueueName-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [QueueId](#API_UpdateQueueName_RequestSyntax) **   <a name="connect-UpdateQueueName-request-uri-QueueId"></a>
The identifier for the queue.
Required: Yes

## Request Body
<a name="API_UpdateQueueName_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateQueueName_RequestSyntax) **   <a name="connect-UpdateQueueName-request-Description"></a>
The description of the queue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

 ** [Name](#API_UpdateQueueName_RequestSyntax) **   <a name="connect-UpdateQueueName-request-Name"></a>
The name of the queue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: No

## Response Syntax
<a name="API_UpdateQueueName_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateQueueName_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateQueueName_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateQueueName_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateQueueName)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateQueueName)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateQueueName)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateQueueName)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateQueueName)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateQueueName)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateQueueName)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateQueueName)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateQueueName)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateQueueName)
