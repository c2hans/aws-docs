---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ImportPhoneNumber.html
---

# ImportPhoneNumber
<a name="API_ImportPhoneNumber"></a>

Imports a claimed phone number from an external service, such as AWS End User Messaging, into an Connect Customer instance. You can call this API only in the same AWS Region where the Connect Customer instance was created.

**Important**
Call the [DescribePhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribePhoneNumber.html) API to verify the status of a previous `ImportPhoneNumber` operation.

If you plan to claim or import numbers and then release numbers frequently, contact us for a service quota exception. Otherwise, it is possible you will be blocked from claiming and releasing any more numbers until up to 180 days past the oldest number released has expired.

 By default you can claim or import and then release up to 200% of your maximum number of active phone numbers. If you claim or import and then release phone numbers using the UI or API during a rolling 180 day cycle that exceeds 200% of your phone number service level quota, you will be blocked from claiming or importing any more numbers until 180 days past the oldest number released has expired.

For example, if you already have 99 claimed or imported numbers and a service level quota of 99 phone numbers, and in any 180 day period you release 99, claim 99, and then release 99, you will have exceeded the 200% limit. At that point you are blocked from claiming any more numbers until you open an Support ticket.

## Request Syntax
<a name="API_ImportPhoneNumber_RequestSyntax"></a>

```
POST /phone-number/import HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "InstanceId": "{{string}}",
   "PhoneNumberDescription": "{{string}}",
   "SourcePhoneNumberArn": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ImportPhoneNumber_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ImportPhoneNumber_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_ImportPhoneNumber_RequestSyntax) **   <a name="connect-ImportPhoneNumber-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [InstanceId](#API_ImportPhoneNumber_RequestSyntax) **   <a name="connect-ImportPhoneNumber-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [PhoneNumberDescription](#API_ImportPhoneNumber_RequestSyntax) **   <a name="connect-ImportPhoneNumber-request-PhoneNumberDescription"></a>
The description of the phone number.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `^[\W\S_]*`
Required: No

 ** [SourcePhoneNumberArn](#API_ImportPhoneNumber_RequestSyntax) **   <a name="connect-ImportPhoneNumber-request-SourcePhoneNumberArn"></a>
The claimed phone number ARN being imported from the external service, such as AWS End User Messaging. If it is from AWS End User Messaging, it looks like the ARN of the phone number to import from AWS End User Messaging.
Type: String
Required: Yes

 ** [Tags](#API_ImportPhoneNumber_RequestSyntax) **   <a name="connect-ImportPhoneNumber-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_ImportPhoneNumber_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PhoneNumberArn": "string",
   "PhoneNumberId": "string"
}
```

## Response Elements
<a name="API_ImportPhoneNumber_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PhoneNumberArn](#API_ImportPhoneNumber_ResponseSyntax) **   <a name="connect-ImportPhoneNumber-response-PhoneNumberArn"></a>
The Amazon Resource Name (ARN) of the phone number.
Type: String

 ** [PhoneNumberId](#API_ImportPhoneNumber_ResponseSyntax) **   <a name="connect-ImportPhoneNumber-response-PhoneNumberId"></a>
A unique identifier for the phone number.
Type: String

## Errors
<a name="API_ImportPhoneNumber_Errors"></a>

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
<a name="API_ImportPhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ImportPhoneNumber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ImportPhoneNumber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ImportPhoneNumber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ImportPhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ImportPhoneNumber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ImportPhoneNumber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ImportPhoneNumber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ImportPhoneNumber)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ImportPhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ImportPhoneNumber)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
