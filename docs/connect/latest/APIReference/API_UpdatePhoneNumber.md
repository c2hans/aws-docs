---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumber.html
---

# UpdatePhoneNumber
<a name="API_UpdatePhoneNumber"></a>

Updates your claimed phone number from its current Connect Customer instance or traffic distribution group to another Connect Customer instance or traffic distribution group in the same AWS Region.

**Important**
After using this API, you must verify that the phone number is attached to the correct flow in the target instance or traffic distribution group. You need to do this because the API switches only the phone number to a new instance or traffic distribution group. It doesn't migrate the flow configuration of the phone number, too.
You can call [DescribePhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribePhoneNumber.html) API to verify the status of a previous [UpdatePhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumber.html) operation.

## Request Syntax
<a name="API_UpdatePhoneNumber_RequestSyntax"></a>

```
PUT /phone-number/{{PhoneNumberId}} HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "InstanceId": "{{string}}",
   "TargetArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdatePhoneNumber_RequestParameters"></a>

The request uses the following URI parameters.

 ** [PhoneNumberId](#API_UpdatePhoneNumber_RequestSyntax) **   <a name="connect-UpdatePhoneNumber-request-uri-PhoneNumberId"></a>
A unique identifier for the phone number.
Required: Yes

## Request Body
<a name="API_UpdatePhoneNumber_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_UpdatePhoneNumber_RequestSyntax) **   <a name="connect-UpdatePhoneNumber-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [InstanceId](#API_UpdatePhoneNumber_RequestSyntax) **   <a name="connect-UpdatePhoneNumber-request-InstanceId"></a>
The identifier of the Connect Customer instance that phone numbers are claimed to. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance. You must enter `InstanceId` or `TargetArn`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [TargetArn](#API_UpdatePhoneNumber_RequestSyntax) **   <a name="connect-UpdatePhoneNumber-request-TargetArn"></a>
The Amazon Resource Name (ARN) for Connect Customer instances or traffic distribution groups that phone number inbound traffic is routed through. You must enter `InstanceId` or `TargetArn`.
Type: String
Required: No

## Response Syntax
<a name="API_UpdatePhoneNumber_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PhoneNumberArn": "string",
   "PhoneNumberId": "string"
}
```

## Response Elements
<a name="API_UpdatePhoneNumber_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PhoneNumberArn](#API_UpdatePhoneNumber_ResponseSyntax) **   <a name="connect-UpdatePhoneNumber-response-PhoneNumberArn"></a>
The Amazon Resource Name (ARN) of the phone number.
Type: String

 ** [PhoneNumberId](#API_UpdatePhoneNumber_ResponseSyntax) **   <a name="connect-UpdatePhoneNumber-response-PhoneNumberId"></a>
A unique identifier for the phone number.
Type: String

## Errors
<a name="API_UpdatePhoneNumber_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** IdempotencyException **
An entity with the same name already exists.
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

 ** ResourceInUseException **
That resource is already in use (for example, you're trying to add a record with the same name as an existing record). If you are trying to delete a resource (for example, DeleteHoursOfOperation or DeletePredefinedAttribute), remove its reference from related resources and then try again.
 ** ResourceId **
The identifier for the resource.
 ** ResourceType **
The type of resource.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdatePhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdatePhoneNumber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdatePhoneNumber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdatePhoneNumber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdatePhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdatePhoneNumber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdatePhoneNumber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdatePhoneNumber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdatePhoneNumber)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdatePhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdatePhoneNumber)
