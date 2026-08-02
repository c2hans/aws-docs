---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateEmailAddress.html
---

# CreateEmailAddress
<a name="API_CreateEmailAddress"></a>

Create new email address in the specified Connect Customer instance. For more information about email addresses, see [Create email addresses](https://docs.aws.amazon.com/connect/latest/adminguide/create-email-address1.html) in the Connect Customer Administrator Guide.

## Request Syntax
<a name="API_CreateEmailAddress_RequestSyntax"></a>

```
PUT /email-addresses/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "DisplayName": "{{string}}",
   "EmailAddress": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateEmailAddress_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateEmailAddress_RequestSyntax) **   <a name="connect-CreateEmailAddress-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateEmailAddress_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateEmailAddress_RequestSyntax) **   <a name="connect-CreateEmailAddress-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Description](#API_CreateEmailAddress_RequestSyntax) **   <a name="connect-CreateEmailAddress-request-Description"></a>
The description of the email address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [DisplayName](#API_CreateEmailAddress_RequestSyntax) **   <a name="connect-CreateEmailAddress-request-DisplayName"></a>
The display name of email address
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [EmailAddress](#API_CreateEmailAddress_RequestSyntax) **   <a name="connect-CreateEmailAddress-request-EmailAddress"></a>
The email address, including the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^\s@]+@[^\s@]+\.[^\s@]+`
Required: Yes

 ** [Tags](#API_CreateEmailAddress_RequestSyntax) **   <a name="connect-CreateEmailAddress-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateEmailAddress_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EmailAddressArn": "string",
   "EmailAddressId": "string"
}
```

## Response Elements
<a name="API_CreateEmailAddress_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EmailAddressArn](#API_CreateEmailAddress_ResponseSyntax) **   <a name="connect-CreateEmailAddress-response-EmailAddressArn"></a>
The Amazon Resource Name (ARN) of the email address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [EmailAddressId](#API_CreateEmailAddress_ResponseSyntax) **   <a name="connect-CreateEmailAddress-response-EmailAddressId"></a>
The identifier of the email address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

## Errors
<a name="API_CreateEmailAddress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

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

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceConflictException **
A resource already has that name.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateEmailAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateEmailAddress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateEmailAddress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateEmailAddress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateEmailAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateEmailAddress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateEmailAddress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateEmailAddress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateEmailAddress)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateEmailAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateEmailAddress)
