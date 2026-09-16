---
source_url: https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_DescribeSavingsPlansOfferings.html
---

# DescribeSavingsPlansOfferings
<a name="API_DescribeSavingsPlansOfferings"></a>

Describes the offerings for the specified Savings Plans.

## Request Syntax
<a name="API_DescribeSavingsPlansOfferings_RequestSyntax"></a>

```
POST /DescribeSavingsPlansOfferings HTTP/1.1
Content-type: application/json

{
   "currencies": [ "{{string}}" ],
   "descriptions": [ "{{string}}" ],
   "durations": [ {{number}} ],
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "offeringIds": [ "{{string}}" ],
   "operations": [ "{{string}}" ],
   "paymentOptions": [ "{{string}}" ],
   "planTypes": [ "{{string}}" ],
   "productType": "{{string}}",
   "serviceCodes": [ "{{string}}" ],
   "usageTypes": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DescribeSavingsPlansOfferings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeSavingsPlansOfferings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [currencies](#API_DescribeSavingsPlansOfferings_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferings-request-currencies"></a>
The currencies.
Type: Array of strings
Valid Values: `CNY | USD | EUR`
Required: No

 ** [descriptions](#API_DescribeSavingsPlansOfferings_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferings-request-descriptions"></a>
The descriptions.
Type: Array of strings
Pattern: `^[a-zA-Z0-9_\- ]+$`
Required: No

 ** [durations](#API_DescribeSavingsPlansOfferings_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferings-request-durations"></a>
The duration, in seconds.
Type: Array of longs
Valid Range: Minimum value of 0.
Required: No

 ** [filters](#API_DescribeSavingsPlansOfferings_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferings-request-filters"></a>
The filters.
Type: Array of [SavingsPlanOfferingFilterElement](API_SavingsPlanOfferingFilterElement.md) objects
Required: No

 ** [maxResults](#API_DescribeSavingsPlansOfferings_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferings-request-maxResults"></a>
The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeSavingsPlansOfferings_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferings-request-nextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[A-Za-z0-9/=\+]+$`
Required: No

 ** [offeringIds](#API_DescribeSavingsPlansOfferings_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferings-request-offeringIds"></a>
The IDs of the offerings.
Type: Array of strings
Pattern: `[a-f0-9]+(-[a-f0-9]+)*`
Required: No

 ** [operations](#API_DescribeSavingsPlansOfferings_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferings-request-operations"></a>
The specific AWS operation for the line item in the billing report.
Type: Array of strings
Length Constraints: Maximum length of 255.
Pattern: `^[a-zA-Z0-9_ \/.:-]*$`
Required: No

 ** [paymentOptions](#API_DescribeSavingsPlansOfferings_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferings-request-paymentOptions"></a>
The payment options.
Type: Array of strings
Valid Values: `All Upfront | Partial Upfront | No Upfront`
Required: No

 ** [planTypes](#API_DescribeSavingsPlansOfferings_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferings-request-planTypes"></a>
The plan types.
Type: Array of strings
Valid Values: `Compute | EC2Instance | SageMaker | Database`
Required: No

 ** [productType](#API_DescribeSavingsPlansOfferings_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferings-request-productType"></a>
The product type.
Type: String
Valid Values: `EC2 | Fargate | Lambda | SageMaker | RDS | DSQL | DynamoDB | ElastiCache | DocDB | Neptune | Timestream | Keyspaces | DMS | OpenSearch`
Required: No

 ** [serviceCodes](#API_DescribeSavingsPlansOfferings_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferings-request-serviceCodes"></a>
The services.
Type: Array of strings
Length Constraints: Maximum length of 255.
Pattern: `^[a-zA-Z]+$`
Required: No

 ** [usageTypes](#API_DescribeSavingsPlansOfferings_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferings-request-usageTypes"></a>
The usage details of the line item in the billing report.
Type: Array of strings
Length Constraints: Maximum length of 255.
Pattern: `^[a-zA-Z0-9_ \/.:-]+$`
Required: No

## Response Syntax
<a name="API_DescribeSavingsPlansOfferings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "searchResults": [
      {
         "currency": "string",
         "description": "string",
         "durationSeconds": number,
         "offeringId": "string",
         "operation": "string",
         "paymentOption": "string",
         "planType": "string",
         "productTypes": [ "string" ],
         "properties": [
            {
               "name": "string",
               "value": "string"
            }
         ],
         "serviceCode": "string",
         "usageType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSavingsPlansOfferings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribeSavingsPlansOfferings_ResponseSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferings-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[A-Za-z0-9/=\+]+$`

 ** [searchResults](#API_DescribeSavingsPlansOfferings_ResponseSyntax) **   <a name="savingsplans-DescribeSavingsPlansOfferings-response-searchResults"></a>
Information about the Savings Plans offerings.
Type: Array of [SavingsPlanOffering](API_SavingsPlanOffering.md) objects

## Errors
<a name="API_DescribeSavingsPlansOfferings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error occurred.
HTTP Status Code: 500

 ** ValidationException **
One of the input parameters is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeSavingsPlansOfferings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/savingsplans-2019-06-28/DescribeSavingsPlansOfferings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/savingsplans-2019-06-28/DescribeSavingsPlansOfferings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/savingsplans-2019-06-28/DescribeSavingsPlansOfferings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/savingsplans-2019-06-28/DescribeSavingsPlansOfferings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/savingsplans-2019-06-28/DescribeSavingsPlansOfferings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/savingsplans-2019-06-28/DescribeSavingsPlansOfferings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/savingsplans-2019-06-28/DescribeSavingsPlansOfferings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/savingsplans-2019-06-28/DescribeSavingsPlansOfferings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/savingsplans-2019-06-28/DescribeSavingsPlansOfferings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/savingsplans-2019-06-28/DescribeSavingsPlansOfferings)
