---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ListBusinessSupportAccountCharges.html
---

# ListBusinessSupportAccountCharges
<a name="API_billing_ListBusinessSupportAccountCharges"></a>

Returns Business Support charges broken down at the linked account level for a given billing month.

## Request Syntax
<a name="API_billing_ListBusinessSupportAccountCharges_RequestSyntax"></a>

```
{
   "accountId": "{{string}}",
   "billingMonth": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_billing_ListBusinessSupportAccountCharges_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountId](#API_billing_ListBusinessSupportAccountCharges_RequestSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportAccountCharges-request-accountId"></a>
The linked account ID to filter results to a specific account. If you don't specify a value, the response includes charges for all linked accounts.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [billingMonth](#API_billing_ListBusinessSupportAccountCharges_RequestSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportAccountCharges-request-billingMonth"></a>
The billing month to retrieve Business Support charges for, in YYYY-MM format. You can request the current month (charges will be estimated) or a past month (charges will be finalized).
Type: String
Pattern: `\d{4}-(0[1-9]|1[0-2])`
Required: Yes

 ** [maxResults](#API_billing_ListBusinessSupportAccountCharges_RequestSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportAccountCharges-request-maxResults"></a>
The maximum number of results to return per page. Default is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_billing_ListBusinessSupportAccountCharges_RequestSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportAccountCharges-request-nextToken"></a>
The pagination token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`
Required: No

## Response Syntax
<a name="API_billing_ListBusinessSupportAccountCharges_ResponseSyntax"></a>

```
{
   "accountCharges": [
      {
         "accountId": "string",
         "supportDiscount": {
            "discountAmount": "string",
            "discountPercentage": "string",
            "discountSource": "string",
            "discountType": "string"
         },
         "supportEligibleSpendByService": [
            {
               "chargeAmount": "string",
               "contributingService": "string",
               "currency": "string",
               "description": "string",
               "itemType": "string"
            }
         ],
         "supportPlanName": "string",
         "tierCharges": [
            {
               "chargePeriodEndDate": number,
               "chargePeriodStartDate": number,
               "tierCharge": "string",
               "tierDescription": "string",
               "tierRate": "string",
               "usageSlice": "string"
            }
         ],
         "totalCharge": "string",
         "totalUsageBasis": "string"
      }
   ],
   "accountCount": number,
   "billingMonth": "string",
   "isEstimated": boolean,
   "nextToken": "string",
   "totalSupportCharge": "string",
   "totalSupportEligibleSpend": "string"
}
```

## Response Elements
<a name="API_billing_ListBusinessSupportAccountCharges_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountCharges](#API_billing_ListBusinessSupportAccountCharges_ResponseSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportAccountCharges-response-accountCharges"></a>
The list of Business Support charges per linked account.
Type: Array of [BusinessSupportAccountCharge](API_billing_BusinessSupportAccountCharge.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [accountCount](#API_billing_ListBusinessSupportAccountCharges_ResponseSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportAccountCharges-response-accountCount"></a>
The total number of linked accounts with Business Support charges in the billing month.
Type: Integer

 ** [billingMonth](#API_billing_ListBusinessSupportAccountCharges_ResponseSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportAccountCharges-response-billingMonth"></a>
The billing month for the returned charges, in YYYY-MM format.
Type: String
Pattern: `\d{4}-(0[1-9]|1[0-2])`

 ** [isEstimated](#API_billing_ListBusinessSupportAccountCharges_ResponseSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportAccountCharges-response-isEstimated"></a>
Specifies whether the Support charge amount is estimated. When false, the charge amount is finalized.
Type: Boolean

 ** [nextToken](#API_billing_ListBusinessSupportAccountCharges_ResponseSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportAccountCharges-response-nextToken"></a>
The pagination token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`

 ** [totalSupportCharge](#API_billing_ListBusinessSupportAccountCharges_ResponseSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportAccountCharges-response-totalSupportCharge"></a>
The total Business Support charge amount for all accounts in the billing month.
Type: String

 ** [totalSupportEligibleSpend](#API_billing_ListBusinessSupportAccountCharges_ResponseSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportAccountCharges-response-totalSupportEligibleSpend"></a>
The total Support-eligible spend from all accounts in the billing month. This includes eligible spend from usage of Amazon Web Services.
Type: String

## Errors
<a name="API_billing_ListBusinessSupportAccountCharges_Errors"></a>

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
<a name="API_billing_ListBusinessSupportAccountCharges_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/ListBusinessSupportAccountCharges)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/ListBusinessSupportAccountCharges)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/ListBusinessSupportAccountCharges)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/ListBusinessSupportAccountCharges)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/ListBusinessSupportAccountCharges)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/ListBusinessSupportAccountCharges)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/ListBusinessSupportAccountCharges)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/ListBusinessSupportAccountCharges)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/ListBusinessSupportAccountCharges)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/ListBusinessSupportAccountCharges)
