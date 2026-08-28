---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_CreateQuote.html
---

# CreateQuote
<a name="API_CreateQuote"></a>

Creates a quote for an Outpost. A quote provides pricing and configuration options based on the requested capacity. You can optionally associate the quote with an existing Outpost or create a standalone quote by specifying only the country code and requested capacities.

## Request Syntax
<a name="API_CreateQuote_RequestSyntax"></a>

```
POST /quotes HTTP/1.1
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
<a name="API_CreateQuote_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateQuote_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CountryCode](#API_CreateQuote_RequestSyntax) **   <a name="outposts-CreateQuote-request-CountryCode"></a>
The country code for the Outpost site location.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `^[A-Z]{2}$`
Required: Yes

 ** [Description](#API_CreateQuote_RequestSyntax) **   <a name="outposts-CreateQuote-request-Description"></a>
A description for the quote.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `^[\S \n]*$`
Required: No

 ** [OutpostIdentifier](#API_CreateQuote_RequestSyntax) **   <a name="outposts-CreateQuote-request-OutpostIdentifier"></a>
The ID or ARN of the Outpost to associate with the quote. If not specified, the quote is created without an Outpost association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
Required: No

 ** [RequestedCapacities](#API_CreateQuote_RequestSyntax) **   <a name="outposts-CreateQuote-request-RequestedCapacities"></a>
The capacity requirements for the quote. Each entry specifies a capacity type (such as Amazon EC2), the unit, and the quantity. For Amazon EC2, the quantity is the number of additional instances to add to the Outpost. For Amazon EBS and Amazon S3, the quantity is the total desired end-state capacity of the Outpost.
Type: Array of [QuoteCapacity](API_QuoteCapacity.md) objects
Array Members: Maximum number of 2000 items.
Required: Yes

 ** [RequestedConstraints](#API_CreateQuote_RequestSyntax) **   <a name="outposts-CreateQuote-request-RequestedConstraints"></a>
The physical constraints for the quote, such as maximum number of racks, maximum power draw per rack, or maximum weight per rack.
Type: Array of [QuoteConstraint](API_QuoteConstraint.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** [RequestedPaymentOptions](#API_CreateQuote_RequestSyntax) **   <a name="outposts-CreateQuote-request-RequestedPaymentOptions"></a>
The payment options to include in the quote pricing. If not specified, all available payment options are returned.
Type: Array of strings
Array Members: Maximum number of 3 items.
Valid Values: `ALL_UPFRONT | NO_UPFRONT | PARTIAL_UPFRONT`
Required: No

 ** [RequestedPaymentTerms](#API_CreateQuote_RequestSyntax) **   <a name="outposts-CreateQuote-request-RequestedPaymentTerms"></a>
The payment terms to include in the quote pricing. If not specified, all available payment terms are returned.
Type: Array of strings
Array Members: Maximum number of 3 items.
Valid Values: `THREE_YEARS | ONE_YEAR | FIVE_YEARS`
Required: No

## Response Syntax
<a name="API_CreateQuote_ResponseSyntax"></a>

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
<a name="API_CreateQuote_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Quote](#API_CreateQuote_ResponseSyntax) **   <a name="outposts-CreateQuote-response-Quote"></a>
Information about the quote.
Type: [Quote](API_Quote.md) object

## Errors
<a name="API_CreateQuote_Errors"></a>

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
<a name="API_CreateQuote_Examples"></a>

### Example
<a name="API_CreateQuote_Example_1"></a>

This example creates a quote for EC2 capacity.

#### Sample Request
<a name="API_CreateQuote_Example_1_Request"></a>

```
aws outposts create-quote --country-code US --requested-capacities QuoteCapacityType=EC2,Unit=c5.24xlarge,Quantity=4
```

#### Sample Response
<a name="API_CreateQuote_Example_1_Response"></a>

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
    "CreatedDate": "2026-01-15T10:30:00Z",
    "ExpirationDate": "2026-02-14T10:30:00Z"
  }
}
```

## See Also
<a name="API_CreateQuote_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/CreateQuote)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/CreateQuote)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/CreateQuote)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/CreateQuote)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/CreateQuote)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/CreateQuote)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/CreateQuote)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/CreateQuote)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/CreateQuote)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/CreateQuote)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
