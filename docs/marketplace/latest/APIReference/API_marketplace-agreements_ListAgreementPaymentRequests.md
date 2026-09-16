---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_ListAgreementPaymentRequests.html
---

# ListAgreementPaymentRequests
<a name="API_marketplace-agreements_ListAgreementPaymentRequests"></a>

Lists payment requests available to you as a seller or buyer. Both sellers (proposers) and buyers (acceptors) can use this operation to find payment requests by specifying their party type and applying optional parameters.

**Note**
 `PartyType` is a required parameter. A `ValidationException` is returned if `PartyType` is not provided. Pagination is supported through `maxResults` (1-50, default 50) and `nextToken` parameters.

## Request Syntax
<a name="API_marketplace-agreements_ListAgreementPaymentRequests_RequestSyntax"></a>

```
{
   "agreementId": "{{string}}",
   "agreementType": "{{string}}",
   "catalog": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "partyType": "{{string}}",
   "status": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_ListAgreementPaymentRequests_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [partyType](#API_marketplace-agreements_ListAgreementPaymentRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementPaymentRequests-request-partyType"></a>
The party type for the payment requests. Required parameter. Use `Proposer` to list payment requests where you are the seller, or `Acceptor` to list payment requests where you are the buyer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[A-Za-z]+`
Required: Yes

 ** [agreementId](#API_marketplace-agreements_ListAgreementPaymentRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementPaymentRequests-request-agreementId"></a>
An optional parameter to list payment requests for a specific agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** [agreementType](#API_marketplace-agreements_ListAgreementPaymentRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementPaymentRequests-request-agreementType"></a>
An optional parameter to list payment requests by agreement type (e.g., `PurchaseAgreement`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z]+`
Required: No

 ** [catalog](#API_marketplace-agreements_ListAgreementPaymentRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementPaymentRequests-request-catalog"></a>
An optional parameter to list payment requests by catalog (e.g., `AWSMarketplace`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9.-]+`
Required: No

 ** [maxResults](#API_marketplace-agreements_ListAgreementPaymentRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementPaymentRequests-request-maxResults"></a>
The maximum number of payment requests to return in a single response (1-50). Default is 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_marketplace-agreements_ListAgreementPaymentRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementPaymentRequests-request-nextToken"></a>
A token to specify where to start pagination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`
Required: No

 ** [status](#API_marketplace-agreements_ListAgreementPaymentRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementPaymentRequests-request-status"></a>
An optional parameter to list payment requests by status. Valid values include `VALIDATING`, `VALIDATION_FAILED`, `PENDING_APPROVAL`, `APPROVED`, `REJECTED`, and `CANCELLED`.
Type: String
Valid Values: `VALIDATING | VALIDATION_FAILED | PENDING_APPROVAL | APPROVED | REJECTED | CANCELLED`
Required: No

## Response Syntax
<a name="API_marketplace-agreements_ListAgreementPaymentRequests_ResponseSyntax"></a>

```
{
   "items": [
      {
         "agreementId": "string",
         "chargeAmount": "string",
         "chargeId": "string",
         "createdAt": number,
         "currencyCode": "string",
         "name": "string",
         "paymentRequestId": "string",
         "status": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_marketplace-agreements_ListAgreementPaymentRequests_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_marketplace-agreements_ListAgreementPaymentRequests_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementPaymentRequests-response-items"></a>
An array of `PaymentRequestSummary` objects containing summary information about each payment request.
Type: Array of [PaymentRequestSummary](API_marketplace-agreements_PaymentRequestSummary.md) objects

 ** [nextToken](#API_marketplace-agreements_ListAgreementPaymentRequests_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementPaymentRequests-response-nextToken"></a>
The token used for pagination. The field is `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`

## Errors
<a name="API_marketplace-agreements_ListAgreementPaymentRequests_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** message **
Description of the error.
 ** reason **
The reason for the access denied exception.
 ** requestId **
The unique identifier for the error.
HTTP Status Code: 400

 ** InternalServerException **
Unexpected error during processing of request.
 ** message **
Description of the error.
 ** requestId **
The unique identifier for the error.
HTTP Status Code: 500

 ** ThrottlingException **
Request was denied due to request throttling.
 ** message **
Description of the error.
 ** requestId **
The unique identifier for the error.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fields **
The fields associated with the error.
 ** message **
Description of the error.
 ** reason **
The reason associated with the error.
 ** requestId **
The unique identifier associated with the error.
HTTP Status Code: 400

## Examples
<a name="API_marketplace-agreements_ListAgreementPaymentRequests_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_ListAgreementPaymentRequests_Example_1"></a>

This example illustrates one usage of ListAgreementPaymentRequests.

```
{
    "partyType": "Proposer",
    "status": "PENDING_APPROVAL",
    "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95",
    "maxResults": 10
}
```

### Sample response
<a name="API_marketplace-agreements_ListAgreementPaymentRequests_Example_2"></a>

This example illustrates one usage of ListAgreementPaymentRequests.

```
{
    "items": [
        {
            "paymentRequestId": "prEXAMPLE-1bb7-5f53-9826-7b2EXAMPLE06",
            "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95",
            "status": "PENDING_APPROVAL",
            "name": "Q1 2024 Usage Charges",
            "chargeId": null,
            "chargeAmount": "1250.50",
            "currencyCode": "USD",
            "createdAt": 1705314600,
            "updatedAt": 1705314600
        },
        {
            "paymentRequestId": "prEXAMPLE-2cc8-6h64-0937-8c3EXAMPLE17",
            "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95",
            "status": "APPROVED",
            "name": "Q4 2023 Usage Charges",
            "chargeId": "chEXAMPLE-4dd9-7h75-1048-9d4EXAMPLE28",
            "chargeAmount": "980.25",
            "currencyCode": "USD",
            "createdAt": 1703081700,
            "updatedAt": 1703151000
        }
    ],
    "nextToken": "eyJNYXJrZXIiOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAyfQ=="
}
```

## See Also
<a name="API_marketplace-agreements_ListAgreementPaymentRequests_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/ListAgreementPaymentRequests)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/ListAgreementPaymentRequests)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/ListAgreementPaymentRequests)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/ListAgreementPaymentRequests)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ListAgreementPaymentRequests)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/ListAgreementPaymentRequests)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/ListAgreementPaymentRequests)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/ListAgreementPaymentRequests)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/ListAgreementPaymentRequests)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/ListAgreementPaymentRequests)
