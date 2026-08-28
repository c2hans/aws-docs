---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_DeleteCustomLineItem.html
---

# DeleteCustomLineItem
<a name="API_DeleteCustomLineItem"></a>

 Deletes the custom line item identified by the given ARN in the current, or previous billing period.

## Request Syntax
<a name="API_DeleteCustomLineItem_RequestSyntax"></a>

```
POST /delete-custom-line-item HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}",
   "BillingPeriodRange": {
      "ExclusiveEndBillingPeriod": "{{string}}",
      "InclusiveStartBillingPeriod": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_DeleteCustomLineItem_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteCustomLineItem_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_DeleteCustomLineItem_RequestSyntax) **   <a name="billingconductor-DeleteCustomLineItem-request-Arn"></a>
 The ARN of the custom line item to be deleted.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:customlineitem/)?[a-zA-Z0-9]{10}`
Required: Yes

 ** [BillingPeriodRange](#API_DeleteCustomLineItem_RequestSyntax) **   <a name="billingconductor-DeleteCustomLineItem-request-BillingPeriodRange"></a>
The billing period range in which the custom line item request will be applied.
Type: [CustomLineItemBillingPeriodRange](API_CustomLineItemBillingPeriodRange.md) object
Required: No

## Response Syntax
<a name="API_DeleteCustomLineItem_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string"
}
```

## Response Elements
<a name="API_DeleteCustomLineItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DeleteCustomLineItem_ResponseSyntax) **   <a name="billingconductor-DeleteCustomLineItem-response-Arn"></a>
The ARN of the deleted custom line item.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:customlineitem/)?[a-zA-Z0-9]{10}`

## Errors
<a name="API_DeleteCustomLineItem_Errors"></a>

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
<a name="API_DeleteCustomLineItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/DeleteCustomLineItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/DeleteCustomLineItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/DeleteCustomLineItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/DeleteCustomLineItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/DeleteCustomLineItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/DeleteCustomLineItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/DeleteCustomLineItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/DeleteCustomLineItem)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/DeleteCustomLineItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/DeleteCustomLineItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
