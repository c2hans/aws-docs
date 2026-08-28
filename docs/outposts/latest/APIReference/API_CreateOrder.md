---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_CreateOrder.html
---

# CreateOrder
<a name="API_CreateOrder"></a>

Creates an order for an Outpost.

## Request Syntax
<a name="API_CreateOrder_RequestSyntax"></a>

```
POST /orders HTTP/1.1
Content-type: application/json

{
   "LineItems": [
      {
         "CatalogItemId": "{{string}}",
         "Quantity": {{number}}
      }
   ],
   "OutpostIdentifier": "{{string}}",
   "PaymentOption": "{{string}}",
   "PaymentTerm": "{{string}}",
   "QuoteIdentifier": "{{string}}",
   "QuoteOptionIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateOrder_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateOrder_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [LineItems](#API_CreateOrder_RequestSyntax) **   <a name="outposts-CreateOrder-request-LineItems"></a>
The line items that make up the order.
Type: Array of [LineItemRequest](API_LineItemRequest.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** [OutpostIdentifier](#API_CreateOrder_RequestSyntax) **   <a name="outposts-CreateOrder-request-OutpostIdentifier"></a>
 The ID or the Amazon Resource Name (ARN) of the Outpost.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
Required: Yes

 ** [PaymentOption](#API_CreateOrder_RequestSyntax) **   <a name="outposts-CreateOrder-request-PaymentOption"></a>
The payment option.
Type: String
Valid Values: `ALL_UPFRONT | NO_UPFRONT | PARTIAL_UPFRONT`
Required: Yes

 ** [PaymentTerm](#API_CreateOrder_RequestSyntax) **   <a name="outposts-CreateOrder-request-PaymentTerm"></a>
The payment terms.
Type: String
Valid Values: `THREE_YEARS | ONE_YEAR | FIVE_YEARS`
Required: No

 ** [QuoteIdentifier](#API_CreateOrder_RequestSyntax) **   <a name="outposts-CreateOrder-request-QuoteIdentifier"></a>
The ID of the quote to use for the order.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:quote/)?oq-[a-f0-9]{17}$`
Required: No

 ** [QuoteOptionIdentifier](#API_CreateOrder_RequestSyntax) **   <a name="outposts-CreateOrder-request-QuoteOptionIdentifier"></a>
The ID of the quote option to use for the order.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 21.
Pattern: `^oqo-[a-f0-9]{17}$`
Required: No

## Response Syntax
<a name="API_CreateOrder_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Order": {
      "LineItems": [
         {
            "AssetInformationList": [
               {
                  "AssetId": "string",
                  "MacAddressList": [ "string" ]
               }
            ],
            "CatalogItemId": "string",
            "LineItemId": "string",
            "PreviousLineItemId": "string",
            "PreviousOrderId": "string",
            "Quantity": number,
            "ShipmentInformation": {
               "ShipmentCarrier": "string",
               "ShipmentTrackingNumber": "string"
            },
            "Status": "string"
         }
      ],
      "OrderFulfilledDate": number,
      "OrderId": "string",
      "OrderSubmissionDate": number,
      "OrderType": "string",
      "OutpostId": "string",
      "PaymentOption": "string",
      "PaymentTerm": "string",
      "QuoteIdentifier": "string",
      "QuoteOptionIdentifier": "string",
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_CreateOrder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Order](#API_CreateOrder_ResponseSyntax) **   <a name="outposts-CreateOrder-response-Order"></a>
Information about this order.
Type: [Order](API_Order.md) object

## Errors
<a name="API_CreateOrder_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting this resource can cause an inconsistent state.
 ** ResourceId **
The ID of the resource causing the conflict.
 ** ResourceType **
The type of the resource causing the conflict.
HTTP Status Code: 409

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** NotFoundException **
The specified request is not valid.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have exceeded a service quota.
HTTP Status Code: 402

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## Examples
<a name="API_CreateOrder_Examples"></a>

### Example 1: Create an order from a quote
<a name="API_CreateOrder_Example_1"></a>

This example creates an order using a quote and quote option.

#### Sample Request
<a name="API_CreateOrder_Example_1_Request"></a>

```
aws outposts create-order --outpost-identifier op-1234567890example --quote-identifier oq-1234567890abcdef0 --quote-option-identifier oqo-1234567890abcdef0 --payment-option ALL_UPFRONT --payment-term THREE_YEARS
```

#### Sample Response
<a name="API_CreateOrder_Example_1_Response"></a>

```
{
  "Order": {
    "OutpostId": "op-1234567890example",
    "QuoteIdentifier": "oq-1234567890abcdef0",
    "QuoteOptionIdentifier": "oqo-1234567890abcdef0",
    "OrderId": "oo-1234567890abcdef0",
    "Status": "PREPARING",
    "LineItems": [
      {
        "LineItemId": "ooi-1234567890abcdef0",
        "Quantity": 1,
        "Status": "PREPARING"
      }
    ],
    "PaymentOption": "ALL_UPFRONT",
    "PaymentTerm": "THREE_YEARS",
    "OrderSubmissionDate": "2026-06-15T10:30:00Z",
    "OrderType": "OUTPOST"
  }
}
```

### Example 2: Create an order with line items
<a name="API_CreateOrder_Example_2"></a>

This example creates an order by specifying line items directly.

#### Sample Request
<a name="API_CreateOrder_Example_2_Request"></a>

```
aws outposts create-order --outpost-identifier op-1234567890example --line-items CatalogItemId=OR-A1B2C3D,Quantity=1 --payment-option ALL_UPFRONT --payment-term THREE_YEARS
```

#### Sample Response
<a name="API_CreateOrder_Example_2_Response"></a>

```
{
  "Order": {
    "OutpostId": "op-1234567890example",
    "OrderId": "oo-2345678901abcdef0",
    "Status": "PREPARING",
    "LineItems": [
      {
        "CatalogItemId": "OR-A1B2C3D",
        "LineItemId": "ooi-2345678901abcdef0",
        "Quantity": 1,
        "Status": "PREPARING"
      }
    ],
    "PaymentOption": "ALL_UPFRONT",
    "PaymentTerm": "THREE_YEARS",
    "OrderSubmissionDate": "2026-06-15T10:30:00Z",
    "OrderType": "OUTPOST"
  }
}
```

## See Also
<a name="API_CreateOrder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/CreateOrder)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/CreateOrder)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/CreateOrder)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/CreateOrder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/CreateOrder)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/CreateOrder)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/CreateOrder)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/CreateOrder)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/CreateOrder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/CreateOrder)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
