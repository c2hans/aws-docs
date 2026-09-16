---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimPhoneNumber.html
---

# ClaimPhoneNumber
<a name="API_ClaimPhoneNumber"></a>

Claims an available phone number to your Connect Customer instance or traffic distribution group. You can call this API only in the same AWS Region where the Connect Customer instance or traffic distribution group was created.

For more information about how to use this operation, see [Claim a phone number in your country](https://docs.aws.amazon.com/connect/latest/adminguide/claim-phone-number.html) and [Claim phone numbers to traffic distribution groups](https://docs.aws.amazon.com/connect/latest/adminguide/claim-phone-numbers-traffic-distribution-groups.html) in the *Connect Customer Administrator Guide*.

**Important**
You can call the [SearchAvailablePhoneNumbers](https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchAvailablePhoneNumbers.html) API for available phone numbers that you can claim. Call the [DescribePhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribePhoneNumber.html) API to verify the status of a previous [ClaimPhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimPhoneNumber.html) operation.

If you plan to claim and release numbers frequently, contact us for a service quota exception. Otherwise, it is possible you will be blocked from claiming and releasing any more numbers until up to 180 days past the oldest number released has expired.

By default you can claim and release up to 200% of your maximum number of active phone numbers. If you claim and release phone numbers using the UI or API during a rolling 180 day cycle that exceeds 200% of your phone number service level quota, you will be blocked from claiming any more numbers until 180 days past the oldest number released has expired.

For example, if you already have 99 claimed numbers and a service level quota of 99 phone numbers, and in any 180 day period you release 99, claim 99, and then release 99, you will have exceeded the 200% limit. At that point you are blocked from claiming any more numbers until you open an AWS support ticket.

## Request Syntax
<a name="API_ClaimPhoneNumber_RequestSyntax"></a>

```
POST /phone-number/claim HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "InstanceId": "{{string}}",
   "PhoneNumber": "{{string}}",
   "PhoneNumberDescription": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "TargetArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ClaimPhoneNumber_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ClaimPhoneNumber_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_ClaimPhoneNumber_RequestSyntax) **   <a name="connect-ClaimPhoneNumber-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [InstanceId](#API_ClaimPhoneNumber_RequestSyntax) **   <a name="connect-ClaimPhoneNumber-request-InstanceId"></a>
The identifier of the Connect Customer instance that phone numbers are claimed to. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance. You must enter `InstanceId` or `TargetArn`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [PhoneNumber](#API_ClaimPhoneNumber_RequestSyntax) **   <a name="connect-ClaimPhoneNumber-request-PhoneNumber"></a>
The phone number you want to claim. Phone numbers are formatted `[+] [country code] [subscriber number including area code]`.
Type: String
Pattern: `\\+[1-9]\\d{1,14}$`
Required: Yes

 ** [PhoneNumberDescription](#API_ClaimPhoneNumber_RequestSyntax) **   <a name="connect-ClaimPhoneNumber-request-PhoneNumberDescription"></a>
The description of the phone number.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `^[\W\S_]*`
Required: No

 ** [Tags](#API_ClaimPhoneNumber_RequestSyntax) **   <a name="connect-ClaimPhoneNumber-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [TargetArn](#API_ClaimPhoneNumber_RequestSyntax) **   <a name="connect-ClaimPhoneNumber-request-TargetArn"></a>
The Amazon Resource Name (ARN) for Connect Customer instances or traffic distribution groups that phone number inbound traffic is routed through. You must enter `InstanceId` or `TargetArn`.
Type: String
Required: No

## Response Syntax
<a name="API_ClaimPhoneNumber_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PhoneNumberArn": "string",
   "PhoneNumberId": "string"
}
```

## Response Elements
<a name="API_ClaimPhoneNumber_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PhoneNumberArn](#API_ClaimPhoneNumber_ResponseSyntax) **   <a name="connect-ClaimPhoneNumber-response-PhoneNumberArn"></a>
The Amazon Resource Name (ARN) of the phone number.
Type: String

 ** [PhoneNumberId](#API_ClaimPhoneNumber_ResponseSyntax) **   <a name="connect-ClaimPhoneNumber-response-PhoneNumberId"></a>
A unique identifier for the phone number.
Type: String

## Errors
<a name="API_ClaimPhoneNumber_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ClaimPhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ClaimPhoneNumber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ClaimPhoneNumber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ClaimPhoneNumber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ClaimPhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ClaimPhoneNumber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ClaimPhoneNumber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ClaimPhoneNumber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ClaimPhoneNumber)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ClaimPhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ClaimPhoneNumber)
