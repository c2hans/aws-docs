---
source_url: https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_DescribeSavingsPlansOfferingRates.html
---

# DescribeSavingsPlansOfferingRates
<a name="API_DescribeSavingsPlansOfferingRates"></a>

Describes the offering rates for Savings Plans you might want to purchase.

## Request Syntax
<a name="API_DescribeSavingsPlansOfferingRates_RequestSyntax"></a>

```
POST /DescribeSavingsPlansOfferingRates HTTP/1.1
Content-type: application/json

{
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "operations": [ "{{string}}" ],
   "products": [ "{{string}}" ],
   "savingsPlanOfferingIds": [ "{{string}}" ],
   "savingsPlanPaymentOptions": [ "{{string}}" ],
   "savingsPlanTypes": [ "{{string}}" ],
   "serviceCodes": [ "{{string}}" ],
   "usageTypes": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DescribeSavingsPlansOfferingRates_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeSavingsPlansOfferingRates_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_DescribeSavingsPlansOfferingRates_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferingRates-request-filters"></a>
The filters.
Type: Array of [SavingsPlanOfferingRateFilterElement](API_SavingsPlanOfferingRateFilterElement.md) objects
Required: No

 ** [maxResults](#API_DescribeSavingsPlansOfferingRates_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferingRates-request-maxResults"></a>
The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeSavingsPlansOfferingRates_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferingRates-request-nextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[A-Za-z0-9/=\+]+$`
Required: No

 ** [operations](#API_DescribeSavingsPlansOfferingRates_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferingRates-request-operations"></a>
The specific AWS operation for the line item in the billing report.
Type: Array of strings
Length Constraints: Maximum length of 255.
Pattern: `^[a-zA-Z0-9_ \/.:-]*$`
Required: No

 ** [products](#API_DescribeSavingsPlansOfferingRates_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferingRates-request-products"></a>
The AWS products.
Type: Array of strings
Valid Values: `EC2 | Fargate | Lambda | SageMaker | RDS | DSQL | DynamoDB | ElastiCache | DocDB | Neptune | Timestream | Keyspaces | DMS | OpenSearch`
Required: No

 ** [savingsPlanOfferingIds](#API_DescribeSavingsPlansOfferingRates_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferingRates-request-savingsPlanOfferingIds"></a>
The IDs of the offerings.
Type: Array of strings
Pattern: `[a-f0-9]+(-[a-f0-9]+)*`
Required: No

 ** [savingsPlanPaymentOptions](#API_DescribeSavingsPlansOfferingRates_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferingRates-request-savingsPlanPaymentOptions"></a>
The payment options.
Type: Array of strings
Valid Values: `All Upfront | Partial Upfront | No Upfront`
Required: No

 ** [savingsPlanTypes](#API_DescribeSavingsPlansOfferingRates_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferingRates-request-savingsPlanTypes"></a>
The plan types.
Type: Array of strings
Valid Values: `Compute | EC2Instance | SageMaker | Database`
Required: No

 ** [serviceCodes](#API_DescribeSavingsPlansOfferingRates_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferingRates-request-serviceCodes"></a>
The services.
Type: Array of strings
Valid Values: `AmazonEC2 | AmazonECS | AmazonEKS | AWSLambda | AmazonSageMaker | AmazonRDS | AuroraDSQL | AmazonDynamoDB | AmazonElastiCache | AmazonDocDB | AmazonNeptune | AmazonTimestream | AmazonMCS | AWSDatabaseMigrationSvc | AmazonES`
Required: No

 ** [usageTypes](#API_DescribeSavingsPlansOfferingRates_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferingRates-request-usageTypes"></a>
The usage details of the line item in the billing report.
Type: Array of strings
Length Constraints: Maximum length of 255.
Pattern: `^[a-zA-Z0-9_ \/.:-]+$`
Required: No

## Response Syntax
<a name="API_DescribeSavingsPlansOfferingRates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "searchResults": [
      {
         "operation": "string",
         "productType": "string",
         "properties": [
            {
               "name": "string",
               "value": "string"
            }
         ],
         "rate": "string",
         "savingsPlanOffering": {
            "currency": "string",
            "durationSeconds": number,
            "offeringId": "string",
            "paymentOption": "string",
            "planDescription": "string",
            "planType": "string"
         },
         "serviceCode": "string",
         "unit": "string",
         "usageType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSavingsPlansOfferingRates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribeSavingsPlansOfferingRates_ResponseSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferingRates-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[A-Za-z0-9/=\+]+$`

 ** [searchResults](#API_DescribeSavingsPlansOfferingRates_ResponseSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferingRates-response-searchResults"></a>
Information about the Savings Plans offering rates.
Type: Array of [SavingsPlanOfferingRate](API_SavingsPlanOfferingRate.md) objects

## Errors
<a name="API_DescribeSavingsPlansOfferingRates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error occurred.
HTTP Status Code: 500

 ** ValidationException **
One of the input parameters is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeSavingsPlansOfferingRates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/savingsplans-2019-06-28/DescribeSavingsPlansOfferingRates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/savingsplans-2019-06-28/DescribeSavingsPlansOfferingRates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/savingsplans-2019-06-28/DescribeSavingsPlansOfferingRates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/savingsplans-2019-06-28/DescribeSavingsPlansOfferingRates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/savingsplans-2019-06-28/DescribeSavingsPlansOfferingRates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/savingsplans-2019-06-28/DescribeSavingsPlansOfferingRates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/savingsplans-2019-06-28/DescribeSavingsPlansOfferingRates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/savingsplans-2019-06-28/DescribeSavingsPlansOfferingRates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/savingsplans-2019-06-28/DescribeSavingsPlansOfferingRates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/savingsplans-2019-06-28/DescribeSavingsPlansOfferingRates)
