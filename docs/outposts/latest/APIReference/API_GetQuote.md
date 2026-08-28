---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetQuote.html
---

# GetQuote
<a name="API_GetQuote"></a>

Gets information about the specified quote.

## Request Syntax
<a name="API_GetQuote_RequestSyntax"></a>

```
GET /quotes/{{QuoteIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetQuote_RequestParameters"></a>

The request uses the following URI parameters.

 ** [QuoteIdentifier](#API_GetQuote_RequestSyntax) **   <a name="outposts-GetQuote-request-uri-QuoteIdentifier"></a>
The ID of the quote.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:quote/)?oq-[a-f0-9]{17}$`
Required: Yes

## Request Body
<a name="API_GetQuote_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetQuote_ResponseSyntax"></a>

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
<a name="API_GetQuote_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Quote](#API_GetQuote_ResponseSyntax) **   <a name="outposts-GetQuote-response-Quote"></a>
Information about the quote.
Type: [Quote](API_Quote.md) object

## Errors
<a name="API_GetQuote_Errors"></a>

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
<a name="API_GetQuote_Examples"></a>

### Example
<a name="API_GetQuote_Example_1"></a>

This example gets information about the specified quote.

#### Sample Request
<a name="API_GetQuote_Example_1_Request"></a>

```
aws outposts get-quote --quote-identifier oq-1234567890abcdef0
```

#### Sample Response
<a name="API_GetQuote_Example_1_Response"></a>

```
{
  "Quote": {
    "QuoteId": "oq-1234567890abcdef0",
    "AccountId": "123456789012",
    "QuoteStatus": "CREATED",
    "CountryCode": "US",
    "RequestedCapacities": [
      {
        "QuoteCapacityType": "EC2",
        "Unit": "c5.24xlarge",
        "Quantity": 4.0
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
              "RackPowerDrawKva": 10.5,
              "RackWeightLbs": 2000.0,
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
              "UpfrontPrice": 100000.00,
              "MonthlyRecurringPrice": 0.0,
              "Currency": "USD"
            }
          }
        ]
      }
    ],
    "OrderingRequirements": [
      {
        "OrderingRequirementType": "OUTPOST_ACTIVE_CHECK_ERROR",
        "Status": "PASS"
      }
    ],
    "CreatedDate": "2026-01-15T10:30:00Z",
    "ExpirationDate": "2026-02-14T10:30:00Z"
  }
}
```

## See Also
<a name="API_GetQuote_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/GetQuote)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/GetQuote)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/GetQuote)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/GetQuote)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/GetQuote)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/GetQuote)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/GetQuote)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/GetQuote)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/GetQuote)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/GetQuote)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
