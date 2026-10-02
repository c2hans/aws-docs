---
source_url: https://docs.aws.amazon.com/accounts/latest/APIReference/API_PutContactInformation.html
---

# PutContactInformation
<a name="API_PutContactInformation"></a>

Updates the primary contact information of an AWS account.

Changing the phone number doesn't send a verification code. To verify the new phone number, call [SendPhoneNumberVerification](API_SendPhoneNumberVerification.md).

For complete details about how to use the primary contact operations, see [Update the primary contact for your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-primary.html).

## Request Syntax
<a name="API_PutContactInformation_RequestSyntax"></a>

```
POST /putContactInformation HTTP/1.1
Content-type: application/json

{
   "AccountId": "{{string}}",
   "ContactInformation": {
      "AddressLine1": "{{string}}",
      "AddressLine2": "{{string}}",
      "AddressLine3": "{{string}}",
      "City": "{{string}}",
      "CompanyName": "{{string}}",
      "CountryCode": "{{string}}",
      "DistrictOrCounty": "{{string}}",
      "FullName": "{{string}}",
      "PhoneNumber": "{{string}}",
      "PostalCode": "{{string}}",
      "StateOrRegion": "{{string}}",
      "WebsiteUrl": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_PutContactInformation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutContactInformation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountId](#API_PutContactInformation_RequestSyntax) **   <a name="accounts-PutContactInformation-request-AccountId"></a>
Specifies the 12-digit account ID number of the AWS account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html) enabled for the Account Management service, and optionally a [delegated administrator](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.
The management account can't specify its own `AccountId`. It must call the operation in standalone context by not including the `AccountId` parameter.
To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.
Type: String
Pattern: `\d{12}`
Required: No

 ** [ContactInformation](#API_PutContactInformation_RequestSyntax) **   <a name="accounts-PutContactInformation-request-ContactInformation"></a>
Contains the details of the primary contact information associated with an AWS account.
Type: [ContactInformation](API_ContactInformation.md) object
Required: Yes

## Response Syntax
<a name="API_PutContactInformation_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutContactInformation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutContactInformation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The operation failed because the calling identity doesn't have the minimum required permissions.
 ** errorType **
The value populated to the `x-amzn-ErrorType` response header by API Gateway.
HTTP Status Code: 403

 ** InternalServerException **
The operation failed because of an error internal to AWS. Try your operation again later.
 ** errorType **
The value populated to the `x-amzn-ErrorType` response header by API Gateway.
HTTP Status Code: 500

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

## See Also
<a name="API_PutContactInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/PutContactInformation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/PutContactInformation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/PutContactInformation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/PutContactInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/PutContactInformation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/PutContactInformation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/PutContactInformation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/PutContactInformation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/PutContactInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/PutContactInformation)
