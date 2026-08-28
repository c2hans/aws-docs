---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_ListBillingAdjustmentRequests.html
---

# ListBillingAdjustmentRequests
<a name="API_marketplace-agreements_ListBillingAdjustmentRequests"></a>

Lists billing adjustment requests for a specific agreement. Sellers (proposers) can use this operation to view all billing adjustment requests associated with an agreement.

## Request Syntax
<a name="API_marketplace-agreements_ListBillingAdjustmentRequests_RequestSyntax"></a>

```
{
   "agreementId": "{{string}}",
   "agreementType": "{{string}}",
   "catalog": "{{string}}",
   "createdAfter": {{number}},
   "createdBefore": {{number}},
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "status": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_ListBillingAdjustmentRequests_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementId](#API_marketplace-agreements_ListBillingAdjustmentRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListBillingAdjustmentRequests-request-agreementId"></a>
The unique identifier of the agreement to list billing adjustment requests for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** [agreementType](#API_marketplace-agreements_ListBillingAdjustmentRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListBillingAdjustmentRequests-request-agreementType"></a>
An optional filter to return billing adjustment requests by agreement type (e.g., `PurchaseAgreement`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z]+`
Required: No

 ** [catalog](#API_marketplace-agreements_ListBillingAdjustmentRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListBillingAdjustmentRequests-request-catalog"></a>
An optional filter to return billing adjustment requests by catalog (e.g., `AWSMarketplace`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9.-]+`
Required: No

 ** [createdAfter](#API_marketplace-agreements_ListBillingAdjustmentRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListBillingAdjustmentRequests-request-createdAfter"></a>
An optional filter to return billing adjustment requests created after the specified timestamp.
Type: Timestamp
Required: No

 ** [createdBefore](#API_marketplace-agreements_ListBillingAdjustmentRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListBillingAdjustmentRequests-request-createdBefore"></a>
An optional filter to return billing adjustment requests created before the specified timestamp.
Type: Timestamp
Required: No

 ** [maxResults](#API_marketplace-agreements_ListBillingAdjustmentRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListBillingAdjustmentRequests-request-maxResults"></a>
The maximum number of billing adjustment requests to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_marketplace-agreements_ListBillingAdjustmentRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListBillingAdjustmentRequests-request-nextToken"></a>
A token to specify where to start pagination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`
Required: No

 ** [status](#API_marketplace-agreements_ListBillingAdjustmentRequests_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListBillingAdjustmentRequests-request-status"></a>
An optional filter to return billing adjustment requests with the specified status.
Type: String
Valid Values: `PENDING | VALIDATION_FAILED | COMPLETED`
Required: No

## Response Syntax
<a name="API_marketplace-agreements_ListBillingAdjustmentRequests_ResponseSyntax"></a>

```
{
   "items": [
      {
         "adjustmentAmount": "string",
         "agreementId": "string",
         "agreementType": "string",
         "billingAdjustmentRequestId": "string",
         "catalog": "string",
         "createdAt": number,
         "currencyCode": "string",
         "originalInvoiceId": "string",
         "status": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_marketplace-agreements_ListBillingAdjustmentRequests_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_marketplace-agreements_ListBillingAdjustmentRequests_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListBillingAdjustmentRequests-response-items"></a>
An array of `BillingAdjustmentSummary` objects containing summary information about each billing adjustment request.
Type: Array of [BillingAdjustmentSummary](API_marketplace-agreements_BillingAdjustmentSummary.md) objects

 ** [nextToken](#API_marketplace-agreements_ListBillingAdjustmentRequests_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_ListBillingAdjustmentRequests-response-nextToken"></a>
The token used for pagination. The field is `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=_-]+`

## Errors
<a name="API_marketplace-agreements_ListBillingAdjustmentRequests_Errors"></a>

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
<a name="API_marketplace-agreements_ListBillingAdjustmentRequests_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_ListBillingAdjustmentRequests_Example_1"></a>

This example illustrates one usage of ListBillingAdjustmentRequests.

```
{
    "agreementId": "agmt-EXAMPLESvIzsqYMyQwI3"
}
```

### Sample response
<a name="API_marketplace-agreements_ListBillingAdjustmentRequests_Example_2"></a>

This example illustrates one usage of ListBillingAdjustmentRequests.

```
{
    "items": [
        {
            "billingAdjustmentRequestId": "ba-EXAMPLE1a2b3c4d5e",
            "status": "PENDING",
            "agreementId": "agmt-EXAMPLESvIzsqYMyQwI3",
            "originalInvoiceId": "E2E20230929a108cfae",
            "adjustmentAmount": "500.00",
            "currencyCode": "USD",
            "createdAt": 1750793400,
            "updatedAt": 1750793400
        },
        {
            "billingAdjustmentRequestId": "ba-EXAMPLE2b3c4d5e6f",
            "status": "PENDING",
            "agreementId": "agmt-EXAMPLESvIzsqYMyQwI3",
            "originalInvoiceId": "E2E20230930b209dfbf",
            "adjustmentAmount": "500.00",
            "currencyCode": "USD",
            "createdAt": 1750793400,
            "updatedAt": 1750793400
        }
    ],
    "nextToken": null
}
```

## See Also
<a name="API_marketplace-agreements_ListBillingAdjustmentRequests_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/ListBillingAdjustmentRequests)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/ListBillingAdjustmentRequests)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/ListBillingAdjustmentRequests)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/ListBillingAdjustmentRequests)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ListBillingAdjustmentRequests)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/ListBillingAdjustmentRequests)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/ListBillingAdjustmentRequests)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/ListBillingAdjustmentRequests)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/ListBillingAdjustmentRequests)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/ListBillingAdjustmentRequests)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
