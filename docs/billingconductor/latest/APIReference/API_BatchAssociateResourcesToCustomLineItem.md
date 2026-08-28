---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_BatchAssociateResourcesToCustomLineItem.html
---

# BatchAssociateResourcesToCustomLineItem
<a name="API_BatchAssociateResourcesToCustomLineItem"></a>

 Associates a batch of resources to a percentage custom line item.

## Request Syntax
<a name="API_BatchAssociateResourcesToCustomLineItem_RequestSyntax"></a>

```
PUT /batch-associate-resources-to-custom-line-item HTTP/1.1
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
<a name="API_BatchAssociateResourcesToCustomLineItem_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchAssociateResourcesToCustomLineItem_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BillingPeriodRange](#API_BatchAssociateResourcesToCustomLineItem_RequestSyntax) **   <a name="billingconductor-BatchAssociateResourcesToCustomLineItem-request-BillingPeriodRange"></a>
The billing period range in which the custom line item request will be applied.
Type: [CustomLineItemBillingPeriodRange](API_CustomLineItemBillingPeriodRange.md) object
Required: No

 ** [ResourceArns](#API_BatchAssociateResourcesToCustomLineItem_RequestSyntax) **   <a name="billingconductor-BatchAssociateResourcesToCustomLineItem-request-ResourceArns"></a>
 A list containing the ARNs of the resources to be associated.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:(customlineitem|billinggroup)/)?[a-zA-Z0-9]{10,12}`
Required: Yes

 ** [TargetArn](#API_BatchAssociateResourcesToCustomLineItem_RequestSyntax) **   <a name="billingconductor-BatchAssociateResourcesToCustomLineItem-request-TargetArn"></a>
 A percentage custom line item ARN to associate the resources to.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:customlineitem/)?[a-zA-Z0-9]{10}`
Required: Yes

## Response Syntax
<a name="API_BatchAssociateResourcesToCustomLineItem_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "FailedAssociatedResources": [
      {
         "Arn": "string",
         "Error": {
            "Message": "string",
            "Reason": "string"
         }
      }
   ],
   "SuccessfullyAssociatedResources": [
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
<a name="API_BatchAssociateResourcesToCustomLineItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedAssociatedResources](#API_BatchAssociateResourcesToCustomLineItem_ResponseSyntax) **   <a name="billingconductor-BatchAssociateResourcesToCustomLineItem-response-FailedAssociatedResources"></a>
 A list of `AssociateResourceResponseElement` for each resource that failed association to a percentage custom line item.
Type: Array of [AssociateResourceResponseElement](API_AssociateResourceResponseElement.md) objects

 ** [SuccessfullyAssociatedResources](#API_BatchAssociateResourcesToCustomLineItem_ResponseSyntax) **   <a name="billingconductor-BatchAssociateResourcesToCustomLineItem-response-SuccessfullyAssociatedResources"></a>
 A list of `AssociateResourceResponseElement` for each resource that's been associated to a percentage custom line item successfully.
Type: Array of [AssociateResourceResponseElement](API_AssociateResourceResponseElement.md) objects

## Errors
<a name="API_BatchAssociateResourcesToCustomLineItem_Errors"></a>

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

 ** ServiceLimitExceededException **
The request would cause a service limit to exceed.
 ** LimitCode **
The unique code identifier of the service limit that is being exceeded.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
 ** ServiceCode **
The unique code for the service of the limit that is being exceeded.
HTTP Status Code: 402

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
<a name="API_BatchAssociateResourcesToCustomLineItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/BatchAssociateResourcesToCustomLineItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/BatchAssociateResourcesToCustomLineItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/BatchAssociateResourcesToCustomLineItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/BatchAssociateResourcesToCustomLineItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/BatchAssociateResourcesToCustomLineItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/BatchAssociateResourcesToCustomLineItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/BatchAssociateResourcesToCustomLineItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/BatchAssociateResourcesToCustomLineItem)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/BatchAssociateResourcesToCustomLineItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/BatchAssociateResourcesToCustomLineItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
