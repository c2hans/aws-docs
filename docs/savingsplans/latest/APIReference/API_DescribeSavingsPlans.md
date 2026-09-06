---
source_url: https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_DescribeSavingsPlans.html
---

# DescribeSavingsPlans
<a name="API_DescribeSavingsPlans"></a>

Describes the specified Savings Plans.

## Request Syntax
<a name="API_DescribeSavingsPlans_RequestSyntax"></a>

```
POST /DescribeSavingsPlans HTTP/1.1
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
   "savingsPlanArns": [ "{{string}}" ],
   "savingsPlanIds": [ "{{string}}" ],
   "states": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DescribeSavingsPlans_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeSavingsPlans_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_DescribeSavingsPlans_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlans-request-filters"></a>
The filters.
Type: Array of [SavingsPlanFilter](API_SavingsPlanFilter.md) objects
Required: No

 ** [maxResults](#API_DescribeSavingsPlans_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlans-request-maxResults"></a>
The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeSavingsPlans_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlans-request-nextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[A-Za-z0-9/=\+]+$`
Required: No

 ** [savingsPlanArns](#API_DescribeSavingsPlans_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlans-request-savingsPlanArns"></a>
The Amazon Resource Names (ARN) of the Savings Plans.
Type: Array of strings
Array Members: Maximum number of 100 items.
Pattern: `arn:aws:[a-z]+:([a-z]{2}-[a-z]+-\d{1}|):(\d{12}):savingsplan\/([0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12})$`
Required: No

 ** [savingsPlanIds](#API_DescribeSavingsPlans_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlans-request-savingsPlanIds"></a>
The IDs of the Savings Plans.
Type: Array of strings
Required: No

 ** [states](#API_DescribeSavingsPlans_RequestSyntax) **   <a name="savingsplans-DescribeSavingsPlans-request-states"></a>
The current states of the Savings Plans.
Type: Array of strings
Valid Values: `payment-pending | payment-failed | active | retired | queued | queued-deleted | pending-return | returned`
Required: No

## Response Syntax
<a name="API_DescribeSavingsPlans_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "savingsPlans": [
      {
         "commitment": "string",
         "currency": "string",
         "description": "string",
         "ec2InstanceFamily": "string",
         "end": "string",
         "offeringId": "string",
         "paymentOption": "string",
         "productTypes": [ "string" ],
         "recurringPaymentAmount": "string",
         "region": "string",
         "returnableUntil": "string",
         "savingsPlanArn": "string",
         "savingsPlanId": "string",
         "savingsPlanType": "string",
         "start": "string",
         "state": "string",
         "tags": {
            "string" : "string"
         },
         "termDurationInSeconds": number,
         "upfrontPaymentAmount": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSavingsPlans_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribeSavingsPlans_ResponseSyntax) **   <a name="savingsplans-DescribeSavingsPlans-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[A-Za-z0-9/=\+]+$`

 ** [savingsPlans](#API_DescribeSavingsPlans_ResponseSyntax) **   <a name="savingsplans-DescribeSavingsPlans-response-savingsPlans"></a>
Information about the Savings Plans.
Type: Array of [SavingsPlan](API_SavingsPlan.md) objects

## Errors
<a name="API_DescribeSavingsPlans_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error occurred.
HTTP Status Code: 500

 ** ValidationException **
One of the input parameters is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeSavingsPlans_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/savingsplans-2019-06-28/DescribeSavingsPlans)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/savingsplans-2019-06-28/DescribeSavingsPlans)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/savingsplans-2019-06-28/DescribeSavingsPlans)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/savingsplans-2019-06-28/DescribeSavingsPlans)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/savingsplans-2019-06-28/DescribeSavingsPlans)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/savingsplans-2019-06-28/DescribeSavingsPlans)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/savingsplans-2019-06-28/DescribeSavingsPlans)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/savingsplans-2019-06-28/DescribeSavingsPlans)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/savingsplans-2019-06-28/DescribeSavingsPlans)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/savingsplans-2019-06-28/DescribeSavingsPlans)
