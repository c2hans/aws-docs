---
source_url: https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_DescribeSavingsPlanRates.html
---

# DescribeSavingsPlanRates
<a name="API_DescribeSavingsPlanRates"></a>

Describes the rates for a specific, existing Savings Plan.

## Request Syntax
<a name="API_DescribeSavingsPlanRates_RequestSyntax"></a>

```
POST /DescribeSavingsPlanRates HTTP/1.1
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
   "savingsPlanId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeSavingsPlanRates_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeSavingsPlanRates_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_DescribeSavingsPlanRates_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlanRates-request-filters"></a>
The filters.
Type: Array of [SavingsPlanRateFilter](API_SavingsPlanRateFilter.md) objects
Required: No

 ** [maxResults](#API_DescribeSavingsPlanRates_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlanRates-request-maxResults"></a>
The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeSavingsPlanRates_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlanRates-request-nextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[A-Za-z0-9/=\+]+$`
Required: No

 ** [savingsPlanId](#API_DescribeSavingsPlanRates_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlanRates-request-savingsPlanId"></a>
The ID of the Savings Plan.
Type: String
Required: Yes

## Response Syntax
<a name="API_DescribeSavingsPlanRates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "savingsPlanId": "string",
   "searchResults": [
      {
         "currency": "string",
         "operation": "string",
         "productType": "string",
         "properties": [
            {
               "name": "string",
               "value": "string"
            }
         ],
         "rate": "string",
         "serviceCode": "string",
         "unit": "string",
         "usageType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSavingsPlanRates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribeSavingsPlanRates_ResponseSyntax) **   <a name="savingsplans-DescribeSavingsPlanRates-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[A-Za-z0-9/=\+]+$`

 ** [savingsPlanId](#API_DescribeSavingsPlanRates_ResponseSyntax) **   <a name="savingsplans-DescribeSavingsPlanRates-response-savingsPlanId"></a>
The ID of the Savings Plan.
Type: String

 ** [searchResults](#API_DescribeSavingsPlanRates_ResponseSyntax) **   <a name="savingsplans-DescribeSavingsPlanRates-response-searchResults"></a>
Information about the Savings Plan rates.
Type: Array of [SavingsPlanRate](API_SavingsPlanRate.md) objects

## Errors
<a name="API_DescribeSavingsPlanRates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ValidationException **
One of the input parameters is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeSavingsPlanRates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/savingsplans-2019-06-28/DescribeSavingsPlanRates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/savingsplans-2019-06-28/DescribeSavingsPlanRates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/savingsplans-2019-06-28/DescribeSavingsPlanRates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/savingsplans-2019-06-28/DescribeSavingsPlanRates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/savingsplans-2019-06-28/DescribeSavingsPlanRates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/savingsplans-2019-06-28/DescribeSavingsPlanRates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/savingsplans-2019-06-28/DescribeSavingsPlanRates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/savingsplans-2019-06-28/DescribeSavingsPlanRates)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/savingsplans-2019-06-28/DescribeSavingsPlanRates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/savingsplans-2019-06-28/DescribeSavingsPlanRates)
