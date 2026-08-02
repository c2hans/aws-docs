---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_DescribeAgreement.html
---

# DescribeAgreement
<a name="API_marketplace-agreements_DescribeAgreement"></a>

Provides details about an agreement, such as the proposer, acceptor, start date, and end date.

## Request Syntax
<a name="API_marketplace-agreements_DescribeAgreement_RequestSyntax"></a>

```
{
   "agreementId": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_DescribeAgreement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementId](#API_marketplace-agreements_DescribeAgreement_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_DescribeAgreement-request-agreementId"></a>
The unique identifier of the agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

## Response Syntax
<a name="API_marketplace-agreements_DescribeAgreement_ResponseSyntax"></a>

```
{
   "acceptanceTime": number,
   "acceptor": {
      "accountId": "string"
   },
   "agreementId": "string",
   "agreementType": "string",
   "endTime": number,
   "estimatedCharges": {
      "agreementValue": "string",
      "currencyCode": "string"
   },
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
```

## Response Elements
<a name="API_marketplace-agreements_DescribeAgreement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [acceptanceTime](#API_marketplace-agreements_DescribeAgreement_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_DescribeAgreement-response-acceptanceTime"></a>
The date and time the offer was accepted or the agreement was created.
 `AcceptanceTime` and `StartTime` can differ for future dated agreements (FDAs).
Type: Timestamp

 ** [acceptor](#API_marketplace-agreements_DescribeAgreement_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_DescribeAgreement-response-acceptor"></a>
The details of the party accepting the agreement terms. This is commonly the buyer for `PurchaseAgreement`.
Type: [Acceptor](API_marketplace-agreements_Acceptor.md) object

 ** [agreementId](#API_marketplace-agreements_DescribeAgreement_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_DescribeAgreement-response-agreementId"></a>
The unique identifier of the agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`

 ** [agreementType](#API_marketplace-agreements_DescribeAgreement_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_DescribeAgreement-response-agreementType"></a>
The type of agreement. Values are `PurchaseAgreement` or `VendorInsightsAgreement`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z]+`

 ** [endTime](#API_marketplace-agreements_DescribeAgreement_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_DescribeAgreement-response-endTime"></a>
The date and time when the agreement ends. The field is `null` for pay-as-you-go agreements, which don’t have end dates.
Type: Timestamp

 ** [estimatedCharges](#API_marketplace-agreements_DescribeAgreement_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_DescribeAgreement-response-estimatedCharges"></a>
The estimated cost of the agreement.
Type: [EstimatedCharges](API_marketplace-agreements_EstimatedCharges.md) object

 ** [proposalSummary](#API_marketplace-agreements_DescribeAgreement_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_DescribeAgreement-response-proposalSummary"></a>
A summary of the proposal received from the proposer.
Type: [ProposalSummary](API_marketplace-agreements_ProposalSummary.md) object

 ** [proposer](#API_marketplace-agreements_DescribeAgreement_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_DescribeAgreement-response-proposer"></a>
The details of the party proposing the agreement terms. This is commonly the seller for `PurchaseAgreement`.
Type: [Proposer](API_marketplace-agreements_Proposer.md) object

 ** [startTime](#API_marketplace-agreements_DescribeAgreement_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_DescribeAgreement-response-startTime"></a>
The date and time when the agreement starts.
Type: Timestamp

 ** [status](#API_marketplace-agreements_DescribeAgreement_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_DescribeAgreement-response-status"></a>
The current status of the agreement.
Statuses include:
+  `ACTIVE` – The terms of the agreement are active.
+  `ARCHIVED` – The agreement ended without a specified reason.
+  `CANCELLED` – The acceptor ended the agreement before the defined end date.
+  `EXPIRED` – The agreement ended on the defined end date.
+  `RENEWED` – The agreement was renewed into a new agreement (for example, an auto-renewal).
+  `REPLACED` – The agreement was replaced using an agreement replacement offer.
+  `TERMINATED` – The agreement ended before the defined end date because of an AWS termination (for example, a payment failure).
Type: String
Valid Values: `ACTIVE | ARCHIVED | CANCELLED | EXPIRED | RENEWED | REPLACED | TERMINATED`

## Errors
<a name="API_marketplace-agreements_DescribeAgreement_Errors"></a>

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

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** message **
Description of the error.
 ** requestId **
The unique identifier for the error.
 ** resourceId **
The unique identifier for the resource.
 ** resourceType **
The type of resource.
HTTP Status Code: 400

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
<a name="API_marketplace-agreements_DescribeAgreement_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_DescribeAgreement_Example_1"></a>

This example illustrates one usage of DescribeAgreement.

```
{
    "agreementId" : "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95"
}
```

### Sample response
<a name="API_marketplace-agreements_DescribeAgreement_Example_2"></a>

This example illustrates one usage of DescribeAgreement.

```
{
   "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95",
   "acceptor": {
        "accountId": "123456789010"
   },
   "proposer": {
        "accountId": "123456789010"
   },
   "startTime": 2019-10-08T21:40:43.644Z,
   "endTime": 2023-10-08T21:40:43.644Z,
   "acceptanceTime": 2019-10-08T00:00:00.000Z,
   "agreementType": "PurchaseAgreement",
   "proposalSummary": {
       "resources": [
           {
               "id": "0EXAMPLE-8ce8-4814-bcf1-636EXAMPLEb5",
               "type": "AmiProduct"
           }
       ],
       "offerId": "ABCDEFGHIJKLMNOP123",
       "offerSetId": "KMZQABLKAXWYG3NW516"
   ],
   "status": "ACTIVE",
   "estimatedCharges": {
       "currencyCode": "USD",
       "agreementValue": "1000"
   }
}
```

## See Also
<a name="API_marketplace-agreements_DescribeAgreement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/DescribeAgreement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/DescribeAgreement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/DescribeAgreement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/DescribeAgreement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/DescribeAgreement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/DescribeAgreement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/DescribeAgreement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/DescribeAgreement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/DescribeAgreement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/DescribeAgreement)
