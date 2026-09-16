---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_BatchDisassociateResourcesFromCustomLineItem.html
---

# BatchDisassociateResourcesFromCustomLineItem
<a name="API_BatchDisassociateResourcesFromCustomLineItem"></a>

 Disassociates a batch of resources from a percentage custom line item.

## Request Syntax
<a name="API_BatchDisassociateResourcesFromCustomLineItem_RequestSyntax"></a>

```
PUT /batch-disassociate-resources-from-custom-line-item HTTP/1.1
Content-type: application/json

{
   "BillingPeriodRange": {
      "ExclusiveEndBillingPeriod": "{{string}}",
      "InclusiveStartBillingPeriod": "{{string}}"
   },
   "ResourceArns": [ "{{string}}" ],
   "TargetArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_BatchDisassociateResourcesFromCustomLineItem_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchDisassociateResourcesFromCustomLineItem_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BillingPeriodRange](#API_BatchDisassociateResourcesFromCustomLineItem_RequestSyntax) **   <a name="billingconductor-BatchDisassociateResourcesFromCustomLineItem-request-BillingPeriodRange"></a>
The billing period range in which the custom line item request will be applied.
Type: [CustomLineItemBillingPeriodRange](API_CustomLineItemBillingPeriodRange.md) object
Required: No

 ** [ResourceArns](#API_BatchDisassociateResourcesFromCustomLineItem_RequestSyntax) **   <a name="billingconductor-BatchDisassociateResourcesFromCustomLineItem-request-ResourceArns"></a>
 A list containing the ARNs of resources to be disassociated.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:(customlineitem|billinggroup)/)?[a-zA-Z0-9]{10,12}`
Required: Yes

 ** [TargetArn](#API_BatchDisassociateResourcesFromCustomLineItem_RequestSyntax) **   <a name="billingconductor-BatchDisassociateResourcesFromCustomLineItem-request-TargetArn"></a>
 A percentage custom line item ARN to disassociate the resources from.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:customlineitem/)?[a-zA-Z0-9]{10}`
Required: Yes

## Response Syntax
<a name="API_BatchDisassociateResourcesFromCustomLineItem_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "FailedDisassociatedResources": [
      {
         "Arn": "string",
         "Error": {
            "Message": "string",
            "Reason": "string"
         }
      }
   ],
   "SuccessfullyDisassociatedResources": [
      {
         "Arn": "string",
         "Error": {
            "Message": "string",
            "Reason": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_BatchDisassociateResourcesFromCustomLineItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedDisassociatedResources](#API_BatchDisassociateResourcesFromCustomLineItem_ResponseSyntax) **   <a name="billingconductor-BatchDisassociateResourcesFromCustomLineItem-response-FailedDisassociatedResources"></a>
 A list of `DisassociateResourceResponseElement` for each resource that failed disassociation from a percentage custom line item.
Type: Array of [DisassociateResourceResponseElement](API_DisassociateResourceResponseElement.md) objects

 ** [SuccessfullyDisassociatedResources](#API_BatchDisassociateResourcesFromCustomLineItem_ResponseSyntax) **   <a name="billingconductor-BatchDisassociateResourcesFromCustomLineItem-response-SuccessfullyDisassociatedResources"></a>
 A list of `DisassociateResourceResponseElement` for each resource that's been disassociated from a percentage custom line item successfully.
Type: Array of [DisassociateResourceResponseElement](API_DisassociateResourceResponseElement.md) objects

## Errors
<a name="API_BatchDisassociateResourcesFromCustomLineItem_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
You can cause an inconsistent state by updating or deleting a resource.
 ** Reason **
Reason for the inconsistent state.
 ** ResourceId **
Identifier of the resource in use.
 ** ResourceType **
Type of the resource in use.
HTTP Status Code: 409

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
<a name="API_BatchDisassociateResourcesFromCustomLineItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/BatchDisassociateResourcesFromCustomLineItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/BatchDisassociateResourcesFromCustomLineItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/BatchDisassociateResourcesFromCustomLineItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/BatchDisassociateResourcesFromCustomLineItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/BatchDisassociateResourcesFromCustomLineItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/BatchDisassociateResourcesFromCustomLineItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/BatchDisassociateResourcesFromCustomLineItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/BatchDisassociateResourcesFromCustomLineItem)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/BatchDisassociateResourcesFromCustomLineItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/BatchDisassociateResourcesFromCustomLineItem)
