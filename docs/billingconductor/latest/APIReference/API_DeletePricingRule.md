---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_DeletePricingRule.html
---

# DeletePricingRule
<a name="API_DeletePricingRule"></a>

 Deletes the pricing rule that's identified by the input Amazon Resource Name (ARN).

## Request Syntax
<a name="API_DeletePricingRule_RequestSyntax"></a>

```
POST /delete-pricing-rule HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeletePricingRule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeletePricingRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_DeletePricingRule_RequestSyntax) **   <a name="billingconductor-DeletePricingRule-request-Arn"></a>
 The Amazon Resource Name (ARN) of the pricing rule that you are deleting.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:pricingrule/)?[a-zA-Z0-9]{10}`
Required: Yes

## Response Syntax
<a name="API_DeletePricingRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string"
}
```

## Response Elements
<a name="API_DeletePricingRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DeletePricingRule_ResponseSyntax) **   <a name="billingconductor-DeletePricingRule-response-Arn"></a>
 The Amazon Resource Name (ARN) of the deleted pricing rule.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:pricingrule/)?[a-zA-Z0-9]{10}`

## Errors
<a name="API_DeletePricingRule_Errors"></a>

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
<a name="API_DeletePricingRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/DeletePricingRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/DeletePricingRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/DeletePricingRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/DeletePricingRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/DeletePricingRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/DeletePricingRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/DeletePricingRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/DeletePricingRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/DeletePricingRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/DeletePricingRule)
