---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_PurchaseReservedInstanceOffering.html
---

# PurchaseReservedInstanceOffering
<a name="API_PurchaseReservedInstanceOffering"></a>

Allows you to purchase Amazon OpenSearch Service Reserved Instances.

## Request Syntax
<a name="API_PurchaseReservedInstanceOffering_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/purchaseReservedInstanceOffering HTTP/1.1
Content-type: application/json

{
   "InstanceCount": {{number}},
   "ReservationName": "{{string}}",
   "ReservedInstanceOfferingId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PurchaseReservedInstanceOffering_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PurchaseReservedInstanceOffering_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceCount](#API_PurchaseReservedInstanceOffering_RequestSyntax) **   <a name="opensearchservice-PurchaseReservedInstanceOffering-request-InstanceCount"></a>
The number of OpenSearch instances to reserve.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [ReservationName](#API_PurchaseReservedInstanceOffering_RequestSyntax) **   <a name="opensearchservice-PurchaseReservedInstanceOffering-request-ReservationName"></a>
A customer-specified identifier to track this reservation.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 64.
Pattern: `.*`
Required: Yes

 ** [ReservedInstanceOfferingId](#API_PurchaseReservedInstanceOffering_RequestSyntax) **   <a name="opensearchservice-PurchaseReservedInstanceOffering-request-ReservedInstanceOfferingId"></a>
The ID of the Reserved Instance offering to purchase.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `\p{XDigit}{8}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{12}`
Required: Yes

## Response Syntax
<a name="API_PurchaseReservedInstanceOffering_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ReservationName": "string",
   "ReservedInstanceId": "string"
}
```

## Response Elements
<a name="API_PurchaseReservedInstanceOffering_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReservationName](#API_PurchaseReservedInstanceOffering_ResponseSyntax) **   <a name="opensearchservice-PurchaseReservedInstanceOffering-response-ReservationName"></a>
The customer-specified identifier used to track this reservation.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 64.
Pattern: `.*`

 ** [ReservedInstanceId](#API_PurchaseReservedInstanceOffering_ResponseSyntax) **   <a name="opensearchservice-PurchaseReservedInstanceOffering-response-ReservedInstanceId"></a>
The ID of the Reserved Instance offering that was purchased.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `\p{XDigit}{8}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{12}`

## Errors
<a name="API_PurchaseReservedInstanceOffering_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** LimitExceededException **
An exception for trying to create more than the allowed number of resources or sub-resources.
HTTP Status Code: 409

 ** ResourceAlreadyExistsException **
An exception for creating a resource that already exists.
HTTP Status Code: 409

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_PurchaseReservedInstanceOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/PurchaseReservedInstanceOffering)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/PurchaseReservedInstanceOffering)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/PurchaseReservedInstanceOffering)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/PurchaseReservedInstanceOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/PurchaseReservedInstanceOffering)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/PurchaseReservedInstanceOffering)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/PurchaseReservedInstanceOffering)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/PurchaseReservedInstanceOffering)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/PurchaseReservedInstanceOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/PurchaseReservedInstanceOffering)
