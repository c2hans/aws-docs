---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ListContracts.html
---

# ListContracts
<a name="API_billing_ListContracts"></a>

Lists the private pricing contracts that your AWS account is an eligible payer account of. This operation is read-only and paginated.

## Request Syntax
<a name="API_billing_ListContracts_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_billing_ListContracts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_billing_ListContracts_RequestSyntax) **   <a name="awscostmanagement-billing_ListContracts-request-maxResults"></a>
The maximum number of contracts to return in a single call. Minimum value of 1, maximum value of 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_billing_ListContracts_RequestSyntax) **   <a name="awscostmanagement-billing_ListContracts-request-nextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`
Required: No

## Response Syntax
<a name="API_billing_ListContracts_ResponseSyntax"></a>

```
{
   "items": [
      {
         "associationStatus": "string",
         "contractArn": "string",
         "contractTerm": {
            "endDateInclusive": number,
            "startDateInclusive": number
         },
         "contractType": "string",
         "lastUpdatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_billing_ListContracts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_billing_ListContracts_ResponseSyntax) **   <a name="awscostmanagement-billing_ListContracts-response-items"></a>
The list of contracts that your AWS account is an eligible payer account of.
Type: Array of [ContractSummary](API_billing_ContractSummary.md) objects

 ** [nextToken](#API_billing_ListContracts_ResponseSyntax) **   <a name="awscostmanagement-billing_ListContracts-response-nextToken"></a>
The pagination token to use on subsequent calls to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`

## Errors
<a name="API_billing_ListContracts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

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
<a name="API_billing_ListContracts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/ListContracts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/ListContracts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/ListContracts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/ListContracts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/ListContracts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/ListContracts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/ListContracts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/ListContracts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/ListContracts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/ListContracts)
