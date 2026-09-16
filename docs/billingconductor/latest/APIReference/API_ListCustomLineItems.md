---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListCustomLineItems.html
---

# ListCustomLineItems
<a name="API_ListCustomLineItems"></a>

 A paginated call to get a list of all custom line items (FFLIs) for the given billing period. If you don't provide a billing period, the current billing period is used.

## Request Syntax
<a name="API_ListCustomLineItems_RequestSyntax"></a>

```
POST /list-custom-line-items HTTP/1.1
Content-type: application/json

{
   "BillingPeriod": "{{string}}",
   "Filters": {
      "AccountIds": [ "{{string}}" ],
      "Arns": [ "{{string}}" ],
      "BillingGroups": [ "{{string}}" ],
      "Names": [ "{{string}}" ]
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListCustomLineItems_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListCustomLineItems_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BillingPeriod](#API_ListCustomLineItems_RequestSyntax) **   <a name="billingconductor-ListCustomLineItems-request-BillingPeriod"></a>
 The preferred billing period to get custom line items (FFLIs).
Type: String
Pattern: `\d{4}-(0?[1-9]|1[012])`
Required: No

 ** [Filters](#API_ListCustomLineItems_RequestSyntax) **   <a name="billingconductor-ListCustomLineItems-request-Filters"></a>
A `ListCustomLineItemsFilter` that specifies the custom line item names and/or billing group Amazon Resource Names (ARNs) to retrieve FFLI information.
Type: [ListCustomLineItemsFilter](API_ListCustomLineItemsFilter.md) object
Required: No

 ** [MaxResults](#API_ListCustomLineItems_RequestSyntax) **   <a name="billingconductor-ListCustomLineItems-request-MaxResults"></a>
 The maximum number of billing groups to retrieve.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListCustomLineItems_RequestSyntax) **   <a name="billingconductor-ListCustomLineItems-request-NextToken"></a>
 The pagination token that's used on subsequent calls to get custom line items (FFLIs).
Type: String
Required: No

## Response Syntax
<a name="API_ListCustomLineItems_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CustomLineItems": [
      {
         "AccountId": "string",
         "Arn": "string",
         "AssociationSize": number,
         "BillingGroupArn": "string",
         "ChargeDetails": {
            "Flat": {
               "ChargeValue": number
            },
            "LineItemFilters": [
               {
                  "Attribute": "string",
                  "AttributeValues": [ "string" ],
                  "MatchOption": "string",
                  "Values": [ "string" ]
               }
            ],
            "Percentage": {
               "PercentageValue": number
            },
            "Type": "string"
         },
         "ComputationRule": "string",
         "CreationTime": number,
         "CurrencyCode": "string",
         "Description": "string",
         "LastModifiedTime": number,
         "Name": "string",
         "PresentationDetails": {
            "Service": "string"
         },
         "ProductCode": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCustomLineItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CustomLineItems](#API_ListCustomLineItems_ResponseSyntax) **   <a name="billingconductor-ListCustomLineItems-response-CustomLineItems"></a>
 A list of `FreeFormLineItemListElements` received.
Type: Array of [CustomLineItemListElement](API_CustomLineItemListElement.md) objects

 ** [NextToken](#API_ListCustomLineItems_ResponseSyntax) **   <a name="billingconductor-ListCustomLineItems-response-NextToken"></a>
 The pagination token that's used on subsequent calls to get custom line items (FFLIs).
Type: String

## Errors
<a name="API_ListCustomLineItems_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
 ** RetryAfterSeconds **
Number of seconds you can retry after the call.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that doesn't exist.
 ** ResourceId **
Resource identifier that was not found.
 ** ResourceType **
Resource type that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
Number of seconds you can safely retry after the call.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't match with the constraints specified by AWS services.
 ** Fields **
The fields that caused the error, if applicable.
 ** Reason **
The reason the request's validation failed.
HTTP Status Code: 400

## See Also
<a name="API_ListCustomLineItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/ListCustomLineItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/ListCustomLineItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/ListCustomLineItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/ListCustomLineItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/ListCustomLineItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/ListCustomLineItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/ListCustomLineItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/ListCustomLineItems)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/ListCustomLineItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/ListCustomLineItems)
