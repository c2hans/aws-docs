---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_ListAgreementCancellationRequests.html
---

# ListAgreementCancellationRequests
<a name="API_marketplace-agreements_ListAgreementCancellationRequests"></a>

Lists agreement cancellation requests available to you as a seller or buyer. Both sellers (proposers) and buyers (acceptors) can use this operation to find cancellation requests by specifying their party type and applying optional filters.

**Note**
 `PartyType` is a required parameter. A `ValidationException` is returned if `PartyType` is not provided.

## Request Syntax
<a name="API_marketplace-agreements_ListAgreementCancellationRequests_RequestSyntax"></a>

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
<a name="API_marketplace-agreements_ListAgreementCancellationRequests_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [partyType](#API_marketplace-agreements_ListAgreementCancellationRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementCancellationRequests-request-partyType"></a>
The party type for the cancellation requests. Required parameter. Use `Proposer` to list cancellation requests where you are the seller, or `Acceptor` to list cancellation requests where you are the buyer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[A-Za-z]+`
Required: Yes

 ** [agreementId](#API_marketplace-agreements_ListAgreementCancellationRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementCancellationRequests-request-agreementId"></a>
An optional parameter to filter cancellation requests for a specific agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** [agreementType](#API_marketplace-agreements_ListAgreementCancellationRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementCancellationRequests-request-agreementType"></a>
An optional parameter to filter cancellation requests by agreement type (e.g., `PurchaseAgreement`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z]+`
Required: No

 ** [catalog](#API_marketplace-agreements_ListAgreementCancellationRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementCancellationRequests-request-catalog"></a>
An optional parameter to filter cancellation requests by catalog (e.g., `AWSMarketplace`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9.-]+`
Required: No

 ** [maxResults](#API_marketplace-agreements_ListAgreementCancellationRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementCancellationRequests-request-maxResults"></a>
The maximum number of cancellation requests to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_marketplace-agreements_ListAgreementCancellationRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementCancellationRequests-request-nextToken"></a>
A token to specify where to start pagination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`
Required: No

 ** [status](#API_marketplace-agreements_ListAgreementCancellationRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementCancellationRequests-request-status"></a>
An optional parameter to filter cancellation requests by status.
Type: String
Valid Values: `PENDING_APPROVAL | APPROVED | REJECTED | CANCELLED | VALIDATION_FAILED`
Required: No

## Response Syntax
<a name="API_marketplace-agreements_ListAgreementCancellationRequests_ResponseSyntax"></a>

```
{
   "items": [
      {
         "agreementCancellationRequestId": "string",
         "agreementId": "string",
         "agreementType": "string",
         "catalog": "string",
         "createdAt": number,
         "reasonCode": "string",
         "status": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_marketplace-agreements_ListAgreementCancellationRequests_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_marketplace-agreements_ListAgreementCancellationRequests_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementCancellationRequests-response-items"></a>
An array of `AgreementCancellationRequestSummary` objects containing summary information about each cancellation request.
Type: Array of [AgreementCancellationRequestSummary](API_marketplace-agreements_AgreementCancellationRequestSummary.md) objects

 ** [nextToken](#API_marketplace-agreements_ListAgreementCancellationRequests_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementCancellationRequests-response-nextToken"></a>
The token used for pagination. The field is `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`

## Errors
<a name="API_marketplace-agreements_ListAgreementCancellationRequests_Errors"></a>

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
<a name="API_marketplace-agreements_ListAgreementCancellationRequests_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_ListAgreementCancellationRequests_Example_1"></a>

This example illustrates one usage of ListAgreementCancellationRequests.

```
{
    "partyType": "Proposer",
    "maxResults": 10
}
```

### Sample response
<a name="API_marketplace-agreements_ListAgreementCancellationRequests_Example_2"></a>

This example illustrates one usage of ListAgreementCancellationRequests.

```
{
    "items": [
        {
            "agreementCancellationRequestId": "acr-EXAMPLEsgew33rhsds",
            "agreementId": "agmt-EXAMPLE752jqvg74yo7k",
            "status": "PENDING_APPROVAL",
            "reasonCode": "OTHER",
            "agreementType": "PurchaseAgreement",
            "catalog": "AWSMarketplace",
            "createdAt": 1736935800,
            "updatedAt": 1737022200
        }
    ]
}
```

## See Also
<a name="API_marketplace-agreements_ListAgreementCancellationRequests_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/ListAgreementCancellationRequests)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/ListAgreementCancellationRequests)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/ListAgreementCancellationRequests)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/ListAgreementCancellationRequests)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ListAgreementCancellationRequests)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/ListAgreementCancellationRequests)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/ListAgreementCancellationRequests)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/ListAgreementCancellationRequests)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/ListAgreementCancellationRequests)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/ListAgreementCancellationRequests)
