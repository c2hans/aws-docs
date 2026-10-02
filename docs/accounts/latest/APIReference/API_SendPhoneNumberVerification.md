---
source_url: https://docs.aws.amazon.com/accounts/latest/APIReference/API_SendPhoneNumberVerification.html
---

# SendPhoneNumberVerification
<a name="API_SendPhoneNumberVerification"></a>

Sends a one-time passcode (OTP) by SMS to the primary contact phone number that is currently associated with the specified AWS account, to begin verifying that phone number. You do not supply a phone number in the request; the operation uses the number currently on file for the account. To use this operation, you must have the `account:SendPhoneNumberVerification` IAM permission. After the code is delivered, call [VerifyPhoneNumber](API_VerifyPhoneNumber.md) with that code to complete verification.

For complete details about how to use the primary contact operations, see [Update the primary contact for your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-primary.html).

## Request Syntax
<a name="API_SendPhoneNumberVerification_RequestSyntax"></a>

```
POST /sendPhoneNumberVerification HTTP/1.1
Content-type: application/json

{
   "AccountId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SendPhoneNumberVerification_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SendPhoneNumberVerification_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountId](#API_SendPhoneNumberVerification_RequestSyntax) **   <a name="accounts-SendPhoneNumberVerification-request-AccountId"></a>
Specifies the 12 digit account ID number of the AWS account that you want to access or modify with this operation.
If you do not specify this parameter, it defaults to the AWS account of the identity used to call the operation.
To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html) enabled for the Account Management service, and optionally a [delegated administrator](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.
The management account can't specify its own `AccountId`; it must call the operation in standalone context by not including the `AccountId` parameter.
To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.
Type: String
Pattern: `\d{12}`
Required: No

## Response Syntax
<a name="API_SendPhoneNumberVerification_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Status": "string"
}
```

## Response Elements
<a name="API_SendPhoneNumberVerification_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Status](#API_SendPhoneNumberVerification_ResponseSyntax) **   <a name="accounts-SendPhoneNumberVerification-response-Status"></a>
The verification status of the phone number. On a successful call, the value is `PENDING`: a verification code has been sent to the account's primary contact phone number and is awaiting entry through [VerifyPhoneNumber](API_VerifyPhoneNumber.md).
Type: String
Valid Values: `PENDING | VERIFIED | UNVERIFIED | NOT_SUPPORTED`

## Errors
<a name="API_SendPhoneNumberVerification_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The operation failed because the calling identity doesn't have the minimum required permissions.
 ** errorType **
The value populated to the `x-amzn-ErrorType` response header by API Gateway.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of a conflict in the current status of the resource. This happens in cases such as the following:
+ You try to enable a Region that is currently being disabled (in a status of DISABLING).
+ You try to change an account’s root user email to an email address that is already in use.
+ The primary contact phone number changes after you call `SendPhoneNumberVerification` and before you call `VerifyPhoneNumber`.
 ** errorType **
The value populated to the `x-amzn-ErrorType` response header by API Gateway.
HTTP Status Code: 409

 ** InternalServerException **
The operation failed because of an error internal to AWS. Try your operation again later.
 ** errorType **
The value populated to the `x-amzn-ErrorType` response header by API Gateway.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation failed because it specified a resource that can't be found.
 ** errorType **
The value populated to the `x-amzn-ErrorType` response header by API Gateway.
HTTP Status Code: 404

 ** TooManyRequestsException **
The operation failed because it was called too frequently and exceeded a throttle limit.
 ** errorType **
The value populated to the `x-amzn-ErrorType` response header by API Gateway.
HTTP Status Code: 429

 ** ValidationException **
The operation failed because one of the input parameters was invalid.
 ** fieldList **
The field where the invalid entry was detected.
 ** message **
The message that informs you about what was invalid about the request.
 ** reason **
The reason that validation failed.
HTTP Status Code: 400

## Examples
<a name="API_SendPhoneNumberVerification_Examples"></a>

### Example 1
<a name="API_SendPhoneNumberVerification_Example_1"></a>

The following example sends a verification code to the primary contact phone number of the account whose credentials are used to call the operation.

#### Sample Request
<a name="API_SendPhoneNumberVerification_Example_1_Request"></a>

```
POST / HTTP/1.1
X-Amz-Target: AWSAccountV20210201.SendPhoneNumberVerification

{}
```

#### Sample Response
<a name="API_SendPhoneNumberVerification_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json

{
   "Status": "PENDING"
}
```

### Example 2
<a name="API_SendPhoneNumberVerification_Example_2"></a>

The following example sends a verification code for the specified member account in an organization. The code is sent to the primary contact phone number of the member account. You must use credentials from either the organization's management account or from the Account Management service's delegated admin account.

#### Sample Request
<a name="API_SendPhoneNumberVerification_Example_2_Request"></a>

```
POST / HTTP/1.1
X-Amz-Target: AWSAccountV20210201.SendPhoneNumberVerification

{
   "AccountId": "123456789012"
}
```

#### Sample Response
<a name="API_SendPhoneNumberVerification_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json

{
   "Status": "PENDING"
}
```

## See Also
<a name="API_SendPhoneNumberVerification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/SendPhoneNumberVerification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/SendPhoneNumberVerification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/SendPhoneNumberVerification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/SendPhoneNumberVerification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/SendPhoneNumberVerification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/SendPhoneNumberVerification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/SendPhoneNumberVerification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/SendPhoneNumberVerification)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/SendPhoneNumberVerification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/SendPhoneNumberVerification)
