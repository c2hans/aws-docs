---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListQuotes.html
---

# ListQuotes
<a name="API_ListQuotes"></a>

Lists the quotes for your AWS account.

## Request Syntax
<a name="API_ListQuotes_RequestSyntax"></a>

```
GET /quotes?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListQuotes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListQuotes_RequestSyntax) **   <a name="outposts-ListQuotes-request-uri-MaxResults"></a>
The maximum page size.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListQuotes_RequestSyntax) **   <a name="outposts-ListQuotes-request-uri-NextToken"></a>
The pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

## Request Body
<a name="API_ListQuotes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListQuotes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Quotes": [
      {
         "AccountId": "string",
         "CountryCode": "string",
         "CreatedDate": number,
         "Description": "string",
         "ExpirationDate": number,
         "OutpostArn": "string",
         "QuoteId": "string",
         "QuoteOptions": [
            {
               "Capacities": [
                  {
                     "Quantity": number,
                     "QuoteCapacityType": "string",
                     "Unit": "string"
                  }
               ],
               "CapacitySummary": {
                  "CapacityChange": [
                     {
                        "Quantity": number,
                        "QuoteCapacityType": "string",
                        "Unit": "string"
                     }
                  ],
                  "ExistingCapacities": [
                     {
                        "Quantity": number,
                        "QuoteCapacityType": "string",
                        "Unit": "string"
                     }
                  ],
                  "FinalCapacities": [
                     {
                        "Quantity": number,
                        "QuoteCapacityType": "string",
                        "Unit": "string"
                     }
                  ]
               },
               "PricingOptions": [
                  {
                     "PricingType": "string",
                     "SubscriptionPricingDetails": {
                        "Currency": "string",
                        "MonthlyRecurringPrice": number,
                        "PaymentOption": "string",
                        "PaymentTerm": "string",
                        "UpfrontPrice": number
                     }
                  }
               ],
               "QuoteOptionIdentifier": "string",
               "Specifications": [
                  {
                     "ExistingRackSpecificationDetails": {
                        "EC2Capacities": [
                           {
                              "Family": "string",
                              "MaxSize": "string",
                              "Quantity": "string"
                           }
                        ],
                        "RackDepthInches": number,
                        "RackHeightInches": number,
                        "RackId": "string",
                        "RackPowerDrawKva": number,
                        "RackUnitHeight": "string",
                        "RackUse": "string",
                        "RackWeightLbs": number,
                        "RackWidthInches": number
                     },
                     "FinalRackSpecificationDetails": {
                        "EC2Capacities": [
                           {
                              "Family": "string",
                              "MaxSize": "string",
                              "Quantity": "string"
                           }
                        ],
                        "RackDepthInches": number,
                        "RackHeightInches": number,
                        "RackId": "string",
                        "RackPowerDrawKva": number,
                        "RackUnitHeight": "string",
                        "RackUse": "string",
                        "RackWeightLbs": number,
                        "RackWidthInches": number
                     },
                     "QuoteSpecificationType": "string",
                     "ServerSpecificationDetails": {
                        "EC2Capacities": [
                           {
                              "Family": "string",
                              "MaxSize": "string",
                              "Quantity": "string"
                           }
                        ],
                        "RackUnitHeight": "string",
                        "ServerDepthInches": number,
                        "ServerHeightInches": number,
                        "ServerPowerDrawKva": number,
                        "ServerWeightLbs": number,
                        "ServerWidthInches": number
                     }
                  }
               ]
            }
         ],
         "QuoteStatus": "string",
         "RequestedCapacities": [
            {
               "Quantity": number,
               "QuoteCapacityType": "string",
               "Unit": "string"
            }
         ],
         "RequestedConstraints": [
            {
               "QuoteConstraintType": "string",
               "Value": "string"
            }
         ],
         "RequestedPaymentOptions": [ "string" ],
         "RequestedPaymentTerms": [ "string" ],
         "StatusMessage": "string",
         "SubmittedOrderId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListQuotes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListQuotes_ResponseSyntax) **   <a name="outposts-ListQuotes-response-NextToken"></a>
The pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

 ** [Quotes](#API_ListQuotes_ResponseSyntax) **   <a name="outposts-ListQuotes-response-Quotes"></a>
Information about the quotes.
Type: Array of [QuoteSummary](API_QuoteSummary.md) objects
Array Members: Maximum number of 1000 items.

## Errors
<a name="API_ListQuotes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

## See Also
<a name="API_ListQuotes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/ListQuotes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/ListQuotes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/ListQuotes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/ListQuotes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/ListQuotes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/ListQuotes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/ListQuotes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/ListQuotes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/ListQuotes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/ListQuotes)
