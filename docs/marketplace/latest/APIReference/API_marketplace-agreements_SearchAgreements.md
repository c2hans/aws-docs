---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_SearchAgreements.html
---

# SearchAgreements
<a name="API_marketplace-agreements_SearchAgreements"></a>

Searches across all agreements that a proposer or an acceptor has in AWS Marketplace. The search returns a list of agreements with basic agreement information.

## Request Syntax
<a name="API_marketplace-agreements_SearchAgreements_RequestSyntax"></a>

```
{
   "catalog": "{{string}}",
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sort": {
      "sortBy": "{{string}}",
      "sortOrder": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_marketplace-agreements_SearchAgreements_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [catalog](#API_marketplace-agreements_SearchAgreements_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SearchAgreements-request-catalog"></a>
The catalog in which the agreement was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9.-]+`
Required: No

 ** [filters](#API_marketplace-agreements_SearchAgreements_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SearchAgreements-request-filters"></a>
The filter name and value pair used to return a specific list of results.
The following filters are supported:
+  `ResourceIdentifier` – The unique identifier of the resource.
+  `ResourceType` – Type of the resource, which is the product (`AmiProduct`, `ContainerProduct`, `SaaSProduct`, `ProfessionalServicesProduct`, or `MachineLearningProduct`).
+  `PartyType` – The party type of the caller. Use `Proposer` or `Acceptor`.
+  `AcceptorAccountId` – The AWS account ID of the party accepting the agreement terms.
+  `OfferId` – The unique identifier of the offer in which the terms are registered in the agreement token.
+  `Status` – The current status of the agreement. Values include `ACTIVE`, `CANCELLED`, `EXPIRED`, `RENEWED`, `REPLACED`, and `TERMINATED`.
+  `BeforeEndTime` – A date used to filter agreements with a date before the `endTime` of an agreement.
+  `AfterEndTime` – A date used to filter agreements with a date after the `endTime` of an agreement.
+  `BeforeStartTime` – A date used to filter agreements with a date before the `startTime` of an agreement.
+  `AfterStartTime` – A date used to filter agreements with a date after the `startTime` of an agreement.
+  `BeforeLastUpdateTime` – A date used to filter agreements with a date before the `lastUpdateTime` of an agreement.
+  `AfterLastUpdateTime` – A date used to filter agreements with a date after the `lastUpdateTime` of an agreement.
+  `AgreementType` – The type of agreement. Supported value includes `PurchaseAgreement`.
+  `OfferSetId` – A unique identifier for the offer set containing this offer. All agreements created from offers in this set include this identifier as context.
+  `EndTimeBehaviorType` – What happens to the agreement when it reaches its end date. Values include `RENEW`, `REPLACE`, and `EXPIRE`.
+  `EndTimeBehaviorReasonCode` – The reason why the agreement doesn't renew at its end date. Values include `PROPOSER_RENEW_OPTED_OUT`, `ACCEPTOR_RENEW_OPTED_OUT`, `NO_RENEWAL_TERM`, and `RENEWAL_LIMIT_EXHAUSTED`.
+  `InitialAgreementId` – The unique identifier of the very first agreement in a chain of related agreements. Use this filter to return every agreement in the same chain.
+  `LicenseArn` – The Amazon Resource Name (ARN) of the AWS License Manager license associated with an entitlement granted by the agreement.
A proposer can use any combination of the preceding filters along with `AgreementType`, which is required.
The following filter combinations are supported when the `PartyType` is `Acceptor`:
+  `AgreementType`
+  `AgreementType` \+ `Status`
+  `AgreementType` \+ `EndTime`
+  `AgreementType` \+ `Status` \+ `EndTime`
+  `AgreementType` \+ `ResourceIdentifier`
+  `AgreementType` \+ `ResourceIdentifier` \+ `EndTime`
+  `AgreementType` \+ `ResourceIdentifier` \+ `Status`
+  `AgreementType` \+ `ResourceIdentifier` \+ `Status` \+ `EndTime`
+  `AgreementType` \+ `ResourceType`
+  `AgreementType` \+ `ResourceType` \+ `EndTime`
+  `AgreementType` \+ `OfferId`
+  `AgreementType` \+ `OfferId` \+ `EndTime`
+  `AgreementType` \+ `OfferId` \+ `Status`
+  `AgreementType` \+ `OfferId` \+ `Status` \+ `EndTime`
+  `AgreementType` \+ `OfferSetId`
+  `AgreementType` \+ `OfferSetId` \+ `EndTime`
+  `AgreementType` \+ `OfferSetId` \+ `Status`
+  `AgreementType` \+ `OfferSetId` \+ `Status` \+ `EndTime`
To filter by `EndTime`, you can use `BeforeEndTime`, `AfterEndTime`, or both.
Type: Array of [Filter](API_marketplace-agreements_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [maxResults](#API_marketplace-agreements_SearchAgreements_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SearchAgreements-request-maxResults"></a>
The maximum number of agreements to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_marketplace-agreements_SearchAgreements_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SearchAgreements-request-nextToken"></a>
A token to specify where to start pagination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`
Required: No

 ** [sort](#API_marketplace-agreements_SearchAgreements_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SearchAgreements-request-sort"></a>
An object that contains the `SortBy` and `SortOrder` attributes. For `SearchAgreements`, `SortBy` supports `EndTime` for both party types, and `StartTime` and `LastUpdateTime` only when `PartyType` is `Proposer`. The default `SortBy` value is `EndTime`.
Type: [Sort](API_marketplace-agreements_Sort.md) object
Required: No

## Response Syntax
<a name="API_marketplace-agreements_SearchAgreements_ResponseSyntax"></a>

```
{
   "agreementViewSummaries": [
      {
         "acceptanceTime": number,
         "acceptor": {
            "accountId": "string"
         },
         "agreementId": "string",
         "agreementType": "string",
         "endTime": number,
         "endTimeBehaviorReasonCode": "string",
         "endTimeBehaviorType": "string",
         "entitlements": [
            {
               "licenseArn": "string"
            }
         ],
         "initialAgreementId": "string",
         "lastUpdateTime": number,
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
         "proposer": {
            "accountId": "string"
         },
         "startTime": number,
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_marketplace-agreements_SearchAgreements_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agreementViewSummaries](#API_marketplace-agreements_SearchAgreements_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SearchAgreements-response-agreementViewSummaries"></a>
A summary of the agreement, including top-level attributes (for example, the agreement ID, proposer, and acceptor).
Type: Array of [AgreementViewSummary](API_marketplace-agreements_AgreementViewSummary.md) objects

 ** [nextToken](#API_marketplace-agreements_SearchAgreements_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SearchAgreements-response-nextToken"></a>
The token used for pagination. The field is `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`

## Errors
<a name="API_marketplace-agreements_SearchAgreements_Errors"></a>

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
<a name="API_marketplace-agreements_SearchAgreements_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_SearchAgreements_Example_1"></a>

This example illustrates one usage of SearchAgreements.

```
{
    "catalog": "AWSMarketplace",
    "filters": [
        {
           "name": "AgreementType",
           "values": ["PurchaseAgreement"]
        },
        {
            "name": "PartyType",
            "values": ["Proposer"]
        },
        {
            "name": "AfterEndTime",
            "values": ["2019-10-08T00:00:00Z"]
        },
        {
            "name": "AcceptorAccountId",
            "values": ["123456789010"]
        }
    ]
}
```

### Sample response
<a name="API_marketplace-agreements_SearchAgreements_Example_2"></a>

This example illustrates one usage of SearchAgreements.

```
{
    "agreementViewSummaries": [
       {
            "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95",
            "acceptor": {
                "accountId": "123456789010"
            },
            "proposer": {
                "accountId": "123456789010"
            },
            "startTime": "2019-10-08T21:40:43Z",
            "endTime": "2026-10-08T21:40:43Z",
            "lastUpdateTime": "2025-04-17T09:12:55Z",
            "acceptanceTime": "2019-10-08T00:00:00Z",
            "agreementType": "PurchaseAgreement",
            "proposalSummary": {
                "resources": [
                    {
                        "id": "0EXAMPLE-8ce8-4814-bcf1-636EXAMPLEb5",
                        "type": "SaaSProduct"
                    }
                ],
                "offerId": "ABCDEFGHIJKLMNOP123",
                "offerSetId": "KMZQABLKAXWYG3NW516"
            },
            "status": "ACTIVE",
            "entitlements": [
                {
                    "licenseArn": "arn:aws:license-manager::123456789012:license/lic-EXAMPLE01234abcd"
                }
            ],
            "initialAgreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95",
            "endTimeBehaviorType": "EXPIRE",
            "endTimeBehaviorReasonCode": "ACCEPTOR_RENEW_OPTED_OUT"
       }
    ],
    "nextToken": null
}
```

## See Also
<a name="API_marketplace-agreements_SearchAgreements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/SearchAgreements)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/SearchAgreements)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/SearchAgreements)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/SearchAgreements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/SearchAgreements)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/SearchAgreements)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/SearchAgreements)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/SearchAgreements)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/SearchAgreements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/SearchAgreements)
