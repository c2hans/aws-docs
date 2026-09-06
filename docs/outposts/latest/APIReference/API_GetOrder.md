---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetOrder.html
---

# GetOrder
<a name="API_GetOrder"></a>

Gets information about the specified order.

## Request Syntax
<a name="API_GetOrder_RequestSyntax"></a>

```
GET /orders/{{OrderId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetOrder_RequestParameters"></a>

The request uses the following URI parameters.

 ** [OrderId](#API_GetOrder_RequestSyntax) **   <a name="outposts-GetOrder-request-uri-OrderId"></a>
The ID of the order.
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `oo-[a-f0-9]{17}$`
Required: Yes

## Request Body
<a name="API_GetOrder_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetOrder_ResponseSyntax"></a>

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
<a name="API_GetOrder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Order](#API_GetOrder_ResponseSyntax) **   <a name="outposts-GetOrder-response-Order"></a>
Information about an order.
Type: [Order](API_Order.md) object

## Errors
<a name="API_GetOrder_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** NotFoundException **
The specified request is not valid.
HTTP Status Code: 404

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_GetOrder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/GetOrder)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/GetOrder)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/GetOrder)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/GetOrder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/GetOrder)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/GetOrder)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/GetOrder)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/GetOrder)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/GetOrder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/GetOrder)
