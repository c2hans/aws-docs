---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_ListAgreementCharges.html
---

# ListAgreementCharges
<a name="API_marketplace-agreements_ListAgreementCharges"></a>

Allows acceptors to view charges and purchase orders that are associated with an agreement. The response includes details about all charges regardless of whether a purchase order is linked to each charge.

## Request Syntax
<a name="API_marketplace-agreements_ListAgreementCharges_RequestSyntax"></a>

```
{
   "agreementId": "{{string}}",
   "agreementType": "{{string}}",
   "catalog": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_ListAgreementCharges_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementId](#API_marketplace-agreements_ListAgreementCharges_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementCharges-request-agreementId"></a>
The unique identifier of the agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** [agreementType](#API_marketplace-agreements_ListAgreementCharges_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementCharges-request-agreementType"></a>
Filter to retrieve charges of a specific agreement type (for example, `PurchaseAgreement`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z]+`
Required: No

 ** [catalog](#API_marketplace-agreements_ListAgreementCharges_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementCharges-request-catalog"></a>
The catalog in which the charges were created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9.-]+`
Required: No

 ** [maxResults](#API_marketplace-agreements_ListAgreementCharges_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementCharges-request-maxResults"></a>
The maximum number of charges to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_marketplace-agreements_ListAgreementCharges_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementCharges-request-nextToken"></a>
A token to specify where to start pagination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`
Required: No

## Response Syntax
<a name="API_marketplace-agreements_ListAgreementCharges_ResponseSyntax"></a>

```
{
   "items": [
      {
         "agreementId": "string",
         "agreementType": "string",
         "amount": "string",
         "currencyCode": "string",
         "id": "string",
         "purchaseOrderReference": "string",
         "revision": number,
         "time": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_marketplace-agreements_ListAgreementCharges_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_marketplace-agreements_ListAgreementCharges_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementCharges-response-items"></a>
A list of agreement charges.
Type: Array of [Charge](API_marketplace-agreements_Charge.md) objects

 ** [nextToken](#API_marketplace-agreements_ListAgreementCharges_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementCharges-response-nextToken"></a>
The token used for pagination. The field is `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`

## Errors
<a name="API_marketplace-agreements_ListAgreementCharges_Errors"></a>

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
<a name="API_marketplace-agreements_ListAgreementCharges_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_ListAgreementCharges_Example_1"></a>

This example illustrates one usage of ListAgreementCharges.

```
{
    "catalog": "AWSMarketplace",
    "maxResults": 20,
    "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95"
}
```

### Sample response
<a name="API_marketplace-agreements_ListAgreementCharges_Example_2"></a>

This example illustrates one usage of ListAgreementCharges.

```
{
    "items": [
        {
            "id": "chEXAMPLE-1aa7-4b42-9614-5c3EXAMPLE56",
            "revision": 1,
            "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95",
            "agreementType": "PurchaseAgreement",
            "purchaseOrderReference": "PO-123",
            "currencyCode": "USD",
            "amount": "100.00",
            "time": "2024-07-15T14:30:00Z"
        },
        {
            "id": "chEXAMPLE-2bb8-5c53-0725-6d4EXAMPLE67",
            "revision": 1,
            "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95",
            "agreementType": "PurchaseAgreement",
            "currencyCode": "USD",
            "amount": "50.00",
            "time": "2024-08-15T14:30:00Z"
        }
    ],
    "nextToken": "eyJhbGciOiJIUzI1NiJ9..."
}
```

## See Also
<a name="API_marketplace-agreements_ListAgreementCharges_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/ListAgreementCharges)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/ListAgreementCharges)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/ListAgreementCharges)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/ListAgreementCharges)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ListAgreementCharges)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/ListAgreementCharges)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/ListAgreementCharges)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/ListAgreementCharges)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/ListAgreementCharges)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/ListAgreementCharges)
