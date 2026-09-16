---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListBillScenarioUsageModifications.html
---

# ListBillScenarioUsageModifications
<a name="API_AWSBCMPricingCalculator_ListBillScenarioUsageModifications"></a>

 Lists the usage modifications associated with a bill scenario.

## Request Syntax
<a name="API_AWSBCMPricingCalculator_ListBillScenarioUsageModifications_RequestSyntax"></a>

```
{
   "billScenarioId": "{{string}}",
   "filters": [
      {
         "matchOption": "{{string}}",
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_AWSBCMPricingCalculator_ListBillScenarioUsageModifications_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [billScenarioId](#API_AWSBCMPricingCalculator_ListBillScenarioUsageModifications_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_ListBillScenarioUsageModifications-request-billScenarioId"></a>
 The unique identifier of the bill scenario to list usage modifications for.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [filters](#API_AWSBCMPricingCalculator_ListBillScenarioUsageModifications_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_ListBillScenarioUsageModifications-request-filters"></a>
 Filters to apply to the list of usage modifications.
Type: Array of [ListUsageFilter](API_AWSBCMPricingCalculator_ListUsageFilter.md) objects
Required: No

 ** [maxResults](#API_AWSBCMPricingCalculator_ListBillScenarioUsageModifications_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_ListBillScenarioUsageModifications-request-maxResults"></a>
 The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_AWSBCMPricingCalculator_ListBillScenarioUsageModifications_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_ListBillScenarioUsageModifications-request-nextToken"></a>
 A token to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_AWSBCMPricingCalculator_ListBillScenarioUsageModifications_ResponseSyntax"></a>

```
{
   "items": [
      {
         "availabilityZone": "string",
         "group": "string",
         "historicalUsage": {
            "billInterval": {
               "end": number,
               "start": number
            },
            "filterExpression": {
               "and": [
                  "Expression"
               ],
               "costCategories": {
                  "key": "string",
                  "matchOptions": [ "string" ],
                  "values": [ "string" ]
               },
               "dimensions": {
                  "key": "string",
                  "matchOptions": [ "string" ],
                  "values": [ "string" ]
               },
               "not": "Expression",
               "or": [
                  "Expression"
               ],
               "tags": {
                  "key": "string",
                  "matchOptions": [ "string" ],
                  "values": [ "string" ]
               }
            },
            "location": "string",
            "operation": "string",
            "serviceCode": "string",
            "usageAccountId": "string",
            "usageType": "string"
         },
         "id": "string",
         "location": "string",
         "operation": "string",
         "quantities": [
            {
               "amount": number,
               "startHour": number,
               "unit": "string"
            }
         ],
         "serviceCode": "string",
         "usageAccountId": "string",
         "usageType": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_AWSBCMPricingCalculator_ListBillScenarioUsageModifications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_AWSBCMPricingCalculator_ListBillScenarioUsageModifications_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_ListBillScenarioUsageModifications-response-items"></a>
 The list of usage modifications associated with the bill scenario.
Type: Array of [BillScenarioUsageModificationItem](API_AWSBCMPricingCalculator_BillScenarioUsageModificationItem.md) objects

 ** [nextToken](#API_AWSBCMPricingCalculator_ListBillScenarioUsageModifications_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_ListBillScenarioUsageModifications-response-nextToken"></a>
 A token to retrieve the next page of results, if any.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\S\s]*`

## Errors
<a name="API_AWSBCMPricingCalculator_ListBillScenarioUsageModifications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** DataUnavailableException **
 The requested data is currently unavailable.
HTTP Status Code: 400

 ** InternalServerException **
 An internal error has occurred. Retry your request, but if the problem persists, contact AWS support.
 ** retryAfterSeconds **
 An internal error has occurred. Retry your request, but if the problem persists, contact AWS support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The specified resource was not found.
 ** resourceId **
 The identifier of the resource that was not found.
 ** resourceType **
 The type of the resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
 The request was denied due to request throttling.
 ** quotaCode **
The quota code that exceeded the throttling limit.
 ** retryAfterSeconds **
The service code that exceeded the throttling limit. Retry your request, but if the problem persists, contact AWS support.
 ** serviceCode **
The service code that exceeded the throttling limit.
HTTP Status Code: 400

 ** ValidationException **
 The input provided fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
 The list of fields that are invalid.
 ** reason **
 The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_AWSBCMPricingCalculator_ListBillScenarioUsageModifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-pricing-calculator-2024-06-19/ListBillScenarioUsageModifications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-pricing-calculator-2024-06-19/ListBillScenarioUsageModifications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/ListBillScenarioUsageModifications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-pricing-calculator-2024-06-19/ListBillScenarioUsageModifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/ListBillScenarioUsageModifications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-pricing-calculator-2024-06-19/ListBillScenarioUsageModifications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-pricing-calculator-2024-06-19/ListBillScenarioUsageModifications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-pricing-calculator-2024-06-19/ListBillScenarioUsageModifications)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bcm-pricing-calculator-2024-06-19/ListBillScenarioUsageModifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/ListBillScenarioUsageModifications)
