---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ListContractualInvestmentAttestations.html
---

# ListContractualInvestmentAttestations
<a name="API_billing_ListContractualInvestmentAttestations"></a>

Lists the investment attestations submitted under a specific private pricing contract. Use this operation to track attestation status, including the terminal statuses `DISBURSED`, `REJECTED`, and `CANCELLED`. This operation is read-only and paginated.

## Request Syntax
<a name="API_billing_ListContractualInvestmentAttestations_RequestSyntax"></a>

```
{
   "contractArn": "{{string}}",
   "investmentSummaryId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_billing_ListContractualInvestmentAttestations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [contractArn](#API_billing_ListContractualInvestmentAttestations_RequestSyntax) **   <a name="awscostmanagement-billing_ListContractualInvestmentAttestations-request-contractArn"></a>
The Amazon Resource Name (ARN) of the contract whose attestations you want to list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `arn:aws[a-z-]*:billing::[0-9]{12}:contract/[a-zA-Z0-9_\+=\.\@-]{0,70}[a-zA-Z0-9]`
Required: Yes

 ** [investmentSummaryId](#API_billing_ListContractualInvestmentAttestations_RequestSyntax) **   <a name="awscostmanagement-billing_ListContractualInvestmentAttestations-request-investmentSummaryId"></a>
The identifier of a specific investment summary to filter the attestations by. If omitted, attestations for all investment summaries in the contract are returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9_\-]+`
Required: No

 ** [maxResults](#API_billing_ListContractualInvestmentAttestations_RequestSyntax) **   <a name="awscostmanagement-billing_ListContractualInvestmentAttestations-request-maxResults"></a>
The maximum number of attestations to return in a single call. Minimum value of 1, maximum value of 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_billing_ListContractualInvestmentAttestations_RequestSyntax) **   <a name="awscostmanagement-billing_ListContractualInvestmentAttestations-request-nextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`
Required: No

## Response Syntax
<a name="API_billing_ListContractualInvestmentAttestations_ResponseSyntax"></a>

```
{
   "items": [
      {
         "attestationId": "string",
         "attestationStatus": "string",
         "attestedAt": number,
         "attestedValue": {
            "currencyAmount": "string",
            "currencyCode": "string"
         },
         "investmentDisbursedAt": number,
         "investmentDistributions": [
            {
               "accountId": "string",
               "investmentAmount": {
                  "currencyAmount": "string",
                  "currencyCode": "string"
               }
            }
         ],
         "investmentId": "string",
         "investmentName": "string",
         "investmentSummaryId": "string",
         "isCancellable": boolean,
         "outcomeDescription": "string",
         "rejectionReasons": [ "string" ],
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_billing_ListContractualInvestmentAttestations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_billing_ListContractualInvestmentAttestations_ResponseSyntax) **   <a name="awscostmanagement-billing_ListContractualInvestmentAttestations-response-items"></a>
The list of investment attestations submitted under the contract.
Type: Array of [InvestmentAttestation](API_billing_InvestmentAttestation.md) objects

 ** [nextToken](#API_billing_ListContractualInvestmentAttestations_ResponseSyntax) **   <a name="awscostmanagement-billing_ListContractualInvestmentAttestations-response-nextToken"></a>
The pagination token to use on subsequent calls to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`

## Errors
<a name="API_billing_ListContractualInvestmentAttestations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The specified ARN in the request doesn't exist.
 ** resourceId **
 Value is a list of resource IDs that were not found.
 ** resourceType **
 Value is the type of resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_billing_ListContractualInvestmentAttestations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/ListContractualInvestmentAttestations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/ListContractualInvestmentAttestations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/ListContractualInvestmentAttestations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/ListContractualInvestmentAttestations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/ListContractualInvestmentAttestations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/ListContractualInvestmentAttestations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/ListContractualInvestmentAttestations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/ListContractualInvestmentAttestations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/ListContractualInvestmentAttestations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/ListContractualInvestmentAttestations)
