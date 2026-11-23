---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_ListAgreementRequests.html
---

# ListAgreementRequests

Lists agreement requests available to you as a buyer (acceptor). You can filter the results by `catalog`, `status`, and `resourceId`.

## Request Syntax
<a name="API_marketplace-agreements_ListAgreementRequests_RequestSyntax"></a>

```
{
   "catalog": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "resourceId": "{{string}}",
   "status": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_ListAgreementRequests_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [catalog](#API_marketplace-agreements_ListAgreementRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementRequests-request-catalog"></a>
An optional parameter to list agreement requests by catalog (for example, `AWSMarketplace`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9.-]+`
Required: No

 ** [maxResults](#API_marketplace-agreements_ListAgreementRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementRequests-request-maxResults"></a>
The maximum number of agreement requests to return in a single response (1-50). Default is 20.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_marketplace-agreements_ListAgreementRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementRequests-request-nextToken"></a>
A token to specify where to start pagination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`
Required: No

 ** [resourceId](#API_marketplace-agreements_ListAgreementRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementRequests-request-resourceId"></a>
An optional parameter to list agreement requests for a specific resource, such as a product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** [status](#API_marketplace-agreements_ListAgreementRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementRequests-request-status"></a>
An optional parameter to list agreement requests by status. Valid values include `DRAFT`, `PENDING_APPROVAL`, `APPROVED`, `ACCEPTED`, `REJECTED`, and `CANCELLED`. If you don't specify a status, agreement requests of all statuses are returned.
Type: String
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | ACCEPTED | REJECTED | CANCELLED`
Required: No

## Response Syntax
<a name="API_marketplace-agreements_ListAgreementRequests_ResponseSyntax"></a>

```
{
   "items": [
      {
         "agreementId": "string",
         "agreementRequestId": "string",
         "agreementType": "string",
         "proposalSummary": {
            "offerId": "string",
            "offerSetId": "string",
            "resources": [
               {
                  "id": "string",
                  "type": "string"
               }
            ]
         },
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_marketplace-agreements_ListAgreementRequests_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_marketplace-agreements_ListAgreementRequests_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementRequests-response-items"></a>
An array of `AgreementRequestSummary` objects containing summary information about each agreement request.
Type: Array of [AgreementRequestSummary](API_marketplace-agreements_AgreementRequestSummary.md) objects

 ** [nextToken](#API_marketplace-agreements_ListAgreementRequests_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListAgreementRequests-response-nextToken"></a>
The token used for pagination. The field is `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`

## Errors
<a name="API_marketplace-agreements_ListAgreementRequests_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** message **
Description of the error.
 ** reason **
The reason for the access denied exception.
 ** requestId **
The unique identifier for the error.
HTTP Status Code: 403

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
HTTP Status Code: 429

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
<a name="API_marketplace-agreements_ListAgreementRequests_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_ListAgreementRequests_Example_1"></a>

This example illustrates one usage of ListAgreementRequests.

```
{
    "status": "PENDING_APPROVAL",
    "maxResults": 10
}
```

### Sample response
<a name="API_marketplace-agreements_ListAgreementRequests_Example_2"></a>

This example illustrates one usage of ListAgreementRequests.

```
{
    "items": [
        {
            "agreementRequestId": "ar-EXAMPLE4a53-9b12-3d4EXAMPLE78",
            "agreementType": "PurchaseAgreement",
            "status": "PENDING_APPROVAL",
            "proposalSummary": {
                "resources": [
                    {
                        "id": "0EXAMPLE-8ce8-4814-bcf1-636EXAMPLEb5",
                        "type": "SaaSProduct"
                    }
                ],
                "offerId": "ABCDEFGHIJKLMNOP123"
            }
        }
    ],
    "nextToken": null
}
```

## See Also
<a name="API_marketplace-agreements_ListAgreementRequests_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/ListAgreementRequests)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/ListAgreementRequests)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/ListAgreementRequests)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/ListAgreementRequests)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ListAgreementRequests)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/ListAgreementRequests)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/ListAgreementRequests)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/ListAgreementRequests)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/ListAgreementRequests)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/ListAgreementRequests)
