---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_UpdateQuote.html
---

# UpdateQuote
<a name="API_UpdateQuote"></a>

Updates the specified quote. You can modify the requested capacities, constraints, payment options, payment terms, or Outpost association.

## Request Syntax
<a name="API_UpdateQuote_RequestSyntax"></a>

```
PATCH /quotes/{{QuoteIdentifier}} HTTP/1.1
Content-type: application/json

{
   "CountryCode": "{{string}}",
   "Description": "{{string}}",
   "OutpostIdentifier": "{{string}}",
   "RequestedCapacities": [
      {
         "Quantity": {{number}},
         "QuoteCapacityType": "{{string}}",
         "Unit": "{{string}}"
      }
   ],
   "RequestedConstraints": [
      {
         "QuoteConstraintType": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "RequestedPaymentOptions": [ "{{string}}" ],
   "RequestedPaymentTerms": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateQuote_RequestParameters"></a>

The request uses the following URI parameters.

 ** [QuoteIdentifier](#API_UpdateQuote_RequestSyntax) **   <a name="outposts-UpdateQuote-request-uri-QuoteIdentifier"></a>
The ID of the quote.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:quote/)?oq-[a-f0-9]{17}$`
Required: Yes

## Request Body
<a name="API_UpdateQuote_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CountryCode](#API_UpdateQuote_RequestSyntax) **   <a name="outposts-UpdateQuote-request-CountryCode"></a>
The country code for the Outpost site location.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `^[A-Z]{2}$`
Required: No

 ** [Description](#API_UpdateQuote_RequestSyntax) **   <a name="outposts-UpdateQuote-request-Description"></a>
A description for the quote.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `^[\S \n]*$`
Required: No

 ** [OutpostIdentifier](#API_UpdateQuote_RequestSyntax) **   <a name="outposts-UpdateQuote-request-OutpostIdentifier"></a>
The ID or ARN of the Outpost to associate with the quote. Specify an empty string to remove the Outpost association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 180.
Pattern: `^((arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17})?$`
Required: No

 ** [RequestedCapacities](#API_UpdateQuote_RequestSyntax) **   <a name="outposts-UpdateQuote-request-RequestedCapacities"></a>
The updated capacity requirements for the quote.
Type: Array of [QuoteCapacity](API_QuoteCapacity.md) objects
Array Members: Maximum number of 2000 items.
Required: No

 ** [RequestedConstraints](#API_UpdateQuote_RequestSyntax) **   <a name="outposts-UpdateQuote-request-RequestedConstraints"></a>
The updated physical constraints for the quote.
Type: Array of [QuoteConstraint](API_QuoteConstraint.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** [RequestedPaymentOptions](#API_UpdateQuote_RequestSyntax) **   <a name="outposts-UpdateQuote-request-RequestedPaymentOptions"></a>
The updated payment options to include in the quote pricing.
Type: Array of strings
Array Members: Maximum number of 3 items.
Valid Values: `ALL_UPFRONT | NO_UPFRONT | PARTIAL_UPFRONT`
Required: No

 ** [RequestedPaymentTerms](#API_UpdateQuote_RequestSyntax) **   <a name="outposts-UpdateQuote-request-RequestedPaymentTerms"></a>
The updated payment terms to include in the quote pricing.
Type: Array of strings
Array Members: Maximum number of 3 items.
Valid Values: `THREE_YEARS | ONE_YEAR | FIVE_YEARS`
Required: No

## Response Syntax
<a name="API_UpdateQuote_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Quote": {
      "AccountId": "string",
      "CountryCode": "string",
      "CreatedDate": number,
      "Description": "string",
      "ExpirationDate": number,
      "OrderingRequirements": [
         {
            "OrderingRequirementType": "string",
            "Status": "string",
            "StatusMessage": "string"
         }
      ],
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
}
```

## Response Elements
<a name="API_UpdateQuote_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Quote](#API_UpdateQuote_ResponseSyntax) **   <a name="outposts-UpdateQuote-response-Quote"></a>
Information about the updated quote.
Type: [Quote](API_Quote.md) object

## Errors
<a name="API_UpdateQuote_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** NotFoundException **
The specified request is not valid.
HTTP Status Code: 404

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## Examples
<a name="API_UpdateQuote_Examples"></a>

### Example
<a name="API_UpdateQuote_Example_1"></a>

This example updates a quote to associate it with an Outpost and change the requested capacities.

#### Sample Request
<a name="API_UpdateQuote_Example_1_Request"></a>

```
aws outposts update-quote --quote-identifier oq-1234567890abcdef0 --outpost-identifier op-1234567890example --requested-capacities QuoteCapacityType=EC2,Unit=m5.24xlarge,Quantity=8
```

#### Sample Response
<a name="API_UpdateQuote_Example_1_Response"></a>

```
{
  "Quote": {
    "QuoteId": "oq-1234567890abcdef0",
    "AccountId": "123456789012",
    "QuoteStatus": "CREATED",
    "OutpostArn": "arn:aws:outposts:us-east-1:123456789012:outpost/op-1234567890example",
    "CountryCode": "US",
    "RequestedCapacities": [
      {
        "QuoteCapacityType": "EC2",
        "Unit": "m5.24xlarge",
        "Quantity": 8.0
      }
    ],
    "QuoteOptions": [
      {
        "QuoteOptionIdentifier": "oqo-1234567890abcdef0",
        "Specifications": [
          {
            "QuoteSpecificationType": "NEW_RACK",
            "FinalRackSpecificationDetails": {
              "RackUse": "COMPUTE",
              "RackPowerDrawKva": 12.0,
              "RackWeightLbs": 2200.0,
              "RackHeightInches": 80.0,
              "RackWidthInches": 24.0,
              "RackDepthInches": 48.0,
              "RackUnitHeight": "HEIGHT_42U"
            }
          }
        ],
        "PricingOptions": [
          {
            "PricingType": "SUBSCRIPTION",
            "SubscriptionPricingDetails": {
              "PaymentOption": "ALL_UPFRONT",
              "PaymentTerm": "THREE_YEARS",
              "UpfrontPrice": 200000.00,
              "MonthlyRecurringPrice": 0.0,
              "Currency": "USD"
            }
          }
        ]
      }
    ],
    "CreatedDate": "2026-01-15T10:30:00Z",
    "ExpirationDate": "2026-02-14T10:30:00Z"
  }
}
```

## See Also
<a name="API_UpdateQuote_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/UpdateQuote)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/UpdateQuote)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/UpdateQuote)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/UpdateQuote)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/UpdateQuote)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/UpdateQuote)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/UpdateQuote)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/UpdateQuote)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/UpdateQuote)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/UpdateQuote)
