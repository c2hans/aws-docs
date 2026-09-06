---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ListEnterpriseSupportLinkedAccountCharges.html
---

# ListEnterpriseSupportLinkedAccountCharges
<a name="API_billing_ListEnterpriseSupportLinkedAccountCharges"></a>

Returns Support-eligible spend broken down at linked account level.

## Request Syntax
<a name="API_billing_ListEnterpriseSupportLinkedAccountCharges_RequestSyntax"></a>

```
{
   "accountId": "{{string}}",
   "billingMonth": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_billing_ListEnterpriseSupportLinkedAccountCharges_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountId](#API_billing_ListEnterpriseSupportLinkedAccountCharges_RequestSyntax) **   <a name="awscostmanagement-billing_ListEnterpriseSupportLinkedAccountCharges-request-accountId"></a>
An optional linked account ID to filter results to a specific account.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [billingMonth](#API_billing_ListEnterpriseSupportLinkedAccountCharges_RequestSyntax) **   <a name="awscostmanagement-billing_ListEnterpriseSupportLinkedAccountCharges-request-billingMonth"></a>
The billing month in YYYY-MM format. This must be a month in the past.
Type: String
Pattern: `\d{4}-(0[1-9]|1[0-2])`
Required: Yes

 ** [maxResults](#API_billing_ListEnterpriseSupportLinkedAccountCharges_RequestSyntax) **   <a name="awscostmanagement-billing_ListEnterpriseSupportLinkedAccountCharges-request-maxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_billing_ListEnterpriseSupportLinkedAccountCharges_RequestSyntax) **   <a name="awscostmanagement-billing_ListEnterpriseSupportLinkedAccountCharges-request-nextToken"></a>
The pagination token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`
Required: No

## Response Syntax
<a name="API_billing_ListEnterpriseSupportLinkedAccountCharges_ResponseSyntax"></a>

```
{
   "linkedAccount": [
      {
         "accountId": "string",
         "accountType": "string",
         "billableSeconds": number,
         "linkedTimePeriods": [
            {
               "beginDate": number,
               "endDate": number
            }
         ],
         "payerAccountId": "string",
         "proratedTotalSupportEligibleSpend": "string",
         "subscriptionTimePeriods": [
            {
               "beginDate": number,
               "endDate": number
            }
         ],
         "supportEligibleSpendByService": [
            {
               "serviceCode": "string",
               "totalSupportEligibleSpend": "string"
            }
         ],
         "totalSeconds": number,
         "totalSupportEligibleReservedInstanceSpend": "string",
         "totalSupportEligibleSavingsPlanSpend": "string",
         "totalSupportEligibleSpend": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_billing_ListEnterpriseSupportLinkedAccountCharges_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [linkedAccount](#API_billing_ListEnterpriseSupportLinkedAccountCharges_ResponseSyntax) **   <a name="awscostmanagement-billing_ListEnterpriseSupportLinkedAccountCharges-response-linkedAccount"></a>
The list of Enterprise Support charges per linked account.
Type: Array of [LinkedAccountCharge](API_billing_LinkedAccountCharge.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [nextToken](#API_billing_ListEnterpriseSupportLinkedAccountCharges_ResponseSyntax) **   <a name="awscostmanagement-billing_ListEnterpriseSupportLinkedAccountCharges-response-nextToken"></a>
The pagination token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`

## Errors
<a name="API_billing_ListEnterpriseSupportLinkedAccountCharges_Errors"></a>

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
<a name="API_billing_ListEnterpriseSupportLinkedAccountCharges_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/ListEnterpriseSupportLinkedAccountCharges)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/ListEnterpriseSupportLinkedAccountCharges)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/ListEnterpriseSupportLinkedAccountCharges)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/ListEnterpriseSupportLinkedAccountCharges)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/ListEnterpriseSupportLinkedAccountCharges)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/ListEnterpriseSupportLinkedAccountCharges)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/ListEnterpriseSupportLinkedAccountCharges)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/ListEnterpriseSupportLinkedAccountCharges)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/ListEnterpriseSupportLinkedAccountCharges)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/ListEnterpriseSupportLinkedAccountCharges)
